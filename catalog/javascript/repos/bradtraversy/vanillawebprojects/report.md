# Architecture report: bradtraversy/vanillawebprojects

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | bradtraversy/vanillawebprojects |
| Description | Mini projects built with HTML5, CSS & JavaScript. No frameworks or libraries |
| Language | JavaScript |
| Stars | 16097 |
| Licence | Not detected |
| Analysed commit / branch | adc66a181a67049fb413c8862181ddc6c45ba22b / master |
| Framework(s) | None detected |
| Files analysed | 85 |
| Components | 21 |

## 2. Architecture in one minute

bradtraversy/vanillawebprojects - Mini projects built with HTML5, CSS & JavaScript. No frameworks or libraries. This repository was analysed statically from 85 file(s) (0 Python). Detected technologies (observed from imports/manifests): no known frameworks/libraries. Files are grouped into 21 component(s): breakout-game package, custom-video-player package, dom-array-methods package, exchange-rate package, expense-tracker package, form-validator package, hangman package, infinite_scroll_blog package. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    breakout_game["breakout-game package"]
    custom_video_player["custom-video-player package"]
    dom_array_methods["dom-array-methods package"]
    exchange_rate["exchange-rate package"]
    expense_tracker["expense-tracker package"]
    form_validator["form-validator package"]
    hangman["hangman package"]
    infinite_scroll_blog["infinite_scroll_blog package"]
    lyrics_search["lyrics-search package"]
    meal_finder["meal-finder package"]
    memory_cards["memory-cards package"]
    modal_menu_slider["modal-menu-slider package"]
    movie_seat_booking["movie-seat-booking package"]
    music_player["music-player package"]
    new_year_countdown["new-year-countdown package"]
    product_filtering["product-filtering package"]
    relaxer_app["relaxer-app package"]
    sortable_list["sortable-list package"]
    speak_number_guess["speak-number-guess package"]
    speech_text_reader["speech-text-reader package"]
    typing_game["typing-game package"]
