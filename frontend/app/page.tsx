import Link from "next/link";
import UrlForm from "@/components/UrlForm";
import { getExamples } from "@/lib/api";
import { SAMPLE_EXAMPLES } from "@/lib/sample";
import type { ExampleRepo } from "@/lib/types";

export const dynamic = "force-dynamic";

async function loadExamples(): Promise<{ examples: ExampleRepo[]; live: boolean }> {
  try {
    const data = await getExamples();
    if (Array.isArray(data) && data.length) return { examples: data, live: true };
  } catch { /* backend offline — fall back to static list */ }
  return { examples: SAMPLE_EXAMPLES, live: false };
}

export default async function HomePage() {
  const { examples, live } = await loadExamples();
  return (
    <>
      <section className="hero">
        <h1>Understand any codebase&rsquo;s architecture in minutes.</h1>
        <p className="lead">
          Paste a public GitHub repository. RepoLens inspects its structure and returns a clear
          architecture diagram plus a readable, evidence-backed report you can share with your team.
        </p>
        <UrlForm />
        <p className="small muted" style={{ marginTop: "1rem" }}>
          No account needed to view an existing report.{" "}
          <Link href="/sample">Explore the sample report first →</Link>
        </p>
      </section>

      <section id="how-it-works" className="section" aria-labelledby="how-h">
        <h2 id="how-h">Free reports vs. fresh analysis</h2>
        <div className="two-col">
          <div className="card">
            <span className="chip chip-accent">Free</span>
            <h3 style={{ margin: ".6rem 0 .4rem" }}>Existing report</h3>
            <p className="muted" style={{ margin: 0 }}>
              If we&apos;ve already analysed a repository, you can read its diagram and report and
              copy or download the Markdown at no cost. The report always shows the commit and date
              it was generated from, so you know exactly how current it is.
            </p>
          </div>
          <div className="card">
            <span className="chip chip-indigo">Paid · one-time</span>
            <h3 style={{ margin: ".6rem 0 .4rem" }}>Fresh analysis</h3>
            <p className="muted" style={{ margin: 0 }}>
              Want the current state of the code? A fresh analysis re-inspects the repository&apos;s
              latest default-branch commit, rebuilds the diagram and report, and saves it as a new
              version. Pricing is shown before you pay — no subscription, no surprises.
            </p>
          </div>
        </div>
        <div className="two-col" style={{ marginTop: "1rem" }}>
          <div className="card">
            <h3 style={{ marginTop: 0 }}>Supported today</h3>
            <p style={{ margin: 0 }}><span className="chip chip-accent">Python</span> <span className="muted">Public GitHub repositories, with framework and tooling detection.</span></p>
          </div>
          <div className="card">
            <h3 style={{ marginTop: 0 }}>Coming later</h3>
            <p style={{ margin: 0 }}><span className="chip">JavaScript / TypeScript</span> <span className="chip">React</span> <span className="muted">Planned once Python report quality is proven.</span></p>
          </div>
        </div>
        <p className="small muted" style={{ marginTop: "1rem" }}>
          How it works: we fetch repository metadata and a file inventory, identify entry points,
          modules and dependencies from source evidence, then generate a Mermaid diagram and a
          structured report. We never execute repository code.
        </p>
      </section>

      <section id="examples" className="section" aria-labelledby="examples-h">
        <h2 id="examples-h">Example repositories</h2>
        <p className="muted">
          Start with a well-known project to see what a report looks like.
          {!live && " (Showing a starter list — the live catalogue will appear when the backend is running.)"}
        </p>
        <div className="grid">
          {examples.map((ex) => {
            const isRequests = ex.owner === "psf" && ex.name === "requests";
            const href = isRequests ? "/sample" : `/report/${ex.owner}/${ex.name}`;
            return (
              <Link className="example-card" key={`${ex.owner}/${ex.name}`} href={href}>
                <span className="small muted mono">{ex.owner}/{ex.name}</span>
                <h3>{ex.name}</h3>
                <p>{ex.description || "Open-source repository"}</p>
                <p className="small">
                  {ex.language && <span className="chip chip-accent">{ex.language}</span>}
                  {typeof ex.stars === "number" && <span className="chip">★ {ex.stars >= 1000 ? `${(ex.stars / 1000).toFixed(1).replace(/\.0$/, "")}k` : ex.stars}</span>}
                  {isRequests && <span className="chip chip-indigo">Sample report available</span>}
                </p>
                <span className="small">{isRequests ? "View sample report →" : "View report →"}</span>
              </Link>
            );
          })}
        </div>
        <div className="card" style={{ marginTop: "1rem", textAlign: "center" }}>
          <strong>See the full format before you submit anything</strong>
          <p className="muted">The sample report for psf/requests works with no backend and no sign-up.</p>
          <Link className="btn" href="/sample">Open the sample report</Link>
        </div>
      </section>
    </>
  );
}
