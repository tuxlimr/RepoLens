"use client";

import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { analyzeRepo, getAnalysis, isTerminalFailure, isTerminalSuccess, parseGithubUrl, ApiError } from "@/lib/api";

type Phase = "idle" | "submitting" | "queued" | "working" | "done" | "error";

export default function UrlForm() {
  const router = useRouter();
  const [url, setUrl] = useState("");
  const [phase, setPhase] = useState<Phase>("idle");
  const [statusText, setStatusText] = useState("");
  const [error, setError] = useState("");
  const timer = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => () => { if (timer.current) clearInterval(timer.current); }, []);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");
    const parsed = parseGithubUrl(url);
    if (!parsed) {
      setPhase("error");
      setError("Please enter a valid public GitHub repository URL, e.g. https://github.com/psf/requests");
      return;
    }
    const canonical = `https://github.com/${parsed.owner}/${parsed.repo}`;
    setPhase("submitting");
    setStatusText("Checking for an existing report…");
    try {
      const res = await analyzeRepo(canonical, false);
      if (res.status === "cached" || res.report) {
        setPhase("done");
        setStatusText("Found an existing report — opening it now.");
        router.push(`/report/${parsed.owner}/${parsed.repo}`);
        return;
      }
      if (!res.analysis_id) {
        // Backend queued without an id: try opening the report route after a short wait.
        setPhase("error");
        setError("The backend accepted the request but returned no analysis ID. Please try again.");
        return;
      }
      setPhase("queued");
      setStatusText("Analysis queued. This usually takes under a minute…");
      const id = res.analysis_id;
      let attempts = 0;
      timer.current = setInterval(async () => {
        attempts += 1;
        try {
          const st = await getAnalysis(id);
          const s = (st.status || "").toLowerCase();
          if (isTerminalSuccess(s)) {
            if (timer.current) clearInterval(timer.current);
            setPhase("done");
            setStatusText("Analysis complete — opening your report.");
            router.push(`/report/${parsed.owner}/${parsed.repo}`);
          } else if (isTerminalFailure(s)) {
            if (timer.current) clearInterval(timer.current);
            setPhase("error");
            setError(st.error || st.message || "Analysis failed. Please try a different repository or try again later.");
          } else {
            setPhase("working");
            setStatusText(
              s.includes("clone") || s.includes("fetch")
                ? "Fetching repository metadata and file inventory…"
                : s.includes("analys") || s.includes("analyz") || s.includes("process") || s.includes("running")
                  ? "Inspecting structure, entry points and dependencies…"
                  : "Analysis in progress — building diagram and report…",
            );
          }
        } catch (err) {
          if (attempts > 3 && err instanceof ApiError && err.unreachable) {
            if (timer.current) clearInterval(timer.current);
            setPhase("error");
            setError(err.message);
          }
        }
        if (attempts >= 90) {
          if (timer.current) clearInterval(timer.current);
          setPhase("error");
          setError("Analysis is taking longer than expected. It may still finish — try opening the report from the home page in a minute, or submit again.");
        }
      }, 2000);
    } catch (err) {
      setPhase("error");
      setError(err instanceof Error ? err.message : "Something went wrong. Please try again.");
    }
  }

  const busy = phase === "submitting" || phase === "queued" || phase === "working";
  return (
    <div className="url-panel">
      <form className="url-form" onSubmit={onSubmit} noValidate>
        <label htmlFor="repo-url">Public GitHub repository URL</label>
        <input
          id="repo-url"
          name="url"
          type="url"
          inputMode="url"
          autoComplete="url"
          placeholder="https://github.com/psf/requests"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          aria-describedby="url-help url-status"
          disabled={busy}
        />
        <button className="btn" type="submit" disabled={busy}>
          {busy ? <><span className="spinner" aria-hidden="true" /> Working…</> : "Analyse repository"}
        </button>
      </form>
      <p id="url-help" className="small muted" style={{ textAlign: "left", marginBottom: 0 }}>
        Public repositories only. If a report already exists you&apos;ll see it instantly, free.
      </p>
      <div id="url-status" aria-live="polite">
        {busy || phase === "done" ? (
          <div className="alert alert-status" role="status">
            <strong>{phase === "done" ? "Done" : phase === "submitting" ? "Checking…" : phase === "queued" ? "Queued" : "Analysing…"}</strong>
            <p style={{ margin: ".35rem 0 0" }}>{statusText}</p>
            {busy && (
              <ul className="progress-steps">
                <li className={phase === "submitting" ? "active" : ""}>1. Check for an existing report</li>
                <li className={phase === "queued" ? "active" : ""}>2. Queue a new analysis</li>
                <li className={phase === "working" ? "active" : ""}>3. Inspect code &amp; build report</li>
              </ul>
            )}
          </div>
        ) : null}
        {phase === "error" && error ? (
          <div className="alert alert-error" role="alert"><strong>Couldn&apos;t analyse that repository.</strong><p style={{ margin: ".35rem 0 0" }}>{error}</p></div>
        ) : null}
      </div>
    </div>
  );
}
