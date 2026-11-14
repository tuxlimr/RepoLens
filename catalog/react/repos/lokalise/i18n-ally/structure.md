# Project structure: lokalise/i18n-ally

**Analysed commit:** `4c504c93cec6c4697134eca379f1476d0eb1c9f6`

**Commit reference:** [4c504c93cec6c4697134eca379f1476d0eb1c9f6](https://github.com/lokalise/i18n-ally/commit/4c504c93cec6c4697134eca379f1476d0eb1c9f6)

**Tree at this commit:** [lokalise/i18n-ally@4c504c93cec6](https://github.com/lokalise/i18n-ally/tree/4c504c93cec6c4697134eca379f1476d0eb1c9f6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lokalise/i18n-ally |
| Description | 🌍 All in one i18n extension for VS Code |
| Stars | 4901 |
| Forks | 413 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `4c504c93cec6c4697134eca379f1476d0eb1c9f6` |
| Retrieved at | 2026-11-14T19:14:34.289912+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    feature-request.md
    framework-support-request.md
  workflows/  (2 files)
    release.yml
    test.yml
  renovate.json5
  stale.yml
.vscode/  (5 files)
  extensions.json
  i18n-ally-reviews.yml
  launch.json
  settings.json
  tasks.json
assets/  (2 files)
  editor/  (1 files)
    index.html
  loader.js
examples/  (460 files)
  by-features/  (182 files)
    100-locales/  (36 files)
      … 36 files under this directory
    collections/  (5 files)
      … 5 files under this directory
    custom-locales-path/  (5 files)
      … 5 files under this directory
    custom-scope-range/  (11 files)
      … 11 files under this directory
    demo/  (8 files)
      … 8 files under this directory
    dir-locales/  (12 files)
      … 12 files under this directory
    encoding/  (8 files)
      … 8 files under this directory
    extractions/  (9 files)
      … 9 files under this directory
    flatten-mode/  (5 files)
      … 5 files under this directory
    flatten-scope-conflict/  (4 files)
      … 4 files under this directory
    js-parser/  (8 files)
      … 8 files under this directory
    js-parser-dir/  (10 files)
      … 10 files under this directory
    json5/  (6 files)
      … 6 files under this directory
    linked/  (8 files)
      … 8 files under this directory
    module-style/  (11 files)
      … 11 files under this directory
    path-matcher/  (19 files)
      … 19 files under this directory
    tag-system-bcp47/  (12 files)
      … 12 files under this directory
    yaml/  (5 files)
      … 5 files under this directory
  by-frameworks/  (277 files)
    angular/  (24 files)
      … 24 files under this directory
    chrome-extension/  (4 files)
      … 4 files under this directory
    custom/  (6 files)
      … 6 files under this directory
    ember/  (5 files)
      … 5 files under this directory
    fluent-vue/  (6 files)
      … 6 files under this directory
    fluent-vue-sfc/  (6 files)
      … 6 files under this directory
    flutter/  (7 files)
      … 7 files under this directory
    i18n-js/  (19 files)
      … 19 files under this directory
    i18next-shopify/  (12 files)
      … 12 files under this directory
    jekyll/  (6 files)
      … 6 files under this directory
    laravel/  (6 files)
      … 6 files under this directory
    lingui-nextjs/  (22 files)
      … 22 files under this directory
    next-international/  (11 files)
      … 11 files under this directory
    next-intl/  (19 files)
      … 19 files under this directory
    next-translate/  (23 files)
      … 23 files under this directory
    ngneat-transloco/  (6 files)
      … 6 files under this directory
    ngx-translate/  (9 files)
      … 9 files under this directory
    non-i18n-project/  (5 files)
      … 5 files under this directory
    php-po/  (4 files)
      … 4 files under this directory
    react-i18next/  (12 files)
      … 12 files under this directory
    ruby-on-rails/  (5 files)
      … 5 files under this directory
    svelte/  (16 files)
      … 16 files under this directory
    ui5/  (9 files)
      … 9 files under this directory
    vue-i18n/  (6 files)
      … 6 files under this directory
    vue-i18n-sfc/  (12 files)
      … 12 files under this directory
    vuex-i18n/  (17 files)
      … 17 files under this directory
  README.md
locales/  (17 files)
  de.json
  en.json
  es.json
  fr.json
  hu.json
  ja.json
  ko.json
  nb-NO.json
  nl-NL.json
  pt-BR.json
  ru.json
  sv-SE.json
  th.json
  tr.json
  uk-UA.json
  zh-CN.json
  zh-TW.json
res/  (291 files)
  dark/  (25 files)
    checkmark.svg
    collection.svg
    empty.svg
    help-documentation.svg
    help-heart.svg
    help-report-issue.svg
    help-review-issues.svg
    help-star.svg
    help-tweet.svg
    hidden.svg
    icon-unknown.svg
    loading.svg
    namespace.svg
    plus.svg
    review-comment.svg
    review-conflict.svg
    review-request-change.svg
    review-suggestions.svg
    string-missing.svg
    string.svg
    symbol-string-gray.svg
    symbol-string.svg
    translate-colored.svg
    translate.svg
    … 1 more files
  flags/  (265 files)
    ad.svg
    ae.svg
    af.svg
    ag.svg
    ai.svg
    al.svg
    am.svg
    an.svg
    ao.svg
    aq.svg
    ar.svg
    as.svg
    at.svg
    au.svg
    aw.svg
    ax.svg
    az.svg
    ba.svg
    bb.svg
    bd.svg
    be.svg
    bf.svg
    bg.svg
    bh.svg
    … 241 more files
  light/  (1 files)
    checkmark.svg
.editorconfig
.eslintignore
.eslintrc.js
.gitattributes
.gitignore
.mocharc.yml
.tazerc.json
.vscodeignore
.yarnrc
CHANGELOG.md
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
README.zh-CN.md
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/stale.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.mocharc.yml` (config)
- `.tazerc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/i18n-ally-reviews.yml` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `.vscode/tasks.json` (config)
- `examples/by-features/100-locales/.vscode/settings.json` (config)
- `examples/by-features/100-locales/locales/af.yml` (config)
- `examples/by-features/100-locales/locales/am.yml` (config)
- `examples/by-features/100-locales/locales/aq.yml` (config)
- `examples/by-features/100-locales/locales/be.yml` (config)
- `examples/by-features/100-locales/locales/ca.yml` (config)
- `examples/by-features/100-locales/locales/cy.yml` (config)
- `examples/by-features/100-locales/locales/de.yml` (config)
- `examples/by-features/100-locales/locales/en-ca.yml` (config)
- `examples/by-features/100-locales/locales/en-uk.yml` (config)
- `examples/by-features/100-locales/locales/en-us.yml` (config)
- `examples/by-features/100-locales/locales/es-ar.yml` (config)
- `examples/by-features/100-locales/locales/es.yml` (config)
- `examples/by-features/100-locales/locales/et.yml` (config)
- `examples/by-features/100-locales/locales/fr-fr.yml` (config)
- `examples/by-features/100-locales/locales/gd.yml` (config)
- `examples/by-features/100-locales/locales/he.yml` (config)
- `examples/by-features/100-locales/locales/hr.yml` (config)
- `examples/by-features/100-locales/locales/ja.yml` (config)
- `examples/by-features/100-locales/locales/ko.yml` (config)
- `examples/by-features/100-locales/locales/mk.yml` (config)
- `examples/by-features/100-locales/locales/mn.yml` (config)
- `examples/by-features/100-locales/locales/mt.yml` (config)
- `examples/by-features/100-locales/locales/ne.yml` (config)
- `examples/by-features/100-locales/locales/no-no.yml` (config)
- `examples/by-features/100-locales/locales/pt-br.yml` (config)
- `examples/by-features/100-locales/locales/ru.yml` (config)
- `examples/by-features/100-locales/locales/th.yml` (config)
- `examples/by-features/100-locales/locales/vi.yml` (config)
- `examples/by-features/100-locales/locales/zh-cn.yml` (config)
- `examples/by-features/100-locales/locales/zh-hk.yml` (config)
- `examples/by-features/100-locales/locales/zh-sg.yml` (config)
- `examples/by-features/100-locales/locales/zh-tw.yml` (config)
- `examples/by-features/100-locales/package.json` (manifest)
- `examples/by-features/collections/.vscode/settings.json` (config)
- `examples/by-features/collections/locales/en.json` (config)
- `examples/by-features/collections/locales/ja.json` (config)
- `examples/by-features/collections/package.json` (manifest)
- `examples/by-features/custom-locales-path/lang/en.json` (config)
- `examples/by-features/custom-locales-path/lang/ja.json` (config)
- `examples/by-features/custom-locales-path/lang/zh-cn.json` (config)
- `examples/by-features/custom-locales-path/package.json` (manifest)
- `examples/by-features/custom-scope-range/.vscode/i18n-ally-custom-framework.yml` (config)
- `examples/by-features/custom-scope-range/.vscode/settings.json` (config)
- `examples/by-features/custom-scope-range/package.json` (manifest)
- `examples/by-features/custom-scope-range/public/locales/en/pages/home.json` (config)
- `examples/by-features/custom-scope-range/public/locales/en/translation.json` (config)
- `examples/by-features/demo/.vscode/settings.json` (config)
- `examples/by-features/demo/locales/en.json` (config)
- `examples/by-features/demo/locales/fr.json` (config)
- `examples/by-features/demo/locales/ja.json` (config)
- `examples/by-features/demo/locales/ko.yml` (config)
- `examples/by-features/demo/locales/zh-cn.yml` (config)
- `examples/by-features/demo/package.json` (manifest)
- `examples/by-features/dir-locales/.vscode/settings.json` (config)
- `examples/by-features/dir-locales/locales/en/a.json` (config)
- `examples/by-features/dir-locales/locales/en/b.json` (config)
- `examples/by-features/dir-locales/locales/ja/a.json` (config)
- `examples/by-features/dir-locales/locales/ja/b.json` (config)
- `examples/by-features/dir-locales/locales/zh-cn/a.json` (config)
- `examples/by-features/dir-locales/locales/zh-cn/b.json` (config)
- `examples/by-features/dir-locales/package.json` (manifest)
- `examples/by-features/encoding/locales/en-us.json` (config)
- `examples/by-features/encoding/locales/en.json` (config)
- `examples/by-features/encoding/locales/ja.json` (config)
- `examples/by-features/encoding/locales/ko.yml` (config)
- `examples/by-features/encoding/locales/zh-cn.json` (config)
- `examples/by-features/encoding/locales/zh-tw.json` (config)
- `examples/by-features/encoding/package.json` (manifest)
- `examples/by-features/extractions/.vscode/settings.json` (config)
- `examples/by-features/extractions/locales/en.json` (config)
- `examples/by-features/extractions/package.json` (manifest)
- `examples/by-features/flatten-mode/lang/en.json` (config)
- `examples/by-features/flatten-mode/lang/ja.yml` (config)
- `examples/by-features/flatten-mode/lang/zh-cn.json` (config)
- `examples/by-features/flatten-mode/package.json` (manifest)
- `examples/by-features/flatten-scope-conflict/lang/en.json` (config)
- `examples/by-features/flatten-scope-conflict/lang/ja.yml` (config)
- `examples/by-features/flatten-scope-conflict/package.json` (manifest)
- `examples/by-features/js-parser-dir/.vscode/settings.json` (config)
- `examples/by-features/js-parser-dir/package.json` (manifest)
- `examples/by-features/js-parser-dir/tsconfig.json` (config)
- `examples/by-features/js-parser/.vscode/settings.json` (config)
- `examples/by-features/js-parser/package.json` (manifest)
- `examples/by-features/js-parser/tsconfig.json` (config)
- `examples/by-features/json5/.vscode/settings.json` (config)
- `examples/by-features/json5/package.json` (manifest)
- `examples/by-features/linked/locales/en.json` (config)
- `examples/by-features/linked/locales/fr.json` (config)
- `examples/by-features/linked/locales/ja.json` (config)
- `examples/by-features/linked/locales/ko.yml` (config)
- `examples/by-features/linked/locales/nl-nl.ini` (config)
- `examples/by-features/linked/locales/zh-cn.yml` (config)
- `examples/by-features/linked/package.json` (manifest)
- `examples/by-features/module-style/modules/moduleA/locales/en.json` (config)
- `examples/by-features/module-style/modules/moduleA/locales/fr.json` (config)
- `examples/by-features/module-style/modules/moduleA/locales/zh-cn.json` (config)
- `examples/by-features/module-style/modules/moduleB/locales/en.json` (config)
- `examples/by-features/module-style/modules/moduleB/locales/fr.json` (config)
- `examples/by-features/module-style/modules/moduleB/locales/zh-cn.json` (config)
- `examples/by-features/module-style/modules/moduleC/nested/locales/en.json` (config)
- `examples/by-features/module-style/modules/moduleC/nested/locales/fr.json` (config)
- `examples/by-features/module-style/modules/moduleC/nested/locales/zh-cn.json` (config)
- `examples/by-features/module-style/package.json` (manifest)
- `examples/by-features/path-matcher/locale-namespaces/.vscode/settings.json` (config)
- `examples/by-features/path-matcher/locale-namespaces/i18n/en/foo.yml` (config)
- `examples/by-features/path-matcher/locale-namespaces/i18n/en/foo/bar.yml` (config)
- `examples/by-features/path-matcher/locale-namespaces/i18n/en/general.yml` (config)
- `examples/by-features/path-matcher/locale-namespaces/i18n/fr/foo.yml` (config)
- `examples/by-features/path-matcher/locale-namespaces/i18n/fr/foo/bar.yml` (config)
- `examples/by-features/path-matcher/locale-namespaces/i18n/fr/general.yml` (config)
- `examples/by-features/path-matcher/locale-namespaces/package.json` (manifest)
- `examples/by-features/path-matcher/namespaces-locale/.vscode/settings.json` (config)
- `examples/by-features/path-matcher/namespaces-locale/i18n/en.yml` (config)
- `examples/by-features/path-matcher/namespaces-locale/i18n/foo/bar/en.yml` (config)
- `examples/by-features/path-matcher/namespaces-locale/i18n/foo/bar/fr.yml` (config)
- `examples/by-features/path-matcher/namespaces-locale/i18n/foo/en.yml` (config)
- `examples/by-features/path-matcher/namespaces-locale/i18n/foo/fr.yml` (config)
- `examples/by-features/path-matcher/namespaces-locale/i18n/general/en.yml` (config)
- `examples/by-features/path-matcher/namespaces-locale/i18n/general/fr.yml` (config)
- `examples/by-features/path-matcher/namespaces-locale/package.json` (manifest)
- `examples/by-features/tag-system-bcp47/.vscode/settings.json` (config)
- `examples/by-features/tag-system-bcp47/locales/de-DE-bavarian.yml` (config)
- `examples/by-features/tag-system-bcp47/locales/de-de.yml` (config)
- `examples/by-features/tag-system-bcp47/locales/de.yml` (config)
- `examples/by-features/tag-system-bcp47/locales/en.yml` (config)
- `examples/by-features/tag-system-bcp47/locales/zh-cn.yml` (config)
- `examples/by-features/tag-system-bcp47/locales/zh-hk.yml` (config)
- `examples/by-features/tag-system-bcp47/locales/zh-sg.yml` (config)
- `examples/by-features/tag-system-bcp47/locales/zh-tw.yml` (config)
- `examples/by-features/tag-system-bcp47/package.json` (manifest)
- `examples/by-features/yaml/locales/en.yml` (config)
- `examples/by-features/yaml/locales/ja.yaml` (config)
- `examples/by-features/yaml/locales/zh-cn.yml` (config)
- `examples/by-features/yaml/package.json` (manifest)
- `examples/by-frameworks/angular/angular.json` (config)
- `examples/by-frameworks/angular/package.json` (manifest)
- `examples/by-frameworks/angular/src/tsconfig.app.json` (config)
- `examples/by-frameworks/angular/src/tsconfig.spec.json` (config)
- `examples/by-frameworks/angular/src/tslint.json` (config)
- `examples/by-frameworks/angular/tsconfig.json` (config)
- `examples/by-frameworks/angular/tslint.json` (config)
- `examples/by-frameworks/chrome-extension/_locales/en/messages.json` (config)
- `examples/by-frameworks/chrome-extension/_locales/ja/messages.json` (config)
- `examples/by-frameworks/chrome-extension/manifest.json` (config)
- `examples/by-frameworks/custom/.vscode/i18n-ally-custom-framework.yml` (config)
- `examples/by-frameworks/custom/.vscode/settings.json` (config)
- `examples/by-frameworks/custom/locales/en.json` (config)
- `examples/by-frameworks/custom/package.json` (manifest)
- `examples/by-frameworks/ember/.vscode/settings.json` (config)
- `examples/by-frameworks/ember/locales/en.json` (config)
- `examples/by-frameworks/ember/locales/zh-cn.json` (config)
- `examples/by-frameworks/ember/package.json` (manifest)
- `examples/by-frameworks/fluent-vue-sfc/.vscode/settings.json` (config)
- `examples/by-frameworks/fluent-vue-sfc/package.json` (manifest)
- `examples/by-frameworks/fluent-vue/.vscode/settings.json` (config)
- `examples/by-frameworks/fluent-vue/package.json` (manifest)
- `examples/by-frameworks/flutter/.vscode/settings.json` (config)
- `examples/by-frameworks/flutter/assets/i18n/en.yaml` (config)
- `examples/by-frameworks/flutter/assets/i18n/es.json` (config)
- `examples/by-frameworks/flutter/assets/i18n/it.json` (config)
- `examples/by-frameworks/flutter/pubspec.yaml` (config)
- `examples/by-frameworks/i18n-js/.vscode/i18n-ally-custom-framework.yml` (config)
- `examples/by-frameworks/i18n-js/.vscode/settings.json` (config)
- `examples/by-frameworks/i18n-js/package.json` (manifest)
- `examples/by-frameworks/i18n-js/public/manifest.json` (config)
- `examples/by-frameworks/i18n-js/src/locales/en.json` (config)
- `examples/by-frameworks/i18n-js/src/locales/sk.json` (config)
- `examples/by-frameworks/i18next-shopify/.vscode/settings.json` (config)
- `examples/by-frameworks/i18next-shopify/package.json` (manifest)
- `examples/by-frameworks/i18next-shopify/public/locales/de/pages/home.json` (config)
- `examples/by-frameworks/i18next-shopify/public/locales/de/translation.json` (config)
- `examples/by-frameworks/i18next-shopify/public/locales/en/pages/home.json` (config)
- `examples/by-frameworks/i18next-shopify/public/locales/en/translation.json` (config)
- `examples/by-frameworks/jekyll/.vscode/settings.json` (config)
- `examples/by-frameworks/jekyll/_i18n/en.yml` (config)
- `examples/by-frameworks/jekyll/_i18n/fr.yml` (config)
- `examples/by-frameworks/laravel/.vscode/settings.json` (config)
- `examples/by-frameworks/laravel/composer.json` (config)
- `examples/by-frameworks/lingui-nextjs/.vscode/settings.json` (config)
- `examples/by-frameworks/lingui-nextjs/package.json` (manifest)
- `examples/by-frameworks/lingui-nextjs/tsconfig.json` (config)
- `examples/by-frameworks/next-international/.vscode/settings.json` (config)
- `examples/by-frameworks/next-international/package.json` (manifest)
- `examples/by-frameworks/next-international/tsconfig.json` (config)
- `examples/by-frameworks/next-intl/.vscode/settings.json` (config)
- `examples/by-frameworks/next-intl/messages/de.json` (config)
- `examples/by-frameworks/next-intl/messages/en.json` (config)
- `examples/by-frameworks/next-intl/package.json` (manifest)
- `examples/by-frameworks/next-intl/tsconfig.json` (config)
- `examples/by-frameworks/next-translate/.vscode/settings.json` (config)
- `examples/by-frameworks/next-translate/i18n.json` (config)
- `examples/by-frameworks/next-translate/locales/ca/common.json` (config)
- `examples/by-frameworks/next-translate/locales/ca/dynamic.json` (config)
- `examples/by-frameworks/next-translate/locales/ca/home.json` (config)
- `examples/by-frameworks/next-translate/locales/ca/more-examples.json` (config)
- `examples/by-frameworks/next-translate/locales/en/common.json` (config)
- `examples/by-frameworks/next-translate/locales/en/dynamic.json` (config)
- `examples/by-frameworks/next-translate/locales/en/home.json` (config)
- `examples/by-frameworks/next-translate/locales/en/more-examples.json` (config)
- `examples/by-frameworks/next-translate/locales/es/common.json` (config)
- `examples/by-frameworks/next-translate/locales/es/dynamic.json` (config)
- `examples/by-frameworks/next-translate/locales/es/home.json` (config)
- `examples/by-frameworks/next-translate/locales/es/more-examples.json` (config)
- `examples/by-frameworks/next-translate/package.json` (manifest)
- `examples/by-frameworks/ngneat-transloco/.vscode/settings.json` (config)
- `examples/by-frameworks/ngneat-transloco/i18n/en.json` (config)
- `examples/by-frameworks/ngneat-transloco/i18n/es.json` (config)
- `examples/by-frameworks/ngneat-transloco/package.json` (manifest)
- `examples/by-frameworks/ngx-translate/.vscode/settings.json` (config)
- `examples/by-frameworks/ngx-translate/package.json` (manifest)
- `examples/by-frameworks/ngx-translate/src/i18n/en.json` (config)
- `examples/by-frameworks/ngx-translate/src/i18n/fr.json` (config)
- `examples/by-frameworks/ngx-translate/tsconfig.json` (config)
- `examples/by-frameworks/non-i18n-project/locales/en.json` (config)
- `examples/by-frameworks/non-i18n-project/locales/ja.json` (config)
- `examples/by-frameworks/non-i18n-project/locales/zh-cn.json` (config)
- `examples/by-frameworks/non-i18n-project/package.json` (manifest)
- `examples/by-frameworks/php-po/.vscode/settings.json` (config)
- `examples/by-frameworks/react-i18next/.vscode/settings.json` (config)
- `examples/by-frameworks/react-i18next/package.json` (manifest)
- `examples/by-frameworks/react-i18next/public/locales/de/pages/home.json` (config)
- `examples/by-frameworks/react-i18next/public/locales/de/translation.json` (config)
- `examples/by-frameworks/react-i18next/public/locales/en/pages/home.json` (config)
- `examples/by-frameworks/react-i18next/public/locales/en/translation.json` (config)
- `examples/by-frameworks/ruby-on-rails/.vscode/settings.json` (config)
- `examples/by-frameworks/ruby-on-rails/config/locales/en.yml` (config)
- `examples/by-frameworks/ruby-on-rails/config/locales/ru.yml` (config)
- `examples/by-frameworks/svelte/.vscode/settings.json` (config)
- `examples/by-frameworks/svelte/messages/ar.json` (config)
- `examples/by-frameworks/svelte/messages/en.json` (config)
- `examples/by-frameworks/svelte/messages/es-ES.json` (config)
- `examples/by-frameworks/svelte/messages/pt-BR.json` (config)
- `examples/by-frameworks/svelte/package.json` (manifest)
- `examples/by-frameworks/svelte/src/routes/about/_locales/ar.json` (config)
- `examples/by-frameworks/svelte/src/routes/about/_locales/default.json` (config)
- `examples/by-frameworks/svelte/src/routes/about/_locales/en.json` (config)
- `examples/by-frameworks/svelte/src/routes/about/_locales/es-ES.json` (config)
- `examples/by-frameworks/svelte/src/routes/about/_locales/pt-BR.json` (config)
- `examples/by-frameworks/ui5/.vscode/settings.json` (config)
- `examples/by-frameworks/ui5/package.json` (manifest)
- `examples/by-frameworks/ui5/webapp/manifest.json` (config)
- `examples/by-frameworks/vue-i18n-sfc/.vscode/settings.json` (config)
- `examples/by-frameworks/vue-i18n-sfc/locales/en.json` (config)
- `examples/by-frameworks/vue-i18n-sfc/locales/ja.json` (config)
- `examples/by-frameworks/vue-i18n-sfc/package.json` (manifest)
- `examples/by-frameworks/vue-i18n/.vscode/settings.json` (config)
- `examples/by-frameworks/vue-i18n/locales/en.json` (config)
- `examples/by-frameworks/vue-i18n/locales/ja.json` (config)
- `examples/by-frameworks/vue-i18n/locales/zh-cn.json` (config)
- `examples/by-frameworks/vue-i18n/package.json` (manifest)
- `examples/by-frameworks/vuex-i18n/todo-demo/app/i18n/de.json` (config)
- `examples/by-frameworks/vuex-i18n/todo-demo/app/i18n/en.json` (config)
- `examples/by-frameworks/vuex-i18n/todo-demo/package.json` (manifest)
- `locales/de.json` (config)
- `locales/en.json` (config)
- `locales/es.json` (config)
- `locales/fr.json` (config)
- `locales/hu.json` (config)
- `locales/ja.json` (config)
- `locales/ko.json` (config)
- `locales/nb-NO.json` (config)
- `locales/nl-NL.json` (config)
- `locales/pt-BR.json` (config)
- `locales/ru.json` (config)
- `locales/sv-SE.json` (config)
- `locales/th.json` (config)
- `locales/tr.json` (config)
- `locales/uk-UA.json` (config)
- `locales/zh-CN.json` (config)
- `locales/zh-TW.json` (config)
- `package.json` (manifest)

## Top-level layout

- `examples` — 460 analysed file(s)
- `res` — 291 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `locales` — 17 analysed file(s)
- `.github` — 7 analysed file(s)
- `.vscode` — 5 analysed file(s)
- `assets` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4c504c93cec6c4697134eca379f1476d0eb1c9f6` is the revision these paths and observations refer to.
