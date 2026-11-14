# Project structure: liyupi/mianshiya

**Analysed commit:** `7354f4859b7425338dfcff6410e9903bca0ec0dd`

**Commit reference:** [7354f4859b7425338dfcff6410e9903bca0ec0dd](https://github.com/liyupi/mianshiya/commit/7354f4859b7425338dfcff6410e9903bca0ec0dd)

**Tree at this commit:** [liyupi/mianshiya@7354f4859b74](https://github.com/liyupi/mianshiya/tree/7354f4859b7425338dfcff6410e9903bca0ec0dd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | liyupi/mianshiya |
| Description | 持续维护的企业面试题库网站，帮你拿到满意 offer！⭐️ 2026年最新Java面试题、前端面试题、AI大模型面试题、AI Agent面试题、RAG面试题、C++面试题、Go面试题、Python面试题、测试面试题、运维面试题、后端面试题、操作系统面试题、计算机网络面试题、Redis面试题、MySQL数据库面试题、算法面试题、Spring面试题、JVM面试题、Java并发面试题、Linux面试题、LLM面试题、Prompt工程面试题、系统设计面试题等1万多道高频程序员求职必备八股文。面试刷题就选面试鸭 💎 React 前端 + Node 后端 + 云开发全栈项目 by 程序员鱼皮 |
| Stars | 6049 |
| Forks | 1229 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `7354f4859b7425338dfcff6410e9903bca0ec0dd` |
| Retrieved at | 2026-11-14T19:14:10.470268+00:00 |
| Files in this snapshot | 396 |

## Directory tree

```text
cloudfunctions/  (109 files)
  comment/  (12 files)
    addComment/  (2 files)
      … 2 files under this directory
    deleteComment/  (2 files)
      … 2 files under this directory
    reviewComment/  (2 files)
      … 2 files under this directory
    searchComments/  (2 files)
      … 2 files under this directory
    thumbUpComment/  (2 files)
      … 2 files under this directory
    updateComment/  (2 files)
      … 2 files under this directory
  common/  (8 files)
    esService/  (3 files)
      … 3 files under this directory
    redisService/  (2 files)
      … 2 files under this directory
    sendEmail/  (3 files)
      … 3 files under this directory
  getCaptcha/  (2 files)
    index.js
    package.json
  login/  (3 files)
    index.js
    package.json
    tcb_custom_login_key(mianshiya-xx).json
  meetQuestion/  (8 files)
    addMeetQuestion/  (2 files)
      … 2 files under this directory
    deleteMeetQuestion/  (2 files)
      … 2 files under this directory
    searchMeetQuestions/  (2 files)
      … 2 files under this directory
    updateMeetQuestion/  (2 files)
      … 2 files under this directory
  message/  (10 files)
    addMessage/  (2 files)
      … 2 files under this directory
    countMyMessages/  (2 files)
      … 2 files under this directory
    searchMessages/  (2 files)
      … 2 files under this directory
    updateAllMessages/  (2 files)
      … 2 files under this directory
    updateMessage/  (2 files)
      … 2 files under this directory
  paper/  (10 files)
    addPaper/  (2 files)
      … 2 files under this directory
    deletePaper/  (2 files)
      … 2 files under this directory
    searchPapers/  (2 files)
      … 2 files under this directory
    updatePaper/  (2 files)
      … 2 files under this directory
    viewPaper/  (2 files)
      … 2 files under this directory
  question/  (22 files)
    addQuestion/  (2 files)
      … 2 files under this directory
    deleteQuestion/  (2 files)
      … 2 files under this directory
    favourQuestion/  (2 files)
      … 2 files under this directory
    getRandomQuestion/  (2 files)
      … 2 files under this directory
    listRecommendQuestions/  (2 files)
      … 2 files under this directory
    reviewQuestion/  (2 files)
      … 2 files under this directory
    searchQuestions/  (2 files)
      … 2 files under this directory
    shareQuestion/  (2 files)
      … 2 files under this directory
    syncQuestionsToES/  (2 files)
      … 2 files under this directory
    updateQuestion/  (2 files)
      … 2 files under this directory
    viewQuestion/  (2 files)
      … 2 files under this directory
  reply/  (6 files)
    addReply/  (2 files)
      … 2 files under this directory
    deleteReply/  (2 files)
      … 2 files under this directory
    searchReplies/  (2 files)
      … 2 files under this directory
  report/  (4 files)
    addReport/  (2 files)
      … 2 files under this directory
    reviewReport/  (2 files)
      … 2 files under this directory
  searchHistory/  (4 files)
    addSearchHistory/  (2 files)
      … 2 files under this directory
    hotSearches/  (2 files)
      … 2 files under this directory
  tag/  (2 files)
    getTagsMap/  (2 files)
      … 2 files under this directory
  user/  (12 files)
    getCurrentUser/  (2 files)
      … 2 files under this directory
    getSimpleUser/  (2 files)
      … 2 files under this directory
    getUserRank/  (2 files)
      … 2 files under this directory
    listUserCycleRank/  (2 files)
      … 2 files under this directory
    listUserTotalRank/  (2 files)
      … 2 files under this directory
    updateUser/  (2 files)
      … 2 files under this directory
  userScore/  (4 files)
    addUserScore/  (2 files)
      … 2 files under this directory
    countUserScoreRank/  (2 files)
      … 2 files under this directory
  .gitignore
  README.md
config/  (7 files)
  config.dev.ts
  config.ts
  defaultSettings.ts
  headerMenu.tsx
  proxy.ts
  questionMenu.tsx
  routes.ts
docker/  (1 files)
  nginx.conf
public/  (1 files)
  robots.txt
server/  (89 files)
  src/  (84 files)
    config/  (3 files)
      … 3 files under this directory
    constant/  (1 files)
      … 1 files under this directory
    dao/  (1 files)
      … 1 files under this directory
    exception/  (2 files)
      … 2 files under this directory
    service/  (73 files)
      … 73 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    app.js
    index.js
    server.js
  .dockerignore
  .gitignore
  Dockerfile
  README.md
  package.json
src/  (173 files)
  components/  (70 files)
    AddMeetQuestionModal/  (2 files)
      … 2 files under this directory
    AddMultipleOptions/  (2 files)
      … 2 files under this directory
    AddQuestionEditModal/  (2 files)
      … 2 files under this directory
    AddSingleOptions/  (2 files)
      … 2 files under this directory
    AffixQuestionDrawer/  (2 files)
      … 2 files under this directory
    CommentItem/  (2 files)
      … 2 files under this directory
    DebounceSelect/  (1 files)
      … 1 files under this directory
    ExamQuestionList/  (2 files)
      … 2 files under this directory
    FormTagTree/  (1 files)
      … 1 files under this directory
    GlobalFooter/  (1 files)
      … 1 files under this directory
    GlobalHeader/  (3 files)
      … 3 files under this directory
    GlobalLoading/  (1 files)
      … 1 files under this directory
    HeaderSearch/  (2 files)
      … 2 files under this directory
    ListMeetQuestionModal/  (2 files)
      … 2 files under this directory
    MyInterestUpdateModal/  (1 files)
      … 1 files under this directory
    NoAuth/  (1 files)
      … 1 files under this directory
    PaperDetailCard/  (2 files)
      … 2 files under this directory
    PaperItem/  (2 files)
      … 2 files under this directory
    PicUploader/  (3 files)
      … 3 files under this directory
    PickedQuestionList/  (2 files)
      … 2 files under this directory
    QuestionDetailCard/  (2 files)
      … 2 files under this directory
    QuestionItem/  (2 files)
      … 2 files under this directory
    QuestionList/  (2 files)
      … 2 files under this directory
    QuestionManageBar/  (2 files)
      … 2 files under this directory
    QuestionQueryList/  (2 files)
      … 2 files under this directory
    QuestionRejectModal/  (1 files)
      … 1 files under this directory
    RankOrder/  (2 files)
      … 2 files under this directory
    ReplyList/  (2 files)
      … 2 files under this directory
    ReportModal/  (1 files)
      … 1 files under this directory
    RichTextEditor/  (2 files)
      … 2 files under this directory
    RichTextViewer/  (2 files)
      … 2 files under this directory
    SelectTags/  (2 files)
      … 2 files under this directory
    TagCard/  (2 files)
      … 2 files under this directory
    TagList/  (2 files)
      … 2 files under this directory
    TagTabList/  (1 files)
      … 1 files under this directory
    TestInit/  (1 files)
      … 1 files under this directory
    TopicMenu/  (1 files)
      … 1 files under this directory
    UserInfoCard/  (2 files)
      … 2 files under this directory
    UserInfoCardPopover/  (2 files)
      … 2 files under this directory
    UserTitleBar/  (1 files)
      … 1 files under this directory
  constant/  (10 files)
    comment.ts
    index.ts
    level.ts
    message.ts
    paper.ts
    question.ts
    report.ts
    reviewStatusEnum.ts
    tag.ts
    user.ts
  layouts/  (5 files)
    AdminLayout.tsx
    BasicLayout.less
    BasicLayout.tsx
    UserLayout.less
    UserLayout.tsx
  models/  (14 files)
    comment.d.ts
    connect.d.ts
    editPaper.ts
    meetQuestion.ts
    message.d.ts
    question.d.ts
    questionEdit.d.ts
    reply.d.ts
    report.d.ts
    searchHistory.d.ts
    tag.ts
    topic.d.ts
    typing.d.ts
    user.ts
  pages/  (47 files)
    AccountCenter/  (10 files)
      … 10 files under this directory
    AddPaper/  (2 files)
      … 2 files under this directory
    AddPaperSucceed/  (2 files)
      … 2 files under this directory
    AddQuestion/  (2 files)
      … 2 files under this directory
    AddSucceed/  (2 files)
      … 2 files under this directory
    DownloadPaper/  (2 files)
      … 2 files under this directory
    Index/  (1 files)
      … 1 files under this directory
    OpCenter/  (6 files)
      … 6 files under this directory
    PaperDetail/  (2 files)
      … 2 files under this directory
    Papers/  (2 files)
      … 2 files under this directory
    QuestionDetail/  (7 files)
      … 7 files under this directory
    Questions/  (2 files)
      … 2 files under this directory
    Ranking/  (1 files)
      … 1 files under this directory
    Tags/  (2 files)
      … 2 files under this directory
    user/  (2 files)
      … 2 files under this directory
    404.tsx
    document.ejs
  plugins/  (2 files)
    axios.js
    moment.js
  services/  (13 files)
    comment.ts
    common.d.ts
    login.ts
    meetQuestion.ts
    message.ts
    paper.ts
    question.ts
    questionEdit.ts
    reply.ts
    report.ts
    searchHistory.ts
    tag.ts
    user.ts
  utils/  (3 files)
    businessUtils.ts
    request.ts
    utils.ts
  wrappers/  (1 files)
    auth.tsx
  access.ts
  app.tsx
  global.less
  global.tsx
  manifest.json
  service-worker.js
  tcb.js
  typings.d.ts
.all-contributorsrc
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.prettierignore
.prettierrc.js
.stylelintrc.js
CODE_OF_CONDUCT.md
Dockerfile
LICENSE
README.md
cloudbaserc.json
jsconfig.json
package.json
tsconfig.json
```

## Entry points

- [cloudfunctions/comment/addComment/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/comment/addComment/index.js)
- [cloudfunctions/comment/deleteComment/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/comment/deleteComment/index.js)
- [cloudfunctions/comment/reviewComment/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/comment/reviewComment/index.js)
- [cloudfunctions/comment/searchComments/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/comment/searchComments/index.js)
- [cloudfunctions/comment/thumbUpComment/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/comment/thumbUpComment/index.js)
- [cloudfunctions/comment/updateComment/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/comment/updateComment/index.js)
- [cloudfunctions/common/esService/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/common/esService/index.js)
- [cloudfunctions/common/redisService/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/common/redisService/index.js)
- [cloudfunctions/common/sendEmail/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/common/sendEmail/index.js)
- [cloudfunctions/getCaptcha/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/getCaptcha/index.js)
- [cloudfunctions/login/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/login/index.js)
- [cloudfunctions/meetQuestion/addMeetQuestion/index.js](https://github.com/liyupi/mianshiya/blob/7354f4859b7425338dfcff6410e9903bca0ec0dd/cloudfunctions/meetQuestion/addMeetQuestion/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| access.ts package | library | Observed | Groups 1 file(s) under access.ts package (observed from repository paths and static analysis). |
| app.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| cloudfunctions package | library | Observed | Groups 52 file(s) under cloudfunctions package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 42 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 81 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constant package | library | Observed | Groups 10 file(s) under constant package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 14 file(s) under data layer (observed from repository paths and static analysis). |
| global.tsx package | library | Observed | Groups 1 file(s) under global.tsx package (observed from repository paths and static analysis). |
| layouts package | library | Observed | Groups 3 file(s) under layouts package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 32 file(s) under pages package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 2 file(s) under plugins package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 8 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 79 file(s) under service / domain layer (observed from repository paths and static analysis). |
| service-worker.js package | library | Observed | Groups 1 file(s) under service-worker.js package (observed from repository paths and static analysis). |
| tcb.js package | library | Observed | Groups 1 file(s) under tcb.js package (observed from repository paths and static analysis). |
| typings.d.ts package | library | Observed | Groups 1 file(s) under typings.d.ts package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |
| wrappers package | library | Observed | Groups 1 file(s) under wrappers package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `Dockerfile` (container)
- `cloudbaserc.json` (config)
- `cloudfunctions/comment/addComment/package.json` (manifest)
- `cloudfunctions/comment/deleteComment/package.json` (manifest)
- `cloudfunctions/comment/reviewComment/package.json` (manifest)
- `cloudfunctions/comment/searchComments/package.json` (manifest)
- `cloudfunctions/comment/thumbUpComment/package.json` (manifest)
- `cloudfunctions/comment/updateComment/package.json` (manifest)
- `cloudfunctions/common/esService/esConfig.json` (config)
- `cloudfunctions/common/esService/package.json` (manifest)
- `cloudfunctions/common/redisService/package.json` (manifest)
- `cloudfunctions/common/sendEmail/package.json` (manifest)
- `cloudfunctions/common/sendEmail/transporter.json` (config)
- `cloudfunctions/getCaptcha/package.json` (manifest)
- `cloudfunctions/login/package.json` (manifest)
- `cloudfunctions/login/tcb_custom_login_key(mianshiya-xx).json` (config)
- `cloudfunctions/meetQuestion/addMeetQuestion/package.json` (manifest)
- `cloudfunctions/meetQuestion/deleteMeetQuestion/package.json` (manifest)
- `cloudfunctions/meetQuestion/searchMeetQuestions/package.json` (manifest)
- `cloudfunctions/meetQuestion/updateMeetQuestion/package.json` (manifest)
- `cloudfunctions/message/addMessage/package.json` (manifest)
- `cloudfunctions/message/countMyMessages/package.json` (manifest)
- `cloudfunctions/message/searchMessages/package.json` (manifest)
- `cloudfunctions/message/updateAllMessages/package.json` (manifest)
- `cloudfunctions/message/updateMessage/package.json` (manifest)
- `cloudfunctions/paper/addPaper/package.json` (manifest)
- `cloudfunctions/paper/deletePaper/package.json` (manifest)
- `cloudfunctions/paper/searchPapers/package.json` (manifest)
- `cloudfunctions/paper/updatePaper/package.json` (manifest)
- `cloudfunctions/paper/viewPaper/package.json` (manifest)
- `cloudfunctions/question/addQuestion/package.json` (manifest)
- `cloudfunctions/question/deleteQuestion/package.json` (manifest)
- `cloudfunctions/question/favourQuestion/package.json` (manifest)
- `cloudfunctions/question/getRandomQuestion/package.json` (manifest)
- `cloudfunctions/question/listRecommendQuestions/package.json` (manifest)
- `cloudfunctions/question/reviewQuestion/package.json` (manifest)
- `cloudfunctions/question/searchQuestions/package.json` (manifest)
- `cloudfunctions/question/shareQuestion/package.json` (manifest)
- `cloudfunctions/question/syncQuestionsToES/package.json` (manifest)
- `cloudfunctions/question/updateQuestion/package.json` (manifest)
- `cloudfunctions/question/viewQuestion/package.json` (manifest)
- `cloudfunctions/reply/addReply/package.json` (manifest)
- `cloudfunctions/reply/deleteReply/package.json` (manifest)
- `cloudfunctions/reply/searchReplies/package.json` (manifest)
- `cloudfunctions/report/addReport/package.json` (manifest)
- `cloudfunctions/report/reviewReport/package.json` (manifest)
- `cloudfunctions/searchHistory/addSearchHistory/package.json` (manifest)
- `cloudfunctions/searchHistory/hotSearches/package.json` (manifest)
- `cloudfunctions/tag/getTagsMap/package.json` (manifest)
- `cloudfunctions/user/getCurrentUser/package.json` (manifest)
- `cloudfunctions/user/getSimpleUser/package.json` (manifest)
- `cloudfunctions/user/getUserRank/package.json` (manifest)
- `cloudfunctions/user/listUserCycleRank/package.json` (manifest)
- `cloudfunctions/user/listUserTotalRank/package.json` (manifest)
- `cloudfunctions/user/updateUser/package.json` (manifest)
- `cloudfunctions/userScore/addUserScore/package.json` (manifest)
- `cloudfunctions/userScore/countUserScoreRank/package.json` (manifest)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `server/.dockerignore` (container)
- `server/Dockerfile` (container)
- `server/package.json` (manifest)
- `server/src/service/common/esService/esConfig.json` (config)
- `server/src/service/common/esService/package.json` (manifest)
- `server/src/service/common/redisService/package.json` (manifest)
- `server/src/service/common/sendEmail/transporter.json` (config)
- `server/src/service/getCaptcha/package.json` (manifest)
- `server/src/service/login/tcb_custom_login_key(mianshiya-test-xxx).json` (config)
- `server/src/service/login/tcb_custom_login_key(mianshiya-xxx).json` (config)
- `src/manifest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 173 analysed file(s)
- `cloudfunctions` — 109 analysed file(s)
- `server` — 89 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `config` — 7 analysed file(s)
- `docker` — 1 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7354f4859b7425338dfcff6410e9903bca0ec0dd` is the revision these paths and observations refer to.
