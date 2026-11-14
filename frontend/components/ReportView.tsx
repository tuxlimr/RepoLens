"use client";

import dynamic from "next/dynamic";
import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { ReportPayload, SourceRef } from "@/lib/types";
import { getReportMarkdown } from "@/lib/api";
import FreshButton from "./FreshButton";

const MermaidDiagram = dynamic(() => import("./MermaidDiagram"), {
  ssr: false,
  loading: () => <p className="muted">Loading diagram…</p>,
});

const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

function fmtDate(iso?: string | null): string {
  if (!iso) return "Unknown date";
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return iso;
  return `${MONTHS[d.getUTCMonth()]} ${d.getUTCDate()}, ${d.getUTCFullYear()}`;
}
function briefSentences(text: string): string {
  const clean = text.replace(/\s+/g, " ").replace(/^#+\s*/g, "").trim();
  if (!clean) return "";
  const parts = clean.split(/(?<=[.!?])\s+/).filter(Boolean);
  if (!parts.length) return clean.slice(0, 280);
  if (parts[0].length >= 90) return parts[0];
  return parts.slice(0, 2).join(" ");
}

function fmtNum(n?: number): string {
  if (typeof n !== "number") return "—";
  return n >= 1000 ? `${(n / 1000).toFixed(1).replace(/\.0$/, "")}k` : String(n);
}
function evidenceUrl(ev: SourceRef, repoUrl: string, branch: string): string | null {
  if (ev.url) return ev.url;
  if (!ev.path) return null;
  const lines = ev.start_line ? `#L${ev.start_line}${ev.end_line ? `-L${ev.end_line}` : ""}` : "";
  return `${repoUrl.replace(/\/$/, "")}/blob/${branch}/${ev.path}${lines}`;
}
function EvidenceLinks({ refs, repoUrl, branch }: { refs: SourceRef[]; repoUrl: string; branch: string }) {
  if (!refs?.length) return null;
  return (
    <ul style={{ margin: ".5rem 0 0", paddingLeft: "1.1rem" }}>
      {refs.map((ev, i) => {
        const href = evidenceUrl(ev, repoUrl, branch);
        const label = `${ev.path}${ev.start_line ? `:${ev.start_line}${ev.end_line ? `–${ev.end_line}` : ""}` : ""}`;
        return (
          <li key={`${ev.path}-${i}`} className="small">
            {href ? <a href={href} target="_blank" rel="noreferrer"><code>{label}</code></a> : <code>{label}</code>}
          </li>
        );
      })}
    </ul>
  );
}

export default function ReportView({ report, isSample = false }: { report: ReportPayload; isSample?: boolean }) {
  const [copied, setCopied] = useState(false);
  const [copyError, setCopyError] = useState("");
  const repo = report.repository;
  const model = report.model;
  const branch = repo.default_branch || "main";
  const sha = report.commit_sha || repo.commit_sha || "";
  const analysedAt = report.analysed_at || report.analyzed_at;
  const componentsById = new Map(model.components.map((c) => [c.id, c]));
  const brief = briefSentences(model.summary || repo.description || "");
  const description = (repo.description || "").trim();
  const descriptionAlreadyInBrief = description.length > 24 && brief.toLowerCase().includes(description.slice(0, 24).toLowerCase());

  async function copyMarkdown() {
    setCopyError("");
    try {
      const md = isSample ? report.markdown : await getReportMarkdown(repo.owner, repo.name).catch(() => report.markdown);
      await navigator.clipboard.writeText(md || report.markdown);
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    } catch {
      // Clipboard API unavailable: fall back to copying the embedded markdown.
      try {
        await navigator.clipboard.writeText(report.markdown);
        setCopied(true);
        setTimeout(() => setCopied(false), 2500);
      } catch {
        setCopyError("Copy failed in this browser — use Download .md instead.");
      }
    }
  }

  async function downloadMarkdown() {
    setCopyError("");
    let md = report.markdown;
    if (!isSample) {
      try { md = await getReportMarkdown(repo.owner, repo.name); } catch { /* fall back to embedded markdown */ }
    }
    const blob = new Blob([md], { type: "text/markdown;charset=utf-8" });
    const href = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = href;
    a.download = `${repo.owner}-${repo.name}-architecture.md`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(href);
  }

  return (
    <article className="report">
      {isSample && (
        <div className="alert alert-status" role="note" style={{ marginBottom: "1.25rem" }}>
          <strong>Sample report.</strong> This hand-written example for <span className="mono">psf/requests</span> shows
          the RepoLens format with no backend required. Live reports contain freshly extracted evidence for the analysed commit.
        </div>
      )}

      <header className="report-hero">
        <p className="small muted" style={{ margin: 0 }}>
          <a href={repo.html_url} target="_blank" rel="noreferrer">{repo.owner}</a> /{" "}
          <a href={repo.html_url} target="_blank" rel="noreferrer">{repo.name}</a>
        </p>
        <h1>
          {repo.full_name || `${repo.owner}/${repo.name}`}
        </h1>
        {brief && (
          <p className="brief">
            <span className="brief-label">In brief</span>
            {brief}
          </p>
        )}
        {description && !descriptionAlreadyInBrief && <p className="repo-description">{description}</p>}
        <div aria-label="Repository facts">
          <span className="chip">★ {fmtNum(repo.stars)} stars</span>
          <span className="chip">⑂ {fmtNum(repo.forks)} forks</span>
          {repo.language && <span className="chip chip-accent">{repo.language}</span>}
          {repo.license && <span className="chip">{repo.license}</span>}
          <span className="chip">Branch: {branch}</span>
          {sha && <span className="chip" title={sha}>Commit <span className="mono">{sha.slice(0, 7)}</span></span>}
          <span className="chip">Analysed {fmtDate(analysedAt)}</span>
          <span className="chip chip-indigo">Report v{report.version}</span>
        </div>
        <div className="actions">
          <a className="btn btn-secondary btn-small" href={repo.html_url} target="_blank" rel="noreferrer">View on GitHub ↗</a>
          <button className="btn btn-secondary btn-small" type="button" onClick={copyMarkdown}>{copied ? "Copied ✓" : "Copy Markdown"}</button>
          <button className="btn btn-secondary btn-small" type="button" onClick={downloadMarkdown}>Download .md</button>
        </div>
        {copyError && <div className="alert alert-error" role="alert">{copyError}</div>}
      </header>

      <div className="report-shell">
      <nav className="toc" aria-label="Table of contents">
        <strong>On this page</strong>
        <ul>
          <li><a href="#at-a-glance">At a glance</a></li>
          <li><a href="#diagram">Diagram</a></li>
          <li><a href="#components">Components</a></li>
          <li><a href="#detections">Technologies</a></li>
          <li><a href="#entry-points">Entry points</a></li>
          <li><a href="#limitations">Limits</a></li>
          <li><a href="#full-report">Full report</a></li>
          <li><a href="#fresh">Fresh analysis</a></li>
        </ul>
      </nav>
      <div>

      <section id="at-a-glance" className="section" aria-labelledby="glance-h">
        <h2 id="glance-h">Architecture at a glance</h2>
        <div className="card" style={{ fontSize: "1.05rem" }}>
          <p style={{ marginTop: 0 }}>{model.summary || "No summary was produced for this analysis."}</p>
          <p className="small muted" style={{ marginBottom: 0 }}>
            {model.components.length} components · {model.relationships.length} relationships ·{" "}
            {model.detections.length} detections
            {model.stats && typeof model.stats.files_considered === "number" ? ` · ${model.stats.files_considered} files considered` : ""}
            {" "}· Analysed {fmtDate(analysedAt)}{sha ? <> at commit <span className="mono">{sha.slice(0, 7)}</span></> : null}
          </p>
        </div>
      </section>

      <section id="diagram" className="section" aria-labelledby="diagram-h">
        <h2 id="diagram-h">Architecture diagram</h2>
        <MermaidDiagram source={report.mermaid} components={model.components} />
        {model.relationships.length > 0 && (
          <>
            <h3 style={{ marginTop: "1.5rem" }}>How components relate</h3>
            <ul>
              {model.relationships.map((r, i) => (
                <li key={i}>
                  <strong>{componentsById.get(r.source)?.name || r.source}</strong>
                  {" → "}
                  <strong>{componentsById.get(r.target)?.name || r.target}</strong>
                  {r.label ? <> — {r.label}</> : null}
                  {r.kind ? <span className="muted small"> ({r.kind})</span> : null}
                </li>
              ))}
            </ul>
          </>
        )}
      </section>

      <section id="components" className="section" aria-labelledby="components-h">
        <h2 id="components-h">Main components</h2>
        {model.components.length === 0 && <p className="muted">No components were identified in this analysis.</p>}
        <div className="component-grid">
        {model.components.map((c) => (
          <div className="component-card" key={c.id}>
            <div style={{ display: "flex", justifyContent: "space-between", gap: "1rem", flexWrap: "wrap", alignItems: "baseline" }}>
              <h3>{c.name}</h3>
              <div>
                <span className="chip chip-accent">{c.kind}</span>
                <span className={c.inferred ? "chip chip-indigo" : "chip"}>{c.inferred ? "Inferred" : "Observed"}</span>
                <span className="chip" title="Confidence in this identification">Confidence {Math.round((c.confidence ?? 0) * 100)}%</span>
              </div>
            </div>
            <p style={{ margin: ".6rem 0 0" }}>{c.responsibility}</p>
            {c.paths?.length > 0 && (
              <p className="small muted" style={{ margin: ".6rem 0 0" }}>
                Key paths: {c.paths.map((p) => <code key={p} style={{ marginRight: ".5rem" }}>{p}</code>)}
              </p>
            )}
            {c.evidence?.length > 0 && (
              <>
                <p className="small" style={{ margin: ".7rem 0 0", fontWeight: 650 }}>Source evidence</p>
                <EvidenceLinks refs={c.evidence} repoUrl={repo.html_url} branch={branch} />
              </>
            )}
          </div>
        ))}
        </div>
        <p className="small muted">
          <strong>Observed</strong> means the component was directly identified in source files.{" "}
          <strong>Inferred</strong> means it is an interpretation drawn from that evidence — treat it with more caution.
        </p>
      </section>

      <section id="detections" className="section" aria-labelledby="detections-h">
        <h2 id="detections-h">Detected technologies</h2>
        {model.detections.length === 0 ? <p className="muted">No frameworks, libraries or tooling were confidently detected.</p> : (
          <div className="card">
            {model.detections.map((d, i) => (
              <span className="chip" key={`${d.name}-${i}`} title={`${d.category} · confidence ${Math.round((d.confidence ?? 0) * 100)}%`}>
                {d.name} <span className="muted">· {d.category} · {Math.round((d.confidence ?? 0) * 100)}%</span>
              </span>
            ))}
            {model.detections.some((d) => d.evidence?.length) && (
              <div style={{ marginTop: ".75rem" }}>
                {model.detections.filter((d) => d.evidence?.length).map((d, i) => (
                  <div key={i} className="small" style={{ marginTop: ".5rem" }}>
                    <strong>{d.name}</strong>
                    <EvidenceLinks refs={d.evidence} repoUrl={repo.html_url} branch={branch} />
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </section>

      <section id="entry-points" className="section" aria-labelledby="entry-h">
        <h2 id="entry-h">Entry points &amp; key files</h2>
        <div className="two-col">
          <div className="card">
            <h3 style={{ marginTop: 0 }}>Entry points</h3>
            {model.entry_points?.length ? <EvidenceLinks refs={model.entry_points} repoUrl={repo.html_url} branch={branch} /> : <p className="muted">No explicit entry points were identified.</p>}
          </div>
          <div className="card">
            <h3 style={{ marginTop: 0 }}>Important files</h3>
            {model.files?.length ? (
              <ul style={{ margin: 0, paddingLeft: "1.1rem" }}>
                {model.files.slice(0, 15).map((f) => (
                  <li key={f.path} className="small">
                    <a href={`${repo.html_url.replace(/\/$/, "")}/blob/${branch}/${f.path}`} target="_blank" rel="noreferrer"><code>{f.path}</code></a>
                    {f.category ? <span className="muted"> · {f.category}</span> : null}
                  </li>
                ))}
              </ul>
            ) : <p className="muted">No file inventory was included.</p>}
          </div>
        </div>
      </section>

      <section id="limitations" className="section" aria-labelledby="limitations-h">
        <h2 id="limitations-h">Limitations &amp; unknowns</h2>
        <div className="callout" role="note">
          {model.limitations?.length ? (
            <ul style={{ margin: 0, paddingLeft: "1.2rem" }}>{model.limitations.map((l, i) => <li key={i}>{l}</li>)}</ul>
          ) : (
            <p style={{ margin: 0 }}>Static analysis only. Runtime behaviour cannot be confirmed without executing the project, which RepoLens does not do.</p>
          )}
        </div>
      </section>

      <section id="full-report" className="section" aria-labelledby="full-h">
        <h2 id="full-h">Full report</h2>
        <details className="report-details">
          <summary>Read the full Markdown report</summary>
          <div className="markdown-body" style={{ marginTop: "1rem" }}>
            {report.markdown ? (
              <ReactMarkdown remarkPlugins={[remarkGfm]}>{report.markdown}</ReactMarkdown>
            ) : (
              <p className="muted">No Markdown report was included in this payload. Use Download .md to fetch it from the API.</p>
            )}
          </div>
        </details>
        <div className="actions">
          <button className="btn btn-secondary btn-small" type="button" onClick={copyMarkdown}>{copied ? "Copied ✓" : "Copy Markdown"}</button>
          <button className="btn btn-secondary btn-small" type="button" onClick={downloadMarkdown}>Download .md</button>
        </div>
      </section>

      <section id="fresh" className="section" aria-labelledby="fresh-h">
        <h2 id="fresh-h">Fresh analysis</h2>
        <div className="card">
          <p style={{ marginTop: 0 }}>
            This report was generated on {fmtDate(analysedAt)}{sha ? <> from commit <span className="mono">{sha.slice(0, 7)}</span></> : null}.
            A fresh analysis re-inspects the repository&apos;s current default-branch commit ({branch}) and saves a new report version —
            useful if the project has changed since then.
          </p>
          {isSample ? (
            <p className="muted">Fresh analysis is disabled on the sample report. Submit the real repository from the home page to run one.</p>
          ) : (
            <FreshButton owner={repo.owner} repo={repo.name} />
          )}
        </div>
      </section>
      </div>
      </div>
    </article>
  );
}
