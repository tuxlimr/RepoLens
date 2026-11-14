import Link from "next/link";
import ReportView from "@/components/ReportView";
import { ApiError, getReport } from "@/lib/api";
import type { ReportPayload } from "@/lib/types";

export const dynamic = "force-dynamic";

export async function generateMetadata({ params }: { params: Promise<{ owner: string; repo: string }> }) {
  const { owner, repo } = await params;
  return { title: `${owner}/${repo} — RepoLens report`, description: `Architecture report for ${owner}/${repo}.` };
}

export default async function ReportPage({
  params,
  searchParams,
}: {
  params: Promise<{ owner: string; repo: string }>;
  searchParams?: Promise<{ sample?: string }>;
}) {
  const { owner, repo } = await params;
  const sp = searchParams ? await searchParams : undefined;
  if (sp?.sample === "1" && owner === "psf" && repo === "requests") {
    const { SAMPLE_REPORT } = await import("@/lib/sample");
    return <ReportView report={SAMPLE_REPORT} isSample />;
  }
  let report: ReportPayload | null = null;
  let errorStatus: number | undefined;
  let unreachable = false;
  try {
    report = await getReport(owner, repo);
  } catch (err) {
    if (err instanceof ApiError) { errorStatus = err.status; unreachable = !!err.unreachable; }
  }

  if (!report) {
    const notFound = errorStatus === 404;
    return (
      <section style={{ maxWidth: 640, margin: "3rem auto", textAlign: "center" }}>
        <h1 style={{ letterSpacing: "-.025em" }}>{notFound ? "No report yet for this repository" : "We couldn't load this report"}</h1>
        <p className="muted">
          {notFound
            ? `${owner}/${repo} hasn't been analysed yet. Submit it from the home page and we'll build its first architecture report — viewing it afterwards is free.`
            : unreachable
              ? "The RepoLens backend isn't reachable right now. Make sure it's running, then refresh this page. You can still explore the sample report meanwhile."
              : "Something went wrong while loading this report. Please refresh, or head home and try again."}
        </p>
        <div className="actions" style={{ justifyContent: "center" }}>
          <Link className="btn" href="/">Analyse a repository</Link>
          <Link className="btn btn-secondary" href="/sample">View sample report</Link>
        </div>
        {notFound && (
          <p className="small muted">
            Looking for <span className="mono">psf/requests</span>? Its sample report is available instantly at{" "}
            <Link href="/sample">/sample</Link>.
          </p>
        )}
      </section>
    );
  }

  return <ReportView report={report} />;
}
