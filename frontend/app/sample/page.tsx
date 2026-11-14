import type { Metadata } from "next";
import ReportView from "@/components/ReportView";
import { SAMPLE_REPORT } from "@/lib/sample";

export const metadata: Metadata = {
  title: "Sample report · psf/requests — RepoLens",
  description: "A hand-written sample RepoLens architecture report for psf/requests.",
};

export default function SamplePage() {
  return <ReportView report={SAMPLE_REPORT} isSample />;
}
