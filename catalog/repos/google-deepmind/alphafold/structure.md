# Project structure: google-deepmind/alphafold

**Analysed commit:** `c77e5d2a8961d1a353632c462914ff0a32a950f6`

**Commit reference:** [c77e5d2a8961d1a353632c462914ff0a32a950f6](https://github.com/google-deepmind/alphafold/commit/c77e5d2a8961d1a353632c462914ff0a32a950f6)

**Tree at this commit:** [google-deepmind/alphafold@c77e5d2a8961](https://github.com/google-deepmind/alphafold/tree/c77e5d2a8961d1a353632c462914ff0a32a950f6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | google-deepmind/alphafold |
| Description | Open source code for AlphaFold 2. |
| Stars | 14939 |
| Forks | 2961 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `c77e5d2a8961d1a353632c462914ff0a32a950f6` |
| Retrieved at | 2026-11-14T19:09:11.631242+00:00 |
| Files in this snapshot | 116 |

## Directory tree

```text
afdb/  (1 files)
  README.md
alphafold/  (88 files)
  common/  (9 files)
    testdata/  (1 files)
      … 1 files under this directory
    __init__.py
    confidence.py
    confidence_test.py
    mmcif_metadata.py
    protein.py
    protein_test.py
    residue_constants.py
    residue_constants_test.py
  data/  (17 files)
    tools/  (8 files)
      … 8 files under this directory
    __init__.py
    feature_processing.py
    mmcif_parsing.py
    msa_identifiers.py
    msa_pairing.py
    parsers.py
    pipeline.py
    pipeline_multimer.py
    templates.py
  model/  (44 files)
    geometry/  (7 files)
      … 7 files under this directory
    tf/  (10 files)
      … 10 files under this directory
    __init__.py
    all_atom.py
    all_atom_multimer.py
    all_atom_test.py
    base_config.py
    base_config_test.py
    common_modules.py
    config.py
    config_test.py
    data.py
    features.py
    folding.py
    folding_multimer.py
    layer_stack.py
    layer_stack_test.py
    lddt.py
    lddt_test.py
    mapping.py
    model.py
    modules.py
    modules_multimer.py
    prng.py
    prng_test.py
    quat_affine.py
    … 3 more files
  notebooks/  (3 files)
    __init__.py
    notebook_utils.py
    notebook_utils_test.py
  relax/  (13 files)
    testdata/  (4 files)
      … 4 files under this directory
    __init__.py
    amber_minimize.py
    amber_minimize_test.py
    cleanup.py
    cleanup_test.py
    relax.py
    relax_test.py
    utils.py
    utils_test.py
  __init__.py
  version.py
docker/  (3 files)
  Dockerfile
  requirements.txt
  run_docker.py
docs/  (1 files)
  technical_note_v2.3.0.md
notebooks/  (1 files)
  AlphaFold.ipynb
scripts/  (11 files)
  download_all_data.sh
  download_alphafold_params.sh
  download_bfd.sh
  download_mgnify.sh
  download_pdb70.sh
  download_pdb_mmcif.sh
  download_pdb_seqres.sh
  download_small_bfd.sh
  download_uniprot.sh
  download_uniref30.sh
  download_uniref90.sh
server/  (2 files)
  README.md
  example.json
.dockerignore
CONTRIBUTING.md
LICENSE
README.md
conftest.py
pyproject.toml
requirements.txt
run_alphafold.py
run_alphafold_test.py
```

## Entry points

- [alphafold/common/confidence_test.py:51](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/common/confidence_test.py#L51)
- [alphafold/common/protein_test.py:174](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/common/protein_test.py#L174)
- [alphafold/common/residue_constants_test.py:226](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/common/residue_constants_test.py#L226)
- [alphafold/model/all_atom_test.py:297](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/model/all_atom_test.py#L297)
- [alphafold/model/base_config_test.py:175](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/model/base_config_test.py#L175)
- [alphafold/model/config_test.py:34](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/model/config_test.py#L34)
- [alphafold/model/layer_stack_test.py:340](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/model/layer_stack_test.py#L340)
- [alphafold/model/lddt_test.py:93](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/model/lddt_test.py#L93)
- [alphafold/model/prng_test.py:42](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/model/prng_test.py#L42)
- [alphafold/model/quat_affine_test.py:145](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/model/quat_affine_test.py#L145)
- [alphafold/model/tf/protein_features_test.py:40](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/model/tf/protein_features_test.py#L40)
- [alphafold/model/tf/shape_helpers_test.py:39](https://github.com/google-deepmind/alphafold/blob/c77e5d2a8961d1a353632c462914ff0a32a950f6/alphafold/model/tf/shape_helpers_test.py#L39)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| alphafold package | library | Observed | Groups 46 file(s) under alphafold package (observed from repository paths and static analysis). Observed top-level classes: AlphaFold, AlphaFoldIteration, AmberRelaxation, Attention, BaseConfig, ConfigMeta. Observed top… |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AlphaFoldConfig, CommonData, Data, DgramFeatures, DistogramHead, EmbeddingsAndEvoform… |
| Data layer | data | Observed | Groups 18 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AlignRatioError, AtomSite, CaDistanceError, DataPipeline, DateError, DuplicateError. Observed top-leve… |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ModelsToRelax. Observed top-level functions: _check_flag, _create_mount, _jnp_to_np, _save… |
| scripts package | library | Observed | Groups 11 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 20 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH sys.stdout. Observed top-level classes: AllAtomTest, AmberMinimizeTest, CleanupTest, ConfidenceTest, ConfigTest,… |

## Important files

- `.dockerignore` (container)
- `docker/Dockerfile` (container)
- `docker/requirements.txt` (manifest)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `server/example.json` (config)

## Top-level layout

- `alphafold` — 88 analysed file(s)
- `scripts` — 11 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `docker` — 3 analysed file(s)
- `server` — 2 analysed file(s)
- `afdb` — 1 analysed file(s)
- `docs` — 1 analysed file(s)
- `notebooks` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c77e5d2a8961d1a353632c462914ff0a32a950f6` is the revision these paths and observations refer to.
