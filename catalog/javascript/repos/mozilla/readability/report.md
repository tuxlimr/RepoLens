# Architecture report: mozilla/readability

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | mozilla/readability |
| Description | A standalone version of the readability lib |
| Language | JavaScript |
| Stars | 11544 |
| Licence | Apache-2.0 |
| Analysed commit / branch | ab4027a8b37669745016869a37a504727992b2ba / main |
| Framework(s) | None detected |
| Files analysed | 372 |
| Components | 3 |

## 2. Architecture in one minute

mozilla/readability - A standalone version of the readability lib. This repository was analysed statically from 372 file(s) (0 Python). Detected technologies (observed from imports/manifests): no known frameworks/libraries. Files are grouped into 3 component(s): Configuration and deployment, Core modules, Tests. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    subgraph config_group
        config["Configuration and deployment"]
    end
    subgraph core_group
        core["Core modules"]
    end
    subgraph test_group
        tests["Tests"]
    end
```

## 4. Main components

### Configuration and deployment (`config`)

- **Kind:** config
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis).
- **Paths:** `package.json`
- **Evidence:** [package.json](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/package.json)

### Core modules (`core`)

- **Kind:** core
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 6 file(s) under core modules (observed from repository paths and static analysis).
- **Paths:** `JSDOMParser.js`, `Readability-readerable.js`, `Readability.js`, `eslint.config.mjs`, `index.d.ts`, `index.js`
- **Evidence:** [JSDOMParser.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/JSDOMParser.js); [Readability-readerable.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/Readability-readerable.js); [Readability.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/Readability.js); [eslint.config.mjs](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/eslint.config.mjs); [index.d.ts](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/index.d.ts); [index.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/index.js)

### Tests (`tests`)

- **Kind:** test
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 352 file(s) under tests (observed from repository paths and static analysis).
- **Paths:** `test/debug-testcase.js`, `test/generate-testcase.js`, `test/test-isProbablyReaderable.js`, `test/test-jsdomparser.js`, `test/test-pages/001/expected-metadata.json`, `test/test-pages/001/expected.html`, `test/test-pages/001/source.html`, `test/test-pages/002/expected-metadata.json`, `test/test-pages/002/expected.html`, `test/test-pages/002/source.html`, `test/test-pages/003-metadata-preferred/expected-metadata.json`, `test/test-pages/003-metadata-preferred/expected.html`, `test/test-pages/003-metadata-preferred/source.html`, `test/test-pages/004-metadata-space-separated-properties/expected-metadata.json`, `test/test-pages/004-metadata-space-separated-properties/expected.html`, `test/test-pages/004-metadata-space-separated-properties/source.html`, `test/test-pages/005-unescape-html-entities/expected-metadata.json`, `test/test-pages/005-unescape-html-entities/expected.html`, `test/test-pages/005-unescape-html-entities/source.html`, `test/test-pages/aclu/expected-metadata.json`, `test/test-pages/aclu/expected.html`, `test/test-pages/aktualne/expected-metadata.json`, `test/test-pages/aktualne/expected.html`, `test/test-pages/archive-of-our-own/expected-metadata.json`, `test/test-pages/archive-of-our-own/expected.html`, `test/test-pages/ars-1/expected-metadata.json`, `test/test-pages/ars-1/expected.html`, `test/test-pages/ars-1/source.html`, `test/test-pages/article-author-tag/expected-metadata.json`, `test/test-pages/article-author-tag/expected.html`, `test/test-pages/base-url-base-element-relative/expected-metadata.json`, `test/test-pages/base-url-base-element-relative/expected.html`, `test/test-pages/base-url-base-element-relative/source.html`, `test/test-pages/base-url-base-element/expected-metadata.json`, `test/test-pages/base-url-base-element/expected.html`, `test/test-pages/base-url-base-element/source.html`, `test/test-pages/base-url/expected-metadata.json`, `test/test-pages/base-url/expected.html`, `test/test-pages/base-url/source.html`, `test/test-pages/basic-tags-cleaning/expected-metadata.json`, `test/test-pages/basic-tags-cleaning/expected.html`, `test/test-pages/basic-tags-cleaning/source.html`, `test/test-pages/bbc-1/expected-metadata.json`, `test/test-pages/bbc-1/expected.html`, `test/test-pages/blogger/expected-metadata.json`, `test/test-pages/blogger/expected.html`, `test/test-pages/blogger/source.html`, `test/test-pages/breitbart/expected-metadata.json`, `test/test-pages/breitbart/expected.html`, `test/test-pages/bug-1255978/expected-metadata.json`, `test/test-pages/bug-1255978/expected.html`, `test/test-pages/buzzfeed-1/expected-metadata.json`, `test/test-pages/buzzfeed-1/expected.html`, `test/test-pages/citylab-1/expected-metadata.json`, `test/test-pages/citylab-1/expected.html`, `test/test-pages/citylab-1/source.html`, `test/test-pages/clean-links/expected-metadata.json`, `test/test-pages/clean-links/expected.html`, `test/test-pages/clean-links/source.html`, `test/test-pages/cnet-svg-classes/expected-metadata.json`, `test/test-pages/cnet-svg-classes/expected.html`, `test/test-pages/cnet-svg-classes/source.html`, `test/test-pages/cnet/expected-metadata.json`, `test/test-pages/cnet/expected.html`, `test/test-pages/cnn/expected-metadata.json`, `test/test-pages/cnn/expected.html`, `test/test-pages/comment-inside-script-parsing/expected-metadata.json`, `test/test-pages/comment-inside-script-parsing/expected.html`, `test/test-pages/comment-inside-script-parsing/source.html`, `test/test-pages/daringfireball-1/expected-metadata.json`, `test/test-pages/daringfireball-1/expected.html`, `test/test-pages/daringfireball-1/source.html`, `test/test-pages/data-url-image/expected-metadata.json`, `test/test-pages/data-url-image/expected.html`, `test/test-pages/data-url-image/source.html`, `test/test-pages/dev418/expected-metadata.json`, `test/test-pages/dev418/expected.html`, `test/test-pages/dev418/source.html`, `test/test-pages/dropbox-blog/expected-metadata.json`, `test/test-pages/dropbox-blog/expected.html`, `test/test-pages/dropbox-blog/source.html`, `test/test-pages/ebb-org/expected-metadata.json`, `test/test-pages/ebb-org/expected.html`, `test/test-pages/ebb-org/source.html`, `test/test-pages/ehow-1/expected-metadata.json`, `test/test-pages/ehow-1/expected.html`, `test/test-pages/ehow-1/source.html`, `test/test-pages/ehow-2/expected-metadata.json`, `test/test-pages/ehow-2/expected.html`, `test/test-pages/ehow-2/source.html`, `test/test-pages/embedded-videos/expected-metadata.json`, `test/test-pages/embedded-videos/expected.html`, `test/test-pages/embedded-videos/source.html`, `test/test-pages/engadget/expected-metadata.json`, `test/test-pages/engadget/expected.html`, `test/test-pages/firefox-nightly-blog/expected-metadata.json`, `test/test-pages/firefox-nightly-blog/expected.html`, `test/test-pages/firefox-nightly-blog/source.html`, `test/test-pages/folha/expected-metadata.json`, `test/test-pages/folha/expected.html`, `test/test-pages/gitlab-blog/expected-metadata.json`, `test/test-pages/gitlab-blog/expected.html`, `test/test-pages/gitlab-blog/source.html`, `test/test-pages/gmw/expected-metadata.json`, `test/test-pages/gmw/expected.html`, `test/test-pages/gmw/source.html`, `test/test-pages/google-sre-book-1/expected-metadata.json`, `test/test-pages/google-sre-book-1/expected.html`, `test/test-pages/google-sre-book-1/source.html`, `test/test-pages/guardian-1/expected-metadata.json`, `test/test-pages/guardian-1/expected.html`, `test/test-pages/heise/expected-metadata.json`, `test/test-pages/heise/expected.html`, `test/test-pages/heise/source.html`, `test/test-pages/herald-sun-1/expected-metadata.json`, `test/test-pages/herald-sun-1/expected.html`, `test/test-pages/herald-sun-1/source.html`, `test/test-pages/hidden-nodes/expected-metadata.json`, `test/test-pages/hidden-nodes/expected.html`, `test/test-pages/hidden-nodes/source.html`, `test/test-pages/hukumusume/expected-metadata.json`, `test/test-pages/hukumusume/expected.html`, `test/test-pages/hukumusume/source.html`, `test/test-pages/iab-1/expected-metadata.json`, `test/test-pages/iab-1/expected.html`, `test/test-pages/iab-1/source.html`, `test/test-pages/ietf-1/expected-metadata.json`, `test/test-pages/ietf-1/expected.html`, `test/test-pages/ietf-1/source.html`, `test/test-pages/invalid-attributes/expected-metadata.json`, `test/test-pages/invalid-attributes/expected.html`, `test/test-pages/invalid-attributes/source.html`, `test/test-pages/js-link-replacement/expected-metadata.json`, `test/test-pages/js-link-replacement/expected.html`, `test/test-pages/js-link-replacement/source.html`, `test/test-pages/keep-images/expected-metadata.json`, `test/test-pages/keep-images/expected.html`, `test/test-pages/keep-images/source.html`, `test/test-pages/keep-tabular-data/expected-metadata.json`, `test/test-pages/keep-tabular-data/expected.html`, `test/test-pages/keep-tabular-data/source.html`, `test/test-pages/la-nacion/expected-metadata.json`, `test/test-pages/la-nacion/expected.html`, `test/test-pages/la-nacion/source.html`, `test/test-pages/lazy-image-1/expected-metadata.json`, `test/test-pages/lazy-image-1/expected.html`, `test/test-pages/lazy-image-2/expected-metadata.json`, `test/test-pages/lazy-image-2/expected.html`, `test/test-pages/lazy-image-3/expected-metadata.json`, `test/test-pages/lazy-image-3/expected.html`, `test/test-pages/lazy-image-3/source.html`, `test/test-pages/lemonde-1/expected-metadata.json`, `test/test-pages/lemonde-1/expected.html`, `test/test-pages/lemonde-1/source.html`, `test/test-pages/liberation-1/expected-metadata.json`, `test/test-pages/liberation-1/expected.html`, `test/test-pages/liberation-1/source.html`, `test/test-pages/lifehacker-post-comment-load/expected-metadata.json`, `test/test-pages/lifehacker-post-comment-load/expected.html`, `test/test-pages/lifehacker-working/expected-metadata.json`, `test/test-pages/lifehacker-working/expected.html`, `test/test-pages/lifehacker-working/source.html`, `test/test-pages/links-in-tables/expected-metadata.json`, `test/test-pages/links-in-tables/expected.html`, `test/test-pages/links-in-tables/source.html`, `test/test-pages/lwn-1/expected-metadata.json`, `test/test-pages/lwn-1/expected.html`, `test/test-pages/lwn-1/source.html`, `test/test-pages/mathjax/expected-metadata.json`, `test/test-pages/mathjax/expected.html`, `test/test-pages/medicalnewstoday/expected-metadata.json`, `test/test-pages/medicalnewstoday/expected.html`, `test/test-pages/medicalnewstoday/source.html`, `test/test-pages/medium-1/expected-metadata.json`, `test/test-pages/medium-1/expected.html`, `test/test-pages/medium-1/source.html`, `test/test-pages/medium-2/expected-metadata.json`, `test/test-pages/medium-2/expected.html`, `test/test-pages/medium-2/source.html`, `test/test-pages/medium-3/expected-metadata.json`, `test/test-pages/medium-3/expected.html`, `test/test-pages/mercurial/expected-metadata.json`, `test/test-pages/mercurial/expected.html`, `test/test-pages/mercurial/source.html`, `test/test-pages/metadata-content-missing/expected-metadata.json`, `test/test-pages/metadata-content-missing/expected.html`, `test/test-pages/metadata-content-missing/source.html`, `test/test-pages/missing-paragraphs/expected-metadata.json`, `test/test-pages/missing-paragraphs/expected.html`, `test/test-pages/missing-paragraphs/source.html`, `test/test-pages/mozilla-1/expected-metadata.json`, `test/test-pages/mozilla-1/expected.html`, `test/test-pages/mozilla-1/source.html`, `test/test-pages/mozilla-2/expected-metadata.json`, `test/test-pages/mozilla-2/expected.html`, `test/test-pages/mozilla-2/source.html`, `test/test-pages/msn/expected-metadata.json`, `test/test-pages/msn/expected.html`, `test/test-pages/normalize-spaces/expected-metadata.json`, `test/test-pages/normalize-spaces/expected.html`, `test/test-pages/normalize-spaces/source.html`, `test/test-pages/nytimes-1/expected-metadata.json`, `test/test-pages/nytimes-1/expected.html`, `test/test-pages/nytimes-2/expected-metadata.json`, `test/test-pages/nytimes-2/expected.html`, `test/test-pages/nytimes-3/expected-metadata.json`, `test/test-pages/nytimes-3/expected.html`, `test/test-pages/nytimes-4/expected-metadata.json`, `test/test-pages/nytimes-4/expected.html`, `test/test-pages/nytimes-5/expected-metadata.json`, `test/test-pages/nytimes-5/expected.html`, `test/test-pages/ol/expected-metadata.json`, `test/test-pages/ol/expected.html`, `test/test-pages/ol/source.html`, `test/test-pages/parsely-metadata/expected-metadata.json`, `test/test-pages/parsely-metadata/expected.html`, `test/test-pages/parsely-metadata/source.html`, `test/test-pages/pixnet/expected-metadata.json`, `test/test-pages/pixnet/expected.html`, `test/test-pages/qq/expected-metadata.json`, `test/test-pages/qq/expected.html`, `test/test-pages/quanta-1/expected-metadata.json`, `test/test-pages/quanta-1/expected.html`, `test/test-pages/remove-aria-hidden/expected-metadata.json`, `test/test-pages/remove-aria-hidden/expected.html`, `test/test-pages/remove-aria-hidden/source.html`, `test/test-pages/remove-extra-brs/expected-metadata.json`, `test/test-pages/remove-extra-brs/expected.html`, `test/test-pages/remove-extra-brs/source.html`, `test/test-pages/remove-extra-paragraphs/expected-metadata.json`, `test/test-pages/remove-extra-paragraphs/expected.html`, `test/test-pages/remove-extra-paragraphs/source.html`, `test/test-pages/remove-script-tags/expected-metadata.json`, `test/test-pages/remove-script-tags/expected.html`, `test/test-pages/remove-script-tags/source.html`, `test/test-pages/reordering-paragraphs/expected-metadata.json`, `test/test-pages/reordering-paragraphs/expected.html`, `test/test-pages/reordering-paragraphs/source.html`, `test/test-pages/replace-brs/expected-metadata.json`, `test/test-pages/replace-brs/expected.html`, `test/test-pages/replace-brs/source.html`, `test/test-pages/replace-font-tags/expected-metadata.json`, `test/test-pages/replace-font-tags/expected.html`, `test/test-pages/replace-font-tags/source.html`, `test/test-pages/royal-road/expected-metadata.json`, `test/test-pages/royal-road/expected.html`, `test/test-pages/rtl-1/expected-metadata.json`, `test/test-pages/rtl-1/expected.html`, `test/test-pages/rtl-1/source.html`, `test/test-pages/rtl-2/expected-metadata.json`, `test/test-pages/rtl-2/expected.html`, `test/test-pages/rtl-2/source.html`, `test/test-pages/rtl-3/expected-metadata.json`, `test/test-pages/rtl-3/expected.html`, `test/test-pages/rtl-3/source.html`, `test/test-pages/rtl-4/expected-metadata.json`, `test/test-pages/rtl-4/expected.html`, `test/test-pages/rtl-4/source.html`, `test/test-pages/salon-1/expected-metadata.json`, `test/test-pages/salon-1/expected.html`, `test/test-pages/schema-org-context-object/expected-metadata.json`, `test/test-pages/schema-org-context-object/expected.html`, `test/test-pages/seattletimes-1/expected-metadata.json`, `test/test-pages/seattletimes-1/expected.html`, `test/test-pages/simplyfound-1/expected-metadata.json`, `test/test-pages/simplyfound-1/expected.html`, `test/test-pages/simplyfound-1/source.html`, `test/test-pages/social-buttons/expected-metadata.json`, `test/test-pages/social-buttons/expected.html`, `test/test-pages/social-buttons/source.html`, `test/test-pages/spiceworks/expected-metadata.json`, `test/test-pages/spiceworks/expected.html`, `test/test-pages/spiceworks/source.html`, `test/test-pages/style-tags-removal/expected-metadata.json`, `test/test-pages/style-tags-removal/expected.html`, `test/test-pages/style-tags-removal/source.html`, `test/test-pages/svg-parsing/expected-metadata.json`, `test/test-pages/svg-parsing/expected.html`, `test/test-pages/svg-parsing/source.html`, `test/test-pages/table-style-attributes/expected-metadata.json`, `test/test-pages/table-style-attributes/expected.html`, `test/test-pages/table-style-attributes/source.html`, `test/test-pages/telegraph/expected-metadata.json`, `test/test-pages/telegraph/expected.html`, `test/test-pages/theverge/expected-metadata.json`, `test/test-pages/theverge/expected.html`, `test/test-pages/title-and-h1-discrepancy/expected-metadata.json`, `test/test-pages/title-and-h1-discrepancy/expected.html`, `test/test-pages/title-and-h1-discrepancy/source.html`, `test/test-pages/title-en-dash/expected-metadata.json`, `test/test-pages/title-en-dash/expected.html`, `test/test-pages/title-en-dash/source.html`, `test/test-pages/tmz-1/expected-metadata.json`, `test/test-pages/tmz-1/expected.html`, `test/test-pages/tmz-1/source.html`, `test/test-pages/toc-missing/expected-metadata.json`, `test/test-pages/toc-missing/expected.html`, `test/test-pages/toc-missing/source.html`, `test/test-pages/topicseed-1/expected-metadata.json`, `test/test-pages/topicseed-1/expected.html`, `test/test-pages/topicseed-1/source.html`, `test/test-pages/tumblr/expected-metadata.json`, `test/test-pages/tumblr/expected.html`, `test/test-pages/tumblr/source.html`, `test/test-pages/v8-blog/expected-metadata.json`, `test/test-pages/v8-blog/expected.html`, `test/test-pages/v8-blog/source.html`, `test/test-pages/videos-1/expected-metadata.json`, `test/test-pages/videos-1/expected.html`, `test/test-pages/videos-2/expected-metadata.json`, `test/test-pages/videos-2/expected.html`, `test/test-pages/videos-2/source.html`, `test/test-pages/visibility-hidden/expected-metadata.json`, `test/test-pages/visibility-hidden/expected.html`, `test/test-pages/visibility-hidden/source.html`, `test/test-pages/wapo-1/expected-metadata.json`, `test/test-pages/wapo-1/expected.html`, `test/test-pages/wapo-1/source.html`, `test/test-pages/wapo-2/expected-metadata.json`, `test/test-pages/wapo-2/expected.html`, `test/test-pages/wapo-2/source.html`, `test/test-pages/webmd-1/expected-metadata.json`, `test/test-pages/webmd-1/expected.html`, `test/test-pages/webmd-1/source.html`, `test/test-pages/webmd-2/expected-metadata.json`, `test/test-pages/webmd-2/expected.html`, `test/test-pages/webmd-2/source.html`, `test/test-pages/wikia/expected-metadata.json`, `test/test-pages/wikia/expected.html`, `test/test-pages/wikipedia-2/expected-metadata.json`, `test/test-pages/wikipedia-3/expected-metadata.json`, `test/test-pages/wikipedia-3/expected.html`, `test/test-pages/wikipedia-4/expected-metadata.json`, `test/test-pages/wikipedia-4/expected.html`, `test/test-pages/wikipedia/expected-metadata.json`, `test/test-pages/wikipedia/expected.html`, `test/test-pages/wordpress/expected-metadata.json`, `test/test-pages/wordpress/expected.html`, `test/test-pages/wordpress/source.html`, `test/test-pages/yahoo-1/expected-metadata.json`, `test/test-pages/yahoo-1/expected.html`, `test/test-pages/yahoo-2/expected-metadata.json`, `test/test-pages/yahoo-2/expected.html`, `test/test-pages/yahoo-3/expected-metadata.json`, `test/test-pages/yahoo-3/expected.html`, `test/test-pages/yahoo-4/expected-metadata.json`, `test/test-pages/yahoo-4/expected.html`, `test/test-pages/yahoo-4/source.html`, `test/test-pages/youth/expected-metadata.json`, `test/test-pages/youth/expected.html`, `test/test-readability.js`, `test/utils.js`
- **Evidence:** [test/debug-testcase.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/debug-testcase.js); [test/generate-testcase.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/generate-testcase.js); [test/test-isProbablyReaderable.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-isProbablyReaderable.js); [test/test-jsdomparser.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-jsdomparser.js); [test/test-pages/001/expected-metadata.json](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-pages/001/expected-metadata.json); [test/test-pages/001/expected.html](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-pages/001/expected.html); [test/test-pages/001/source.html](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-pages/001/source.html); [test/test-pages/002/expected-metadata.json](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-pages/002/expected-metadata.json)

## 5. Execution flow

**Observed** entry point(s):

- [index.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/index.js)

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. No internal import relationships between components were observed.

## 6. Project structure

### `(root)`

- `.gitattributes` - other (55 bytes)
- `.gitignore` - other (80 bytes)
- `.npmignore` - other (69 bytes)
- `.prettierrc.js` - source, JavaScript (351 bytes)
- `.release-it.json` - config (275 bytes)
- `.taskcluster.yml` - config (1203 bytes)
- `CHANGELOG.md` - docs (5667 bytes)
- `CODE_OF_CONDUCT.md` - docs (691 bytes)
- `CONTRIBUTING.md` - docs (3413 bytes)
- `JSDOMParser.js` - source, JavaScript (37436 bytes)
- `LICENSE.md` - docs (11358 bytes)
- `NOTICE` - docs (90 bytes)
- `README.md` - docs (7376 bytes)
- `Readability-readerable.js` - source, JavaScript (4279 bytes)
- `Readability.js` - source, JavaScript (90944 bytes)
- `SECURITY.md` - docs (1134 bytes)
- `eslint.config.mjs` - source, JavaScript (1109 bytes)
- `index.d.ts` - source, TypeScript (4114 bytes)
- `index.js` - source, JavaScript (192 bytes)
- `package.json` - manifest (1159 bytes)

### `test`

- `test/debug-testcase.js` - test, JavaScript (561 bytes)
- `test/generate-testcase.js` - test, JavaScript (6106 bytes)
- `test/test-isProbablyReaderable.js` - test, JavaScript (5266 bytes)
- `test/test-jsdomparser.js` - test, JavaScript (21919 bytes)
- `test/test-pages/001/expected-metadata.json` - test (243 bytes)
- `test/test-pages/001/expected.html` - test (5912 bytes)
- `test/test-pages/001/source.html` - test (12533 bytes)
- `test/test-pages/002/expected-metadata.json` - test (377 bytes)
- `test/test-pages/002/expected.html` - test (30165 bytes)
- `test/test-pages/002/source.html` - test (142208 bytes)
- `test/test-pages/003-metadata-preferred/expected-metadata.json` - test (218 bytes)
- `test/test-pages/003-metadata-preferred/expected.html` - test (1043 bytes)
- `test/test-pages/003-metadata-preferred/source.html` - test (2408 bytes)
- `test/test-pages/004-metadata-space-separated-properties/expected-metadata.json` - test (181 bytes)
- `test/test-pages/004-metadata-space-separated-properties/expected.html` - test (1043 bytes)
- `test/test-pages/004-metadata-space-separated-properties/source.html` - test (1725 bytes)
- `test/test-pages/005-unescape-html-entities/expected-metadata.json` - test (159 bytes)
- `test/test-pages/005-unescape-html-entities/expected.html` - test (54 bytes)
- `test/test-pages/005-unescape-html-entities/source.html` - test (221 bytes)
- `test/test-pages/aclu/expected-metadata.json` - test (392 bytes)
- `test/test-pages/aclu/expected.html` - test (13846 bytes)
- `test/test-pages/aktualne/expected-metadata.json` - test (365 bytes)
- `test/test-pages/aktualne/expected.html` - test (5942 bytes)
- `test/test-pages/archive-of-our-own/expected-metadata.json` - test (389 bytes)
- `test/test-pages/archive-of-our-own/expected.html` - test (24975 bytes)
- `test/test-pages/ars-1/expected-metadata.json` - test (305 bytes)
- `test/test-pages/ars-1/expected.html` - test (5994 bytes)
- `test/test-pages/ars-1/source.html` - test (55990 bytes)
- `test/test-pages/article-author-tag/expected-metadata.json` - test (413 bytes)
- `test/test-pages/article-author-tag/expected.html` - test (18890 bytes)
- `test/test-pages/base-url-base-element-relative/expected-metadata.json` - test (648 bytes)
- `test/test-pages/base-url-base-element-relative/expected.html` - test (1895 bytes)
- `test/test-pages/base-url-base-element-relative/source.html` - test (1806 bytes)
- `test/test-pages/base-url-base-element/expected-metadata.json` - test (639 bytes)
- `test/test-pages/base-url-base-element/expected.html` - test (1835 bytes)
- `test/test-pages/base-url-base-element/source.html` - test (1793 bytes)
- `test/test-pages/base-url/expected-metadata.json` - test (629 bytes)
- `test/test-pages/base-url/expected.html` - test (1844 bytes)
- `test/test-pages/base-url/source.html` - test (1764 bytes)
- `test/test-pages/basic-tags-cleaning/expected-metadata.json` - test (291 bytes)
- `test/test-pages/basic-tags-cleaning/expected.html` - test (987 bytes)
- `test/test-pages/basic-tags-cleaning/source.html` - test (1404 bytes)
- `test/test-pages/bbc-1/expected-metadata.json` - test (376 bytes)
- `test/test-pages/bbc-1/expected.html` - test (7944 bytes)
- `test/test-pages/blogger/expected-metadata.json` - test (344 bytes)
- `test/test-pages/blogger/expected.html` - test (18100 bytes)
- `test/test-pages/blogger/source.html` - test (154796 bytes)
- `test/test-pages/breitbart/expected-metadata.json` - test (429 bytes)
- `test/test-pages/breitbart/expected.html` - test (3815 bytes)
- `test/test-pages/bug-1255978/expected-metadata.json` - test (561 bytes)
- `test/test-pages/bug-1255978/expected.html` - test (8545 bytes)
- `test/test-pages/buzzfeed-1/expected-metadata.json` - test (301 bytes)
- `test/test-pages/buzzfeed-1/expected.html` - test (3622 bytes)
- `test/test-pages/citylab-1/expected-metadata.json` - test (333 bytes)
- `test/test-pages/citylab-1/expected.html` - test (14136 bytes)
- `test/test-pages/citylab-1/source.html` - test (173900 bytes)
- `test/test-pages/clean-links/expected-metadata.json` - test (495 bytes)
- `test/test-pages/clean-links/expected.html` - test (85894 bytes)
- `test/test-pages/clean-links/source.html` - test (182350 bytes)
- `test/test-pages/cnet-svg-classes/expected-metadata.json` - test (359 bytes)
- `test/test-pages/cnet-svg-classes/expected.html` - test (35029 bytes)
- `test/test-pages/cnet-svg-classes/source.html` - test (136890 bytes)
- `test/test-pages/cnet/expected-metadata.json` - test (324 bytes)
- `test/test-pages/cnet/expected.html` - test (5922 bytes)
- `test/test-pages/cnn/expected-metadata.json` - test (318 bytes)
- `test/test-pages/cnn/expected.html` - test (3265 bytes)
- `test/test-pages/comment-inside-script-parsing/expected-metadata.json` - test (287 bytes)
- `test/test-pages/comment-inside-script-parsing/expected.html` - test (987 bytes)
- `test/test-pages/comment-inside-script-parsing/source.html` - test (1221 bytes)
- `test/test-pages/daringfireball-1/expected-metadata.json` - test (231 bytes)
- `test/test-pages/daringfireball-1/expected.html` - test (3265 bytes)
- `test/test-pages/daringfireball-1/source.html` - test (10116 bytes)
- `test/test-pages/data-url-image/expected-metadata.json` - test (913 bytes)
- `test/test-pages/data-url-image/expected.html` - test (66160 bytes)
- `test/test-pages/data-url-image/source.html` - test (65841 bytes)
- `test/test-pages/dev418/expected-metadata.json` - test (382 bytes)
- `test/test-pages/dev418/expected.html` - test (2937 bytes)
- `test/test-pages/dev418/source.html` - test (3815 bytes)
- `test/test-pages/dropbox-blog/expected-metadata.json` - test (650 bytes)
- `test/test-pages/dropbox-blog/expected.html` - test (31048 bytes)
- `test/test-pages/dropbox-blog/source.html` - test (80114 bytes)
- `test/test-pages/ebb-org/expected-metadata.json` - test (416 bytes)
- `test/test-pages/ebb-org/expected.html` - test (16104 bytes)
- `test/test-pages/ebb-org/source.html` - test (39614 bytes)
- `test/test-pages/ehow-1/expected-metadata.json` - test (540 bytes)
- `test/test-pages/ehow-1/expected.html` - test (7378 bytes)
- `test/test-pages/ehow-1/source.html` - test (67383 bytes)
- `test/test-pages/ehow-2/expected-metadata.json` - test (565 bytes)
- `test/test-pages/ehow-2/expected.html` - test (12367 bytes)
- `test/test-pages/ehow-2/source.html` - test (107092 bytes)
- `test/test-pages/embedded-videos/expected-metadata.json` - test (636 bytes)
- `test/test-pages/embedded-videos/expected.html` - test (1840 bytes)
- `test/test-pages/embedded-videos/source.html` - test (2059 bytes)
- `test/test-pages/engadget/expected-metadata.json` - test (342 bytes)
- `test/test-pages/engadget/expected.html` - test (18725 bytes)
- `test/test-pages/firefox-nightly-blog/expected-metadata.json` - test (432 bytes)
- `test/test-pages/firefox-nightly-blog/expected.html` - test (28154 bytes)
- `test/test-pages/firefox-nightly-blog/source.html` - test (82821 bytes)
- `test/test-pages/folha/expected-metadata.json` - test (364 bytes)
- `test/test-pages/folha/expected.html` - test (3019 bytes)
- `test/test-pages/gitlab-blog/expected-metadata.json` - test (375 bytes)
- `test/test-pages/gitlab-blog/expected.html` - test (12931 bytes)
- `test/test-pages/gitlab-blog/source.html` - test (71975 bytes)
- `test/test-pages/gmw/expected-metadata.json` - test (386 bytes)
- `test/test-pages/gmw/expected.html` - test (11521 bytes)
- `test/test-pages/gmw/source.html` - test (143533 bytes)
- `test/test-pages/google-sre-book-1/expected-metadata.json` - test (543 bytes)
- `test/test-pages/google-sre-book-1/expected.html` - test (42063 bytes)
- `test/test-pages/google-sre-book-1/source.html` - test (70029 bytes)
- `test/test-pages/guardian-1/expected-metadata.json` - test (398 bytes)
- `test/test-pages/guardian-1/expected.html` - test (66157 bytes)
- `test/test-pages/heise/expected-metadata.json` - test (380 bytes)
- `test/test-pages/heise/expected.html` - test (2738 bytes)
- `test/test-pages/heise/source.html` - test (62142 bytes)
- `test/test-pages/herald-sun-1/expected-metadata.json` - test (444 bytes)
- `test/test-pages/herald-sun-1/expected.html` - test (5996 bytes)
- `test/test-pages/herald-sun-1/source.html` - test (62123 bytes)
- `test/test-pages/hidden-nodes/expected-metadata.json` - test (1133 bytes)
- `test/test-pages/hidden-nodes/expected.html` - test (1010 bytes)
- `test/test-pages/hidden-nodes/source.html` - test (3369 bytes)
- `test/test-pages/hukumusume/expected-metadata.json` - test (309 bytes)
- `test/test-pages/hukumusume/expected.html` - test (14022 bytes)
- `test/test-pages/hukumusume/source.html` - test (24662 bytes)
- `test/test-pages/iab-1/expected-metadata.json` - test (591 bytes)
- `test/test-pages/iab-1/expected.html` - test (6822 bytes)
- `test/test-pages/iab-1/source.html` - test (102377 bytes)
- `test/test-pages/ietf-1/expected-metadata.json` - test (161 bytes)
- `test/test-pages/ietf-1/expected.html` - test (56074 bytes)
- `test/test-pages/ietf-1/source.html` - test (64711 bytes)
- `test/test-pages/invalid-attributes/expected-metadata.json` - test (203 bytes)
- `test/test-pages/invalid-attributes/expected.html` - test (154 bytes)
- `test/test-pages/invalid-attributes/source.html` - test (437 bytes)
- `test/test-pages/js-link-replacement/expected-metadata.json` - test (164 bytes)
- `test/test-pages/js-link-replacement/expected.html` - test (114 bytes)
- `test/test-pages/js-link-replacement/source.html` - test (209 bytes)
- `test/test-pages/keep-images/expected-metadata.json` - test (322 bytes)
- `test/test-pages/keep-images/expected.html` - test (30270 bytes)
- `test/test-pages/keep-images/source.html` - test (141158 bytes)
- `test/test-pages/keep-tabular-data/expected-metadata.json` - test (256 bytes)
- `test/test-pages/keep-tabular-data/expected.html` - test (43083 bytes)
- `test/test-pages/keep-tabular-data/source.html` - test (64206 bytes)
- `test/test-pages/la-nacion/expected-metadata.json` - test (321 bytes)
- `test/test-pages/la-nacion/expected.html` - test (8417 bytes)
- `test/test-pages/la-nacion/source.html` - test (63471 bytes)
- `test/test-pages/lazy-image-1/expected-metadata.json` - test (380 bytes)
- `test/test-pages/lazy-image-1/expected.html` - test (16435 bytes)
- `test/test-pages/lazy-image-2/expected-metadata.json` - test (668 bytes)
- `test/test-pages/lazy-image-2/expected.html` - test (153073 bytes)
- `test/test-pages/lazy-image-3/expected-metadata.json` - test (170 bytes)
- `test/test-pages/lazy-image-3/expected.html` - test (698 bytes)
- `test/test-pages/lazy-image-3/source.html` - test (664 bytes)
- `test/test-pages/lemonde-1/expected-metadata.json` - test (408 bytes)
- `test/test-pages/lemonde-1/expected.html` - test (12378 bytes)
- `test/test-pages/lemonde-1/source.html` - test (87454 bytes)
- `test/test-pages/liberation-1/expected-metadata.json` - test (351 bytes)
- `test/test-pages/liberation-1/expected.html` - test (3004 bytes)
- `test/test-pages/liberation-1/source.html` - test (140861 bytes)
- `test/test-pages/lifehacker-post-comment-load/expected-metadata.json` - test (532 bytes)
- `test/test-pages/lifehacker-post-comment-load/expected.html` - test (26568 bytes)
- `test/test-pages/lifehacker-working/expected-metadata.json` - test (532 bytes)
- `test/test-pages/lifehacker-working/expected.html` - test (26568 bytes)
- `test/test-pages/lifehacker-working/source.html` - test (128053 bytes)
- `test/test-pages/links-in-tables/expected-metadata.json` - test (330 bytes)
- `test/test-pages/links-in-tables/expected.html` - test (12661 bytes)
- `test/test-pages/links-in-tables/source.html` - test (131911 bytes)
- `test/test-pages/lwn-1/expected-metadata.json` - test (621 bytes)
- `test/test-pages/lwn-1/expected.html` - test (59235 bytes)
- `test/test-pages/lwn-1/source.html` - test (87143 bytes)
- `test/test-pages/mathjax/expected-metadata.json` - test (200 bytes)
- `test/test-pages/mathjax/expected.html` - test (32045 bytes)
- `test/test-pages/medicalnewstoday/expected-metadata.json` - test (400 bytes)
- `test/test-pages/medicalnewstoday/expected.html` - test (7103 bytes)
- `test/test-pages/medicalnewstoday/source.html` - test (150967 bytes)
- `test/test-pages/medium-1/expected-metadata.json` - test (350 bytes)
- `test/test-pages/medium-1/expected.html` - test (23167 bytes)
- `test/test-pages/medium-1/source.html` - test (119561 bytes)
- `test/test-pages/medium-2/expected-metadata.json` - test (331 bytes)
- `test/test-pages/medium-2/expected.html` - test (6328 bytes)
- `test/test-pages/medium-2/source.html` - test (48123 bytes)
- `test/test-pages/medium-3/expected-metadata.json` - test (447 bytes)
- `test/test-pages/medium-3/expected.html` - test (38681 bytes)
- `test/test-pages/mercurial/expected-metadata.json` - test (208 bytes)
- `test/test-pages/mercurial/expected.html` - test (38264 bytes)
- `test/test-pages/mercurial/source.html` - test (64599 bytes)
- `test/test-pages/metadata-content-missing/expected-metadata.json` - test (174 bytes)
- `test/test-pages/metadata-content-missing/expected.html` - test (1043 bytes)
- `test/test-pages/metadata-content-missing/source.html` - test (1571 bytes)
- `test/test-pages/missing-paragraphs/expected-metadata.json` - test (1300 bytes)
- `test/test-pages/missing-paragraphs/expected.html` - test (2806 bytes)
- `test/test-pages/missing-paragraphs/source.html` - test (3729 bytes)
- `test/test-pages/mozilla-1/expected-metadata.json` - test (444 bytes)
- `test/test-pages/mozilla-1/expected.html` - test (5008 bytes)
- `test/test-pages/mozilla-1/source.html` - test (95492 bytes)
- `test/test-pages/mozilla-2/expected-metadata.json` - test (278 bytes)
- `test/test-pages/mozilla-2/expected.html` - test (5973 bytes)
- `test/test-pages/mozilla-2/source.html` - test (25490 bytes)
- `test/test-pages/msn/expected-metadata.json` - test (382 bytes)
- `test/test-pages/msn/expected.html` - test (3743 bytes)
- `test/test-pages/normalize-spaces/expected-metadata.json` - test (648 bytes)
- `test/test-pages/normalize-spaces/expected.html` - test (979 bytes)
- `test/test-pages/normalize-spaces/source.html` - test (1134 bytes)
- `test/test-pages/nytimes-1/expected-metadata.json` - test (308 bytes)
- `test/test-pages/nytimes-1/expected.html` - test (9288 bytes)
- `test/test-pages/nytimes-2/expected-metadata.json` - test (377 bytes)
- `test/test-pages/nytimes-2/expected.html` - test (11523 bytes)
- `test/test-pages/nytimes-3/expected-metadata.json` - test (403 bytes)
- `test/test-pages/nytimes-3/expected.html` - test (21627 bytes)
- `test/test-pages/nytimes-4/expected-metadata.json` - test (384 bytes)
- `test/test-pages/nytimes-4/expected.html` - test (14823 bytes)
- `test/test-pages/nytimes-5/expected-metadata.json` - test (456 bytes)
- `test/test-pages/nytimes-5/expected.html` - test (38663 bytes)
- `test/test-pages/ol/expected-metadata.json` - test (238 bytes)
- `test/test-pages/ol/expected.html` - test (217 bytes)
- `test/test-pages/ol/source.html` - test (195 bytes)
- `test/test-pages/parsely-metadata/expected-metadata.json` - test (641 bytes)
- `test/test-pages/parsely-metadata/expected.html` - test (1043 bytes)
- `test/test-pages/parsely-metadata/source.html` - test (1739 bytes)
- `test/test-pages/pixnet/expected-metadata.json` - test (517 bytes)
- `test/test-pages/pixnet/expected.html` - test (24065 bytes)
- `test/test-pages/qq/expected-metadata.json` - test (290 bytes)
- `test/test-pages/qq/expected.html` - test (3682 bytes)
- `test/test-pages/quanta-1/expected-metadata.json` - test (358 bytes)
- `test/test-pages/quanta-1/expected.html` - test (21304 bytes)
- `test/test-pages/remove-aria-hidden/expected-metadata.json` - test (301 bytes)
- `test/test-pages/remove-aria-hidden/expected.html` - test (333 bytes)
- `test/test-pages/remove-aria-hidden/source.html` - test (543 bytes)
- `test/test-pages/remove-extra-brs/expected-metadata.json` - test (292 bytes)
- `test/test-pages/remove-extra-brs/expected.html` - test (987 bytes)
- `test/test-pages/remove-extra-brs/source.html` - test (1201 bytes)
- `test/test-pages/remove-extra-paragraphs/expected-metadata.json` - test (290 bytes)
- `test/test-pages/remove-extra-paragraphs/expected.html` - test (987 bytes)
- `test/test-pages/remove-extra-paragraphs/source.html` - test (1272 bytes)
- `test/test-pages/remove-script-tags/expected-metadata.json` - test (291 bytes)
- `test/test-pages/remove-script-tags/expected.html` - test (987 bytes)
- `test/test-pages/remove-script-tags/source.html` - test (1539 bytes)
- `test/test-pages/reordering-paragraphs/expected-metadata.json` - test (780 bytes)
- `test/test-pages/reordering-paragraphs/expected.html` - test (1801 bytes)
- `test/test-pages/reordering-paragraphs/source.html` - test (2108 bytes)
- `test/test-pages/replace-brs/expected-metadata.json` - test (171 bytes)
- `test/test-pages/replace-brs/expected.html` - test (1056 bytes)
- `test/test-pages/replace-brs/source.html` - test (1195 bytes)
- `test/test-pages/replace-font-tags/expected-metadata.json` - test (638 bytes)
- `test/test-pages/replace-font-tags/expected.html` - test (1152 bytes)
- `test/test-pages/replace-font-tags/source.html` - test (1293 bytes)
- `test/test-pages/royal-road/expected-metadata.json` - test (382 bytes)
- `test/test-pages/royal-road/expected.html` - test (44958 bytes)
- `test/test-pages/rtl-1/expected-metadata.json` - test (171 bytes)
- `test/test-pages/rtl-1/expected.html` - test (1046 bytes)
- `test/test-pages/rtl-1/source.html` - test (1214 bytes)
- `test/test-pages/rtl-2/expected-metadata.json` - test (171 bytes)
- `test/test-pages/rtl-2/expected.html` - test (1046 bytes)
- `test/test-pages/rtl-2/source.html` - test (1224 bytes)
- `test/test-pages/rtl-3/expected-metadata.json` - test (171 bytes)
- `test/test-pages/rtl-3/expected.html` - test (1056 bytes)
- `test/test-pages/rtl-3/source.html` - test (1214 bytes)
- `test/test-pages/rtl-4/expected-metadata.json` - test (170 bytes)
- `test/test-pages/rtl-4/expected.html` - test (1056 bytes)
- `test/test-pages/rtl-4/source.html` - test (1214 bytes)
- `test/test-pages/salon-1/expected-metadata.json` - test (346 bytes)
- `test/test-pages/salon-1/expected.html` - test (15806 bytes)
- `test/test-pages/schema-org-context-object/expected-metadata.json` - test (434 bytes)
- `test/test-pages/schema-org-context-object/expected.html` - test (13468 bytes)
- `test/test-pages/seattletimes-1/expected-metadata.json` - test (560 bytes)
- `test/test-pages/seattletimes-1/expected.html` - test (16496 bytes)
- `test/test-pages/simplyfound-1/expected-metadata.json` - test (525 bytes)
- `test/test-pages/simplyfound-1/expected.html` - test (2264 bytes)
- `test/test-pages/simplyfound-1/source.html` - test (33152 bytes)
- `test/test-pages/social-buttons/expected-metadata.json` - test (642 bytes)
- `test/test-pages/social-buttons/expected.html` - test (2423 bytes)
- `test/test-pages/social-buttons/source.html` - test (3308 bytes)
- `test/test-pages/spiceworks/expected-metadata.json` - test (432 bytes)
- `test/test-pages/spiceworks/expected.html` - test (5733 bytes)
- `test/test-pages/spiceworks/source.html` - test (186175 bytes)
- `test/test-pages/style-tags-removal/expected-metadata.json` - test (634 bytes)
- `test/test-pages/style-tags-removal/expected.html` - test (977 bytes)
- `test/test-pages/style-tags-removal/source.html` - test (1326 bytes)
- `test/test-pages/svg-parsing/expected-metadata.json` - test (597 bytes)
- `test/test-pages/svg-parsing/expected.html` - test (2854 bytes)
- `test/test-pages/svg-parsing/source.html` - test (2761 bytes)
- `test/test-pages/table-style-attributes/expected-metadata.json` - test (228 bytes)
- `test/test-pages/table-style-attributes/expected.html` - test (12237 bytes)
- `test/test-pages/table-style-attributes/source.html` - test (14417 bytes)
- `test/test-pages/telegraph/expected-metadata.json` - test (521 bytes)
- `test/test-pages/telegraph/expected.html` - test (3664 bytes)
- `test/test-pages/theverge/expected-metadata.json` - test (399 bytes)
- `test/test-pages/theverge/expected.html` - test (9239 bytes)
- `test/test-pages/title-and-h1-discrepancy/expected-metadata.json` - test (674 bytes)
- `test/test-pages/title-and-h1-discrepancy/expected.html` - test (1081 bytes)
- `test/test-pages/title-and-h1-discrepancy/source.html` - test (1295 bytes)
- `test/test-pages/title-en-dash/expected-metadata.json` - test (645 bytes)
- `test/test-pages/title-en-dash/expected.html` - test (992 bytes)
- `test/test-pages/title-en-dash/source.html` - test (1189 bytes)
- `test/test-pages/tmz-1/expected-metadata.json` - test (359 bytes)
- `test/test-pages/tmz-1/expected.html` - test (1748 bytes)
- `test/test-pages/tmz-1/source.html` - test (92266 bytes)
- `test/test-pages/toc-missing/expected-metadata.json` - test (546 bytes)
- `test/test-pages/toc-missing/expected.html` - test (72606 bytes)
- `test/test-pages/toc-missing/source.html` - test (128400 bytes)
- `test/test-pages/topicseed-1/expected-metadata.json` - test (452 bytes)
- `test/test-pages/topicseed-1/expected.html` - test (12001 bytes)
- `test/test-pages/topicseed-1/source.html` - test (112812 bytes)
- `test/test-pages/tumblr/expected-metadata.json` - test (433 bytes)
- `test/test-pages/tumblr/expected.html` - test (3451 bytes)
- `test/test-pages/tumblr/source.html` - test (31244 bytes)
- `test/test-pages/v8-blog/expected-metadata.json` - test (281 bytes)
- `test/test-pages/v8-blog/expected.html` - test (21710 bytes)
- `test/test-pages/v8-blog/source.html` - test (33095 bytes)
- `test/test-pages/videos-1/expected-metadata.json` - test (251 bytes)
- `test/test-pages/videos-1/expected.html` - test (44065 bytes)
- `test/test-pages/videos-2/expected-metadata.json` - test (453 bytes)
- `test/test-pages/videos-2/expected.html` - test (13907 bytes)
- `test/test-pages/videos-2/source.html` - test (179950 bytes)
- `test/test-pages/visibility-hidden/expected-metadata.json` - test (330 bytes)
- `test/test-pages/visibility-hidden/expected.html` - test (474 bytes)
- `test/test-pages/visibility-hidden/source.html` - test (1431 bytes)
- `test/test-pages/wapo-1/expected-metadata.json` - test (410 bytes)
- `test/test-pages/wapo-1/expected.html` - test (11642 bytes)
- `test/test-pages/wapo-1/source.html` - test (180153 bytes)
- `test/test-pages/wapo-2/expected-metadata.json` - test (356 bytes)
- `test/test-pages/wapo-2/expected.html` - test (8406 bytes)
- `test/test-pages/wapo-2/source.html` - test (125800 bytes)
- `test/test-pages/webmd-1/expected-metadata.json` - test (537 bytes)
- `test/test-pages/webmd-1/expected.html` - test (3089 bytes)
- `test/test-pages/webmd-1/source.html` - test (182401 bytes)
- `test/test-pages/webmd-2/expected-metadata.json` - test (312 bytes)
- `test/test-pages/webmd-2/expected.html` - test (3618 bytes)
- `test/test-pages/webmd-2/source.html` - test (136836 bytes)
- `test/test-pages/wikia/expected-metadata.json` - test (413 bytes)
- `test/test-pages/wikia/expected.html` - test (8864 bytes)
- `test/test-pages/wikipedia-2/expected-metadata.json` - test (283 bytes)
- `test/test-pages/wikipedia-3/expected-metadata.json` - test (535 bytes)
- `test/test-pages/wikipedia-3/expected.html` - test (37003 bytes)
- `test/test-pages/wikipedia-4/expected-metadata.json` - test (297 bytes)
- `test/test-pages/wikipedia-4/expected.html` - test (130694 bytes)
- `test/test-pages/wikipedia/expected-metadata.json` - test (548 bytes)
- `test/test-pages/wikipedia/expected.html` - test (114434 bytes)
- `test/test-pages/wordpress/expected-metadata.json` - test (500 bytes)
- `test/test-pages/wordpress/expected.html` - test (10651 bytes)
- `test/test-pages/wordpress/source.html` - test (181493 bytes)
- `test/test-pages/yahoo-1/expected-metadata.json` - test (533 bytes)
- `test/test-pages/yahoo-1/expected.html` - test (10457 bytes)
- `test/test-pages/yahoo-2/expected-metadata.json` - test (325 bytes)
- `test/test-pages/yahoo-2/expected.html` - test (4272 bytes)
- `test/test-pages/yahoo-3/expected-metadata.json` - test (855 bytes)
- `test/test-pages/yahoo-3/expected.html` - test (6214 bytes)
- `test/test-pages/yahoo-4/expected-metadata.json` - test (475 bytes)
- `test/test-pages/yahoo-4/expected.html` - test (3733 bytes)
- `test/test-pages/yahoo-4/source.html` - test (142850 bytes)
- `test/test-pages/youth/expected-metadata.json` - test (777 bytes)
- `test/test-pages/youth/expected.html` - test (8623 bytes)
- `test/test-readability.js` - test, JavaScript (12856 bytes)
- `test/utils.js` - test, JavaScript (1119 bytes)

## 7. Key dependencies and integrations

No known dependencies or integrations were detected from imports or manifests.

## 8. Data and state

No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.

## 9. Configuration and deployment clues

- `.release-it.json` (config)
- `.taskcluster.yml` (config)
- `package.json` (manifest)

## 10. Design observations

- Tests are present alongside source code (Observed from test file paths).

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

## 12. Source references

- [JSDOMParser.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/JSDOMParser.js)
- [Readability-readerable.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/Readability-readerable.js)
- [Readability.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/Readability.js)
- [eslint.config.mjs](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/eslint.config.mjs)
- [index.d.ts](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/index.d.ts)
- [index.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/index.js)
- [package.json](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/package.json)
- [test/debug-testcase.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/debug-testcase.js)
- [test/generate-testcase.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/generate-testcase.js)
- [test/test-isProbablyReaderable.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-isProbablyReaderable.js)
- [test/test-jsdomparser.js](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-jsdomparser.js)
- [test/test-pages/001/expected-metadata.json](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-pages/001/expected-metadata.json)
- [test/test-pages/001/expected.html](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-pages/001/expected.html)
- [test/test-pages/001/source.html](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-pages/001/source.html)
- [test/test-pages/002/expected-metadata.json](https://github.com/mozilla/readability/blob/ab4027a8b37669745016869a37a504727992b2ba/test/test-pages/002/expected-metadata.json)
