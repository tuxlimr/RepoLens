# Project structure: agentskills/agentskills

**Analysed commit:** `83021e2be457a9b6679148719c1f6074f0ad975e`

**Commit reference:** [83021e2be457a9b6679148719c1f6074f0ad975e](https://github.com/agentskills/agentskills/commit/83021e2be457a9b6679148719c1f6074f0ad975e)

**Tree at this commit:** [agentskills/agentskills@83021e2be457](https://github.com/agentskills/agentskills/tree/83021e2be457a9b6679148719c1f6074f0ad975e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | agentskills/agentskills |
| Description | Specification and documentation for Agent Skills |
| Stars | 27291 |
| Forks | 2031 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `83021e2be457a9b6679148719c1f6074f0ad975e` |
| Retrieved at | 2026-11-14T19:07:21.437089+00:00 |
| Files in this snapshot | 133 |

## Directory tree

```text
.claude/  (2 files)
  hooks/  (1 files)
    session-start.sh
  settings.json
docs/  (108 files)
  client-implementation/  (1 files)
    adding-skills-support.mdx
  images/  (90 files)
    logos/  (90 files)
      … 90 files under this directory
  skill-creation/  (5 files)
    best-practices.mdx
    evaluating-skills.mdx
    optimizing-descriptions.mdx
    quickstart.mdx
    using-scripts.mdx
  snippets/  (3 files)
    ClientShowcase.jsx
    LogoCarousel.jsx
    clients.jsx
  LICENSE
  README.md
  clients.mdx
  docs.json
  favicon.svg
  footer.js
  home.mdx
  specification.mdx
  style.css
skills-ref/  (15 files)
  src/  (7 files)
    skills_ref/  (7 files)
      … 7 files under this directory
  tests/  (4 files)
    __init__.py
    test_parser.py
    test_prompt.py
    test_validator.py
  .gitignore
  LICENSE
  README.md
  pyproject.toml
.gitignore
AGENTS.md
CONTRIBUTING.md
GOVERNANCE.md
LICENSE
MAINTAINERS.md
README.md
package.json
```

## Entry points

- [skills-ref/src/skills_ref/cli.py:22](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/skills-ref/src/skills_ref/cli.py#L22)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: SkillProperties. |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _is_skill_md_file, main, read_properties_cmd, to_prompt_cmd, validate_cmd. |
| skills-ref package | library | Observed | Groups 5 file(s) under skills-ref package (observed from repository paths and static analysis). Observed top-level classes: ParseError, SkillError, ValidationError. Observed top-level functions: _validate_compatibility,… |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: test_allowed_tools_accepted, test_compatibility_too_long, test_description_too_long, test_empty_list, test… |

## Important files

- `.claude/settings.json` (config)
- `docs/docs.json` (config)
- `package.json` (manifest)
- `skills-ref/pyproject.toml` (manifest)

## Top-level layout

- `docs` — 108 analysed file(s)
- `skills-ref` — 15 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.claude` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `83021e2be457a9b6679148719c1f6074f0ad975e` is the revision these paths and observations refer to.
