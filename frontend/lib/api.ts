import type {
  AnalysisStatusResponse,
  AnalyzeResponse,
  ExampleRepo,
  FreshPaymentResponse,
  ReportPayload,
} from "./types";

export const API_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export class ApiError extends Error {
  status?: number;
  unreachable?: boolean;
  constructor(message: string, opts?: { status?: number; unreachable?: boolean }) {
    super(message);
    this.name = "ApiError";
    this.status = opts?.status;
    this.unreachable = opts?.unreachable;
  }
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  let res: Response;
  try {
    res = await fetch(`${API_URL}${path}`, {
      ...init,
      headers: { "Content-Type": "application/json", ...(init?.headers || {}) },
      cache: "no-store",
    });
  } catch {
    throw new ApiError(
      `Cannot reach the RepoLens backend at ${API_URL}. Is it running? Start it and try again.`,
      { unreachable: true },
    );
  }
  if (!res.ok) {
    let detail = "";
    try {
      const body: unknown = await res.json();
      if (body && typeof body === "object") {
        const b = body as Record<string, unknown>;
        detail = String(b.detail ?? b.error ?? b.message ?? "");
      }
    } catch {
      try { detail = await res.text(); } catch { /* ignore */ }
    }
    throw new ApiError(detail || `Request failed (${res.status})`, { status: res.status });
  }
  return (await res.json()) as T;
}

export function parseGithubUrl(input: string): { owner: string; repo: string } | null {
  const trimmed = input.trim();
  if (!trimmed) return null;
  // Accept https://github.com/owner/repo(.git)(/...) and owner/repo shorthand is NOT accepted.
  try {
    const withProtocol = /^https?:\/\//i.test(trimmed) ? trimmed : `https://${trimmed}`;
    const url = new URL(withProtocol);
    if (url.hostname !== "github.com" && url.hostname !== "www.github.com") return null;
    const parts = url.pathname.split("/").filter(Boolean);
    if (parts.length < 2) return null;
    const owner = parts[0];
    const repo = parts[1].replace(/\.git$/i, "");
    if (!/^[A-Za-z0-9_.-]+$/.test(owner) || !/^[A-Za-z0-9_.-]+$/.test(repo)) return null;
    return { owner, repo };
  } catch {
    return null;
  }
}

export function analyzeRepo(url: string, fresh = false): Promise<AnalyzeResponse> {
  return request<AnalyzeResponse>("/api/analyze", {
    method: "POST",
    body: JSON.stringify({ url, fresh }),
  });
}

export function getAnalysis(id: string | number): Promise<AnalysisStatusResponse> {
  return request<AnalysisStatusResponse>(`/api/analyses/${encodeURIComponent(String(id))}`);
}

export function getReport(owner: string, repo: string): Promise<ReportPayload> {
  return request<ReportPayload>(
    `/api/reports/${encodeURIComponent(owner)}/${encodeURIComponent(repo)}`,
  );
}

export async function getReportMarkdown(owner: string, repo: string): Promise<string> {
  let res: Response;
  try {
    res = await fetch(
      `${API_URL}/api/reports/${encodeURIComponent(owner)}/${encodeURIComponent(repo)}/markdown`,
      { cache: "no-store" },
    );
  } catch {
    throw new ApiError(`Cannot reach the RepoLens backend at ${API_URL}.`, { unreachable: true });
  }
  if (!res.ok) throw new ApiError(`Could not load Markdown (${res.status})`, { status: res.status });
  return res.text();
}

export function getExamples(): Promise<ExampleRepo[]> {
  return request<ExampleRepo[]>("/api/examples");
}

export function startFreshPayment(url: string): Promise<FreshPaymentResponse> {
  return request<FreshPaymentResponse>("/api/payments/fresh", {
    method: "POST",
    body: JSON.stringify({ url }),
  });
}

export function isTerminalSuccess(status: string): boolean {
  return ["completed", "complete", "done", "succeeded", "success", "finished", "cached", "ready"].includes(status.toLowerCase());
}
export function isTerminalFailure(status: string): boolean {
  return ["failed", "error", "cancelled", "canceled"].includes(status.toLowerCase());
}
