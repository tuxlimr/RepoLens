# Project structure: sahat/hackathon-starter

**Analysed commit:** `e735ca8f29d18158b7553244d4e6625ef7eaa383`

**Commit reference:** [e735ca8f29d18158b7553244d4e6625ef7eaa383](https://github.com/sahat/hackathon-starter/commit/e735ca8f29d18158b7553244d4e6625ef7eaa383)

**Tree at this commit:** [sahat/hackathon-starter@e735ca8f29d1](https://github.com/sahat/hackathon-starter/tree/e735ca8f29d18158b7553244d4e6625ef7eaa383)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sahat/hackathon-starter |
| Description | A boilerplate for Node.js web applications |
| Stars | 35260 |
| Forks | 8103 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e735ca8f29d18158b7553244d4e6625ef7eaa383` |
| Retrieved at | 2026-11-14T19:10:42.858579+00:00 |
| Files in this snapshot | 155 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (2 files)
    build.yml
    dependabot-automerge.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.husky/  (1 files)
  pre-commit
config/  (6 files)
  cacheBust.js
  flash.js
  morgan.js
  nodemailer.js
  passport.js
  token-revocation.js
controllers/  (7 files)
  ai-agent.js
  ai.js
  api.js
  contact.js
  home.js
  user.js
  webauthn.js
models/  (2 files)
  Session.js
  User.js
patches/  (3 files)
  passport+0.7.0.patch
  passport-oauth1+1.3.0.patch
  passport-oauth2+1.8.0.patch
public/  (8 files)
  css/  (1 files)
    main.scss
  js/  (4 files)
    lib/  (1 files)
      … 1 files under this directory
    cookieconsent-bundle.js
    main.js
    theme.js
  bootstrap-logo.svg
  privacy-policy.html
  terms-of-use.html
test/  (65 files)
  e2e/  (10 files)
    chart.e2e.test.js
    foursquare.e2e.test.js
    giphy.e2e.test.js
    google-maps.e2e.test.js
    here-maps.e2e.test.js
    llm-classifier.e2e.test.js
    lob.e2e.test.js
    nyt.e2e.test.js
    rag.e2e.test.js
    twilio.e2e.test.js
  e2e-nokey/  (7 files)
    github-api.e2e.test.js
    lastfm.e2e.test.js
    pubchem.e2e.test.js
    scraping.e2e.test.js
    theme.e2e.test.js
    upload.e2e.test.js
    wikipedia.e2e.test.js
  fixtures/  (28 files)
    GET_http%3A%2F%2Fws.audioscrobbler.com%2F6f1cdb8d5707.json
    GET_http%3A%2F%2Fws.audioscrobbler.com%2F7953f90072b4.json
    GET_http%3A%2F%2Fws.audioscrobbler.com%2Ff72869b8a412.json
    GET_https%3A%2F%2Fapi.giphy.com%2F4189fbfa3255.json
    GET_https%3A%2F%2Fapi.giphy.com%2Fec0c29439d0f.json
    GET_https%3A%2F%2Fapi.github.com%2Fdb109715600b.json
    GET_https%3A%2F%2Fapi.nytimes.com%2F9148841df88c.json
    GET_https%3A%2F%2Fen.wikipedia.org%2F34742f7aced6.json
    GET_https%3A%2F%2Fen.wikipedia.org%2F6cdd4d058049.json
    GET_https%3A%2F%2Fen.wikipedia.org%2F86d779039568.json
    GET_https%3A%2F%2Fen.wikipedia.org%2F89d31365348d.json
    GET_https%3A%2F%2Fnews.ycombinator.com%2F8a5edab28263.json
    GET_https%3A%2F%2Fplaces-api.foursquare.com%2F478c17e7311f.json
    GET_https%3A%2F%2Fplaces-api.foursquare.com%2F582378fe2f4b.json
    GET_https%3A%2F%2Fpubchem.ncbi.nlm.nih.gov%2F70ef24fb1b8c.json
    GET_https%3A%2F%2Fpubchem.ncbi.nlm.nih.gov%2F7463b67dbfdc.json
    GET_https%3A%2F%2Fpubchem.ncbi.nlm.nih.gov%2F8f7968925bbc.json
    GET_https%3A%2F%2Fpubchem.ncbi.nlm.nih.gov%2F99f2b46bd3d0.json
    GET_https%3A%2F%2Fpubchem.ncbi.nlm.nih.gov%2Ff1e57595e1d5.json
    GET_https%3A%2F%2Fwww.alphavantage.co%2F567c59988309.json
    POST_https%3A%2F%2Fapi.groq.com%2F85cb85fde355_e594495b41b8.json
    POST_https%3A%2F%2Fapi.twilio.com%2F736bd01d4665_25ca7364ce02.json
    POST_https%3A%2F%2Fapi.twilio.com%2F736bd01d4665_9cf625bb20f5.json
    POST_https%3A%2F%2Fapi.twilio.com%2F736bd01d4665_cec34eae746f.json
    … 4 more files
  tools/  (4 files)
    nock-server-fixtures.js
    playwright-start-and-log.js
    simple-link-image-check.js
    start-with-memory-db.js
  TESTING.md
  app-links.test.js
  app.test.js
  cacheBust.test.js
  contact.test.js
  docs-links.test.js
  flash.test.js
  models.test.js
  morgan.test.js
  nodemailer.test.js
  passport.test.js
  playwright.config.js
  session.test.js
  token-revocation.test.js
  user.test.js
  webauthn.test.js
views/  (44 files)
  account/  (9 files)
    forgot.pug
    login.pug
    profile.pug
    reset.pug
    signup.pug
    totp-setup.pug
    two-factor.pug
    webauthn-login.pug
    webauthn-register.pug
  ai/  (5 files)
    ai-agent.pug
    index.pug
    llm-camera.pug
    llm-classifier.pug
    rag.pug
  api/  (24 files)
    chart.pug
    facebook.pug
    foursquare.pug
    giphy.pug
    github.pug
    google-drive.pug
    google-maps.pug
    google-sheets.pug
    here-maps.pug
    index.pug
    lastfm.pug
    lob.pug
    nyt.pug
    paypal.pug
    pubchem.pug
    quickbooks.pug
    scraping.pug
    steam.pug
    stripe.pug
    tumblr.pug
    twilio.pug
    twitch.pug
    upload.pug
    wikipedia.pug
  partials/  (3 files)
    flash.pug
    footer.pug
    header.pug
  contact.pug
  home.pug
  layout.pug
.env.example
.gitattributes
.gitignore
.prettierignore
.prettierrc
AGENTS.md
CHANGELOG.md
CLAUDE.md
LICENSE
PROD_CHECKLIST.md
README.md
SECURITY.md
app.js
eslint.config.mjs
package.json
```

## Entry points

- [app.js](https://github.com/sahat/hackathon-starter/blob/e735ca8f29d18158b7553244d4e6625ef7eaa383/app.js)
- [public/js/main.js](https://github.com/sahat/hackathon-starter/blob/e735ca8f29d18158b7553244d4e6625ef7eaa383/public/js/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 7 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 3 file(s) under public package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 65 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/dependabot-automerge.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `test` — 65 analysed file(s)
- `views` — 44 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `public` — 8 analysed file(s)
- `controllers` — 7 analysed file(s)
- `config` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `patches` — 3 analysed file(s)
- `models` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e735ca8f29d18158b7553244d4e6625ef7eaa383` is the revision these paths and observations refer to.
