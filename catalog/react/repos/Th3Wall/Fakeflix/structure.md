# Project structure: Th3Wall/Fakeflix

**Analysed commit:** `2ef25d14a112e3c90e4b482b4c964b9404d436b6`

**Commit reference:** [2ef25d14a112e3c90e4b482b4c964b9404d436b6](https://github.com/Th3Wall/Fakeflix/commit/2ef25d14a112e3c90e4b482b4c964b9404d436b6)

**Tree at this commit:** [Th3Wall/Fakeflix@2ef25d14a112](https://github.com/Th3Wall/Fakeflix/tree/2ef25d14a112e3c90e4b482b4c964b9404d436b6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Th3Wall/Fakeflix |
| Description | Not the usual clone that you can find on the web. |
| Stars | 4948 |
| Forks | 666 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `2ef25d14a112e3c90e4b482b4c964b9404d436b6` |
| Retrieved at | 2026-11-14T19:14:33.434089+00:00 |
| Files in this snapshot | 133 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    azure-static-web-apps-jolly-coast-0bfdaf303.yml
  FUNDING.yml
public/  (3 files)
  index.html
  manifest.json
  robots.txt
src/  (120 files)
  components/  (36 files)
    Banner/  (2 files)
      … 2 files under this directory
    Credits/  (2 files)
      … 2 files under this directory
    DetailModal/  (2 files)
      … 2 files under this directory
    InputField/  (2 files)
      … 2 files under this directory
    Loader/  (2 files)
      … 2 files under this directory
    Navbar/  (2 files)
      … 2 files under this directory
    PlayAnimation/  (2 files)
      … 2 files under this directory
    Poster/  (2 files)
      … 2 files under this directory
    Row/  (2 files)
      … 2 files under this directory
    RowPoster/  (2 files)
      … 2 files under this directory
    Searchbar/  (2 files)
      … 2 files under this directory
    SignIn/  (2 files)
      … 2 files under this directory
    SignUp/  (2 files)
      … 2 files under this directory
    SkeletonBanner/  (2 files)
      … 2 files under this directory
    SkeletonElement/  (2 files)
      … 2 files under this directory
    SkeletonPage/  (2 files)
      … 2 files under this directory
    SkeletonPoster/  (2 files)
      … 2 files under this directory
    SplashAnimation/  (2 files)
      … 2 files under this directory
  firebase/  (1 files)
    firebaseUtils.js
  hooks/  (7 files)
    useGenreConversion.js
    useLazyLoad.js
    useOutsideClick.js
    useRetrieveCategory.js
    useRetrieveData.js
    useScroll.js
    useViewport.js
  pages/  (16 files)
    Auth/  (2 files)
      … 2 files under this directory
    Category/  (2 files)
      … 2 files under this directory
    Homepage/  (2 files)
      … 2 files under this directory
    Movies/  (2 files)
      … 2 files under this directory
    MyList/  (2 files)
      … 2 files under this directory
    Popular/  (2 files)
      … 2 files under this directory
    Search/  (2 files)
      … 2 files under this directory
    TVSeries/  (2 files)
      … 2 files under this directory
  redux/  (50 files)
    auth/  (5 files)
      … 5 files under this directory
    favourites/  (5 files)
      … 5 files under this directory
    modal/  (4 files)
      … 4 files under this directory
    movies/  (15 files)
      … 15 files under this directory
    search/  (4 files)
      … 4 files under this directory
    series/  (14 files)
      … 14 files under this directory
    rootReducer.js
    rootSaga.js
    store.js
  scss/  (2 files)
    _mixin.scss
    _variables.scss
  App.js
  axiosInstance.js
  dataConfig.js
  index.js
  index.scss
  motionUtils.js
  requests.js
  utils.js
.babelrc
.env.sample
.eslintrc
.gitignore
LICENSE
README.md
google803f79ad64114124.html
package.json
```

## Entry points

- [src/App.js](https://github.com/Th3Wall/Fakeflix/blob/2ef25d14a112e3c90e4b482b4c964b9404d436b6/src/App.js)
- [src/index.js](https://github.com/Th3Wall/Fakeflix/blob/2ef25d14a112e3c90e4b482b4c964b9404d436b6/src/index.js)
- [src/redux/auth/index.js](https://github.com/Th3Wall/Fakeflix/blob/2ef25d14a112e3c90e4b482b4c964b9404d436b6/src/redux/auth/index.js)
- [src/redux/favourites/index.js](https://github.com/Th3Wall/Fakeflix/blob/2ef25d14a112e3c90e4b482b4c964b9404d436b6/src/redux/favourites/index.js)
- [src/redux/modal/index.js](https://github.com/Th3Wall/Fakeflix/blob/2ef25d14a112e3c90e4b482b4c964b9404d436b6/src/redux/modal/index.js)
- [src/redux/movies/index.js](https://github.com/Th3Wall/Fakeflix/blob/2ef25d14a112e3c90e4b482b4c964b9404d436b6/src/redux/movies/index.js)
- [src/redux/search/index.js](https://github.com/Th3Wall/Fakeflix/blob/2ef25d14a112e3c90e4b482b4c964b9404d436b6/src/redux/search/index.js)
- [src/redux/series/index.js](https://github.com/Th3Wall/Fakeflix/blob/2ef25d14a112e3c90e4b482b4c964b9404d436b6/src/redux/series/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| axiosInstance.js package | library | Observed | Groups 1 file(s) under axiosinstance.js package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 18 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dataConfig.js package | library | Observed | Groups 1 file(s) under dataconfig.js package (observed from repository paths and static analysis). |
| firebase package | library | Observed | Groups 1 file(s) under firebase package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 7 file(s) under hooks package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| motionUtils.js package | library | Observed | Groups 1 file(s) under motionutils.js package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 8 file(s) under pages package (observed from repository paths and static analysis). |
| redux package | library | Observed | Groups 50 file(s) under redux package (observed from repository paths and static analysis). |
| requests.js package | library | Observed | Groups 1 file(s) under requests.js package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |

## Important files

- `.env.sample` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/azure-static-web-apps-jolly-coast-0bfdaf303.yml` (ci)
- `package.json` (manifest)
- `public/manifest.json` (config)

## Top-level layout

- `src` — 120 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `public` — 3 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2ef25d14a112e3c90e4b482b4c964b9404d436b6` is the revision these paths and observations refer to.
