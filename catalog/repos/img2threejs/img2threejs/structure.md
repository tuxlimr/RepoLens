# Project structure: img2threejs/img2threejs

**Analysed commit:** `0c0c49bc168e648dbaf9c8c080474de0b3a941b6`

**Commit reference:** [0c0c49bc168e648dbaf9c8c080474de0b3a941b6](https://github.com/img2threejs/img2threejs/commit/0c0c49bc168e648dbaf9c8c080474de0b3a941b6)

**Tree at this commit:** [img2threejs/img2threejs@0c0c49bc168e](https://github.com/img2threejs/img2threejs/tree/0c0c49bc168e648dbaf9c8c080474de0b3a941b6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | img2threejs/img2threejs |
| Description | Rebuild the object in a reference image as a code-only, procedural, quality-gated, animation-ready Three.js model. Token-efficient image-to-3D. |
| Stars | 21369 |
| Forks | 1811 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `0c0c49bc168e648dbaf9c8c080474de0b3a941b6` |
| Retrieved at | 2026-11-14T19:07:59.777671+00:00 |
| Files in this snapshot | 357 |

## Directory tree

```text
.github/  (14 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    contribution_intent.yml
    feature_request.yml
  workflows/  (8 files)
    beta-release.yml
    ci.yml
    cli-publish.yml
    docs-quality.yml
    issue-triage.yml
    pr-issue-close-policy.yml
    readme-tables-sync.yml
    release.yml
  FUNDING.yml
  pull_request_template.md
  release.yml
assets/  (6 files)
  sponsors/  (5 files)
    atlas-cloud-logomark-black.svg
    atlas-cloud-logomark-white.svg
    minimax-logomark.svg
    tripo-logomark-black.svg
    tripo-logomark-white.svg
  logo.svg
bin/  (2 files)
  img2threejs.mjs
  img2threejs.mjs-test.mjs
docs/  (33 files)
  integrations/  (1 files)
    reference_fidelity_tooling.md
  materials/  (4 files)
    IMAGE_MATERIAL_ANALYSIS.md
    README.md
    THREEJS_MATERIAL_REFERENCE.md
    material-reference.json
  pipelines/  (1 files)
    character-rigging-animation-1.5.2.md
  raw/  (2 files)
    .keep
    img2threejs-skill-dataset.json
  specs/  (5 files)
    vocabulary/  (3 files)
      … 3 files under this directory
    render-profile.v2.example.json
    render-profile.v2.schema.json
  standard-prompts/  (5 files)
    README.md
    build.md
    glb-force-measured.md
    polish.md
    vfx.md
  ARCHITECTURE.md
  EMISSION_TARGET_SOCKET.md
  GLB_ANIMATED_CHARACTER_PROMPT.md
  GLB_CHARACTER_ANIMATION_PROMPT.md
  GLB_CHARACTER_POLISH_PROMPT.md
  GLB_CHARACTER_PROMPT.md
  HAIR_PIPELINE.md
  INSTALL.md
  PLUGINS.md
  RESEARCH_TRELLIS2_TO_IMG2THREEJS.md
  STAGE_R_BACKLOG.md
  STAGE_R_TEST_PLAN.md
  TOKEN_COST.md
  UPGRADE_PLAN.md
  issue-triage.md
forge/  (225 files)
  _shared/  (21 files)
    domains/  (2 files)
      … 2 files under this directory
    artifact_cache.py
    chirality.py
    color_metrics.py
    feature_acceptance_policy.py
    glb_container.py
    image_hash.py
    jpeg.py
    material_physics.py
    pipeline_routing.py
    scalp_field.py
    sdf_primitives.py
    spec_augmentation.py
    spec_search.py
    spec_search_profiles.json
    status_banner.py
    subdivision.py
    targets.py
    vertex_paint.py
    workflow_state.py
  materials/  (3 files)
    __init__.py
    compatibility.py
    reference.py
  stage1_intake/  (24 files)
    analyze_texture.py
    bind_detail_properties.py
    build_detail_inventory.py
    camera_fitting_math.py
    camera_fitting_solver.py
    camera_fitting_types.py
    camera_image_helpers.py
    check_intake_correctness.py
    check_reference_admission.py
    delight_albedo.py
    detect_reference_effects.py
    extract_gradient_stops.py
    extract_hair_evidence.py
    extract_landmarks.py
    extract_part_color_recipe.py
    extract_pbr_evidence.py
    label_glb_nodes.py
    material_region_analysis.py
    probe_glb.py
    probe_image.py
    run_vision_adapter.py
    search_specs.py
    semantic_decomposition.py
    solve_camera_pose.py
  stage2_spec/  (7 files)
    apply_material_analysis.py
    derive_geometry.py
    hair_profile.py
    humanoid_proportions.py
    new_pre_spec_assessment.py
    new_sculpt_spec.py
    validate_sculpt_spec.py
  stage3_build/  (9 files)
    bake_projected_texture.py
    decimate.py
    emit_target.py
    module_cache.py
    morph_targets.py
    orchestrate_passes.py
    run_gates.py
    uv_unwrap.py
    visual_hull.py
  stage4_review/  (33 files)
    _fit_divine_eye.py
    append_review.py
    attachment_anchor.py
    calibrate_eye.py
    check_part_coverage.py
    compare_region_passes.py
    correction_loop.py
    diagnose_render.py
    diagnose_render_multi_angle.py
    divine_eye.py
    fit_params.py
    geometry_integrity.py
    hair_gate.py
    interior_difference.py
    joint_loops.py
    make_comparison_sheet.py
    material_comparator.py
    material_feedback.py
    material_gate.py
    material_views.py
    mesh_reference_compare.py
    multi_pass.py
    objectness.py
    pairwise_penetration.py
    … 9 more files
  stage5_rig/  (14 files)
    CONTRACT_1.5.2.md
    NOTES.md
    __init__.py
    action_design.py
    clip_features.py
    emit_animation_runtime.py
    emit_rig.py
    geodesic_skinning.py
    glb_rig_reference.py
    mesh_parity.py
    rig_gates.py
    rig_spec.py
    skin_conditioning.py
    validate_rig_payload.py
  tests/  (110 files)
    fixtures/  (7 files)
      … 7 files under this directory
    oracle_support.py
    showcase_test_support.py
    test_action_design.py
    test_albedo_color_space.py
    test_analyze_texture.py
    test_attachment_anchor.py
    test_attachment_does_not_override_primitive.py
    test_calibrate_eye.py
    test_camera_fitting.py
    test_camera_fitting_cli.py
    test_camera_fitting_safety.py
    test_character_rig_derivation.py
    test_chirality.py
    test_clip_features.py
    test_color_metrics.py
    test_color_recipe.py
    test_correction_loop.py
    test_decimation_wiring.py
    test_divine_eye.py
    test_domain_registry.py
    test_domain_spec_contract.py
    test_emit_animation_runtime.py
    test_emit_animation_runtime_tsc_smoke.py
    test_emit_target.py
    … 79 more files
  next.py
  report.py
  requirements.txt
  state.py
grimoire/  (24 files)
  character/  (6 files)
    head_construction.md
    likeness_maximization.md
    reconstruction.md
    structure_decomposition.md
    stylized_hair_threejs.md
    threejs_hair_parameter_contract.json
  feedback/  (2 files)
    render_capture.md
    shading_realism.md
  glossary/  (1 files)
    3d_vocabulary.md
  intake/  (6 files)
    detail_inventory.md
    image_analysis.md
    local_spec_search.md
    quality_contract.md
    surface_topology.md
    validation_rubric.md
  readiness/  (5 files)
    action_rigging.md
    animation_contract.md
    joint_attachment.md
    procedural_rigging_contract.md
    standard_character_pipeline.md
  review/  (3 files)
    divine_eye_microscope.md
    gates_reference.md
    self_correction.md
  scripts.md
integrations/  (28 files)
  glb_character_pipeline/  (23 files)
    configs/  (4 files)
      … 4 files under this directory
    node/  (8 files)
      … 8 files under this directory
    python/  (6 files)
      … 6 files under this directory
    .python-version
    PIPELINE.md
    README.md
    build-character.sh
    pyproject.toml
  mesh3d/  (1 files)
    generate_reference_mesh.py
  vision/  (4 files)
    .python-version
    README.md
    pyproject.toml
    reference_vision.py
scripts/  (14 files)
  ci/  (10 files)
    tests/  (1 files)
      … 1 files under this directory
    link-baseline.txt
    md_links.py
    md_tables.py
    mdcommon.py
    plugin_table.py
    pr_scope.py
    showcase_table.py
    skill-budget.json
    skill_budget.py
  capture_threejs_playwright.py
  character_audit.sh
  issue_triage.py
  release_metadata.py
skills/  (1 files)
  generic-extract-skill.md
.gitignore
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
LAB-FINDINGS.md
LICENSE
README.md
ROADMAP.md
SKILL.md
package.json
```

## Entry points

- [forge/materials/compatibility.py:105](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/materials/compatibility.py#L105)
- [forge/next.py:115](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/next.py#L115)
- [forge/report.py:37](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/report.py#L37)
- [forge/stage1_intake/analyze_texture.py:254](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/stage1_intake/analyze_texture.py#L254)
- [forge/stage1_intake/bind_detail_properties.py:98](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/stage1_intake/bind_detail_properties.py#L98)
- [forge/stage1_intake/build_detail_inventory.py:348](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/stage1_intake/build_detail_inventory.py#L348)
- [forge/stage1_intake/check_intake_correctness.py:115](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/stage1_intake/check_intake_correctness.py#L115)
- [forge/stage1_intake/check_reference_admission.py:215](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/stage1_intake/check_reference_admission.py#L215)
- [forge/stage1_intake/delight_albedo.py:351](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/stage1_intake/delight_albedo.py#L351)
- [forge/stage1_intake/detect_reference_effects.py:274](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/stage1_intake/detect_reference_effects.py#L274)
- [forge/stage1_intake/extract_gradient_stops.py:148](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/stage1_intake/extract_gradient_stops.py#L148)
- [forge/stage1_intake/extract_hair_evidence.py:384](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/forge/stage1_intake/extract_hair_evidence.py#L384)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 91 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Acceptance, BandCheck, BlendReport, BoneMatch, Chain, ChainResolutionError. Observed top-… |
| External integrations | external | Observed | Groups 9 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: acc, embedded_image, sample_texture. |
| forge package | library | Observed | Groups 35 file(s) under forge package (observed from repository paths and static analysis). Observed top-level classes: AliasSettings, AspectDescriptor, Bm25Config, Bm25Index, Bm25Settings, BoneSpec. Observed top-level… |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: changed_files, files_from_args, iter_lines, report, strip_frontmatter_lines. |
| Tests | test | Observed | Groups 111 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Accepted, ActionReadyPrecondition, AlbedoColorSpace, AnalyzeTextureTest, AreaWeighting, ArgvDriftGuard. Ob… |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/contribution_intent.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/release.yml` (config)
- `.github/workflows/beta-release.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/cli-publish.yml` (ci)
- `.github/workflows/docs-quality.yml` (ci)
- `.github/workflows/issue-triage.yml` (ci)
- `.github/workflows/pr-issue-close-policy.yml` (ci)
- `.github/workflows/readme-tables-sync.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `docs/materials/material-reference.json` (config)
- `docs/raw/img2threejs-skill-dataset.json` (config)
- `docs/specs/render-profile.v2.example.json` (config)
- `docs/specs/render-profile.v2.schema.json` (config)
- `forge/_shared/spec_search_profiles.json` (config)
- `forge/requirements.txt` (manifest)
- `grimoire/character/threejs_hair_parameter_contract.json` (config)
- `integrations/glb_character_pipeline/configs/girl-character-section-regions.json` (config)
- `integrations/glb_character_pipeline/configs/girl-character-spokes.json` (config)
- `integrations/glb_character_pipeline/node/package.json` (manifest)
- `integrations/glb_character_pipeline/pyproject.toml` (manifest)
- `integrations/vision/pyproject.toml` (manifest)
- `package.json` (manifest)
- `scripts/ci/skill-budget.json` (config)

## Top-level layout

- `forge` — 225 analysed file(s)
- `docs` — 33 analysed file(s)
- `integrations` — 28 analysed file(s)
- `grimoire` — 24 analysed file(s)
- `.github` — 14 analysed file(s)
- `scripts` — 14 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `assets` — 6 analysed file(s)
- `bin` — 2 analysed file(s)
- `skills` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 11 file(s) were skipped during inventory (3 x lockfile excluded; 8 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0c0c49bc168e648dbaf9c8c080474de0b3a941b6` is the revision these paths and observations refer to.