```

## 4. Main components

### breakout-game package (`breakout_game`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under breakout-game package (observed from repository paths and static analysis).
- **Paths:** `breakout-game/script.js`
- **Evidence:** [breakout-game/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/breakout-game/script.js)

### custom-video-player package (`custom_video_player`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under custom-video-player package (observed from repository paths and static analysis).
- **Paths:** `custom-video-player/script.js`
- **Evidence:** [custom-video-player/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/custom-video-player/script.js)

### dom-array-methods package (`dom_array_methods`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under dom-array-methods package (observed from repository paths and static analysis).
- **Paths:** `dom-array-methods/script.js`
- **Evidence:** [dom-array-methods/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/dom-array-methods/script.js)

### exchange-rate package (`exchange_rate`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under exchange-rate package (observed from repository paths and static analysis).
- **Paths:** `exchange-rate/script.js`
- **Evidence:** [exchange-rate/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/exchange-rate/script.js)

### expense-tracker package (`expense_tracker`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under expense-tracker package (observed from repository paths and static analysis).
- **Paths:** `expense-tracker/script.js`
- **Evidence:** [expense-tracker/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/expense-tracker/script.js)

### form-validator package (`form_validator`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under form-validator package (observed from repository paths and static analysis).
- **Paths:** `form-validator/script.js`
- **Evidence:** [form-validator/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/form-validator/script.js)

### hangman package (`hangman`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under hangman package (observed from repository paths and static analysis).
- **Paths:** `hangman/script.js`
- **Evidence:** [hangman/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/hangman/script.js)

### infinite_scroll_blog package (`infinite_scroll_blog`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under infinite_scroll_blog package (observed from repository paths and static analysis).
- **Paths:** `infinite_scroll_blog/script.js`
- **Evidence:** [infinite_scroll_blog/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/infinite_scroll_blog/script.js)

### lyrics-search package (`lyrics_search`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under lyrics-search package (observed from repository paths and static analysis).
- **Paths:** `lyrics-search/script.js`
- **Evidence:** [lyrics-search/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/lyrics-search/script.js)

### meal-finder package (`meal_finder`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under meal-finder package (observed from repository paths and static analysis).
- **Paths:** `meal-finder/script.js`
- **Evidence:** [meal-finder/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/meal-finder/script.js)

### memory-cards package (`memory_cards`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under memory-cards package (observed from repository paths and static analysis).
- **Paths:** `memory-cards/script.js`
- **Evidence:** [memory-cards/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/memory-cards/script.js)

### modal-menu-slider package (`modal_menu_slider`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under modal-menu-slider package (observed from repository paths and static analysis).
- **Paths:** `modal-menu-slider/script.js`
- **Evidence:** [modal-menu-slider/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/modal-menu-slider/script.js)

### movie-seat-booking package (`movie_seat_booking`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under movie-seat-booking package (observed from repository paths and static analysis).
- **Paths:** `movie-seat-booking/script.js`
- **Evidence:** [movie-seat-booking/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/movie-seat-booking/script.js)

### music-player package (`music_player`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under music-player package (observed from repository paths and static analysis).
- **Paths:** `music-player/script.js`
- **Evidence:** [music-player/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/music-player/script.js)

### new-year-countdown package (`new_year_countdown`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under new-year-countdown package (observed from repository paths and static analysis).
- **Paths:** `new-year-countdown/script.js`
- **Evidence:** [new-year-countdown/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/new-year-countdown/script.js)

### product-filtering package (`product_filtering`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under product-filtering package (observed from repository paths and static analysis).
- **Paths:** `product-filtering/script.js`
- **Evidence:** [product-filtering/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/product-filtering/script.js)

### relaxer-app package (`relaxer_app`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under relaxer-app package (observed from repository paths and static analysis).
- **Paths:** `relaxer-app/script.js`
- **Evidence:** [relaxer-app/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/relaxer-app/script.js)

### sortable-list package (`sortable_list`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under sortable-list package (observed from repository paths and static analysis).
- **Paths:** `sortable-list/script.js`
- **Evidence:** [sortable-list/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/sortable-list/script.js)

### speak-number-guess package (`speak_number_guess`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under speak-number-guess package (observed from repository paths and static analysis).
- **Paths:** `speak-number-guess/script.js`
- **Evidence:** [speak-number-guess/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/speak-number-guess/script.js)

### speech-text-reader package (`speech_text_reader`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under speech-text-reader package (observed from repository paths and static analysis).
- **Paths:** `speech-text-reader/script.js`
- **Evidence:** [speech-text-reader/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/speech-text-reader/script.js)

### typing-game package (`typing_game`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under typing-game package (observed from repository paths and static analysis).
- **Paths:** `typing-game/script.js`
- **Evidence:** [typing-game/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/typing-game/script.js)

## 5. Execution flow

No entry point was observed; the startup flow below is therefore limited.

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. No internal import relationships between components were observed.

## 6. Project structure

### `(root)`

- `readme.md` - docs (4505 bytes)

### `breakout-game`

- `breakout-game/README.md` - docs (406 bytes)
- `breakout-game/index.html` - other (844 bytes)
- `breakout-game/plan.txt` - docs (338 bytes)
- `breakout-game/script.js` - source, JavaScript (5189 bytes)
- `breakout-game/style.css` - other (937 bytes)

### `custom-video-player`

- `custom-video-player/README.md` - docs (305 bytes)
- `custom-video-player/css/progress.css` - other (2982 bytes)
- `custom-video-player/css/style.css` - other (1097 bytes)
- `custom-video-player/index.html` - other (1389 bytes)
- `custom-video-player/script.js` - source, JavaScript (1608 bytes)

### `dom-array-methods`

- `dom-array-methods/index.html` - other (878 bytes)
- `dom-array-methods/readme.md` - docs (369 bytes)
- `dom-array-methods/script.js` - source, JavaScript (2477 bytes)
- `dom-array-methods/style.css` - other (1092 bytes)

### `exchange-rate`

- `exchange-rate/README.md` - docs (354 bytes)
- `exchange-rate/index.html` - other (5570 bytes)
- `exchange-rate/script.js` - source, JavaScript (1265 bytes)
- `exchange-rate/style.css` - other (2025 bytes)

### `expense-tracker`

- `expense-tracker/index.html` - other (1512 bytes)
- `expense-tracker/readme.md` - docs (324 bytes)
- `expense-tracker/script.js` - source, JavaScript (2917 bytes)
- `expense-tracker/style.css` - other (2290 bytes)

### `form-validator`

- `form-validator/index.html` - other (1444 bytes)
- `form-validator/readme.md` - docs (391 bytes)
- `form-validator/script.js` - source, JavaScript (2274 bytes)
- `form-validator/style.css` - other (1480 bytes)

### `hangman`

- `hangman/README.md` - docs (373 bytes)
- `hangman/index.html` - other (1869 bytes)
- `hangman/script.js` - source, JavaScript (2981 bytes)
- `hangman/style.css` - other (2002 bytes)

### `infinite_scroll_blog`

- `infinite_scroll_blog/index.html` - other (723 bytes)
- `infinite_scroll_blog/readme.md` - docs (377 bytes)
- `infinite_scroll_blog/script.js` - source, JavaScript (1883 bytes)
- `infinite_scroll_blog/style.css` - other (1690 bytes)

### `lyrics-search`

- `lyrics-search/index.html` - other (761 bytes)
- `lyrics-search/readme.md` - docs (267 bytes)
- `lyrics-search/script.js` - source, JavaScript (2396 bytes)
- `lyrics-search/style.css` - other (1789 bytes)

### `meal-finder`

- `meal-finder/index.html` - other (1120 bytes)
- `meal-finder/readme.md` - docs (372 bytes)
- `meal-finder/script.js` - source, JavaScript (3253 bytes)
- `meal-finder/style.css` - other (2435 bytes)

### `memory-cards`

- `memory-cards/index.html` - other (2510 bytes)
- `memory-cards/readme.md` - docs (352 bytes)
- `memory-cards/script.js` - source, JavaScript (3686 bytes)
- `memory-cards/style.css` - other (2984 bytes)

### `modal-menu-slider`

- `modal-menu-slider/README.md` - docs (290 bytes)
- `modal-menu-slider/index.html` - other (4606 bytes)
- `modal-menu-slider/script.js` - source, JavaScript (1335 bytes)
- `modal-menu-slider/style.css` - other (2782 bytes)

### `movie-seat-booking`

- `movie-seat-booking/README.md` - docs (541 bytes)
- `movie-seat-booking/index.html` - other (3133 bytes)
- `movie-seat-booking/script.js` - source, JavaScript (2041 bytes)
- `movie-seat-booking/style.css` - other (1750 bytes)

### `music-player`

- `music-player/index.html` - other (1338 bytes)
- `music-player/readme.md` - docs (275 bytes)
- `music-player/script.js` - source, JavaScript (3995 bytes)
- `music-player/style.css` - other (2335 bytes)

### `new-year-countdown`

- `new-year-countdown/README.md` - docs (355 bytes)
- `new-year-countdown/index.html` - other (1005 bytes)
- `new-year-countdown/script.js` - source, JavaScript (1209 bytes)
- `new-year-countdown/style.css` - other (1406 bytes)

### `product-filtering`

- `product-filtering/index.html` - other (3410 bytes)
- `product-filtering/script.js` - source, JavaScript (4570 bytes)

### `relaxer-app`

- `relaxer-app/README.md` - docs (335 bytes)
- `relaxer-app/index.html` - other (625 bytes)
- `relaxer-app/script.js` - source, JavaScript (569 bytes)
- `relaxer-app/style.css` - other (1707 bytes)

### `sortable-list`

- `sortable-list/README.md` - docs (365 bytes)
- `sortable-list/index.html` - other (752 bytes)
- `sortable-list/script.js` - source, JavaScript (2946 bytes)
- `sortable-list/style.css` - other (1525 bytes)

### `speak-number-guess`

- `speak-number-guess/index.html` - other (546 bytes)
- `speak-number-guess/readme.md` - docs (337 bytes)
- `speak-number-guess/script.js` - source, JavaScript (1695 bytes)
- `speak-number-guess/style.css` - other (674 bytes)

### `speech-text-reader`

- `speech-text-reader/README.md` - docs (366 bytes)
- `speech-text-reader/index.html` - other (855 bytes)
- `speech-text-reader/script.js` - source, JavaScript (2790 bytes)
- `speech-text-reader/style.css` - other (2129 bytes)

### `typing-game`

- `typing-game/index.html` - other (1595 bytes)
- `typing-game/readme.md` - docs (357 bytes)
- `typing-game/script.js` - source, JavaScript (2718 bytes)
- `typing-game/style.css` - other (1763 bytes)

## 7. Key dependencies and integrations

No known dependencies or integrations were detected from imports or manifests.

## 8. Data and state

No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.

## 9. Configuration and deployment clues

No configuration, manifest, CI, or container files were observed.

## 10. Design observations

- No strong design patterns could be established from the available evidence.

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

## 12. Source references

- [breakout-game/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/breakout-game/script.js)
- [custom-video-player/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/custom-video-player/script.js)
- [dom-array-methods/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/dom-array-methods/script.js)
- [exchange-rate/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/exchange-rate/script.js)
- [expense-tracker/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/expense-tracker/script.js)
- [form-validator/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/form-validator/script.js)
- [hangman/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/hangman/script.js)
- [infinite_scroll_blog/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/infinite_scroll_blog/script.js)
- [lyrics-search/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/lyrics-search/script.js)
- [meal-finder/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/meal-finder/script.js)
- [memory-cards/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/memory-cards/script.js)
- [modal-menu-slider/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/modal-menu-slider/script.js)
- [movie-seat-booking/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/movie-seat-booking/script.js)
- [music-player/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/music-player/script.js)
- [new-year-countdown/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/new-year-countdown/script.js)
- [product-filtering/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/product-filtering/script.js)
- [relaxer-app/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/relaxer-app/script.js)
- [sortable-list/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/sortable-list/script.js)
- [speak-number-guess/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/speak-number-guess/script.js)
- [speech-text-reader/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/speech-text-reader/script.js)
- [typing-game/script.js](https://github.com/bradtraversy/vanillawebprojects/blob/adc66a181a67049fb413c8862181ddc6c45ba22b/typing-game/script.js)
