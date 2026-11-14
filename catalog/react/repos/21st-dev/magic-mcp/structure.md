# Project structure: 21st-dev/magic-mcp

**Analysed commit:** `6b5299e8a83ceffa73d4fc4e148905bb3eeeeb55`

**Commit reference:** [6b5299e8a83ceffa73d4fc4e148905bb3eeeeb55](https://github.com/21st-dev/magic-mcp/commit/6b5299e8a83ceffa73d4fc4e148905bb3eeeeb55)

**Tree at this commit:** [21st-dev/magic-mcp@6b5299e8a83c](https://github.com/21st-dev/magic-mcp/tree/6b5299e8a83ceffa73d4fc4e148905bb3eeeeb55)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | 21st-dev/magic-mcp |
| Description | It's like v0, but in your Cursor / Claude Code / Windsurf: search 10,000+ React/Tailwind components, generate new UI with AI, and publish your own — right from your editor. Magic MCP is now the 21st MCP; this package keeps old configs working. Setup: 21st.dev/mcp |
| Stars | 6531 |
| Forks | 534 |
| Licence | ISC |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `6b5299e8a83ceffa73d4fc4e148905bb3eeeeb55` |
| Retrieved at | 2026-11-14T19:14:03.858780+00:00 |
| Files in this snapshot | 19 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.codex-plugin/  (1 files)
  plugin.json
.cursor-plugin/  (1 files)
  plugin.json
.github/  (1 files)
  workflows/  (1 files)
    npm-publish.yml
skills/  (1 files)
  21st-ui/  (1 files)
    SKILL.md
src/  (1 files)
  index.ts
.gitignore
.mcp.json
Dockerfile
LICENSE
README.md
llms-install.md
mcp.json
package.json
server.json
smithery.yaml
tsconfig.json
```

## Entry points

- [src/index.ts](https://github.com/21st-dev/magic-mcp/blob/6b5299e8a83ceffa73d4fc4e148905bb3eeeeb55/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.cursor-plugin/plugin.json` (config)
- `.github/workflows/npm-publish.yml` (ci)
- `.mcp.json` (config)
- `Dockerfile` (container)
- `mcp.json` (config)
- `package.json` (manifest)
- `server.json` (config)
- `smithery.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 11 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)
- `.cursor-plugin` — 1 analysed file(s)
- `.github` — 1 analysed file(s)
- `skills` — 1 analysed file(s)
- `src` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6b5299e8a83ceffa73d4fc4e148905bb3eeeeb55` is the revision these paths and observations refer to.
