# Project structure: jackwener/OpenCLI

**Analysed commit:** `9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8`

**Commit reference:** [9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8](https://github.com/jackwener/OpenCLI/commit/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8)

**Tree at this commit:** [jackwener/OpenCLI@9bc5f5ca132e](https://github.com/jackwener/OpenCLI/tree/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jackwener/OpenCLI |
| Description | Make Any Website into CLI & Use your logged-in browser by AI agent.  |
| Stars | 31079 |
| Forks | 3040 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8` |
| Retrieved at | 2026-11-14T19:10:46.975073+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (14 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    new_site_adapter.yml
  actions/  (1 files)
    setup-chrome/  (1 files)
      … 1 files under this directory
  workflows/  (7 files)
    build-extension.yml
    ci.yml
    doc-check.yml
    docs.yml
    e2e-headed.yml
    release.yml
    security.yml
  RELEASING.md
  pull_request_template.md
autoresearch/  (37 files)
  commands/  (4 files)
    debug.ts
    fix.ts
    plan.ts
    run.ts
  presets/  (7 files)
    browser-reliability.ts
    combined-reliability.ts
    index.ts
    save-reliability.ts
    skill-quality.ts
    v2ex-reliability.ts
    zhihu-reliability.ts
  save-adapters/  (6 files)
    xhs-explore-deep.ts
    xhs-note-comments.ts
    xhs-search-full.ts
    zhihu-hot-detail.ts
    zhihu-question-full.ts
    zhihu-search-detail.ts
  baseline-browse.txt
  baseline-skill.txt
  browse-tasks.json
  config.ts
  engine.ts
  eval-all.ts
  eval-browse.ts
  eval-publish.ts
  eval-save.ts
  eval-skill.ts
  eval-v2ex.ts
  eval-zhihu.ts
  logger.ts
  publish-tasks.json
  run-browse.sh
  run-save.sh
  run-skill.sh
  save-tasks.json
  v2ex-tasks.json
  zhihu-tasks.json
cases/  (4 files)
  README.md
  daily-rl-research-monitor.md
  find-paper-implementation.md
  track-conference-papers.md
clis/  (737 files)
  12306/  (10 files)
    auth.js
    me.js
    orders.js
    passengers.js
    price.js
    stations.js
    train.js
    trains.js
    utils.js
    utils.test.js
  1688/  (13 files)
    assets.js
    assets.test.js
    auth.js
    download.js
    download.test.js
    item.js
    item.test.js
    search.js
    search.test.js
    shared.js
    shared.test.js
    store.js
    store.test.js
  1point3acres/  (12 files)
    auth.js
    auth.test.js
    digest.js
    forum.js
    forums.js
    hot.js
    latest.js
    notifications.js
    search.js
    thread.js
    user.js
    utils.js
  36kr/  (6 files)
    article.js
    hot.js
    hot.test.js
    news.js
    news.test.js
    search.js
  51job/  (7 files)
    company.js
    company.test.js
    detail.js
    hot.js
    search.js
    utils.js
    utils.test.js
  _atlassian/  (2 files)
    shared.js
    shared.test.js
  _shared/  (6 files)
    auth-regressions.test.js
    common.js
    google-account.js
    search-adapter.js
    site-auth.js
    site-auth.test.js
  aibase/  (2 files)
    news.js
    news.test.js
  amazon/  (17 files)
    auth.js
    bestsellers.js
    bestsellers.test.js
    discussion.js
    discussion.test.js
    movers-shakers.js
    new-releases.js
    offer.js
    offer.test.js
    product.js
    product.test.js
    rankings.js
    rankings.test.js
    search.js
    search.test.js
    shared.js
    shared.test.js
  apple-podcasts/  (5 files)
    episodes.js
    search.js
    top.js
    utils.js
    utils.test.js
  archive/  (5 files)
    archive.test.js
    item.js
    search.js
    snapshots.js
    wayback.js
  arxiv/  (6 files)
    arxiv.test.js
    author.js
    paper.js
    recent.js
    search.js
    utils.js
  autohome/  (6 files)
    __fixtures__/  (2 files)
      … 2 files under this directory
    autohome.test.js
    brand.js
    score.js
    utils.js
  baidu-scholar/  (1 files)
    search.js
  band/  (5 files)
    auth.js
    bands.js
    mentions.js
    post.js
    posts.js
  barchart/  (4 files)
    flow.js
    greeks.js
    options.js
    quote.js
  bbc/  (3 files)
    news.js
    topic.js
    utils.js
  bilibili/  (26 files)
    auth.js
    comment.js
    comment.test.js
    comments.js
    creator-stats.js
    download.js
    download.test.js
    dynamic.js
    favorite.js
    feed.js
    follow.js
    follow.test.js
    following.js
    history.js
    hot.js
    me.js
    ranking.js
    relation.js
    search.js
    subtitle.js
    summary.js
    unfollow.js
    user-videos.js
    utils.js
    … 2 more files
  binance/  (12 files)
    asks.js
    commands.test.js
    depth.js
    gainers.js
    klines.js
    losers.js
    pairs.js
    price.js
    prices.js
    ticker.js
    top.js
    trades.js
  bloomberg/  (16 files)
    businessweek.js
    businessweek.test.js
    crypto.js
    economics.js
    feeds.js
    green.js
    industries.js
    main.js
    markets.js
    news.js
    opinions.js
    politics.js
    pursuits.js
    tech.js
    utils.js
    utils.test.js
  bluesky/  (9 files)
    feeds.js
    followers.js
    following.js
    profile.js
    search.js
    starter-packs.js
    thread.js
    trending.js
    user.js
  booking/  (2 files)
    booking.test.js
    search.js
  boss/  (21 files)
    __fixtures__/  (1 files)
      … 1 files under this directory
    auth.js
    auth.test.js
    batchgreet.js
    chatlist.js
    chatmsg.js
    detail.js
    detail.test.js
    exchange.js
    greet.js
    invite.js
    joblist.js
    mark.js
    recommend.js
    resume.js
    search.js
    search.test.js
    send.js
    stats.js
    utils.js
    utils.test.js
  brave/  (1 files)
    search.js
  chaoxing/  (5 files)
    assignments.js
    auth.js
    exams.js
    utils.js
    utils.test.js
  chatgpt/  (23 files)
    ask-file.js
    ask-file.test.js
    ask.js
    auth.js
    commands.test.js
    current-ui.test.js
    deep-research-result.js
    detail.js
    envelope.test.js
    file-upload-scope.test.js
    history.js
    image.js
    image.test.js
    model.js
    model.test.js
    new.js
    project-file-add.js
    project-list.js
    read.js
    send.js
    status.js
    utils.js
    utils.test.js
  chess/  (8 files)
    analyze.js
    game.js
    game.test.js
    games.js
    games.test.js
    stats.js
    utils.js
    utils.test.js
  claude/  (12 files)
    ask.js
    ask.test.js
    auth.js
    commands.test.js
    detail.js
    history.js
    new.js
    read.js
    send.js
    status.js
    utils.js
    utils.test.js
  cnki/  (1 files)
    search.js
  coingecko/  (8 files)
    categories.js
    coin.js
    coingecko.test.js
    derivatives.js
    exchanges.js
    global.js
    top.js
    trending.js
  confluence/  (6 files)
    commands.test.js
    create.js
    page.js
    search.js
    shared.js
    update.js
  coupang/  (7 files)
    add-to-cart.js
    auth.js
    coupang.test.js
    product.js
    search.js
    utils.js
    utils.test.js
  crates/  (3 files)
    crate.js
    search.js
    utils.js
  ctrip/  (17 files)
    attraction.js
    auth.js
    auth.test.js
    bus.js
    cruise.js
    ctrip.test.js
    ferry.js
    flight-round.js
    flight.js
    hotel-search.js
    hotel-suggest.js
    hotel.js
    package.js
    search.js
    tour.js
    train.js
    utils.js
  dblp/  (8 files)
    author.js
    browser.js
    browser.test.js
    dblp.test.js
    paper.js
    search.js
    utils.js
    venue.js
  deepseek/  (13 files)
    ask.js
    ask.test.js
    auth.js
    detail.js
    history.js
    new.js
    read.js
    send.js
    send.test.js
    status.js
    usage.js
    utils.js
    utils.test.js
  defillama/  (4 files)
    defillama.test.js
    protocol.js
    protocols.js
    utils.js
  devto/  (5 files)
    latest.js
    read.js
    tag.js
    top.js
    user.js
  dianping/  (8 files)
    __fixtures__/  (2 files)
      … 2 files under this directory
    auth.js
    cityResolver.js
    dianping.test.js
    search.js
    shop.js
    utils.js
  dictionary/  (3 files)
    examples.js
    search.js
    synonyms.js
  dockerhub/  (3 files)
    image.js
    search.js
    utils.js
  dongchedi/  (11 files)
    __fixtures__/  (3 files)
      … 3 files under this directory
    dongchedi.test.js
    koubei.js
    models.js
    score.js
    search.js
    series.js
    specs.js
    utils.js
  douban/  (14 files)
    auth.js
    auth.test.js
    book-hot.js
    download.js
    download.test.js
    marks.js
    movie-hot.js
    photos.js
    reviews.js
    search.js
    subject.js
    top250.js
    utils.js
    utils.test.js
  doubao/  (12 files)
    ask.js
    auth.js
    detail.js
    history.js
    meeting-summary.js
    meeting-transcript.js
    new.js
    read.js
    send.js
    status.js
    utils.js
    utils.test.js
  douyin/  (48 files)
    _shared/  (22 files)
      … 22 files under this directory
    activities.js
    auth.js
    collections.js
    delete.js
    delete.test.js
    detail.LICENSE
    detail.js
    detail.test.js
    draft.js
    draft.test.js
    drafts.js
    hashtag.js
    hashtag.test.js
    location.js
    profile.js
    publish-upload-id.test.js
    publish.js
    search.js
    search.test.js
    stats.js
    stats.test.js
    update.js
    user-videos.js
    user-videos.test.js
    … 2 more files
  dribbble/  (11 files)
    auth.js
    collection.js
    designer.js
    dribbble.test.js
    member.js
    portfolio.js
    profile.js
    service.js
    shot-detail.js
    shot.js
    utils.js
  duckduckgo/  (3 files)
    search.js
    search.test.js
    suggest.js
  eastmoney/  (16 files)
    _secid.js
    announcement.js
    convertible.js
    convertible.test.js
    etf.js
    holders.js
    hot-rank.js
    index-board.js
    kline.js
    kuaixun.js
    longhu.js
    money-flow.js
    northbound.js
    quote.js
    rank.js
    sectors.js
  endoflife/  (2 files)
    product.js
    utils.js
  facebook/  (19 files)
    __fixtures__/  (1 files)
      … 1 files under this directory
    add-friend.js
    auth.js
    events.js
    feed.js
    feed.test.js
    friends.js
    groups.js
    join-group.js
    marketplace-inbox.js
    marketplace-listings.js
    marketplace.test.js
    memories.js
    notifications.js
    notifications.test.js
    profile.js
    profile.test.js
    search.js
    search.test.js
  flathub/  (4 files)
    app.js
    flathub.test.js
    search.js
    utils.js
  flomo/  (3 files)
    auth.js
    memos.js
    memos.test.js
  gemini/  (23 files)
    ask.js
    ask.test.js
    auth.js
    auth.test.js
    commands.test.js
    current-ui.test.js
    deep-research-result.js
    deep-research-result.test.js
    deep-research.js
    deep-research.test.js
    detail.js
    history.js
    image-pipeline.test.js
    image.js
    image.test.js
    models.js
    models.test.js
    new.js
    read.js
    reply-state.test.js
    status.js
    utils.js
    utils.test.js
  geogebra/  (11 files)
    add-circle.js
    add-line.js
    add-point.js
    add-polygon.js
    eval.js
    geogebra.test.js
    hexagon.js
    info.js
    list.js
    triangle.js
    utils.js
  gitee/  (5 files)
    auth.js
    index.js
    search.js
    trending.js
    user.js
  github/  (1 files)
    auth.js
  github-trending/  (1 files)
    repos.js
  gmail/  (7 files)
    attachments.js
    auth.js
    labels.js
    search.js
    thread.js
    utils.js
    utils.test.js
  google/  (8 files)
    images.js
    images.test.js
    news.js
    search.js
    suggest.js
    trends.js
    utils.js
    utils.test.js
  google-scholar/  (3 files)
    cite.js
    profile.js
    search.js
  goproxy/  (4 files)
    goproxy.test.js
    module.js
    utils.js
    versions.js
  gov-law/  (3 files)
    recent.js
    search.js
    shared.js
  gov-policy/  (6 files)
    __fixtures__/  (2 files)
      … 2 files under this directory
    gov-policy.test.js
    recent.js
    search.js
    utils.js
  grok/  (20 files)
    ask.js
    ask.test.js
    auth.js
    auth.test.js
    delete.js
    detail.js
    export-all.js
    export-utils.js
    export.js
    export.test.js
    history.js
    image.js
    image.test.ts
    new.js
    pin.js
    read.js
    send.js
    status.js
    utils.js
    utils.test.js
  guazi/  (6 files)
    __fixtures__/  (2 files)
      … 2 files under this directory
    browse.js
    car.js
    guazi.test.js
    utils.js
  hackernews/  (9 files)
    ask.js
    best.js
    jobs.js
    new.js
    read.js
    search.js
    show.js
    top.js
    user.js
  hf/  (6 files)
    auth.js
    datasets.js
    models.js
    paper.js
    spaces.js
    top.js
  hltv/  (15 files)
    event-matches.js
    hltv.test.js
    match-map.js
    match-series.js
    player-duel.js
    player-form.js
    player-map-pool.js
    player-matches.js
    player-summary.js
    player-teammate-impact.js
    player-vs-team.js
    search.js
    team-map-pool.js
    team-matches.js
    utils.js
  homebrew/  (4 files)
    cask.js
    formula.js
    popular.js
    utils.js
  huodongxing/  (2 files)
    events.js
    events.test.js
  hupu/  (11 files)
    __fixtures__/  (1 files)
      … 1 files under this directory
    auth.js
    detail.js
    hot.js
    hot.test.js
    like.js
    mentions.js
    reply.js
    search.js
    unlike.js
    utils.js
  imdb/  (8 files)
    person.js
    reviews.js
    search.js
    title.js
    top.js
    trending.js
    utils.js
    utils.test.js
  indeed/  (4 files)
    indeed.test.js
    job.js
    search.js
    utils.js
  instagram/  (42 files)
    _shared/  (13 files)
      … 13 files under this directory
    auth.js
    collection-create.js
    collection-delete.js
    comment.js
    download.js
    download.test.js
    explore.js
    follow.js
    followers.js
    following.js
    instagram.test.js
    like.js
    note.js
    note.test.js
    post.js
    post.test.js
    profile.js
    reel.js
    reel.test.js
    save.js
    saved.js
    search.js
    story.js
    story.test.js
    … 5 more files
  jd/  (12 files)
    add-cart.js
    auth.js
    cart.js
    commands.test.js
    detail.js
    item.js
    item.test.js
    item.test.ts
    page-state.js
    reviews.js
    search.js
    search.test.js
  jianyu/  (9 files)
    shared/  (5 files)
      … 5 files under this directory
    auth.js
    detail.js
    search.js
    search.test.js
  jike/  (16 files)
    auth-read.test.js
    auth.js
    comment.js
    create.js
    feed.js
    like.js
    notifications.js
    notifications.test.js
    post.js
    read.test.js
    repost.js
    search.js
    search.test.js
    topic.js
    user.js
    utils.js
  jimeng/  (5 files)
    auth.js
    generate.js
    history.js
    new.js
    workspaces.js
  jira/  (7 files)
    attachments.js
    commands.test.js
    comments.js
    issue.js
    links.js
    search.js
    shared.js
  juejin/  (4 files)
    hot.js
    juejin.test.js
    recommend.js
    utils.js
  ke/  (6 files)
    auth.js
    chengjiao.js
    ershoufang.js
    utils.js
    xiaoqu.js
    zufang.js
  kimi/  (5 files)
    _utils.js
    audit-extras.js
    auth.js
    chat.js
    kimi.test.js
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
PRIVACY.md
README.md
README.zh-CN.md
TESTING.md
```

## Entry points

- [autoresearch/presets/index.ts](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/autoresearch/presets/index.ts)
- [clis/bloomberg/main.js](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/clis/bloomberg/main.js)
- [clis/confluence/page.js](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/clis/confluence/page.js)
- [clis/flathub/app.js](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/clis/flathub/app.js)
- [clis/gitee/index.js](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/clis/gitee/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| autoresearch package | library | Observed | Groups 30 file(s) under autoresearch package (observed from repository paths and static analysis). |
| clis package | library | Observed | Groups 722 file(s) under clis package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/new_site_adapter.yml` (config)
- `.github/actions/setup-chrome/action.yml` (config)
- `.github/workflows/build-extension.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/doc-check.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/e2e-headed.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/security.yml` (ci)
- `autoresearch/browse-tasks.json` (config)
- `autoresearch/publish-tasks.json` (config)
- `autoresearch/save-tasks.json` (config)
- `autoresearch/v2ex-tasks.json` (config)
- `autoresearch/zhihu-tasks.json` (config)
- `clis/autohome/__fixtures__/koubei.json` (config)
- `clis/dongchedi/__fixtures__/search.json` (config)
- `clis/dongchedi/__fixtures__/series-detail.json` (config)
- `clis/dongchedi/__fixtures__/series-score.json` (config)

## Top-level layout

- `clis` — 737 analysed file(s)
- `autoresearch` — 37 analysed file(s)
- `.github` — 14 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `cases` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8` is the revision these paths and observations refer to.
