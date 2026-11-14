import Link from "next/link";
import UrlForm from "@/components/UrlForm";
import { getCatalogs, getCatalogSnapshots, type CatalogSnapshotRow, type CatalogSummary } from "@/lib/api";

export const dynamic = "force-dynamic";

const ORDER = ["python", "javascript", "react"];

function stars(n?: number) {
  if (typeof n !== "number") return "—";
  return n >= 1000 ? `${(n / 1000).toFixed(n >= 10000 ? 0 : 1).replace(/\.0$/, "")}k` : String(n);
}

async function loadHome(): Promise<{ catalogs: CatalogSummary[]; featured: CatalogSnapshotRow[] }> {
  try {
    const catalogs = await getCatalogs();
    const featured = await getCatalogSnapshots("python", { limit: 6 }).then((r) => r.snapshots).catch(() => []);
    return { catalogs, featured };
  } catch {
    return { catalogs: [], featured: [] };
  }
}

export default async function HomePage() {
  const { catalogs, featured } = await loadHome();
  const byEco = new Map(catalogs.map((c) => [c.ecosystem, c]));
  return (
    <div className="page">
      <section className="hero">
        <div>
          <p className="eyebrow">Architecture, without the cold start</p>
          <h1>Understand any codebase&rsquo;s architecture in minutes.</h1>
          <p className="lead">
            Paste a public GitHub URL. RepoLens returns a block diagram and a report you can
            actually read — entry points, modules, and the commit they came from.
          </p>
          <UrlForm />
          <p className="small muted hero-note">
            Existing reports are free. <Link href="/sample">Read the sample first</Link>
            {" "}or <Link href="/catalog">browse the catalog</Link>.
          </p>
        </div>
        <aside className="sketch" aria-hidden="true">
          <div className="sketch-top"><span>Block diagram</span><span>commit pinned</span></div>
          <div className="sketch-board">
            <div className="sketch-row">
              <div className="sketch-node"><strong>Entry</strong><span>CLI, HTTP, or main</span></div>
            </div>
            <div className="sketch-row">
              <div className="sketch-node hot"><strong>Core</strong><span>domain and orchestration</span></div>
              <div className="sketch-node"><strong>API</strong><span>routes and handlers</span></div>
            </div>
            <div className="sketch-row">
              <div className="sketch-node"><strong>Data</strong><span>stores and files</span></div>
              <div className="sketch-node"><strong>Outside</strong><span>services it calls</span></div>
            </div>
          </div>
        </aside>
      </section>

      <section className="band" aria-labelledby="catalog-h">
        <div className="band-head">
          <h2 id="catalog-h">Three catalogs, already read</h2>
          <Link href="/catalog">Open the full catalog</Link>
        </div>
        <div className="ecosystems">
          {ORDER.map((eco) => {
            const row = byEco.get(eco);
            const label = eco === "javascript" ? "JavaScript" : eco[0].toUpperCase() + eco.slice(1);
            return (
              <Link className="eco-card" key={eco} href={`/catalog?ecosystem=${eco}`}>
                <span className="small muted">{label}</span>
                <p className="eco-count">{row ? row.completed.toLocaleString() : "—"}</p>
                <span className="small">Pinned snapshots with a commit, a diagram, and a report.</span>
              </Link>
            );
          })}
        </div>
      </section>

      <section id="how-it-works" className="band" aria-labelledby="how-h">
        <h2 id="how-h">Free to read. Fresh when the code has moved.</h2>
        <div className="two-col">
          <div className="card">
            <span className="chip chip-accent">Free</span>
            <h3>Existing report</h3>
            <p className="muted">Open a stored analysis, read the diagram, and copy or download the Markdown. The commit and the date stay visible, so you know what was inspected.</p>
          </div>
          <div className="card">
            <span className="chip chip-indigo">One-time</span>
            <h3>Fresh analysis</h3>
            <p className="muted">Re-read the current default-branch commit, rebuild the diagram and the report, and keep the older version. You see the price before anything is charged.</p>
          </div>
        </div>
        <p className="small muted">Repository code is never executed. Findings are either observed in files or marked as inference.</p>
      </section>

      <section className="band" aria-labelledby="featured-h">
        <div className="band-head">
          <h2 id="featured-h">Start with a Python project</h2>
          <Link href="/catalog?ecosystem=python">More Python</Link>
        </div>
        {featured.length === 0 ? (
          <div className="card">
            <p>The catalog appears here when the API is running. The sample report is available either way.</p>
            <Link className="btn" href="/sample">Open the sample report</Link>
          </div>
        ) : (
          <div className="repo-grid">
            {featured.map((repo) => (
              <Link className="example-card" key={`${repo.owner}/${repo.name}`} href={`/report/${repo.owner}/${repo.name}`}>
                <span className="small muted mono">{repo.owner}/{repo.name}</span>
                <h3>{repo.name}</h3>
                <p>
                  <span className="chip">★ {stars(repo.stars)}</span>
                  {repo.language && <span className="chip chip-accent">{repo.language}</span>}
                </p>
                <span className="small mono">{repo.commit_sha.slice(0, 7)}</span>
              </Link>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
