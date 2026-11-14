# Project structure: cloudflare/security-audit-skill

**Analysed commit:** `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`

**Commit reference:** [c1c8a8c1471069fb0e188eeaff69b8e8db6564a8](https://github.com/cloudflare/security-audit-skill/commit/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8)

**Tree at this commit:** [cloudflare/security-audit-skill@c1c8a8c14710](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cloudflare/security-audit-skill |
| Description | A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings |
| Stars | 72484 |
| Forks | 4840 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8` |
| Retrieved at | 2026-11-14T19:10:33.869637+00:00 |
| Files in this snapshot | 22 |

## Directory tree

```text
skills/  (20 files)
  security-audit/  (20 files)
    AI-AND-LLM.md
    ATTACK-CLASSES.md
    CLIENT-SIDE.md
    CLOUD-AND-DEPLOYMENT.md
    DATA-ISOLATION-AND-LIFECYCLE.md
    DESKTOP-MOBILE-AND-LOCAL-IPC.md
    HUNTING.md
    MEMORY-SAFETY-AND-BINARY.md
    PROTOCOLS-RPC-AND-MESSAGING.md
    RECONNAISSANCE.md
    RESOURCE-EXHAUSTION-AND-AVAILABILITY.md
    SKILL.md
    SUPPLY-CHAIN-AND-RELEASE.md
    VALIDATION-AND-REPORTING.md
    WEB-PROTOCOL-AND-AUTH.md
    report-schema.json
    validate-coverage-ledger.cjs
    validate-coverage-ledger.test.cjs
    validate-findings.cjs
    validate-findings.test.cjs
LICENSE
README.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 4 file(s) under skills package (observed from repository paths and static analysis). |

## Important files

- `skills/security-audit/report-schema.json` (config)

## Top-level layout

- `skills` — 20 analysed file(s)
- `(root files)` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8` is the revision these paths and observations refer to.
