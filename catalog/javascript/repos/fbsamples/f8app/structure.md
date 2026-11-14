# Project structure: fbsamples/f8app

**Analysed commit:** `119f062943c9d7dfa2892a178199435d6854a06f`

**Commit reference:** [119f062943c9d7dfa2892a178199435d6854a06f](https://github.com/fbsamples/f8app/commit/119f062943c9d7dfa2892a178199435d6854a06f)

**Tree at this commit:** [fbsamples/f8app@119f062943c9](https://github.com/fbsamples/f8app/tree/119f062943c9d7dfa2892a178199435d6854a06f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fbsamples/f8app |
| Description | Source code of the official F8 app of 2017, powered by React Native and other Facebook open source projects. |
| Stars | 13869 |
| Forks | 2449 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `119f062943c9d7dfa2892a178199435d6854a06f` |
| Retrieved at | 2026-11-14T19:11:49.718353+00:00 |
| Files in this snapshot | 303 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
__mocks__/  (1 files)
  react-native.js
android/  (18 files)
  app/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    BUCK
    build.gradle
    proguard-rules.pro
  gradle/  (1 files)
    wrapper/  (1 files)
      … 1 files under this directory
  keystores/  (2 files)
    BUCK
    debug.keystore.properties
  build.gradle
  gradle.properties
  gradlew
  gradlew.bat
  settings.gradle
ios/  (14 files)
  F82017/  (7 files)
    Base.lproj/  (1 files)
      … 1 files under this directory
    Images.xcassets/  (1 files)
      … 1 files under this directory
    AppDelegate.h
    AppDelegate.m
    F82017.entitlements
    Info.plist
    main.m
  F82017-tvOS/  (1 files)
    Info.plist
  F82017-tvOSTests/  (1 files)
    Info.plist
  F82017.xcodeproj/  (3 files)
    xcshareddata/  (2 files)
      … 2 files under this directory
    project.pbxproj
  F82017Tests/  (2 files)
    F82017Tests.m
    Info.plist
js/  (171 files)
  actions/  (13 files)
    config.js
    filter.js
    index.js
    installation.js
    login.js
    navigation.js
    notifications.js
    parse.js
    schedule.js
    surveys.js
    test.js
    types.js
    video.js
  common/  (37 files)
    __tests__/  (1 files)
      … 1 files under this directory
    ActionsOverlay.js
    Carousel.js
    F8ActionSheet.js
    F8BackgroundRepeat.js
    F8Button.js
    F8Colors.js
    F8DrawerLayout.js
    F8Fonts.js
    F8Header.js
    F8Linking.js
    F8Modal.js
    F8PageControl.js
    F8ScrollingHeader.js
    F8SegmentedControl.js
    F8StyleSheet.js
    F8Text.js
    F8TimelineBackground.js
    F8TimelineSegment.js
    F8Toast.js
    F8Tooltip.js
    F8Touchable.js
    F8WebView.js
    Hitbox.js
    ItemsWithSeparator.js
    … 12 more files
  filter/  (7 files)
    FilterScreen.android.js
    FilterScreen.ios.js
    FriendsList.js
    Header.js
    Section.js
    TopicItem.js
    topicIcons.js
  login/  (2 files)
    LoginModal.js
    LoginScreen.js
  rating/  (7 files)
    Header.js
    RadioButtons.js
    RatingQuestion.js
    RatingScreen.js
    StarRating.js
    StarRatings.js
    WrittenResponse.js
  reducers/  (24 files)
    __mocks__/  (1 files)
      … 1 files under this directory
    __tests__/  (3 files)
      … 3 files under this directory
    config.js
    createParseReducer.js
    faqs.js
    friendsSchedules.js
    index.js
    maps.js
    navigation.js
    notifications.js
    pages.js
    policies.js
    schedule.js
    scheduleFilter.js
    scheduleTopics.js
    sessions.js
    surveys.js
    testEventDates.js
    user.js
    videoFilter.js
    videoTopics.js
    videos.js
  store/  (6 files)
    analytics.js
    array.js
    compatibility.js
    configureStore.js
    promise.js
    track.js
  tabs/  (62 files)
    demos/  (4 files)
      … 4 files under this directory
    info/  (8 files)
      … 8 files under this directory
    maps/  (3 files)
      … 3 files under this directory
    notifications/  (7 files)
      … 7 files under this directory
    schedule/  (33 files)
      … 33 files under this directory
    videos/  (5 files)
      … 5 files under this directory
    F8TabsView.js
    MenuItem.js
  video/  (3 files)
    F8VideoPlayer.js
    VideoControls.js
    VideoLoader.js
  F8Analytics.js
  F8App.js
  F8Navigator.js
  FacebookSDK.js
  Playground.js
  PushNotificationsController.js
  env.js
  flow-lib.js
  relay-environment.js
  setup.js
scripts/  (5 files)
  generate-graphql-schema.js
  open-ios-project.js
  optimize-images.sh
  pre-push-checks.sh
  run-android-app.sh
server/  (76 files)
  graphql/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    .babelrc
    Dockerfile
    package.json
  mongorestore/  (40 files)
    data/  (39 files)
      … 39 files under this directory
    Dockerfile
  parse-dashboard/  (2 files)
    Dockerfile
    config.json
  parse-server/  (23 files)
    cloud/  (19 files)
      … 19 files under this directory
    .babelrc
    Dockerfile
    config.json
    package.json
  .gitignore
.babelrc
.buckconfig
.eslintignore
.eslintrc
.flowconfig
.gitattributes
.gitignore
.watchmanconfig
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
app.json
docker-compose.yml
index.android.js
index.ios.js
package.json
```

## Entry points

- [js/actions/index.js](https://github.com/fbsamples/f8app/blob/119f062943c9d7dfa2892a178199435d6854a06f/js/actions/index.js)
- [js/reducers/index.js](https://github.com/fbsamples/f8app/blob/119f062943c9d7dfa2892a178199435d6854a06f/js/reducers/index.js)
- [server/graphql/src/index.js](https://github.com/fbsamples/f8app/blob/119f062943c9d7dfa2892a178199435d6854a06f/server/graphql/src/index.js)
- [server/parse-server/cloud/index.js](https://github.com/fbsamples/f8app/blob/119f062943c9d7dfa2892a178199435d6854a06f/server/parse-server/cloud/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| android package | library | Observed | Groups 2 file(s) under android package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 47 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| ios package | library | Observed | Groups 1 file(s) under ios package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 171 file(s) under js package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 25 file(s) under server package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `android/app/build.gradle` (manifest)
- `android/build.gradle` (manifest)
- `app.json` (config)
- `docker-compose.yml` (container)
- `ios/F82017/Images.xcassets/AppIcon.appiconset/Contents.json` (config)
- `package.json` (manifest)
- `server/graphql/Dockerfile` (container)
- `server/graphql/package.json` (manifest)
- `server/mongorestore/Dockerfile` (container)
- `server/mongorestore/data/Agenda.metadata.json` (config)
- `server/mongorestore/data/Attendance.metadata.json` (config)
- `server/mongorestore/data/Demo.metadata.json` (config)
- `server/mongorestore/data/FAQ.metadata.json` (config)
- `server/mongorestore/data/Maps.metadata.json` (config)
- `server/mongorestore/data/MeetupSponsors.metadata.json` (config)
- `server/mongorestore/data/Meetups.metadata.json` (config)
- `server/mongorestore/data/Notification.metadata.json` (config)
- `server/mongorestore/data/Page.metadata.json` (config)
- `server/mongorestore/data/PendingNotifications.metadata.json` (config)
- `server/mongorestore/data/Policy.metadata.json` (config)
- `server/mongorestore/data/Speakers.metadata.json` (config)
- `server/mongorestore/data/Survey.metadata.json` (config)
- `server/mongorestore/data/SurveyQuestions.metadata.json` (config)
- `server/mongorestore/data/SurveyResult.metadata.json` (config)
- `server/mongorestore/data/UTestAgenda.metadata.json` (config)
- `server/mongorestore/data/UnmaskedAgenda.metadata.json` (config)
- `server/mongorestore/data/Video.metadata.json` (config)
- `server/mongorestore/data/_Audience.metadata.json` (config)
- `server/mongorestore/data/_Cardinality.metadata.json` (config)
- `server/mongorestore/data/_EventDimension.metadata.json` (config)
- `server/mongorestore/data/_GlobalConfig.metadata.json` (config)
- `server/mongorestore/data/_Installation.metadata.json` (config)
- `server/mongorestore/data/_JobStatus.metadata.json` (config)
- `server/mongorestore/data/_Join:mySchedule:_User.metadata.json` (config)
- `server/mongorestore/data/_PushStatus.metadata.json` (config)
- `server/mongorestore/data/_QueryToolQuery.metadata.json` (config)
- `server/mongorestore/data/_Role.metadata.json` (config)
- `server/mongorestore/data/_SCHEMA.metadata.json` (config)
- `server/mongorestore/data/_Session.metadata.json` (config)
- `server/mongorestore/data/_User.metadata.json` (config)
- `server/mongorestore/data/_dummy.metadata.json` (config)
- `server/mongorestore/data/objectlabs-system.metadata.json` (config)
- `server/parse-dashboard/Dockerfile` (container)
- `server/parse-dashboard/config.json` (config)
- `server/parse-server/Dockerfile` (container)
- `server/parse-server/config.json` (config)
- `server/parse-server/package.json` (manifest)

## Top-level layout

- `js` — 171 analysed file(s)
- `server` — 76 analysed file(s)
- `android` — 18 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `ios` — 14 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `__mocks__` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `119f062943c9d7dfa2892a178199435d6854a06f` is the revision these paths and observations refer to.
