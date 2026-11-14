/** Types mirroring the RepoLens backend API contract (see backend/app/models.py). */

export interface Repository {
  owner: string;
  name: string;
  full_name: string;
  html_url: string;
  description?: string | null;
  stars: number;
  forks: number;
  open_issues?: number;
  language?: string | null;
  license?: string | null;
  default_branch: string;
  commit_sha?: string | null;
  topics?: string[];
  created_at?: string | null;
  updated_at?: string | null;
  retrieved_at?: string | null;
  [key: string]: unknown;
}

export interface SourceRef {
  path: string;
  start_line?: number | null;
  end_line?: number | null;
  url?: string | null;
}

export type Evidence = SourceRef;

export interface Component {
  id: string;
  name: string;
  kind: string;
  responsibility: string;
  paths: string[];
  evidence: Evidence[];
  confidence: number;
  inferred: boolean;
}

export interface Relationship {
  source: string;
  target: string;
  label: string;
  kind: string;
}

export interface Detection {
  name: string;
  category: string;
  confidence: number;
  evidence: Evidence[];
}

export interface FileInfo {
  path: string;
  size?: number;
  category?: string;
  language?: string | null;
}

export interface ArchitectureModel {
  components: Component[];
  relationships: Relationship[];
  detections: Detection[];
  entry_points: SourceRef[];
  files: FileInfo[];
  limitations: string[];
  summary: string;
  stats: Record<string, unknown>;
}

export interface ReportPayload {
  id: string | number;
  version: number | string;
  commit_sha?: string | null;
  analysed_at?: string | null;
  analyzed_at?: string | null;
  repository: Repository;
  model: ArchitectureModel;
  mermaid: string;
  markdown: string;
}

export interface AnalyzeResponse {
  status: "cached" | "queued" | string;
  analysis_id?: string | number | null;
  report?: ReportPayload | null;
  message?: string;
  [key: string]: unknown;
}

export interface AnalysisStatusResponse {
  id?: string | number;
  analysis_id?: string | number;
  status: string;
  error?: string | null;
  message?: string | null;
  owner?: string;
  repo?: string;
  repository?: { owner?: string; name?: string; full_name?: string } | null;
  report?: ReportPayload | null;
  [key: string]: unknown;
}

export interface ExampleRepo {
  owner: string;
  name: string;
  description?: string | null;
  stars?: number;
  language?: string | null;
  topics?: string[];
}

export interface PaymentInfo {
  amount_cents: number;
  status: string;
  currency?: string;
  mock?: boolean;
  provider?: string;
  [key: string]: unknown;
}

export interface FreshPaymentResponse {
  payment: PaymentInfo;
  analysis_id: string | number;
  [key: string]: unknown;
}
