import type { Metadata } from "next";
import Link from "next/link";
import { Fraunces, Outfit } from "next/font/google";
import "./globals.css";

const outfit = Outfit({ subsets: ["latin"], variable: "--font-sans" });
const fraunces = Fraunces({ subsets: ["latin"], variable: "--font-display" });

export const metadata: Metadata = {
  title: "RepoLens — Understand any codebase's architecture",
  description:
    "Paste a public GitHub repository and get a readable architecture diagram and Markdown report, backed by source evidence.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${outfit.variable} ${fraunces.variable}`}>
      <body>
        <a className="skip-link" href="#main">Skip to content</a>
        <header className="site-header">
          <div className="site-header-inner">
            <Link className="brand" href="/">
              <span className="brand-mark" aria-hidden="true" />
              Repo<span>Lens</span>
            </Link>
            <nav className="nav-links" aria-label="Primary">
              <Link href="/catalog">Catalog</Link>
              <Link href="/sample">Sample</Link>
              <Link href="/#how-it-works">How it works</Link>
            </nav>
          </div>
        </header>
        <main id="main">{children}</main>
        <footer className="site-footer">
          <div className="container footer-grid">
            <div>
              <p className="brand footer-brand">Repo<span>Lens</span></p>
              <p>
                An automated reading of a public repository&apos;s architecture.
                Not a security audit, and not a guarantee of completeness.
              </p>
            </div>
            <div>
              <p className="footer-label">Look around</p>
              <p><Link href="/catalog">Browse the catalog</Link></p>
              <p><Link href="/sample">Read the sample report</Link></p>
            </div>
            <div>
              <p className="footer-label">Boundary</p>
              <p>Public repositories only. Source is linked, not copied. Repository code is never executed.</p>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
