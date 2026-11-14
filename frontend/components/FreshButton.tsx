"use client";

import { useEffect, useRef, useState } from "react";
import { getAnalysis, isTerminalFailure, isTerminalSuccess, startFreshPayment } from "@/lib/api";

export default function FreshButton({ owner, repo }: { owner: string; repo: string }) {
  const [phase, setPhase] = useState<"idle" | "paying" | "working" | "error">("idle");
  const [message, setMessage] = useState("");
  const [isMock, setIsMock] = useState(false);
  const timer = useRef<ReturnType<typeof setInterval> | null>(null);
  useEffect(() => () => { if (timer.current) clearInterval(timer.current); }, []);

  async function onClick() {
    setPhase("paying");
    setMessage("Starting fresh analysis…");
    const url = `https://github.com/${owner}/${repo}`;
    try {
      const res = await startFreshPayment(url);
      const mock =
        res.payment?.mock === true ||
        /mock|demo|sandbox/i.test(String(res.payment?.status ?? "")) ||
        /mock|demo/i.test(String(res.payment?.provider ?? ""));
      setIsMock(mock);
      const price =
        typeof res.payment?.amount_cents === "number"
          ? ` ($${(res.payment.amount_cents / 100).toFixed(2)})`
          : "";
      setMessage(
        mock
          ? `Demo / mock checkout${price} — no real payment was taken. Fresh analysis queued; this page will reload when it's ready.`
          : `Payment confirmed${price}. Fresh analysis queued; this page will reload when it's ready.`,
      );
      setPhase("working");
      let attempts = 0;
      timer.current = setInterval(async () => {
        attempts += 1;
        try {
          const st = await getAnalysis(res.analysis_id);
          const s = (st.status || "").toLowerCase();
          if (isTerminalSuccess(s)) {
            if (timer.current) clearInterval(timer.current);
            window.location.reload();
          } else if (isTerminalFailure(s)) {
            if (timer.current) clearInterval(timer.current);
            setPhase("error");
            setMessage(st.error || st.message || "Fresh analysis failed. Please try again.");
          } else {
            setMessage("Fresh analysis in progress — inspecting the current commit and rebuilding the report…");
          }
        } catch { /* keep polling through transient errors */ }
        if (attempts >= 90) {
          if (timer.current) clearInterval(timer.current);
          setPhase("error");
          setMessage("Fresh analysis is taking longer than expected. Refresh this page in a minute to check for the new version.");
        }
      }, 2000);
    } catch (err) {
      setPhase("error");
      setMessage(err instanceof Error ? err.message : "Could not start a fresh analysis.");
    }
  }

  const busy = phase === "paying" || phase === "working";
  return (
    <div>
      <button className="btn" type="button" onClick={onClick} disabled={busy}>
        {busy ? <><span className="spinner" aria-hidden="true" /> Fresh analysis running…</> : "Run fresh analysis"}
      </button>
      <p className="small muted" style={{ marginTop: ".5rem" }}>
        Paid, one-time. Re-analyses the repository&apos;s current default-branch commit and saves a new
        report version. You&apos;ll see exactly what will be analysed before anything is charged
        {isMock ? " — in this demo, checkout is mocked and no real payment is taken." : "."}
      </p>
      <div aria-live="polite">
        {message && phase !== "idle" && (
          <div className={phase === "error" ? "alert alert-error" : "alert alert-status"} role={phase === "error" ? "alert" : "status"}>
            {isMock && phase !== "error" ? <strong>Demo / mock checkout. </strong> : null}
            {message}
          </div>
        )}
      </div>
    </div>
  );
}
