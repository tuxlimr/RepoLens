# Project structure: makerspet/oomwoo

**Analysed commit:** `108e9d34575f84d8547298fd594a7ea513f35093`

**Commit reference:** [108e9d34575f84d8547298fd594a7ea513f35093](https://github.com/makerspet/oomwoo/commit/108e9d34575f84d8547298fd594a7ea513f35093)

**Tree at this commit:** [makerspet/oomwoo@108e9d34575f](https://github.com/makerspet/oomwoo/tree/108e9d34575f84d8547298fd594a7ea513f35093)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | makerspet/oomwoo |
| Description | Open-source vacuum robot cleaner |
| Stars | 13098 |
| Forks | 824 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `108e9d34575f84d8547298fd594a7ea513f35093` |
| Retrieved at | 2026-11-14T19:09:55.449574+00:00 |
| Files in this snapshot | 107 |

## Directory tree

```text
.github/  (5 files)
  assets/  (2 files)
    star-history-dark.svg
    star-history-light.svg
  scripts/  (1 files)
    gen_star_history.py
  workflows/  (2 files)
    host-contribution-tests.yml
    star-history.yml
contributions/  (90 files)
  clean-and-map/  (3 files)
    Arkz-Deepak/  (1 files)
      … 1 files under this directory
    yugeeklab/  (1 files)
      … 1 files under this directory
    README.md
  cleaning-jobs/  (2 files)
    Valdi320/  (1 files)
      … 1 files under this directory
    README.md
  compute-benchmark/  (6 files)
    xbattlax/  (5 files)
      … 5 files under this directory
    README.md
  control-app/  (1 files)
    README.md
  dock-cycle/  (8 files)
    xbattlax/  (7 files)
      … 7 files under this directory
    README.md
  dust-bin/  (1 files)
    README.md
  esp32-p4/  (1 files)
    README.md
  floor-care/  (1 files)
    README.md
  health-monitor/  (3 files)
    bilusss/  (1 files)
      … 1 files under this directory
    xbattlax/  (1 files)
      … 1 files under this directory
    README.md
  io-board-interface/  (23 files)
    smailzhu/  (5 files)
      … 5 files under this directory
    xbattlax/  (17 files)
      … 17 files under this directory
    README.md
  io-pcb/  (1 files)
    README.md
  live-robot-bringup/  (1 files)
    README.md
  mac-dev-env/  (2 files)
    DingoOz/  (1 files)
      … 1 files under this directory
    README.md
  mcu-io-firmware/  (2 files)
    Creative-Dhanush/  (1 files)
      … 1 files under this directory
    README.md
  nav-localize/  (1 files)
    README.md
  obstacle-avoidance/  (1 files)
    README.md
  part-specs/  (15 files)
    IKsares/  (1 files)
      … 1 files under this directory
    OsakaTX/  (11 files)
      … 11 files under this directory
    Scowt/  (1 files)
      … 1 files under this directory
    serengon/  (1 files)
      … 1 files under this directory
    README.md
  recovery-safety/  (12 files)
    xbattlax/  (11 files)
      … 11 files under this directory
    README.md
  source-3d-models/  (1 files)
    README.md
  stair-climbing/  (1 files)
    README.md
  urdf-gazebo-sim/  (2 files)
    alvarosamudio/  (1 files)
      … 1 files under this directory
    README.md
  vacuum-fan/  (1 files)
    README.md
  README.md
docs/  (8 files)
  blog/  (2 files)
    oomwoo-one-first-ros2-package.md
    oomwoo-one-simulate-in-gazebo.md
  ARCHITECTURE.md
  BUILD_INSTRUCTIONS.md
  CONTRIBUTING.md
  RFC_BACKLOG.md
  SOFTWARE_INTERFACES.md
  design-document.md
.gitignore
BOM.md
LICENSE
README.md
```

## Entry points

- [.github/scripts/gen_star_history.py:163](https://github.com/makerspet/oomwoo/blob/108e9d34575f84d8547298fd594a7ea513f35093/.github/scripts/gen_star_history.py#L163)
- [contributions/dock-cycle/xbattlax/tools/sim_dock_ir_scenario.py:77](https://github.com/makerspet/oomwoo/blob/108e9d34575f84d8547298fd594a7ea513f35093/contributions/dock-cycle/xbattlax/tools/sim_dock_ir_scenario.py#L77)
- [contributions/io-board-interface/smailzhu/conformance/generate_gate_vectors.py:184](https://github.com/makerspet/oomwoo/blob/108e9d34575f84d8547298fd594a7ea513f35093/contributions/io-board-interface/smailzhu/conformance/generate_gate_vectors.py#L184)
- [contributions/io-board-interface/xbattlax/conformance/generate_vectors.py:189](https://github.com/makerspet/oomwoo/blob/108e9d34575f84d8547298fd594a7ea513f35093/contributions/io-board-interface/xbattlax/conformance/generate_vectors.py#L189)
- [contributions/io-board-interface/xbattlax/tools/sim_mcu.py:70](https://github.com/makerspet/oomwoo/blob/108e9d34575f84d8547298fd594a7ea513f35093/contributions/io-board-interface/xbattlax/tools/sim_mcu.py#L70)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| contributions package | library | Observed | Groups 9 file(s) under contributions package (observed from repository paths and static analysis). Observed top-level classes: CircleObstacle, ControllerState, Decision, DecisionKind, DockIrFrame, DockSpec. Observed top… |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: P, R, _bytes_initializer, _check_file, _identifier, _payload_hex. |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CommandGateVectorTest, ContractDriftTest, CorpusFreshnessTest, CorpusSchemaTest, DockIrModelTest, FrameCodec… |

## Important files

- `.github/workflows/host-contribution-tests.yml` (ci)
- `.github/workflows/star-history.yml` (ci)
- `contributions/io-board-interface/smailzhu/conformance/command_gate_vectors_v1.json` (config)
- `contributions/io-board-interface/xbattlax/conformance/golden_vectors_v1.json` (config)
- `contributions/io-board-interface/xbattlax/conformance/protocol_v1.json` (config)
- `contributions/recovery-safety/xbattlax/oomwoo_recovery_safety/setup.cfg` (manifest)
- `contributions/recovery-safety/xbattlax/oomwoo_recovery_safety/setup.py` (manifest)

## Top-level layout

- `contributions` — 90 analysed file(s)
- `docs` — 8 analysed file(s)
- `.github` — 5 analysed file(s)
- `(root files)` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `108e9d34575f84d8547298fd594a7ea513f35093` is the revision these paths and observations refer to.
