# Project structure: iamkun/dayjs

**Analysed commit:** `d3e43be0489ff1d010aca42b3115b6059215ed60`

**Commit reference:** [d3e43be0489ff1d010aca42b3115b6059215ed60](https://github.com/iamkun/dayjs/commit/d3e43be0489ff1d010aca42b3115b6059215ed60)

**Tree at this commit:** [iamkun/dayjs@d3e43be0489f](https://github.com/iamkun/dayjs/tree/d3e43be0489ff1d010aca42b3115b6059215ed60)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | iamkun/dayjs |
| Description | ⏰ Day.js 2kB immutable date-time library alternative to Moment.js with the same modern API |
| Stars | 48648 |
| Forks | 2984 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | dev |
| Analysed commit | `d3e43be0489ff1d010aca42b3115b6059215ed60` |
| Retrieved at | 2026-11-14T19:10:37.456292+00:00 |
| Files in this snapshot | 375 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (1 files)
    --bug-report.md
  workflows/  (3 files)
    check.yml
    lint-test.yml
    release.yml
  FUNDING.yml
docs/  (37 files)
  demo/  (1 files)
    index.js
  en/  (4 files)
    API-reference.md
    I18n.md
    Installation.md
    Plugin.md
  es-es/  (5 files)
    API-reference.md
    I18n.md
    Installation.md
    Plugin.md
    README-es-es.md
  fr/  (1 files)
    README-fr.md
  he/  (1 files)
    README-he.md
  ja/  (5 files)
    API-reference.md
    I18n.md
    Installation.md
    Plugin.md
    README-ja.md
  ko/  (5 files)
    API-reference.md
    I18n.md
    Installation.md
    Plugin.md
    README-ko.md
  pt-br/  (5 files)
    API-reference.md
    I18n.md
    Installation.md
    Plugin.md
    README-pt-br.md
  ru/  (2 files)
    LICENSE-ru
    README-ru.md
  si/  (1 files)
    README-si.md
  sw/  (1 files)
    README-sw.md
  tr/  (1 files)
    README-tr.md
  zh-cn/  (5 files)
    API-reference.md
    I18n.md
    Installation.md
    Plugin.md
    README.zh-CN.md
patches/  (1 files)
  @semantic-release+github+11.0.4.patch
src/  (184 files)
  locale/  (143 files)
    af.js
    am.js
    ar-dz.js
    ar-iq.js
    ar-kw.js
    ar-ly.js
    ar-ma.js
    ar-sa.js
    ar-tn.js
    ar.js
    az.js
    be.js
    bg.js
    bi.js
    bm.js
    bn-bd.js
    bn.js
    bo.js
    br.js
    bs.js
    ca.js
    cs.js
    cv.js
    cy.js
    … 119 more files
  plugin/  (38 files)
    advancedFormat/  (1 files)
      … 1 files under this directory
    arraySupport/  (1 files)
      … 1 files under this directory
    badMutable/  (1 files)
      … 1 files under this directory
    bigIntSupport/  (1 files)
      … 1 files under this directory
    buddhistEra/  (1 files)
      … 1 files under this directory
    calendar/  (1 files)
      … 1 files under this directory
    customParseFormat/  (1 files)
      … 1 files under this directory
    dayOfYear/  (1 files)
      … 1 files under this directory
    devHelper/  (1 files)
      … 1 files under this directory
    duration/  (1 files)
      … 1 files under this directory
    isBetween/  (1 files)
      … 1 files under this directory
    isLeapYear/  (1 files)
      … 1 files under this directory
    isMoment/  (1 files)
      … 1 files under this directory
    isSameOrAfter/  (1 files)
      … 1 files under this directory
    isSameOrBefore/  (1 files)
      … 1 files under this directory
    isToday/  (1 files)
      … 1 files under this directory
    isTomorrow/  (1 files)
      … 1 files under this directory
    isYesterday/  (1 files)
      … 1 files under this directory
    isoWeek/  (1 files)
      … 1 files under this directory
    isoWeeksInYear/  (1 files)
      … 1 files under this directory
    localeData/  (1 files)
      … 1 files under this directory
    localizedFormat/  (2 files)
      … 2 files under this directory
    minMax/  (1 files)
      … 1 files under this directory
    negativeYear/  (1 files)
      … 1 files under this directory
    objectSupport/  (1 files)
      … 1 files under this directory
    pluralGetSet/  (1 files)
      … 1 files under this directory
    preParsePostFormat/  (1 files)
      … 1 files under this directory
    quarterOfYear/  (1 files)
      … 1 files under this directory
    relativeTime/  (1 files)
      … 1 files under this directory
    timezone/  (1 files)
      … 1 files under this directory
    toArray/  (1 files)
      … 1 files under this directory
    toObject/  (1 files)
      … 1 files under this directory
    updateLocale/  (1 files)
      … 1 files under this directory
    utc/  (1 files)
      … 1 files under this directory
    weekOfYear/  (1 files)
      … 1 files under this directory
    weekYear/  (1 files)
      … 1 files under this directory
    weekday/  (1 files)
      … 1 files under this directory
  constant.js
  index.js
  utils.js
test/  (95 files)
  __mocks__/  (1 files)
    dayjs.js
  issues/  (2 files)
    issue2027.correct-order.test.js
    issue2027.swapped-order.test.js
  locale/  (41 files)
    ar-dz.test.js
    ar-iq.test.js
    ar-kw.test.js
    ar-ly.test.js
    ar-ma.test.js
    ar-sa.test.js
    ar-tn.test.js
    ar.test.js
    be.test.js
    bg.test.js
    bn-bd.test.js
    bn.test.js
    br.test.js
    cs.test.js
    de.test.js
    en.test.js
    et.test.js
    fi.test.js
    he.test.js
    hr.test.js
    hu.test.js
    is.test.js
    it-ch.test.js
    it.test.js
    … 17 more files
  plugin/  (39 files)
    advancedFormat.test.js
    arraySupport.test.js
    badMutable.test.js
    bigIntSupport.test.js
    buddhistEra.test.js
    calendar.test.js
    customParseFormat.test.js
    dayOfYear.test.js
    declarations.test.js
    devHelper.test.js
    duration.test.js
    isBetween.test.js
    isLeapYear.test.js
    isMoment.test.js
    isSameOrAfter.test.js
    isSameOrBefore.test.js
    isToday.test.js
    isTomorrow.test.js
    isYesterday.test.js
    isoWeek.test.js
    isoWeeksInYear.test.js
    localeData.test.js
    localizedFormat.test.js
    minMax.test.js
    … 15 more files
  browser.spec.js
  comparison.test.js
  constructor.test.js
  display.test.js
  get-set.test.js
  locale.test.js
  manipulate.test.js
  parse.test.js
  plugin.test.js
  query.test.js
  timezone.test.js
  utils.test.js
types/  (40 files)
  locale/  (2 files)
    index.d.ts
    types.d.ts
  plugin/  (37 files)
    advancedFormat.d.ts
    arraySupport.d.ts
    badMutable.d.ts
    bigIntSupport.d.ts
    buddhistEra.d.ts
    calendar.d.ts
    customParseFormat.d.ts
    dayOfYear.d.ts
    devHelper.d.ts
    duration.d.ts
    isBetween.d.ts
    isLeapYear.d.ts
    isMoment.d.ts
    isSameOrAfter.d.ts
    isSameOrBefore.d.ts
    isToday.d.ts
    isTomorrow.d.ts
    isYesterday.d.ts
    isoWeek.d.ts
    isoWeeksInYear.d.ts
    localeData.d.ts
    localizedFormat.d.ts
    minMax.d.ts
    negativeYear.d.ts
    … 13 more files
  index.d.ts
.editorconfig
.eslintrc.json
.gitignore
.npmignore
.releaserc
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
babel.config.js
karma.sauce.conf.js
package.json
prettier.config.js
```

## Entry points

- [src/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/index.js)
- [src/plugin/advancedFormat/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/advancedFormat/index.js)
- [src/plugin/arraySupport/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/arraySupport/index.js)
- [src/plugin/badMutable/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/badMutable/index.js)
- [src/plugin/bigIntSupport/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/bigIntSupport/index.js)
- [src/plugin/buddhistEra/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/buddhistEra/index.js)
- [src/plugin/calendar/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/calendar/index.js)
- [src/plugin/customParseFormat/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/customParseFormat/index.js)
- [src/plugin/dayOfYear/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/dayOfYear/index.js)
- [src/plugin/devHelper/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/devHelper/index.js)
- [src/plugin/duration/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/duration/index.js)
- [src/plugin/isBetween/index.js](https://github.com/iamkun/dayjs/blob/d3e43be0489ff1d010aca42b3115b6059215ed60/src/plugin/isBetween/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constant.js package | library | Observed | Groups 1 file(s) under constant.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| locale package | library | Observed | Groups 143 file(s) under locale package (observed from repository paths and static analysis). |
| plugin package | library | Observed | Groups 38 file(s) under plugin package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 95 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 40 file(s) under types package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/check.yml` (ci)
- `.github/workflows/lint-test.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `src` — 184 analysed file(s)
- `test` — 95 analysed file(s)
- `types` — 40 analysed file(s)
- `docs` — 37 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 5 analysed file(s)
- `patches` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d3e43be0489ff1d010aca42b3115b6059215ed60` is the revision these paths and observations refer to.
