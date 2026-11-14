# Project structure: smol-ai/developer

**Analysed commit:** `a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82`

**Commit reference:** [a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82](https://github.com/smol-ai/developer/commit/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82)

**Tree at this commit:** [smol-ai/developer@a6747d1a6ccd](https://github.com/smol-ai/developer/tree/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | smol-ai/developer |
| Description | the first library to let you embed a developer agent in your own app! |
| Stars | 12172 |
| Forks | 1068 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82` |
| Retrieved at | 2026-11-14T19:10:14.513940+00:00 |
| Files in this snapshot | 47 |

## Directory tree

```text
.devcontainer/  (2 files)
  devcontainer.json
  dockerfile
examples/  (5 files)
  v1_pong_game/  (5 files)
    ai.js
    index.html
    main.js
    shared_deps.md
    style.css
smol_dev/  (5 files)
  __init__.py
  api.py
  main.py
  prompts.py
  utils.py
v0/  (27 files)
  code2prompt/  (2 files)
    code2prompt-gpt3.md
    code2prompt-gpt4.md
  code2prompt2code/  (7 files)
    background.js
    content_script.js
    manifest.json
    popup.html
    popup.js
    shared_dependencies.md
    styles.css
  exampleChromeExtension/  (8 files)
    background.js
    content_script.js
    manifest.json
    popup.html
    popup.js
    prompt used for this extension.md
    shared_dependencies.md
    styles.css
  static/  (1 files)
    readme.md
  code2prompt.py
  constants.py
  debugger.py
  debugger_no_modal.py
  main.py
  main_no_modal.py
  readme.md
  utils.py
  v0_readme.md
.example.env
.gitignore
LICENSE
Makefile
main.py
prompt.md
pyproject.toml
readme.md
```

## Entry points

- [main.py:14](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/main.py#L14)
- [smol_dev/main.py:78](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/smol_dev/main.py#L78)
- [v0/debugger_no_modal.py:109](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/v0/debugger_no_modal.py#L109)
- [v0/main_no_modal.py:208](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/v0/main_no_modal.py#L208)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: generate_file, generate_response, main, read_file, walk_directory, write_file. |
| smol_dev package | library | Observed | Groups 4 file(s) under smol_dev package (observed from repository paths and static analysis). Observed top-level classes: StepTypes. Observed top-level functions: _generate_code, _generate_file_paths, _generate_shared_d… |
| v0 package | library | Observed | Groups 10 file(s) under v0 package (observed from repository paths and static analysis). Observed top-level functions: clean_dir, generate_response, main, read_file, walk_directory. |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.devcontainer/dockerfile` (container)
- `pyproject.toml` (manifest)
- `v0/code2prompt2code/manifest.json` (config)
- `v0/exampleChromeExtension/manifest.json` (config)

## Top-level layout

- `v0` — 27 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `examples` — 5 analysed file(s)
- `smol_dev` — 5 analysed file(s)
- `.devcontainer` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82` is the revision these paths and observations refer to.
