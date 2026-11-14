# Project structure: ManimCommunity/manim

**Analysed commit:** `e8afc6398bc7ac4d4beaa2debd79325f9167d374`

**Commit reference:** [e8afc6398bc7ac4d4beaa2debd79325f9167d374](https://github.com/ManimCommunity/manim/commit/e8afc6398bc7ac4d4beaa2debd79325f9167d374)

**Tree at this commit:** [ManimCommunity/manim@e8afc6398bc7](https://github.com/ManimCommunity/manim/tree/e8afc6398bc7ac4d4beaa2debd79325f9167d374)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ManimCommunity/manim |
| Description | A community-maintained Python framework for creating mathematical animations.  |
| Stars | 42506 |
| Forks | 3329 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `e8afc6398bc7ac4d4beaa2debd79325f9167d374` |
| Retrieved at | 2026-11-14T19:06:39.853590+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (19 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    installation_issue.md
  PULL_REQUEST_TEMPLATE/  (3 files)
    bugfix.md
    documentation.md
    hackathon.md
  scripts/  (1 files)
    ci_build_cairo.py
  workflows/  (7 files)
    cffconvert.yml
    ci.yml
    codeql.yml
    dependent-issues.yml
    publish-docker.yml
    python-publish.yml
    release-publish-documentation.yml
  PULL_REQUEST_TEMPLATE.md
  codeql.yml
  dependabot.yml
  manimdependency.json
  release.yml
benchmarks/  (1 files)
  bench_lissajous.py
docker/  (5 files)
  Dockerfile
  readme.md
  texlive-packages.txt
  texlive-profile.txt
  verify_image.py
docs/  (645 files)
  i18n/  (545 files)
    fr/  (2 files)
      … 2 files under this directory
    gettext/  (528 files)
      … 528 files under this directory
    hi/  (1 files)
      … 1 files under this directory
    pt/  (1 files)
      … 1 files under this directory
    sv/  (10 files)
      … 10 files under this directory
    readyForTranslation
    stripUntranslatable.awk
    stripUntranslatable.sh
  source/  (94 files)
    _static/  (6 files)
      … 6 files under this directory
    _templates/  (3 files)
      … 3 files under this directory
    changelog/  (35 files)
      … 35 files under this directory
    contributing/  (11 files)
      … 11 files under this directory
    faq/  (6 files)
      … 6 files under this directory
    guides/  (8 files)
      … 8 files under this directory
    installation/  (4 files)
      … 4 files under this directory
    reference_index/  (7 files)
      … 7 files under this directory
    tutorials/  (4 files)
      … 4 files under this directory
    changelog.rst
    conf.py
    contributing.rst
    examples.rst
    index.rst
    installation.rst
    plugins.rst
    reference.rst
    robots.txt
    tutorials_guides.rst
  Makefile
  html
  make.bat
  requirements.txt
  rtd-requirements.txt
  skip-manim
example_scenes/  (7 files)
  advanced_tex_fonts.py
  basic.py
  custom_template.tex
  customtex.py
  manim.cfg
  manim_jupyter_example.ipynb
  opengl.py
logo/  (6 files)
  dark/  (2 files)
    dark_background.svg
    transparent_background.svg
  light/  (2 files)
    light_background.svg
    transparent_background.svg
  monochromatic/  (2 files)
    monochromatic_black.svg
    monochromatic_white.svg
manim/  (98 files)
  _config/  (9 files)
    __init__.py
    cli_colors.py
    default.cfg
    logger_utils.py
    output.py
    output_plan.py
    render_session.py
    utils.py
    video_encoder.py
  _run/  (8 files)
    __init__.py
    cache.py
    frames.py
    listeners.py
    loop.py
    mode.py
    record.py
    selection.py
  animation/  (18 files)
    updaters/  (3 files)
      … 3 files under this directory
    __init__.py
    animation.py
    changing.py
    composition.py
    creation.py
    fading.py
    growing.py
    indication.py
    movement.py
    numbers.py
    rotation.py
    specialized.py
    speedmodifier.py
    transform.py
    transform_matching_parts.py
  cli/  (19 files)
    cache/  (2 files)
      … 2 files under this directory
    cfg/  (2 files)
      … 2 files under this directory
    checkhealth/  (3 files)
      … 3 files under this directory
    init/  (2 files)
      … 2 files under this directory
    plugins/  (2 files)
      … 2 files under this directory
    render/  (6 files)
      … 6 files under this directory
    __init__.py
    default_group.py
  mobject/  (39 files)
    geometry/  (8 files)
      … 8 files under this directory
    graphing/  (6 files)
      … 6 files under this directory
    opengl/  (10 files)
      … 10 files under this directory
    svg/  (3 files)
      … 3 files under this directory
    text/  (5 files)
      … 5 files under this directory
    __init__.py
    frame.py
    graph.py
    logo.py
    matrix.py
    mobject.py
    table.py
  __init__.py
  __main__.py
  constants.py
  data_structures.py
  manager.py
.codecov.yml
.codespell_ignorewords
.codespellrc
.dockerignore
.flake8
.git-blame-ignore-revs
.gitattributes
.gitignore
.pre-commit-config.yaml
.pylintrc
.readthedocs.yml
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
LICENSE.community
README.md
crowdin.yml
lgtm.yml
```

## Entry points

- [.github/scripts/ci_build_cairo.py:222](https://github.com/ManimCommunity/manim/blob/e8afc6398bc7ac4d4beaa2debd79325f9167d374/.github/scripts/ci_build_cairo.py#L222)
- [benchmarks/bench_lissajous.py:423](https://github.com/ManimCommunity/manim/blob/e8afc6398bc7ac4d4beaa2debd79325f9167d374/benchmarks/bench_lissajous.py#L423)
- [manim/__main__.py:102](https://github.com/ManimCommunity/manim/blob/e8afc6398bc7ac4d4beaa2debd79325f9167d374/manim/__main__.py#L102)
- [manim/animation/creation.py:642](https://github.com/ManimCommunity/manim/blob/e8afc6398bc7ac4d4beaa2debd79325f9167d374/manim/animation/creation.py#L642)
- [manim/animation/transform.py:871](https://github.com/ManimCommunity/manim/blob/e8afc6398bc7ac4d4beaa2debd79325f9167d374/manim/animation/transform.py#L871)
- [manim/mobject/geometry/shape_matchers.py:71](https://github.com/ManimCommunity/manim/blob/e8afc6398bc7ac4d4beaa2debd79325f9167d374/manim/mobject/geometry/shape_matchers.py#L71)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). Observed top-level classes: VerifyImage. |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Group. Observed top-level classes: AddTextLetterByLetter, AddTextWordByWord, A… |
| example_scenes package | library | Observed | Groups 4 file(s) under example_scenes package (observed from repository paths and static analysis). Observed top-level classes: GuiTest, GuiTest2, InCodeTexTemplate, InlineFullScreenQuad, InlineShaderExample, Interactiv… |
| manim package | library | Observed | Groups 93 file(s) under manim package (observed from repository paths and static analysis). Observed top-level classes: Add, Angle, AnimatedBoundary, Animation, AnimationGroup, AnnotationDot. Observed top-level function… |

## Important files

- `.codecov.yml` (config)
- `.dockerignore` (container)
- `.github/codeql.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/manimdependency.json` (config)
- `.github/release.yml` (config)
- `.github/workflows/cffconvert.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/dependent-issues.yml` (ci)
- `.github/workflows/publish-docker.yml` (ci)
- `.github/workflows/python-publish.yml` (ci)
- `.github/workflows/release-publish-documentation.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yml` (config)
- `crowdin.yml` (config)
- `docker/Dockerfile` (container)
- `docs/requirements.txt` (manifest)
- `example_scenes/manim.cfg` (config)
- `lgtm.yml` (config)
- `manim/_config/default.cfg` (config)

## Top-level layout

- `docs` — 645 analysed file(s)
- `manim` — 98 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 19 analysed file(s)
- `example_scenes` — 7 analysed file(s)
- `logo` — 6 analysed file(s)
- `docker` — 5 analysed file(s)
- `benchmarks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `e8afc6398bc7ac4d4beaa2debd79325f9167d374` is the revision these paths and observations refer to.
