# Project structure: CSFrequency/react-firebase-hooks

**Analysed commit:** `09bf06b28c82b4c3c1beabb1b32a8007232ed045`

**Commit reference:** [09bf06b28c82b4c3c1beabb1b32a8007232ed045](https://github.com/CSFrequency/react-firebase-hooks/commit/09bf06b28c82b4c3c1beabb1b32a8007232ed045)

**Tree at this commit:** [CSFrequency/react-firebase-hooks@09bf06b28c82](https://github.com/CSFrequency/react-firebase-hooks/tree/09bf06b28c82b4c3c1beabb1b32a8007232ed045)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | CSFrequency/react-firebase-hooks |
| Description | React Hooks for Firebase. |
| Stars | 3629 |
| Forks | 295 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `09bf06b28c82b4c3c1beabb1b32a8007232ed045` |
| Retrieved at | 2026-11-14T19:15:11.346799+00:00 |
| Files in this snapshot | 68 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    build.yml
    checks.yml
.opensource/  (1 files)
  project.json
auth/  (16 files)
  README.md
  index.ts
  package.json
  types.ts
  useAuthState.ts
  useCreateUserWithEmailAndPassword.ts
  useDeleteUser.ts
  useIdToken.ts
  useSendEmailVerification.ts
  useSendPasswordResetEmail.ts
  useSendSignInLinkToEmail.ts
  useSignInWithEmailAndPassword.ts
  useSignInWithEmailLink.ts
  useSignInWithPopup.ts
  useSignOut.ts
  useUpdateUser.ts
database/  (8 files)
  helpers/  (2 files)
    index.ts
    useListReducer.ts
  README.md
  index.ts
  package.json
  types.ts
  useList.ts
  useObject.ts
firestore/  (8 files)
  helpers/  (1 files)
    index.ts
  README.md
  index.ts
  package.json
  types.ts
  useCollection.ts
  useDocument.test.ts
  useDocument.ts
functions/  (4 files)
  README.md
  index.ts
  package.json
  useHttpsCallable.ts
messaging/  (4 files)
  README.md
  index.ts
  package.json
  useToken.ts
storage/  (5 files)
  README.md
  index.ts
  package.json
  useDownloadURL.ts
  useUploadFile.ts
test/  (1 files)
  firebase.ts
util/  (5 files)
  index.ts
  package.json
  refHooks.ts
  useIsMounted.ts
  useLoadingValue.ts
.editorconfig
.firebaserc
.gitignore
LICENSE
README.md
babel.config.js
firebase.json
firestore.indexes.json
firestore.rules
jest.config.ts
package.json
prettier.config.js
rollup.config.js
tsconfig.json
```

## Entry points

- [auth/index.ts](https://github.com/CSFrequency/react-firebase-hooks/blob/09bf06b28c82b4c3c1beabb1b32a8007232ed045/auth/index.ts)
- [database/helpers/index.ts](https://github.com/CSFrequency/react-firebase-hooks/blob/09bf06b28c82b4c3c1beabb1b32a8007232ed045/database/helpers/index.ts)
- [database/index.ts](https://github.com/CSFrequency/react-firebase-hooks/blob/09bf06b28c82b4c3c1beabb1b32a8007232ed045/database/index.ts)
- [firestore/helpers/index.ts](https://github.com/CSFrequency/react-firebase-hooks/blob/09bf06b28c82b4c3c1beabb1b32a8007232ed045/firestore/helpers/index.ts)
- [firestore/index.ts](https://github.com/CSFrequency/react-firebase-hooks/blob/09bf06b28c82b4c3c1beabb1b32a8007232ed045/firestore/index.ts)
- [functions/index.ts](https://github.com/CSFrequency/react-firebase-hooks/blob/09bf06b28c82b4c3c1beabb1b32a8007232ed045/functions/index.ts)
- [messaging/index.ts](https://github.com/CSFrequency/react-firebase-hooks/blob/09bf06b28c82b4c3c1beabb1b32a8007232ed045/messaging/index.ts)
- [storage/index.ts](https://github.com/CSFrequency/react-firebase-hooks/blob/09bf06b28c82b4c3c1beabb1b32a8007232ed045/storage/index.ts)
- [util/index.ts](https://github.com/CSFrequency/react-firebase-hooks/blob/09bf06b28c82b4c3c1beabb1b32a8007232ed045/util/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| auth package | library | Observed | Groups 14 file(s) under auth package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 9 file(s) under data layer (observed from repository paths and static analysis). |
| firestore package | library | Observed | Groups 6 file(s) under firestore package (observed from repository paths and static analysis). |
| functions package | library | Observed | Groups 2 file(s) under functions package (observed from repository paths and static analysis). |
| messaging package | library | Observed | Groups 2 file(s) under messaging package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 4 file(s) under util package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/checks.yml` (ci)
- `.opensource/project.json` (config)
- `auth/package.json` (manifest)
- `database/package.json` (manifest)
- `firebase.json` (config)
- `firestore.indexes.json` (config)
- `firestore/package.json` (manifest)
- `functions/package.json` (manifest)
- `messaging/package.json` (manifest)
- `package.json` (manifest)
- `storage/package.json` (manifest)
- `tsconfig.json` (config)
- `util/package.json` (manifest)

## Top-level layout

- `auth` — 16 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `database` — 8 analysed file(s)
- `firestore` — 8 analysed file(s)
- `storage` — 5 analysed file(s)
- `util` — 5 analysed file(s)
- `functions` — 4 analysed file(s)
- `messaging` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `.opensource` — 1 analysed file(s)
- `test` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `09bf06b28c82b4c3c1beabb1b32a8007232ed045` is the revision these paths and observations refer to.
