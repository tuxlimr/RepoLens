import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "RepoLens — Understand any codebase's architecture",
  description:
    "Paste a public GitHub repository and get a readable architecture diagram and Markdown report, backed by source evidence.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <a className="skip-link" href="#main">Skip to content</a>
        <header className="site-header">
          <div className="site-header-inner">
            <Link className="brand" href="/">Repo<span>Lens</span></Link>
            <nav className="nav-links" aria-label="Primary">
              <Link href="/sample">Sample report</Link>
              <Link href="/#examples">Examples</Link>
              <Link href="/#how-it-works">How it works</Link>
            </nav>
          </div>
        </header>
        <main id="main" className="container">{children}</main>
        <footer className="site-footer">
          <div className="container">
            <p>
              <strong>RepoLens</strong> produces an automated interpretation of a public
              repository&apos;s architecture. It is not a security audit, and it is not a
              guarantee of completeness — always verify important claims against the linked source.
            </p>
            <p>Public repositories only. No repository code is executed during analysis.</p>
          </div>
        </footer>
      </body>
    </html>
  );
}
