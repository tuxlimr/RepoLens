# Project structure: 0xAX/linux-insides

**Analysed commit:** `4fa356494fa6de2143dbfbd729e66bf469439ca3`

**Commit reference:** [4fa356494fa6de2143dbfbd729e66bf469439ca3](https://github.com/0xAX/linux-insides/commit/4fa356494fa6de2143dbfbd729e66bf469439ca3)

**Tree at this commit:** [0xAX/linux-insides@4fa356494fa6](https://github.com/0xAX/linux-insides/tree/4fa356494fa6de2143dbfbd729e66bf469439ca3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | 0xAX/linux-insides |
| Description | A book-in-progress about the Linux kernel and its insides. |
| Stars | 33756 |
| Forks | 3578 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `4fa356494fa6de2143dbfbd729e66bf469439ca3` |
| Retrieved at | 2026-11-14T19:07:00.557485+00:00 |
| Files in this snapshot | 141 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (2 files)
    content-issue.yml
    question.yml
  workflows/  (5 files)
    check-code-snippets.yaml
    check-links.yaml
    generate-e-books.yaml
    labeler.yaml
    release-e-books.yaml
  FUNDING.yml
  dependabot.yaml
  labeler.yml
  labels.yml
  pull-request-template.md
Assets/  (1 files)
  banner.svg
Booting/  (17 files)
  images/  (10 files)
    early-4g-page-tables.svg
    early-bss.svg
    early-heap.svg
    early-page-table.svg
    early-stack.svg
    kernel-relocation-2.svg
    kernel-relocation.svg
    segment-descriptor.svg
    segment-selector.svg
    startup_32.svg
  README.md
  linux-bootstrap-1.md
  linux-bootstrap-2.md
  linux-bootstrap-3.md
  linux-bootstrap-4.md
  linux-bootstrap-5.md
  linux-bootstrap-6.md
Cgroups/  (2 files)
  README.md
  linux-cgroups-1.md
Concepts/  (5 files)
  README.md
  linux-cpu-1.md
  linux-cpu-2.md
  linux-cpu-3.md
  linux-cpu-4.md
Contributing/  (1 files)
  linux-contributing-1.md
DataStructures/  (16 files)
  images/  (12 files)
    bit-array.svg
    bitmap-words.svg
    const-mask.svg
    container-of.svg
    doubly-linked-list.svg
    find-first-bit.svg
    find-next-bit-words.svg
    find-next-bit.svg
    intrusive-list.svg
    list-add.svg
    singly-linked-list.svg
    task-struct-list.svg
  README.md
  linux-datastructures-1.md
  linux-datastructures-2.md
  linux-datastructures-3.md
Initialization/  (19 files)
  images/  (8 files)
    direct-mapping.svg
    early-page-table-identity-mapping.svg
    early-page-tables-after-init.svg
    early-top-pgt-entries.svg
    idt-descriptor.svg
    idt-gate-descriptor.svg
    interrupt-stack-frame-full.svg
    interrupt-stack-frame.svg
  README.md
  linux-initialization-1.md
  linux-initialization-10.md
  linux-initialization-2.md
  linux-initialization-3.md
  linux-initialization-4.md
  linux-initialization-5.md
  linux-initialization-6.md
  linux-initialization-7.md
  linux-initialization-8.md
  linux-initialization-9.md
Interrupts/  (11 files)
  README.md
  linux-interrupts-1.md
  linux-interrupts-10.md
  linux-interrupts-2.md
  linux-interrupts-3.md
  linux-interrupts-4.md
  linux-interrupts-5.md
  linux-interrupts-6.md
  linux-interrupts-7.md
  linux-interrupts-8.md
  linux-interrupts-9.md
KernelStructures/  (1 files)
  .gitkeep
MM/  (4 files)
  README.md
  linux-mm-1.md
  linux-mm-2.md
  linux-mm-3.md
SyncPrim/  (7 files)
  README.md
  linux-sync-1.md
  linux-sync-2.md
  linux-sync-3.md
  linux-sync-4.md
  linux-sync-5.md
  linux-sync-6.md
SysCall/  (7 files)
  README.md
  linux-syscall-1.md
  linux-syscall-2.md
  linux-syscall-3.md
  linux-syscall-4.md
  linux-syscall-5.md
  linux-syscall-6.md
Timers/  (8 files)
  README.md
  linux-timers-1.md
  linux-timers-2.md
  linux-timers-3.md
  linux-timers-4.md
  linux-timers-5.md
  linux-timers-6.md
  linux-timers-7.md
Toolchain/  (6 files)
  README.md
  linux-toolchain-1.md
  linux-toolchain-2.md
  linux-toolchain-3.md
  linux-toolchain-4.md
  linux-toolchain-5.md
X86/  (3 files)
  README.md
  linux-x86-1.md
  linux-x86-2.md
scripts/  (5 files)
  .python-version
  README.md
  check_code_snippets.py
  latex.py
  pyproject.toml
.editorconfig
.gitattributes
.gitignore
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
LINKS.md
Makefile
README.md
SUMMARY.md
book-A5.json
book.json
contributors.md
lychee.toml
```

## Entry points

- [scripts/check_code_snippets.py:200](https://github.com/0xAX/linux-insides/blob/4fa356494fa6de2143dbfbd729e66bf469439ca3/scripts/check_code_snippets.py#L200)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: __api_url__, __compare__, __excluded__, __fetch_raw__, __get__, __handle_md__. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: pandoc. |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/content-issue.yml` (config)
- `.github/ISSUE_TEMPLATE/question.yml` (config)
- `.github/dependabot.yaml` (config)
- `.github/labeler.yml` (config)
- `.github/labels.yml` (config)
- `.github/workflows/check-code-snippets.yaml` (ci)
- `.github/workflows/check-links.yaml` (ci)
- `.github/workflows/generate-e-books.yaml` (ci)
- `.github/workflows/labeler.yaml` (ci)
- `.github/workflows/release-e-books.yaml` (ci)
- `Dockerfile` (container)
- `book-A5.json` (config)
- `book.json` (config)
- `lychee.toml` (config)
- `scripts/pyproject.toml` (manifest)

## Top-level layout

- `Initialization` — 19 analysed file(s)
- `Booting` — 17 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `DataStructures` — 16 analysed file(s)
- `.github` — 12 analysed file(s)
- `Interrupts` — 11 analysed file(s)
- `Timers` — 8 analysed file(s)
- `SyncPrim` — 7 analysed file(s)
- `SysCall` — 7 analysed file(s)
- `Toolchain` — 6 analysed file(s)
- `Concepts` — 5 analysed file(s)
- `scripts` — 5 analysed file(s)
- `MM` — 4 analysed file(s)
- `X86` — 3 analysed file(s)
- `Cgroups` — 2 analysed file(s)
- `Assets` — 1 analysed file(s)
- `Contributing` — 1 analysed file(s)
- `KernelStructures` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4fa356494fa6de2143dbfbd729e66bf469439ca3` is the revision these paths and observations refer to.
