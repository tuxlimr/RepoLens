# Project structure: black-forest-labs/flux

**Analysed commit:** `802fb4713906133fcbd0d8dc5351620ca4773036`

**Commit reference:** [802fb4713906133fcbd0d8dc5351620ca4773036](https://github.com/black-forest-labs/flux/commit/802fb4713906133fcbd0d8dc5351620ca4773036)

**Tree at this commit:** [black-forest-labs/flux@802fb4713906](https://github.com/black-forest-labs/flux/tree/802fb4713906133fcbd0d8dc5351620ca4773036)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | black-forest-labs/flux |
| Description | Official inference repo for FLUX.1 models |
| Stars | 26058 |
| Forks | 1935 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `802fb4713906133fcbd0d8dc5351620ca4773036` |
| Retrieved at | 2026-11-14T19:07:27.179659+00:00 |
| Files in this snapshot | 51 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yaml
docs/  (5 files)
  fill.md
  image-editing.md
  image-variation.md
  structural-conditioning.md
  text-to-image.md
model_cards/  (4 files)
  FLUX.1-Krea-dev.md
  FLUX.1-dev.md
  FLUX.1-kontext-dev.md
  FLUX.1-schnell.md
model_licenses/  (2 files)
  LICENSE-FLUX1-dev
  LICENSE-FLUX1-schnell
src/  (31 files)
  flux/  (31 files)
    modules/  (5 files)
      … 5 files under this directory
    trt/  (14 files)
      … 14 files under this directory
    __init__.py
    __main__.py
    cli.py
    cli_control.py
    cli_fill.py
    cli_kontext.py
    cli_redux.py
    content_filters.py
    math.py
    model.py
    sampling.py
    util.py
.gitignore
LICENSE
README.md
demo_gr.py
demo_st.py
demo_st_fill.py
pyproject.toml
setup.py
```

## Entry points

- [src/flux/__main__.py:9](https://github.com/black-forest-labs/flux/blob/802fb4713906133fcbd0d8dc5351620ca4773036/src/flux/__main__.py#L9)
- [src/flux/cli.py](https://github.com/black-forest-labs/flux/blob/802fb4713906133fcbd0d8dc5351620ca4773036/src/flux/cli.py)
- [src/flux/cli_control.py:389](https://github.com/black-forest-labs/flux/blob/802fb4713906133fcbd0d8dc5351620ca4773036/src/flux/cli_control.py#L389)
- [src/flux/cli_fill.py:333](https://github.com/black-forest-labs/flux/blob/802fb4713906133fcbd0d8dc5351620ca4773036/src/flux/cli_fill.py#L333)
- [src/flux/cli_kontext.py:367](https://github.com/black-forest-labs/flux/blob/802fb4713906133fcbd0d8dc5351620ca4773036/src/flux/cli_kontext.py#L367)
- [src/flux/cli_redux.py:289](https://github.com/black-forest-labs/flux/blob/802fb4713906133fcbd0d8dc5351620ca4773036/src/flux/cli_redux.py#L289)
- [demo_gr.py:246](https://github.com/black-forest-labs/flux/blob/802fb4713906133fcbd0d8dc5351620ca4773036/demo_gr.py#L246)
- [demo_st.py:296](https://github.com/black-forest-labs/flux/blob/802fb4713906133fcbd0d8dc5351620ca4773036/demo_st.py#L296)
- [demo_st_fill.py:501](https://github.com/black-forest-labs/flux/blob/802fb4713906133fcbd0d8dc5351620ca4773036/demo_st_fill.py#L501)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Flux, FluxLoraWrapper, FluxParams. |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: FluxGenerator, SamplingOptions. Observed top-level functions: add_border_and_mask, app, cl… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| flux package | library | Observed | Groups 24 file(s) under flux package (observed from repository paths and static analysis). Observed top-level classes: AttnBlock, AutoEncoder, AutoEncoderParams, BaseEngine, CLIPEngine, CannyImageEncoder. Observed top-l… |

## Important files

- `.github/workflows/ci.yaml` (ci)
- `pyproject.toml` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `src` — 31 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `docs` — 5 analysed file(s)
- `model_cards` — 4 analysed file(s)
- `model_licenses` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `802fb4713906133fcbd0d8dc5351620ca4773036` is the revision these paths and observations refer to.
