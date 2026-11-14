# Project structure: cpaczek/skylight

**Analysed commit:** `3656b4d56e11e23af58c8f12168d2edec88e7b53`

**Commit reference:** [3656b4d56e11e23af58c8f12168d2edec88e7b53](https://github.com/cpaczek/skylight/commit/3656b4d56e11e23af58c8f12168d2edec88e7b53)

**Tree at this commit:** [cpaczek/skylight@3656b4d56e11](https://github.com/cpaczek/skylight/tree/3656b4d56e11e23af58c8f12168d2edec88e7b53)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cpaczek/skylight |
| Description | Project the aircraft passing overhead onto your ceiling in real time, from an RTL-SDR — with a live sky layer (sun, moon, stars, ISS) and where each plane is headed. |
| Stars | 3394 |
| Forks | 415 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `3656b4d56e11e23af58c8f12168d2edec88e7b53` |
| Retrieved at | 2026-11-14T19:15:20.797680+00:00 |
| Files in this snapshot | 336 |

## Directory tree

```text
docs/  (5 files)
  camera-profile.md
  handoff-2026-10-14.md
  handoff-2026-10-15.md
  handoff-2026-10-16.md
  pass-archive.md
passes/  (16 files)
  src/  (3 files)
    index.ts
    query.ts
    row.ts
  test/  (4 files)
    fixtures/  (1 files)
      … 1 files under this directory
    ingest.test.ts
    query.test.ts
    row.test.ts
  tools/  (3 files)
    geometry-backfill.ts
    geometry-extract.py
    rescore.ts
  .gitignore
  README.md
  package.json
  schema.sql
  tsconfig.json
  wrangler.toml
pi-setup/  (13 files)
  README.md
  install-on-pi.sh
  provision-sd.sh
  setup-kiosk.sh
  skylight-exposure.service
  skylight-exposure.timer
  skylight-keypress.py
  skylight-server.service
  skylight-tracker.service
  skylight-tv-kiosk.sh
  skylight-update.service
  skylight-update.sh
  skylight-update.timer
scripts/  (5 files)
  deploy-to-pi.sh
  fetch-vision-model.sh
  install-rtlsdr-fedora.sh
  run-dump1090-local.sh
  screenshot.mjs
server/  (26 files)
  src/  (17 files)
    enrich/  (5 files)
      … 5 files under this directory
    airlines.ts
    airports.ts
    allowed-hosts.ts
    config-store.ts
    datasource.ts
    geocode.ts
    hub.ts
    index.ts
    satcat.ts
    sfo-ground.ts
    telemetry.ts
    tle.ts
  test/  (7 files)
    allowed-hosts.test.ts
    api-source.test.ts
    geocode.test.ts
    poller-source.test.ts
    route-check.test.ts
    seen-pos.test.ts
    telemetry.test.ts
  package.json
  tsconfig.json
shared/  (30 files)
  src/  (16 files)
    aim.ts
    aircraft.ts
    airport.ts
    camera-profile.ts
    camera.ts
    celestial.ts
    config.ts
    constants.ts
    format.ts
    geo.ts
    index.ts
    messages.ts
    route.ts
    skyEvents.ts
    stars.ts
    tracker-messages.ts
  test/  (12 files)
    aim-fixage.test.ts
    aim-geometry.test.ts
    aim-mount.test.ts
    aim-predict.test.ts
    axis-steer.test.ts
    celestial-planets.test.ts
    config-merge.test.ts
    format.test.ts
    horizon.test.ts
    route-plausible.test.ts
    sky-events.test.ts
    sky-projection.test.ts
  package.json
  tsconfig.json
stabilizer/  (17 files)
  skylight_stab/  (9 files)
    __init__.py
    __main__.py
    archive.py
    deband.py
    detect.py
    pipeline.py
    plan.py
    service.py
    video.py
  systemd/  (1 files)
    skylight-stabilizer.service
  tests/  (3 files)
    test_archive.py
    test_deband.py
    test_plan.py
  tools/  (1 files)
    export_flatfield_ts.py
  .gitignore
  README.md
  requirements.txt
stream/  (4 files)
  .env.example
  README.md
  skylight-stream@.service
  start-stream.sh
telemetry/  (7 files)
  src/  (1 files)
    index.ts
  .gitignore
  README.md
  package.json
  schema.sql
  tsconfig.json
  wrangler.toml
tracker/  (143 files)
  scripts/  (63 files)
    analysis/  (24 files)
      … 24 files under this directory
    calib/  (5 files)
      … 5 files under this directory
    camera-web/  (2 files)
      … 2 files under this directory
    lib/  (3 files)
      … 3 files under this directory
    passes/  (6 files)
      … 6 files under this directory
    cal-analyze.ts
    characterize-camera.ts
    goto-pose.ts
    measure-fov.ts
    measure-vision-lag.ts
    motion-profile.ts
    motion-validate.ts
    onvif-cmd.ts
    onvif-ptz.ts
    print-camera-profile.ts
    probe-abs-speed.ts
    probe-mech.ts
    probe-onvif-speed.ts
    probe-speed-zoom.ts
    probe-speed-zoomchange.ts
    probe-tilt-reach.ts
    probe-tilt-slip.ts
    probe-zoom-busy.ts
    probe-zoomdrive.ts
    probe-zoomfocus.ts
    stabilize-cli.ts
    survey-ring.ts
    visca-diag.ts
  src/  (39 files)
    calibration/  (3 files)
      … 3 files under this directory
    camera/  (5 files)
      … 5 files under this directory
    passes/  (8 files)
      … 8 files under this directory
    pointing/  (8 files)
      … 8 files under this directory
    video/  (4 files)
      … 4 files under this directory
    vision/  (6 files)
      … 6 files under this directory
    hub.ts
    index.ts
    loop.ts
    record.ts
    upstream.ts
  test/  (39 files)
    sim/  (4 files)
      … 4 files under this directory
    autocal.test.ts
    departure.test.ts
    focus.test.ts
    frame-geom.test.ts
    landmarks.test.ts
    lead-learn.test.ts
    loop-sim.test.ts
    merge-blobs.test.ts
    motion.test.ts
    nextpass.test.ts
    passes-archive.test.ts
    passes-clip.test.ts
    passes-geometry.test.ts
    passes-quality.test.ts
    passes-summary.test.ts
    passes-uploader.test.ts
    pipeline.test.ts
    planner.test.ts
    predict-latency.test.ts
    sharpness.test.ts
    silhouette.test.ts
    smooth-geo.test.ts
    speed-floor.test.ts
    speed-surface.test.ts
    … 11 more files
  package.json
  tsconfig.json
web/  (60 files)
  src/  (49 files)
    control/  (3 files)
      … 3 files under this directory
    display/  (9 files)
      … 9 files under this directory
    lib/  (4 files)
      … 4 files under this directory
    stream/  (2 files)
      … 2 files under this directory
    styles/  (5 files)
      … 5 files under this directory
    tracker/  (13 files)
      … 13 files under this directory
    tv/  (12 files)
      … 12 files under this directory
    types/  (1 files)
      … 1 files under this directory
  test/  (3 files)
    crop-follow.test.ts
    geolocation.test.ts
    live-stab.test.ts
  control.html
  index.html
  package.json
  stream.html
  tracker.html
  tsconfig.json
  tv.html
  vite.config.ts
.dockerignore
.gitignore
Dockerfile
LICENSE
README.md
compose.yaml
package.json
pnpm-workspace.yaml
tsconfig.base.json
vitest.config.ts
```

## Entry points

- [stabilizer/skylight_stab/__main__.py:47](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/stabilizer/skylight_stab/__main__.py#L47)
- [tracker/scripts/calib/pass_bias_fit.py:96](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/tracker/scripts/calib/pass_bias_fit.py#L96)
- [tracker/scripts/calib/remount_fit.py:158](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/tracker/scripts/calib/remount_fit.py#L158)
- [tracker/scripts/camera-web/camweb.py:55](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/tracker/scripts/camera-web/camweb.py#L55)
- [tracker/scripts/camera-web/exposure-by-sun.py:62](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/tracker/scripts/camera-web/exposure-by-sun.py#L62)
- [server/src/index.ts](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/server/src/index.ts)
- [tracker/src/index.ts](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/tracker/src/index.ts)
- [passes/src/index.ts](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/passes/src/index.ts)
- [shared/src/index.ts](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/shared/src/index.ts)
- [telemetry/src/index.ts](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/telemetry/src/index.ts)
- [web/src/control/main.tsx](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/web/src/control/main.tsx)
- [web/src/display/main.tsx](https://github.com/cpaczek/skylight/blob/3656b4d56e11e23af58c8f12168d2edec88e7b53/web/src/display/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 23 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 5 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: best_match, call, grad_img, isotropic, login, main. |
| passes package | library | Observed | Groups 6 file(s) under passes package (observed from repository paths and static analysis). Observed top-level functions: ms. |
| pi-setup package | library | Observed | Groups 6 file(s) under pi-setup package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 15 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level functions: _fail_path, _failures, _log, _pending, _record_failure, mark. |
| shared package | library | Observed | Groups 16 file(s) under shared package (observed from repository paths and static analysis). |
| stabilizer package | library | Observed | Groups 8 file(s) under stabilizer package (observed from repository paths and static analysis). Observed top-level classes: Analysis, Blob, Clean, Debander, FlatField, Guard. Observed top-level functions: _json_req, _ke… |
| stream package | library | Observed | Groups 1 file(s) under stream package (observed from repository paths and static analysis). |
| telemetry package | library | Observed | Groups 1 file(s) under telemetry package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 68 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: _Resp. Observed top-level functions: _fake, staircase, synthetic, test_big_file_multipart, test_bridges_sho… |
| tracker package | library | Observed | Groups 95 file(s) under tracker package (observed from repository paths and static analysis). Observed top-level classes: Dither, Stepper, Traj. Observed top-level functions: _axis, _azel, _rot, _vec, azel2vec, bracket. |
| web package | library | Observed | Groups 45 file(s) under web package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `Dockerfile` (container)
- `compose.yaml` (container)
- `package.json` (manifest)
- `passes/package.json` (manifest)
- `passes/tsconfig.json` (config)
- `passes/wrangler.toml` (config)
- `pnpm-workspace.yaml` (config)
- `server/package.json` (manifest)
- `server/src/enrich/airlines.json` (config)
- `server/src/enrich/types.json` (config)
- `server/tsconfig.json` (config)
- `shared/package.json` (manifest)
- `shared/tsconfig.json` (config)
- `stabilizer/requirements.txt` (manifest)
- `stream/.env.example` (config)
- `telemetry/package.json` (manifest)
- `telemetry/tsconfig.json` (config)
- `telemetry/wrangler.toml` (config)
- `tracker/package.json` (manifest)
- `tracker/tsconfig.json` (config)
- `tsconfig.base.json` (config)
- `web/package.json` (manifest)
- `web/tsconfig.json` (config)

## Top-level layout

- `tracker` — 143 analysed file(s)
- `web` — 60 analysed file(s)
- `shared` — 30 analysed file(s)
- `server` — 26 analysed file(s)
- `stabilizer` — 17 analysed file(s)
- `passes` — 16 analysed file(s)
- `pi-setup` — 13 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `telemetry` — 7 analysed file(s)
- `docs` — 5 analysed file(s)
- `scripts` — 5 analysed file(s)
- `stream` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (2 x likely secret file excluded; 1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3656b4d56e11e23af58c8f12168d2edec88e7b53` is the revision these paths and observations refer to.
