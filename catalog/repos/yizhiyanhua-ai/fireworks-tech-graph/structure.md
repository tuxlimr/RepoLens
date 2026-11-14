# Project structure: yizhiyanhua-ai/fireworks-tech-graph

**Analysed commit:** `1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f`

**Commit reference:** [1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/commit/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f)

**Tree at this commit:** [yizhiyanhua-ai/fireworks-tech-graph@1ca1ff9cfcb6](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/tree/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yizhiyanhua-ai/fireworks-tech-graph |
| Description | Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns. |
| Stars | 11992 |
| Forks | 937 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f` |
| Retrieved at | 2026-11-14T19:10:18.877071+00:00 |
| Files in this snapshot | 241 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    ci.yml
    release.yml
  FUNDING.yml
  pull_request_template.md
agents/  (1 files)
  openai.yaml
assets/  (2 files)
  icons/  (1 files)
    cloud/  (1 files)
      … 1 files under this directory
  samples/  (1 files)
    showcase-gif-manifest.json
docs/  (11 files)
  releases/  (9 files)
    README.md
    v1.0.0.md
    v1.0.1.md
    v1.0.2.md
    v1.0.3.md
    v1.0.4.md
    v1.0.5.md
    v1.1.0.md
    v1.2.0.md
  CAPABILITIES.md
  ROADMAP.md
examples/  (2 files)
  README.md
  interactive-architecture.html
fixtures/  (23 files)
  quality-baseline/  (11 files)
    agent-runtime-style1.json
    agent-runtime-style10.json
    agent-runtime-style11.json
    agent-runtime-style12.json
    agent-runtime-style2.json
    agent-runtime-style3.json
    agent-runtime-style4.json
    agent-runtime-style5.json
    agent-runtime-style6.json
    agent-runtime-style7.json
    agent-runtime-style9.json
  agent-memory-types-style4.json
  api-flow-style7.json
  c4-review-canvas-style9.json
  cloud-fabric-style10.json
  dark-luxury-style8.svg
  event-transit-style11.json
  mem0-style1.json
  microservices-style3.json
  multi-agent-style5.json
  ops-pulse-style12.json
  system-architecture-style6.json
  tool-call-style2.json
references/  (20 files)
  composition-quality-contract.md
  diagram-layout-reference.md
  icons.md
  motion-effects.md
  png-export.md
  style-1-flat-icon.md
  style-10-cloud-fabric.md
  style-11-event-transit.md
  style-12-ops-pulse.md
  style-2-dark-terminal.md
  style-3-blueprint.md
  style-4-notion-clean.md
  style-5-glassmorphism.md
  style-6-claude-official.md
  style-7-openai.md
  style-8-dark-luxury.md
  style-9-c4-review-canvas.md
  style-diagram-matrix.md
  svg-layout-best-practices.md
  visual-quality.md
schemas/  (4 files)
  architecture-v1.schema.json
  diagram-v1.schema.json
  sequence-v1.schema.json
  workflow-v1.schema.json
scripts/  (20 files)
  README.md
  composition_quality.py
  diagram_ir.py
  export-interactive-html.py
  fireworks.py
  fireworks_geometry.py
  generate-diagram.sh
  generate-from-template.py
  interactive_html.py
  motion.py
  png_export.py
  renderer_runtime.js
  semantic_contracts.py
  style_quality.py
  svg2gif.js
  svg2png.js
  svg_canvas.py
  test-all-styles.sh
  validate-svg.sh
  validate_svg.py
skills/  (112 files)
  fireworks-tech-graph/  (112 files)
    agents/  (1 files)
      … 1 files under this directory
    assets/  (2 files)
      … 2 files under this directory
    docs/  (11 files)
      … 11 files under this directory
    examples/  (2 files)
      … 2 files under this directory
    fixtures/  (23 files)
      … 23 files under this directory
    references/  (20 files)
      … 20 files under this directory
    schemas/  (4 files)
      … 4 files under this directory
    scripts/  (20 files)
      … 20 files under this directory
    templates/  (10 files)
      … 10 files under this directory
    tests/  (11 files)
      … 11 files under this directory
    CHANGELOG.md
    CONTRIBUTING.md
    LICENSE
    README.md
    README.zh.md
    SECURITY.md
    SKILL.md
    package.json
templates/  (10 files)
  agent-architecture.svg
  architecture.svg
  comparison-matrix.svg
  data-flow.svg
  er-diagram.svg
  flowchart.svg
  sequence.svg
  state-machine.svg
  timeline.svg
  use-case.svg
tests/  (11 files)
  snapshots/  (1 files)
    quality-upgrade.json
  test_cli.py
  test_diagram_ir.py
  test_geometry_contracts.py
  test_interactive_html.py
  test_motion.py
  test_python_compatibility.py
  test_quality_upgrade.py
  test_semantic_contracts.py
  test_skill_compatibility.py
  test_validate_svg.py
tools/  (3 files)
  check_project_consistency.py
  distribution.py
  install-canary.sh
.gitignore
.nojekyll
.npmignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
README.zh.md
SECURITY.md
SKILL.md
agentloop-core.svg
index.html
package.json
robots.txt
site.webmanifest
sitemap.xml
```

## Entry points

- [scripts/export-interactive-html.py:7](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/scripts/export-interactive-html.py#L7)
- [scripts/fireworks.py:254](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/scripts/fireworks.py#L254)
- [scripts/generate-from-template.py:3414](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/scripts/generate-from-template.py#L3414)
- [scripts/interactive_html.py:355](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/scripts/interactive_html.py#L355)
- [scripts/svg_canvas.py:70](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/scripts/svg_canvas.py#L70)
- [scripts/validate_svg.py:961](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/scripts/validate_svg.py#L961)
- [skills/fireworks-tech-graph/scripts/export-interactive-html.py:7](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/skills/fireworks-tech-graph/scripts/export-interactive-html.py#L7)
- [skills/fireworks-tech-graph/scripts/fireworks.py:254](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/skills/fireworks-tech-graph/scripts/fireworks.py#L254)
- [skills/fireworks-tech-graph/scripts/generate-from-template.py:3414](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/skills/fireworks-tech-graph/scripts/generate-from-template.py#L3414)
- [skills/fireworks-tech-graph/scripts/interactive_html.py:355](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/skills/fireworks-tech-graph/scripts/interactive_html.py#L355)
- [skills/fireworks-tech-graph/scripts/svg_canvas.py:70](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/skills/fireworks-tech-graph/scripts/svg_canvas.py#L70)
- [skills/fireworks-tech-graph/scripts/validate_svg.py:961](https://github.com/yizhiyanhua-ai/fireworks-tech-graph/blob/1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f/skills/fireworks-tech-graph/scripts/validate_svg.py#L961)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 60 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 14 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ArrowRender, Bounds, Collision, ElementContext, Node. Observed top-level functions: _file… |
| scripts package | library | Observed | Groups 13 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: CompositionContract, DiagramIR, DiagramValidationError, EdgeIR, NodeIR, RouteInteractions. Observ… |
| skills package | library | Observed | Groups 13 file(s) under skills package (observed from repository paths and static analysis). Observed top-level classes: CompositionContract, DiagramIR, DiagramValidationError, EdgeIR, NodeIR, RouteInteractions. Observe… |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ArtifactGeometryTest, DiagramIRTest, EngineeringSemanticContractTest, InteractiveHTMLTest, MotionPlanTest,… |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `agents/openai.yaml` (config)
- `assets/icons/cloud/manifest-v1.json` (config)
- `assets/samples/showcase-gif-manifest.json` (config)
- `fixtures/agent-memory-types-style4.json` (config)
- `fixtures/api-flow-style7.json` (config)
- `fixtures/c4-review-canvas-style9.json` (config)
- `fixtures/cloud-fabric-style10.json` (config)
- `fixtures/event-transit-style11.json` (config)
- `fixtures/mem0-style1.json` (config)
- `fixtures/microservices-style3.json` (config)
- `fixtures/multi-agent-style5.json` (config)
- `fixtures/ops-pulse-style12.json` (config)
- `fixtures/quality-baseline/agent-runtime-style1.json` (config)
- `fixtures/quality-baseline/agent-runtime-style10.json` (config)
- `fixtures/quality-baseline/agent-runtime-style11.json` (config)
- `fixtures/quality-baseline/agent-runtime-style12.json` (config)
- `fixtures/quality-baseline/agent-runtime-style2.json` (config)
- `fixtures/quality-baseline/agent-runtime-style3.json` (config)
- `fixtures/quality-baseline/agent-runtime-style4.json` (config)
- `fixtures/quality-baseline/agent-runtime-style5.json` (config)
- `fixtures/quality-baseline/agent-runtime-style6.json` (config)
- `fixtures/quality-baseline/agent-runtime-style7.json` (config)
- `fixtures/quality-baseline/agent-runtime-style9.json` (config)
- `fixtures/system-architecture-style6.json` (config)
- `fixtures/tool-call-style2.json` (config)
- `package.json` (manifest)
- `schemas/architecture-v1.schema.json` (config)
- `schemas/diagram-v1.schema.json` (config)
- `schemas/sequence-v1.schema.json` (config)
- `schemas/workflow-v1.schema.json` (config)
- `skills/fireworks-tech-graph/agents/openai.yaml` (config)
- `skills/fireworks-tech-graph/assets/icons/cloud/manifest-v1.json` (config)
- `skills/fireworks-tech-graph/assets/samples/showcase-gif-manifest.json` (config)
- `skills/fireworks-tech-graph/fixtures/agent-memory-types-style4.json` (config)
- `skills/fireworks-tech-graph/fixtures/api-flow-style7.json` (config)
- `skills/fireworks-tech-graph/fixtures/c4-review-canvas-style9.json` (config)
- `skills/fireworks-tech-graph/fixtures/cloud-fabric-style10.json` (config)
- `skills/fireworks-tech-graph/fixtures/event-transit-style11.json` (config)
- `skills/fireworks-tech-graph/fixtures/mem0-style1.json` (config)
- `skills/fireworks-tech-graph/fixtures/microservices-style3.json` (config)
- `skills/fireworks-tech-graph/fixtures/multi-agent-style5.json` (config)
- `skills/fireworks-tech-graph/fixtures/ops-pulse-style12.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style1.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style10.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style11.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style12.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style2.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style3.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style4.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style5.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style6.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style7.json` (config)
- `skills/fireworks-tech-graph/fixtures/quality-baseline/agent-runtime-style9.json` (config)
- `skills/fireworks-tech-graph/fixtures/system-architecture-style6.json` (config)
- `skills/fireworks-tech-graph/fixtures/tool-call-style2.json` (config)
- `skills/fireworks-tech-graph/package.json` (manifest)
- `skills/fireworks-tech-graph/schemas/architecture-v1.schema.json` (config)
- `skills/fireworks-tech-graph/schemas/diagram-v1.schema.json` (config)
- `skills/fireworks-tech-graph/schemas/sequence-v1.schema.json` (config)
- `skills/fireworks-tech-graph/schemas/workflow-v1.schema.json` (config)

## Top-level layout

- `skills` — 112 analysed file(s)
- `fixtures` — 23 analysed file(s)
- `references` — 20 analysed file(s)
- `scripts` — 20 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `docs` — 11 analysed file(s)
- `tests` — 11 analysed file(s)
- `templates` — 10 analysed file(s)
- `.github` — 6 analysed file(s)
- `schemas` — 4 analysed file(s)
- `tools` — 3 analysed file(s)
- `assets` — 2 analysed file(s)
- `examples` — 2 analysed file(s)
- `agents` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1ca1ff9cfcb67893a43d32b9ef3a1b782c44a46f` is the revision these paths and observations refer to.
