# Project structure: SesameAILabs/csm

**Analysed commit:** `daed31e6d42cf71873999075de204fa37d2acec3`

**Commit reference:** [daed31e6d42cf71873999075de204fa37d2acec3](https://github.com/SesameAILabs/csm/commit/daed31e6d42cf71873999075de204fa37d2acec3)

**Tree at this commit:** [SesameAILabs/csm@daed31e6d42c](https://github.com/SesameAILabs/csm/tree/daed31e6d42cf71873999075de204fa37d2acec3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | SesameAILabs/csm |
| Description | A Conversational Speech Generation Model |
| Stars | 14749 |
| Forks | 1474 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `daed31e6d42cf71873999075de204fa37d2acec3` |
| Retrieved at | 2026-11-14T19:09:17.163480+00:00 |
| Files in this snapshot | 9 |

## Directory tree

```text
.gitignore
LICENSE
README.md
generator.py
models.py
requirements.txt
run_csm.py
setup.py
watermarking.py
```

## Entry points

- [run_csm.py:116](https://github.com/SesameAILabs/csm/blob/daed31e6d42cf71873999075de204fa37d2acec3/run_csm.py#L116)
- [watermarking.py:78](https://github.com/SesameAILabs/csm/blob/daed31e6d42cf71873999075de204fa37d2acec3/watermarking.py#L78)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: Generator, Segment. Observed top-level functions: load_csm_1b, load_llama3_tokenizer. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Model, ModelArgs. Observed top-level functions: _create_causal_mask, _index_causal_mask, _multinomial_s… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: check_audio_from_file, cli_check_audio, load_audio, load_prompt_audio, load_watermarker,… |

## Important files

- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `(root files)` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `daed31e6d42cf71873999075de204fa37d2acec3` is the revision these paths and observations refer to.
