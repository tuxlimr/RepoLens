# Project structure: antonioru/beautiful-react-hooks

**Analysed commit:** `ee987048b0c138d51bff59f92bc9d5f1bafddbfb`

**Commit reference:** [ee987048b0c138d51bff59f92bc9d5f1bafddbfb](https://github.com/antonioru/beautiful-react-hooks/commit/ee987048b0c138d51bff59f92bc9d5f1bafddbfb)

**Tree at this commit:** [antonioru/beautiful-react-hooks@ee987048b0c1](https://github.com/antonioru/beautiful-react-hooks/tree/ee987048b0c138d51bff59f92bc9d5f1bafddbfb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | antonioru/beautiful-react-hooks |
| Description | 🔥 A collection of beautiful and (hopefully) useful React hooks to speed-up your components and hooks development 🔥 |
| Stars | 8339 |
| Forks | 577 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ee987048b0c138d51bff59f92bc9d5f1bafddbfb` |
| Retrieved at | 2026-11-14T19:13:41.833080+00:00 |
| Files in this snapshot | 258 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    branch-tests.yml
    ci.yml
  PULL_REQUEST_TEMPLATE.md
  tests_checker.yml
docs/  (76 files)
  utils/  (5 files)
    _CustomLogo.js
    _EmptyComponent.js
    _custom.css
    _setup.js
    _styleguidist.theme.js
  Installation.md
  Introduction.md
  README.es-ES.md
  README.it-IT.md
  README.jp-JP.md
  README.pl-PL.md
  README.pt-BR.md
  README.tr-TR.md
  README.uk-UA.md
  README.zh-CN.md
  useAudio.md
  useConditionalTimeout.md
  useCookie.md
  useDarkMode.md
  useDebouncedCallback.md
  useDefaultedState.md
  useDidMount.md
  useDrag.md
  useDragEvents.md
  useDropZone.md
  useEvent.md
  useGeolocation.md
  useGeolocationEvents.md
  useGeolocationState.md
  … 47 more files
scripts/  (4 files)
  commit-version.sh
  generate-doc-append-types.js
  generate-exports.js
  update-version.js
src/  (74 files)
  factory/  (2 files)
    createHandlerSetter.ts
    createStorageHook.ts
  shared/  (11 files)
    geolocationUtils.ts
    isAPISupported.ts
    isClient.ts
    isDevelopment.ts
    isFunction.ts
    noop.ts
    safeHasOwnProperty.ts
    safelyParseJson.ts
    swipeUtils.ts
    types.ts
    warnOnce.ts
  useAudio.ts
  useConditionalTimeout.ts
  useCookie.ts
  useDarkMode.ts
  useDebouncedCallback.ts
  useDefaultedState.ts
  useDidMount.ts
  useDrag.ts
  useDragEvents.ts
  useDropZone.ts
  useEvent.ts
  useGeolocation.ts
  useGeolocationEvents.ts
  useGeolocationState.ts
  useGlobalEvent.ts
  useHorizontalSwipe.ts
  useInfiniteScroll.ts
  useInterval.ts
  useIsFirstRender.ts
  useLifecycle.ts
  useLocalStorage.ts
  useLongPress.ts
  useMediaQuery.ts
  useMouse.ts
  … 37 more files
test/  (78 files)
  mocks/  (8 files)
    AudioApi.mock.js
    CookieStoreApi.mock.js
    GeoLocationApi.mock.js
    IntersectionObserver.mock.js
    MatchMediaQueryList.mock.js
    ResizeObserver.mock.js
    SpeechSynthesis.mock.js
    SpeechSynthesisUtterance.mock.js
  utils/  (4 files)
    ReactRouterWrapper.js
    assertFunction.js
    assertHook.js
    promiseDelay.js
  _setup.js
  geolocationUtils.spec.js
  isAPISupported.spec.js
  isClient.spec.js
  safeHasOwnProperty.spec.js
  useAudio.spec.js
  useConditionalTimeout.spec.js
  useCookie.spec.js
  useDarkMode.spec.js
  useDebouncedCallback.spec.js
  useDefaultedState.spec.js
  useDidMount.spec.js
  useDrag.spec.js
  useDragEvents.spec.js
  useDropZone.spec.js
  useEvent.spec.js
  useGeolocation.spec.js
  useGeolocationEvents.spec.js
  useGeolocationState.spec.js
  useGlobalEvent.spec.js
  useHandlerSetter.spec.js
  useInfiniteScroll.spec.js
  useInterval.spec.js
  useIsFirstRender.spec.js
  … 42 more files
.eslintignore
.eslintrc.js
.gitignore
.huskyrc
.mocharc.json
.nycrc
.releaserc.json
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
HOOK_DOCUMENTATION_TEMPLATE.md
LICENSE.txt
README.md
babel.config.js
package.json
styleguide.config.js
tsconfig.cjs.json
tsconfig.esm.json
tsconfig.json
tsconfig.types.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| factory package | library | Observed | Groups 2 file(s) under factory package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 11 file(s) under shared package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 78 file(s) under tests (observed from repository paths and static analysis). |
| useAudio.ts package | library | Observed | Groups 1 file(s) under useaudio.ts package (observed from repository paths and static analysis). |
| useConditionalTimeout.ts package | library | Observed | Groups 1 file(s) under useconditionaltimeout.ts package (observed from repository paths and static analysis). |
| useCookie.ts package | library | Observed | Groups 1 file(s) under usecookie.ts package (observed from repository paths and static analysis). |
| useDarkMode.ts package | library | Observed | Groups 1 file(s) under usedarkmode.ts package (observed from repository paths and static analysis). |
| useDebouncedCallback.ts package | library | Observed | Groups 1 file(s) under usedebouncedcallback.ts package (observed from repository paths and static analysis). |
| useDefaultedState.ts package | library | Observed | Groups 1 file(s) under usedefaultedstate.ts package (observed from repository paths and static analysis). |
| useDidMount.ts package | library | Observed | Groups 1 file(s) under usedidmount.ts package (observed from repository paths and static analysis). |
| useDrag.ts package | library | Observed | Groups 1 file(s) under usedrag.ts package (observed from repository paths and static analysis). |
| useDragEvents.ts package | library | Observed | Groups 1 file(s) under usedragevents.ts package (observed from repository paths and static analysis). |
| useDropZone.ts package | library | Observed | Groups 1 file(s) under usedropzone.ts package (observed from repository paths and static analysis). |
| useEvent.ts package | library | Observed | Groups 1 file(s) under useevent.ts package (observed from repository paths and static analysis). |
| useGeolocation.ts package | library | Observed | Groups 1 file(s) under usegeolocation.ts package (observed from repository paths and static analysis). |
| useGeolocationEvents.ts package | library | Observed | Groups 1 file(s) under usegeolocationevents.ts package (observed from repository paths and static analysis). |
| useGeolocationState.ts package | library | Observed | Groups 1 file(s) under usegeolocationstate.ts package (observed from repository paths and static analysis). |
| useGlobalEvent.ts package | library | Observed | Groups 1 file(s) under useglobalevent.ts package (observed from repository paths and static analysis). |
| useHorizontalSwipe.ts package | library | Observed | Groups 1 file(s) under usehorizontalswipe.ts package (observed from repository paths and static analysis). |
| useInfiniteScroll.ts package | library | Observed | Groups 1 file(s) under useinfinitescroll.ts package (observed from repository paths and static analysis). |
| useInterval.ts package | library | Observed | Groups 1 file(s) under useinterval.ts package (observed from repository paths and static analysis). |
| useIsFirstRender.ts package | library | Observed | Groups 1 file(s) under useisfirstrender.ts package (observed from repository paths and static analysis). |
| useLifecycle.ts package | library | Observed | Groups 1 file(s) under uselifecycle.ts package (observed from repository paths and static analysis). |
| useLocalStorage.ts package | library | Observed | Groups 1 file(s) under uselocalstorage.ts package (observed from repository paths and static analysis). |
| useLongPress.ts package | library | Observed | Groups 1 file(s) under uselongpress.ts package (observed from repository paths and static analysis). |
| useMediaQuery.ts package | library | Observed | Groups 1 file(s) under usemediaquery.ts package (observed from repository paths and static analysis). |
| useMouse.ts package | library | Observed | Groups 1 file(s) under usemouse.ts package (observed from repository paths and static analysis). |
| useMouseEvents.ts package | library | Observed | Groups 1 file(s) under usemouseevents.ts package (observed from repository paths and static analysis). |
| useMouseState.ts package | library | Observed | Groups 1 file(s) under usemousestate.ts package (observed from repository paths and static analysis). |
| useMutableState.ts package | library | Observed | Groups 1 file(s) under usemutablestate.ts package (observed from repository paths and static analysis). |
| useMutationObserver.ts package | library | Observed | Groups 1 file(s) under usemutationobserver.ts package (observed from repository paths and static analysis). |
| useObjectState.ts package | library | Observed | Groups 1 file(s) under useobjectstate.ts package (observed from repository paths and static analysis). |
| useObservable.ts package | library | Observed | Groups 1 file(s) under useobservable.ts package (observed from repository paths and static analysis). |
| useOnlineState.ts package | library | Observed | Groups 1 file(s) under useonlinestate.ts package (observed from repository paths and static analysis). |
| usePreviousValue.ts package | library | Observed | Groups 1 file(s) under usepreviousvalue.ts package (observed from repository paths and static analysis). |
| useQueryParam.ts package | library | Observed | Groups 1 file(s) under usequeryparam.ts package (observed from repository paths and static analysis). |
| useQueryParams.ts package | library | Observed | Groups 1 file(s) under usequeryparams.ts package (observed from repository paths and static analysis). |
| useRenderInfo.ts package | library | Observed | Groups 1 file(s) under userenderinfo.ts package (observed from repository paths and static analysis). |
| useRequestAnimationFrame.ts package | library | Observed | Groups 1 file(s) under userequestanimationframe.ts package (observed from repository paths and static analysis). |
| useResizeObserver.ts package | library | Observed | Groups 1 file(s) under useresizeobserver.ts package (observed from repository paths and static analysis). |
| useSearchQuery.ts package | library | Observed | Groups 1 file(s) under usesearchquery.ts package (observed from repository paths and static analysis). |
| useSessionStorage.ts package | library | Observed | Groups 1 file(s) under usesessionstorage.ts package (observed from repository paths and static analysis). |
| useSpeechRecognition.ts package | library | Observed | Groups 1 file(s) under usespeechrecognition.ts package (observed from repository paths and static analysis). |
| useSpeechSynthesis.ts package | library | Observed | Groups 1 file(s) under usespeechsynthesis.ts package (observed from repository paths and static analysis). |
| useSwipe.ts package | library | Observed | Groups 1 file(s) under useswipe.ts package (observed from repository paths and static analysis). |
| useSwipeEvents.ts package | library | Observed | Groups 1 file(s) under useswipeevents.ts package (observed from repository paths and static analysis). |
| useSystemVoices.ts package | library | Observed | Groups 1 file(s) under usesystemvoices.ts package (observed from repository paths and static analysis). |
| useThrottledCallback.ts package | library | Observed | Groups 1 file(s) under usethrottledcallback.ts package (observed from repository paths and static analysis). |
| useTimeout.ts package | library | Observed | Groups 1 file(s) under usetimeout.ts package (observed from repository paths and static analysis). |
| useToggle.ts package | library | Observed | Groups 1 file(s) under usetoggle.ts package (observed from repository paths and static analysis). |
| useTouch.ts package | library | Observed | Groups 1 file(s) under usetouch.ts package (observed from repository paths and static analysis). |
| useTouchEvents.ts package | library | Observed | Groups 1 file(s) under usetouchevents.ts package (observed from repository paths and static analysis). |
| useTouchState.ts package | library | Observed | Groups 1 file(s) under usetouchstate.ts package (observed from repository paths and static analysis). |
| useUnmount.ts package | library | Observed | Groups 1 file(s) under useunmount.ts package (observed from repository paths and static analysis). |
| useUpdateEffect.ts package | library | Observed | Groups 1 file(s) under useupdateeffect.ts package (observed from repository paths and static analysis). |
| useURLSearchParams.ts package | library | Observed | Groups 1 file(s) under useurlsearchparams.ts package (observed from repository paths and static analysis). |
| useValidatedState.ts package | library | Observed | Groups 1 file(s) under usevalidatedstate.ts package (observed from repository paths and static analysis). |
| useValueHistory.ts package | library | Observed | Groups 1 file(s) under usevaluehistory.ts package (observed from repository paths and static analysis). |
| useVerticalSwipe.ts package | library | Observed | Groups 1 file(s) under useverticalswipe.ts package (observed from repository paths and static analysis). |
| useViewportSpy.ts package | library | Observed | Groups 1 file(s) under useviewportspy.ts package (observed from repository paths and static analysis). |
| useViewportState.ts package | library | Observed | Groups 1 file(s) under useviewportstate.ts package (observed from repository paths and static analysis). |
| useWillUnmount.ts package | library | Observed | Groups 1 file(s) under usewillunmount.ts package (observed from repository paths and static analysis). |
| useWindowResize.ts package | library | Observed | Groups 1 file(s) under usewindowresize.ts package (observed from repository paths and static analysis). |
| useWindowScroll.ts package | library | Observed | Groups 1 file(s) under usewindowscroll.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/tests_checker.yml` (config)
- `.github/workflows/branch-tests.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.mocharc.json` (config)
- `.releaserc.json` (config)
- `package.json` (manifest)
- `tsconfig.cjs.json` (config)
- `tsconfig.esm.json` (config)
- `tsconfig.json` (config)
- `tsconfig.types.json` (config)

## Top-level layout

- `test` — 78 analysed file(s)
- `docs` — 76 analysed file(s)
- `src` — 74 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 6 analysed file(s)
- `scripts` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ee987048b0c138d51bff59f92bc9d5f1bafddbfb` is the revision these paths and observations refer to.
