"use client";

import { useEffect, useId, useRef, useState } from "react";
import type { Component } from "@/lib/types";

export default function MermaidDiagram({ source, components }: { source: string; components: Component[] }) {
  const ref = useRef<HTMLDivElement>(null);
  const reactId = useId().replace(/[^a-zA-Z0-9]/g, "");
  const [error, setError] = useState<string>("");
  const [rendered, setRendered] = useState(false);

  useEffect(() => {
    let cancelled = false;
    async function render() {
      if (!source?.trim()) { setError("No diagram source was provided for this report."); return; }
      try {
        const mermaid = (await import("mermaid")).default;
        mermaid.initialize({ startOnLoad: false, theme: "neutral", securityLevel: "strict", flowchart: { useMaxWidth: true } });
        const { svg } = await mermaid.render(`repolens-${reactId}`, source);
        if (!cancelled && ref.current) {
          ref.current.innerHTML = svg;
          setRendered(true);
        }
      } catch (err) {
        if (!cancelled) setError(err instanceof Error ? err.message : "Diagram could not be rendered.");
      }
    }
    render();
    return () => { cancelled = true; };
  }, [source, reactId]);

  if (error) {
    return (
      <div>
        <div className="alert alert-error" role="alert">
          <strong>The architecture diagram couldn&apos;t be rendered.</strong>
          <p style={{ margin: ".35rem 0 0" }}>Here are the components in text form instead. The raw diagram source is below.</p>
        </div>
        <ul>
          {components.map((c) => (
            <li key={c.id}><strong>{c.name}</strong> — {c.responsibility}</li>
          ))}
        </ul>
        <pre className="source" aria-label="Mermaid diagram source">{source}</pre>
      </div>
    );
  }

  return (
    <div>
      <div className="diagram-wrap" role="img" aria-label="Architecture diagram. A textual list of components follows below." ref={ref}>
        {!rendered && <p className="muted"><span className="spinner dark" aria-hidden="true" /> Rendering diagram…</p>}
      </div>
      <details style={{ marginTop: ".75rem" }}>
        <summary className="small" style={{ cursor: "pointer", fontWeight: 650 }}>View diagram source (Mermaid)</summary>
        <pre className="source">{source}</pre>
      </details>
      <div className="sr-only">
        <h3>Components in this diagram</h3>
        <ul>{components.map((c) => <li key={c.id}>{c.name}: {c.responsibility}</li>)}</ul>
      </div>
    </div>
  );
}
