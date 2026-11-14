import Link from "next/link";
import { getCatalogs, getCatalogSnapshots } from "@/lib/api";

export const dynamic = "force-dynamic";

const ORDER = ["python", "javascript", "react"] as const;
const PAGE_SIZE = 24;

function label(eco: string) {
  if (eco === "javascript") return "JavaScript";
  return eco[0].toUpperCase() + eco.slice(1);
}
function stars(n: number) {
  return n >= 1000 ? `${(n / 1000).toFixed(n >= 10000 ? 0 : 1).replace(/\.0$/, "")}k` : String(n);
}

export default async function CatalogPage({
  searchParams,
}: {
  searchParams?: Promise<{ ecosystem?: string; q?: string; page?: string }>;
}) {
  const sp = searchParams ? await searchParams : {};
  const ecosystem = ORDER.includes(sp.ecosystem as (typeof ORDER)[number]) ? sp.ecosystem! : "python";
  const q = (sp.q || "").trim();
  const page = Math.max(1, Number(sp.page || "1") || 1);
  const offset = (page - 1) * PAGE_SIZE;

  let catalogs: Awaited<ReturnType<typeof getCatalogs>> = [];
  let snapshots: Awaited<ReturnType<typeof getCatalogSnapshots>> | null = null;
  let offline = false;
  try {
    catalogs = await getCatalogs();
    snapshots = await getCatalogSnapshots(ecosystem, { limit: PAGE_SIZE, offset, q });
  } catch {
    offline = true;
  }

  const total = snapshots?.total ?? 0;
  const pages = Math.max(1, Math.ceil(total / PAGE_SIZE));
  const href = (nextPage: number, eco = ecosystem) => {
    const params = new URLSearchParams({ ecosystem: eco, page: String(nextPage) });
    if (q) params.set("q", q);
    return `/catalog?${params.toString()}`;
  };

  return (
    <div className="page">
      <p className="eyebrow">The corpus</p>
      <h1 className="display" style={{ fontSize: "clamp(2.4rem, 5vw, 3.6rem)", margin: "0 0 .4rem" }}>
        Reports you can open now.
      </h1>
      <p className="lead muted" style={{ maxWidth: 640, marginTop: 0 }}>
        Each card is a static snapshot. The short hash is the commit that was actually downloaded.
      </p>

      <div className="ecosystems" style={{ marginTop: "1.2rem" }}>
        {ORDER.map((eco) => {
          const count = catalogs.find((c) => c.ecosystem === eco)?.completed;
          const active = eco === ecosystem;
          return (
            <Link key={eco} href={`/catalog?ecosystem=${eco}`} className="eco-card" aria-current={active ? "page" : undefined} style={active ? { borderColor: "#b5522a" } : undefined}>
              <span className="small muted">{label(eco)}</span>
              <p className="eco-count">{typeof count === "number" ? count.toLocaleString() : "—"}</p>
            </Link>
          );
        })}
      </div>

      <form className="catalog-bar" action="/catalog" method="get">
        <input type="hidden" name="ecosystem" value={ecosystem} />
        <label className="sr-only" htmlFor="catalog-q">Search {label(ecosystem)} repositories</label>
        <input id="catalog-q" name="q" defaultValue={q} placeholder={`Search ${label(ecosystem)} by owner or name`} />
        <button className="btn" type="submit">Search</button>
      </form>

      {offline && (
        <div className="empty-state card">
          <h2>The catalog API is not reachable</h2>
          <p className="muted">Start the backend, then refresh. The sample report still opens without it.</p>
          <Link className="btn" href="/sample">Open the sample</Link>
        </div>
      )}

      {!offline && snapshots && snapshots.snapshots.length === 0 && (
        <div className="empty-state card">
          <h2>Nothing matches</h2>
          <p className="muted">Try another name, or clear the search.</p>
          <Link className="btn btn-secondary" href={`/catalog?ecosystem=${ecosystem}`}>Clear search</Link>
        </div>
      )}

      {snapshots && snapshots.snapshots.length > 0 && (
        <>
          <p className="small muted">{total.toLocaleString()} repositories{q ? ` matching “${q}”` : ""}.</p>
          <div className="repo-grid">
            {snapshots.snapshots.map((repo) => (
              <Link className="example-card" key={`${repo.owner}/${repo.name}`} href={`/report/${repo.owner}/${repo.name}`}>
                <span className="small muted mono">{repo.owner}/{repo.name}</span>
                <h3>{repo.name}</h3>
                <p>
                  <span className="chip">★ {stars(repo.stars)}</span>
                  {repo.language && <span className="chip chip-accent">{repo.language}</span>}
                </p>
                <span className="small mono" title={repo.commit_sha}>{repo.commit_sha.slice(0, 7)}</span>
              </Link>
            ))}
          </div>
          <div className="pager">
            {page > 1 ? <Link className="btn btn-secondary" href={href(page - 1)}>Previous</Link> : <span />}
            <span className="small muted">Page {page} of {pages}</span>
            {page < pages ? <Link className="btn btn-secondary" href={href(page + 1)}>Next</Link> : <span />}
          </div>
        </>
      )}
    </div>
  );
}
