# Project structure: minimaxir/big-list-of-naughty-strings

**Analysed commit:** `db33ec7b1d5d9616a88c76394b7d0897bd0b97eb`

**Commit reference:** [db33ec7b1d5d9616a88c76394b7d0897bd0b97eb](https://github.com/minimaxir/big-list-of-naughty-strings/commit/db33ec7b1d5d9616a88c76394b7d0897bd0b97eb)

**Tree at this commit:** [minimaxir/big-list-of-naughty-strings@db33ec7b1d5d](https://github.com/minimaxir/big-list-of-naughty-strings/tree/db33ec7b1d5d9616a88c76394b7d0897bd0b97eb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | minimaxir/big-list-of-naughty-strings |
| Description | The Big List of Naughty Strings is a list of strings which have a high probability of causing issues when used as user-input data. |
| Stars | 47716 |
| Forks | 2144 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `db33ec7b1d5d9616a88c76394b7d0897bd0b97eb` |
| Retrieved at | 2026-11-14T19:06:35.286806+00:00 |
| Files in this snapshot | 16 |

## Directory tree

```text
naughtystrings/  (6 files)
  internal/  (1 files)
    resource.go
  Makefile
  __init__.py
  go.mod
  naughtystrings.go
  naughtystrings_test.go
scripts/  (2 files)
  texttobase64.sh
  txt_to_json.py
.gitattributes
LICENSE
README.md
blns.base64.json
blns.base64.txt
blns.json
blns.txt
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| naughtystrings package | library | Observed | Groups 4 file(s) under naughtystrings package (observed from repository paths and static analysis). Observed top-level functions: naughty_strings. |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `blns.base64.json` (config)
- `blns.json` (config)
- `naughtystrings/go.mod` (manifest)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 8 analysed file(s)
- `naughtystrings` — 6 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `db33ec7b1d5d9616a88c76394b7d0897bd0b97eb` is the revision these paths and observations refer to.
