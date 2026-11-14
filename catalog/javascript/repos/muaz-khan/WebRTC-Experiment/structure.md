# Project structure: muaz-khan/WebRTC-Experiment

**Analysed commit:** `bbcdbc13b3d7864369f0d09a7c089277dec946da`

**Commit reference:** [bbcdbc13b3d7864369f0d09a7c089277dec946da](https://github.com/muaz-khan/WebRTC-Experiment/commit/bbcdbc13b3d7864369f0d09a7c089277dec946da)

**Tree at this commit:** [muaz-khan/WebRTC-Experiment@bbcdbc13b3d7](https://github.com/muaz-khan/WebRTC-Experiment/tree/bbcdbc13b3d7864369f0d09a7c089277dec946da)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | muaz-khan/WebRTC-Experiment |
| Description | WebRTC, WebRTC and WebRTC. Everything here is all about WebRTC!! |
| Stars | 12047 |
| Forks | 3855 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `bbcdbc13b3d7864369f0d09a7c089277dec946da` |
| Retrieved at | 2026-11-14T19:12:12.438242+00:00 |
| Files in this snapshot | 780 |

## Directory tree

```text
Canvas-Designer/  (40 files)
  Help/  (1 files)
    index.html
  dev/  (25 files)
    amd.js
    arc-handler.js
    arrow-handler.js
    bezier-handler.js
    common.js
    data-uris.js
    decorator.js
    drag-helper.js
    draw-helper.js
    eraser-handler.js
    events-handler.js
    file-selector.js
    head.js
    image-handler.js
    line-handler.js
    marker-handler.js
    pdf-handler.js
    pencil-handler.js
    quadratic-handler.js
    rect-handler.js
    share-drawings.js
    tail.js
    text-handler.js
    webrtc-handler.js
    … 1 more files
  .gitignore
  .npmignore
  .travis.yml
  Gruntfile.js
  LICENSE
  README.md
  bower.json
  canvas-designer-widget.js
  index.html
  multiple.html
  package.json
  server.js
  simple.html
  widget.html
Chrome-Extensions/  (107 files)
  Screen-Capturing.js/  (4 files)
    README.md
    Screen-Capturing.js
    index.html
    server.js
  desktopCapture/  (6 files)
    different-api/  (2 files)
      … 2 files under this directory
    README.md
    background-script.js
    content-script.js
    manifest.json
  desktopCapture-p2p/  (35 files)
    background/  (20 files)
      … 20 files under this directory
    extension-pages/  (10 files)
      … 10 files under this directory
    screen-receivers/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    manifest.json
    server.js
  file-sharing/  (8 files)
    README.md
    background.js
    info.html
    manifest.json
    options.html
    options.js
    popup.html
    popup.js
  get-any-webrtc-peer-stream/  (3 files)
    RTCPeerConnection-override.js
    content-script.js
    manifest.json
  getUserMedia-on-http/  (9 files)
    example/  (2 files)
      … 2 files under this directory
    README.md
    background-script.js
    camera-mic.html
    camera-mic.js
    content-script.js
    manifest.json
    webrtc-handler.js
  screen-recording/  (29 files)
    RecordRTC/  (6 files)
      … 6 files under this directory
    background/  (9 files)
      … 9 files under this directory
    preview/  (3 files)
      … 3 files under this directory
    README.md
    camera-mic.html
    camera-mic.js
    dropdown.html
    dropdown.js
    manifest.json
    options.html
    options.js
    preview.html
    video.html
    video.js
  tabCapture/  (10 files)
    CodecsHandler.js
    IceServersHandler.js
    README.md
    index.html
    manifest.json
    options.html
    options.js
    shareStreamUsingRTCMultiConnection.js
    socket.io.js
    tab-capturing.js
  .gitignore
  LICENSE
  README.md
ConcatenateBlobs/  (4 files)
  ConcatenateBlobs.js
  README.md
  index.html
  package.json
Conversation.js/  (15 files)
  AndroidRTC/  (7 files)
    scripts/  (4 files)
      … 4 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    index.html
    manifest.json
  demos/  (4 files)
    common-signaling.js
    common-styles.css
    cross-language-chat.html
    search-user.html
  README.md
  conversation.js
  package.json
  server.js
DataChannel/  (28 files)
  dev/  (15 files)
    DataChannel.js
    DataConnector.js
    FileConverter.js
    FileReceiver.js
    FileSaver.js
    FileSender.js
    IceServersHandler.js
    RTCPeerConnection.js
    SocketConnector.js
    TextReceiver.js
    TextSender.js
    externalIceServers.js
    globals.js
    head.js
    tail.js
  .gitignore
  .jshintrc
  .npmignore
  .travis.yml
  DataChannel.js
  Gruntfile.js
  README.md
  auto-session-establishment.html
  bower.json
  index.html
  package.json
  server.js
  simple.html
DetectRTC/  (37 files)
  dev/  (13 files)
    CheckDeviceSupport.js
    DetectLocalIPAddress.js
    DetectRTC.js
    Objects.js
    common.js
    detectCaptureStream.js
    detectDesktopOS.js
    detectOSName.js
    detectPrivateBrowsing.js
    getBrowserInfo.js
    head.js
    isMobile.js
    tail.js
  simple-demos/  (2 files)
    select-cameras.html
    simple-demo.html
  test/  (9 files)
    html-test-files/  (4 files)
      … 4 files under this directory
    CheckDeviceSupport.js
    DetectRTC.js
    browserstack.config.js
    detectOSName.js
    getBrowserInfo.js
  .gitignore
  .jshintrc
  .npmignore
  .travis.yml
  DetectRTC.js
  Gruntfile.js
  LICENSE
  README.md
  bower.json
  index.html
  npm-test.js
  package.json
  server.js
FileBufferReader/  (34 files)
  demo/  (5 files)
    IceServersHandler.js
    PeerConnection.js
    PeerUI.js
    adapter-latest.js
    index.html
  dev/  (9 files)
    FileBufferReader.js
    FileBufferReaderHelper.js
    FileBufferReceiver.js
    FileConverter.js
    FileSelector.js
    binarize.js
    common.js
    head.js
    tail.js
  fbr-client/  (9 files)
    demo/  (3 files)
      … 3 files under this directory
    .gitignore
    .npmignore
    README.md
    index.html
    package.json
    server.js
  .gitignore
  .npmignore
  .travis.yml
  FileBufferReader.js
  Gruntfile.js
  LICENSE
  README.md
  bower.json
  index.html
  package.json
  server.js
Firefox-Extensions/  (15 files)
  enable-screen-capturing/  (5 files)
    test/  (1 files)
      … 1 files under this directory
    README.md
    content-script.js
    index.js
    package.json
  enable-screen-capturing-old/  (3 files)
    README.md
    bootstrap.js
    install.rdf
  enable-screen-capturing-old2/  (6 files)
    test/  (1 files)
      … 1 files under this directory
    FirefoxScreenAddon.js
    README.md
    content-script.js
    index.js
    package.json
  README.md
MediaStreamRecorder/  (46 files)
  AudioStreamRecorder/  (8 files)
    lib/  (2 files)
      … 2 files under this directory
    FlashAudioRecorder.js
    FlashAudioRecorder.md
    MediaRecorderWrapper.js
    README.md
    StereoAudioRecorder.js
    StereoAudioRecorderHelper.js
  FileSystem/  (3 files)
    FileReader.js
    FileWriter.js
    README.md
  VideoStreamRecorder/  (6 files)
    lib/  (2 files)
      … 2 files under this directory
    GifRecorder.js
    README.md
    WhammyRecorder.js
    WhammyRecorderHelper.js
  common/  (7 files)
    ConcatenateBlobs.js
    Cross-Browser-Declarations.js
    MediaStreamRecorder.js
    MultiStreamRecorder.js
    MultiStreamsMixer.js
    OpentTokStreamRecorder.js
    amd.js
  demos/  (9 files)
    MultiStreamRecorder.html
    README.md
    audio-recorder.html
    flash-audio-recorder-upload.html
    flash-audio-recorder.html
    gif-recorder.html
    index.html
    opentok-stream-recorder.html
    video-recorder.html
  lib/  (1 files)
    AjaxRequest/  (1 files)
      … 1 files under this directory
  tests/  (1 files)
    flash-audio-recorder-memory-usage.html
  .gitignore
  .npmignore
  .travis.yml
  Gruntfile.js
  LICENSE
  MediaStreamRecorder.js
  README.md
  bower.json
  npm-test.js
  package.json
  server.js
MultiRTC/  (40 files)
  MultiRTC-firebase/  (13 files)
    FileBufferReader.js
    README.md
    firebase.js
    index.html
    linkify.js
    package.json
    scrol-bars.css
    style.css
    ui.main.js
    ui.peer-connection.js
    ui.settings.js
    ui.share-files.js
    ui.users-list.js
  MultiRTC-socketio/  (13 files)
    public/  (10 files)
      … 10 files under this directory
    README.md
    package.json
    signaler.js
  MultiRTC-websocket/  (12 files)
    FileBufferReader.js
    README.md
    index.html
    linkify.js
    package.json
    scrol-bars.css
    style.css
    ui.main.js
    ui.peer-connection.js
    ui.settings.js
    ui.share-files.js
    ui.users-list.js
  .gitignore
  README.md
MultiStreamsMixer/  (29 files)
  dev/  (16 files)
    README.md
    amd.js
    append-streams.js
    cross-browser-declarations.js
    draw-videos-on-canvas.js
    get-mixed-audio-stream.js
    get-mixed-stream.js
    get-mixed-video-stream.js
    get-video-element.js
    head.js
    init.js
    module.exports.js
    release-streams.js
    replace-streams.js
    start-drawing-frames.js
    tail.js
  .gitignore
  .npmignore
  .travis.yml
  Gruntfile.js
  LICENSE
  MultiStreamsMixer.js
  MultiStreamsMixer.ts
  README.md
  bower.json
  index.html
  npm-test.js
  package.json
  server.js
PluginRTC/  (3 files)
  Plugin.EveryWhere.js
  Plugin.Temasys.js
  README.md
Pluginfree-Screen-Sharing/  (3 files)
  README.md
  conference.js
  index.html
Pre-recorded-Media-Streaming/  (6 files)
  MediaStreamer.js
  README.md
  index-2.html
  index-old.html
  index.html
  streamer.js
RTCMultiConnection/  (96 files)
  admin/  (2 files)
    admin-ui.js
    index.html
  demos/  (34 files)
    SSEConnection/  (8 files)
      … 8 files under this directory
    dashboard/  (4 files)
      … 4 files under this directory
    video-conference/  (2 files)
      … 2 files under this directory
    Audio-Conferencing.html
    Call-By-UserName.html
    One-to-One.html
    README.md
    SSEConnection.html
    Scalable-Broadcast.html
    Video-Conferencing.html
    camera-zoom.html
    file-sharing.html
    getStats.html
    index.html
    menu.js
    screen-sharing.html
    stylesheet.css
    text-chat-file-sharing.html
    translate-text-chat.html
    video-and-screen-sharing.html
    video-broadcasting.html
    video-conferencing-chat-filesharing.html
    vuejs-video-conferencing.html
  dev/  (38 files)
    BandwidthHandler.js
    BluetoothConnection.js
    CodecsHandler.js
    FileProgressBarHandler.js
    FileSelector.js
    FirebaseConnection.js
    IceServersHandler.js
    MediaStreamRecorder.js
    MultiPeersHandler.js
    MultiStreamsMixer.js
    OnIceCandidateHandler.js
    Plugin.EveryWhere.js
    PubNubConnection.js
    README.md
    RTCMultiConnection.js
    RTCPeerConnection.js
    RecordingHandler.js
    SSEConnection.js
    SignalRConnection.js
    SipConnection.js
    SocketConnection.js
    StreamHasData.js
    StreamsHandler.js
    TextSenderReceiver.js
    … 14 more files
  docs/  (8 files)
    README.md
    api.md
    getting-started.md
    how-to-use.md
    installation-guide.md
    ios-android.md
    tips-tricks.md
    upgrade.md
  .gitignore
  .jshintrc
  .npmignore
  .travis.yml
  CONTRIBUTING.md
  Gruntfile.js
  LICENSE.md
  README.md
  bower.json
  config.json
  logs.json
  npm-test.js
  package.json
  server.js
RTCMultiConnection-Server/  (9 files)
  .gitignore
  .npmignore
  LICENSE
  README.md
  bower.json
  config.json
  logs.json
  package.json
  server.js
RTCMultiConnection-SignalR/  (16 files)
  RTCMultiConnection/  (12 files)
    Properties/  (1 files)
      … 1 files under this directory
    Scripts/  (2 files)
      … 2 files under this directory
    RTCMultiConnection.csproj
    RTCMultiConnectionHub.cs
    RTCMultiConnectionSignaling.cs
    SignalRConnection.js
    Web.Debug.config
    Web.Release.config
    Web.config
    index.html
    packages.config
  packages/  (1 files)
    README.md
  LICENSE
  README.md
  RTCMultiConnection.sln
RTCPeerConnection/  (9 files)
  README.md
  RTCPeerConnection-Helpers.js
  RTCPeerConnection-v1.1.js
  RTCPeerConnection-v1.2.js
  RTCPeerConnection-v1.3.js
  RTCPeerConnection-v1.4.js
  RTCPeerConnection-v1.5.js
  RTCPeerConnection-v1.6.js
  RTCPeerConnection.js
RTCall/  (3 files)
  README.md
  RTCall.js
  index.html
Record-Entire-Meeting/  (12 files)
  uploads/  (1 files)
    README.md
  .gitignore
  .npmignore
  Browser-Recording-Helper.js
  Concatenate-Recordings.js
  MediaStreamRecorder.js
  Nodejs-Recording-Handler.js
  README.md
  Write-Recordings-To-Disk.js
  index.html
  package.json
  server.js
RecordRTC/  (147 files)
  Canvas-Recording/  (9 files)
    Canvas-Animation-Recording-Plus-Microphone-Plus-Mp3.html
    Canvas-Animation-Recording-Plus-Microphone.html
    Canvas-Animation-Recording-Plus-Mp3.html
    Canvas-Animation-Recording.html
    README.md
    canvas-designer.js
    index.html
    record-canvas-drawings.html
    webpage-recording.html
  MRecordRTC/  (2 files)
    README.md
    index.html
  PHP-and-FFmpeg/  (5 files)
    uploads/  (1 files)
      … 1 files under this directory
    .htaccess
    README.md
    index.html
    save.php
  RecordRTC-over-Socketio/  (7 files)
    ffmpeg-output/  (1 files)
      … 1 files under this directory
    uploads/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    server.js
  RecordRTC-to-ASPNETMVC/  (16 files)
    RecordRTC_to_ASPNETMVC/  (14 files)
      … 14 files under this directory
    README.md
    RecordRTC_to_ASPNETMVC.sln
  RecordRTC-to-Nodejs/  (5 files)
    .gitignore
    README.md
    index.html
    package.json
    server.js
  RecordRTC-to-PHP/  (6 files)
    uploads/  (1 files)
      … 1 files under this directory
    .htaccess
    README.md
    delete.php
    index.html
    save.php
  WebGL-Recording/  (8 files)
    assets/  (2 files)
      … 2 files under this directory
    README.md
    index.html
    logic.js
    plotly.html
    style.css
    view.js
  dev/  (21 files)
    CanvasRecorder.js
    Cross-Browser-Declarations.js
    DiskStorage.js
    GetRecorderType.js
    GifRecorder.js
    MRecordRTC.js
    MediaStreamRecorder.js
    MultiStreamRecorder.js
    MultiStreamsMixer.js
    README.md
    RecordRTC-Configuration.js
    RecordRTC.IndexedDB.js
    RecordRTC.js
    RecordRTC.promises.js
    StereoAudioRecorder.js
    Storage.js
    WebAssemblyRecorder.js
    Whammy.js
    WhammyRecorder.js
    amd.js
    isMediaRecorderCompatible.js
  libs/  (3 files)
    gif-recorder.js
    webm-wasm.js
    webm-worker.js
  simple-demos/  (38 files)
    16khz-audio-recording.html
    README.md
    Record-Mp3-or-Wav.html
    RecordRTCPromisesHandler.html
    RecordRTC_Extension.html
    WebAssemblyRecorder.html
    audio-recording.html
    auto-stop-on-silence.html
    bitsPerSecond.html
    calculate-recording-duration.html
    destroy.html
    edge-audio-recording.html
    embedded-iframes.html
    gif-recording.html
    index.html
    isTypeSupported.html
    multi-audios-recording.html
    multi-cameras-recording.html
    onStateChanged.html
    onTimeStamp.html
    ondataavailable-StereoAudioRecorder.html
    ondataavailable.html
    pass-getUserMedia-constraints.html
    php-upload-jquery.html
    … 14 more files
  test/  (13 files)
    html-test-files/  (6 files)
      … 6 files under this directory
    README.md
    audio-recording-using-StereoAudioRecorder.js
    audio-recording.js
    browserstack.config.js
    canvas-recording.js
    video-recording-using-WhammyRecorder.js
    video-recording.js
  .gitignore
  .jshintrc
  .npmignore
  .travis.yml
  CONTRIBUTING.md
  Gruntfile.js
  LICENSE
  README.md
  RecordRTC.js
  bower.json
  index.html
  npm-test.js
  package.json
  server.js
Reliable-Signaler/  (22 files)
  datachannel-client/  (5 files)
    README.md
    index.html
    package.json
    server.js
    style.css
  rtcmulticonnection-client/  (5 files)
    README.md
    index.html
    package.json
    server.js
    style.css
  videoconferencing-client/  (7 files)
    README.md
    RTCPeerConnection-v1.5.js
    conference.js
    index.html
    package.json
    server.js
    style.css
  README.md
  index.js
  package.json
  reliable-signaler.js
  signaler.js
Translator.js/  (3 files)
  README.md
  Translator.js
  index.html
WebRTC-File-Sharing/  (4 files)
  File.js
  PeerConnection.js
  README.md
  index.html
WebRTC-Scalable-Broadcast/  (8 files)
  .gitignore
  .npmignore
  README.md
  WebRTC-Scalable-Broadcast.js
  index.html
  package.json
  server.js
  share-files.html
audio-broadcast/  (4 files)
  README.md
  broadcast-ui.js
  broadcast.js
  index.html
broadcast/  (4 files)
  README.md
  broadcast-ui.js
  broadcast.js
  index.html
chat-hangout/  (4 files)
  README.md
  hangout-ui.js
  hangout.js
  index.html
demos/  (10 files)
  MediaStreamTrack.getSources.html
  README.md
  audio-only-streaming.html
  client-side-datachannel.html
  client-side-socket-io.html
  client-side-websocket.html
  client-side.html
  remote-stream-recording.html
  screen-and-video-from-single-peer.html
  switch-streams.html
desktop-sharing/  (3 files)
  README.md
  index.html
  old.html
docs/  (15 files)
  How-to-Broadcast-Screen-using-WebRTC.html
  README.md
  RTP-usage.html
  STUN-or-TURN.html
  Share-Files-using-Filejs.html
  TURN-server-installation-guide.html
  WebRTC-PeerConnection.html
  WebRTC-Signaling-Concepts.html
  echo-cancellation.html
  how-file-broadcast-works.html
  how-to-WebRTC-video-conferencing.html
  how-to-broadcast-video-using-RTCWeb-APIs.html
  how-to-install-tabCapture-extension.html
  how-to-share-audio-only-streams.html
  how-to-switch-streams.html
.gitignore
LICENSE
README.md
Signaling.md
```

## Entry points

- [Canvas-Designer/server.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/Canvas-Designer/server.js)
- [ConcatenateBlobs/ConcatenateBlobs.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/ConcatenateBlobs/ConcatenateBlobs.js)
- [Conversation.js/conversation.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/Conversation.js/conversation.js)
- [DataChannel/DataChannel.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/DataChannel/DataChannel.js)
- [DetectRTC/DetectRTC.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/DetectRTC/DetectRTC.js)
- [FileBufferReader/fbr-client/server.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/FileBufferReader/fbr-client/server.js)
- [FileBufferReader/FileBufferReader.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/FileBufferReader/FileBufferReader.js)
- [Firefox-Extensions/enable-screen-capturing-old2/index.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/Firefox-Extensions/enable-screen-capturing-old2/index.js)
- [Firefox-Extensions/enable-screen-capturing/index.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/Firefox-Extensions/enable-screen-capturing/index.js)
- [MediaStreamRecorder/MediaStreamRecorder.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/MediaStreamRecorder/MediaStreamRecorder.js)
- [MultiRTC/MultiRTC-socketio/signaler.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/MultiRTC/MultiRTC-socketio/signaler.js)
- [MultiStreamsMixer/MultiStreamsMixer.js](https://github.com/muaz-khan/WebRTC-Experiment/blob/bbcdbc13b3d7864369f0d09a7c089277dec946da/MultiStreamsMixer/MultiStreamsMixer.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| audio-broadcast package | library | Observed | Groups 2 file(s) under audio-broadcast package (observed from repository paths and static analysis). |
| broadcast package | library | Observed | Groups 2 file(s) under broadcast package (observed from repository paths and static analysis). |
| Canvas-Designer package | library | Observed | Groups 28 file(s) under canvas-designer package (observed from repository paths and static analysis). |
| chat-hangout package | library | Observed | Groups 2 file(s) under chat-hangout package (observed from repository paths and static analysis). |
| Chrome-Extensions package | library | Observed | Groups 69 file(s) under chrome-extensions package (observed from repository paths and static analysis). |
| ConcatenateBlobs package | library | Observed | Groups 1 file(s) under concatenateblobs package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 55 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Conversation.js package | library | Observed | Groups 7 file(s) under conversation.js package (observed from repository paths and static analysis). |
| DataChannel package | library | Observed | Groups 18 file(s) under datachannel package (observed from repository paths and static analysis). |
| DetectRTC package | library | Observed | Groups 17 file(s) under detectrtc package (observed from repository paths and static analysis). |
| FileBufferReader package | library | Observed | Groups 18 file(s) under filebufferreader package (observed from repository paths and static analysis). |
| Firefox-Extensions package | library | Observed | Groups 6 file(s) under firefox-extensions package (observed from repository paths and static analysis). |
| MediaStreamRecorder package | library | Observed | Groups 25 file(s) under mediastreamrecorder package (observed from repository paths and static analysis). |
| MultiRTC package | library | Observed | Groups 23 file(s) under multirtc package (observed from repository paths and static analysis). |
| MultiStreamsMixer package | library | Observed | Groups 20 file(s) under multistreamsmixer package (observed from repository paths and static analysis). |
| Pluginfree-Screen-Sharing package | library | Observed | Groups 1 file(s) under pluginfree-screen-sharing package (observed from repository paths and static analysis). |
| PluginRTC package | library | Observed | Groups 2 file(s) under pluginrtc package (observed from repository paths and static analysis). |
| Pre-recorded-Media-Streaming package | library | Observed | Groups 2 file(s) under pre-recorded-media-streaming package (observed from repository paths and static analysis). |
| Record-Entire-Meeting package | library | Observed | Groups 6 file(s) under record-entire-meeting package (observed from repository paths and static analysis). |
| RecordRTC package | library | Observed | Groups 37 file(s) under recordrtc package (observed from repository paths and static analysis). |
| Reliable-Signaler package | library | Observed | Groups 8 file(s) under reliable-signaler package (observed from repository paths and static analysis). |
| RTCall package | library | Observed | Groups 1 file(s) under rtcall package (observed from repository paths and static analysis). |
| RTCMultiConnection package | library | Observed | Groups 47 file(s) under rtcmulticonnection package (observed from repository paths and static analysis). |
| RTCMultiConnection-Server package | library | Observed | Groups 1 file(s) under rtcmulticonnection-server package (observed from repository paths and static analysis). |
| RTCMultiConnection-SignalR package | library | Observed | Groups 6 file(s) under rtcmulticonnection-signalr package (observed from repository paths and static analysis). |
| RTCPeerConnection package | library | Observed | Groups 8 file(s) under rtcpeerconnection package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 25 file(s) under tests (observed from repository paths and static analysis). |
| Translator.js package | library | Observed | Groups 1 file(s) under translator.js package (observed from repository paths and static analysis). |
| WebRTC-File-Sharing package | library | Observed | Groups 2 file(s) under webrtc-file-sharing package (observed from repository paths and static analysis). |
| WebRTC-Scalable-Broadcast package | library | Observed | Groups 2 file(s) under webrtc-scalable-broadcast package (observed from repository paths and static analysis). |

## Important files

- `Canvas-Designer/.travis.yml` (ci)
- `Canvas-Designer/bower.json` (config)
- `Canvas-Designer/package.json` (manifest)
- `Chrome-Extensions/desktopCapture-p2p/manifest.json` (config)
- `Chrome-Extensions/desktopCapture/different-api/manifest.json` (config)
- `Chrome-Extensions/desktopCapture/manifest.json` (config)
- `Chrome-Extensions/file-sharing/manifest.json` (config)
- `Chrome-Extensions/get-any-webrtc-peer-stream/manifest.json` (config)
- `Chrome-Extensions/getUserMedia-on-http/manifest.json` (config)
- `Chrome-Extensions/screen-recording/manifest.json` (config)
- `Chrome-Extensions/tabCapture/manifest.json` (config)
- `ConcatenateBlobs/package.json` (manifest)
- `Conversation.js/AndroidRTC/manifest.json` (config)
- `Conversation.js/package.json` (manifest)
- `DataChannel/.travis.yml` (ci)
- `DataChannel/bower.json` (config)
- `DataChannel/package.json` (manifest)
- `DetectRTC/.travis.yml` (ci)
- `DetectRTC/bower.json` (config)
- `DetectRTC/package.json` (manifest)
- `FileBufferReader/.travis.yml` (ci)
- `FileBufferReader/bower.json` (config)
- `FileBufferReader/fbr-client/package.json` (manifest)
- `FileBufferReader/package.json` (manifest)
- `Firefox-Extensions/enable-screen-capturing-old2/package.json` (manifest)
- `Firefox-Extensions/enable-screen-capturing/package.json` (manifest)
- `MediaStreamRecorder/.travis.yml` (ci)
- `MediaStreamRecorder/bower.json` (config)
- `MediaStreamRecorder/package.json` (manifest)
- `MultiRTC/MultiRTC-firebase/package.json` (manifest)
- `MultiRTC/MultiRTC-socketio/package.json` (manifest)
- `MultiRTC/MultiRTC-websocket/package.json` (manifest)
- `MultiStreamsMixer/.travis.yml` (ci)
- `MultiStreamsMixer/bower.json` (config)
- `MultiStreamsMixer/package.json` (manifest)
- `RTCMultiConnection-Server/bower.json` (config)
- `RTCMultiConnection-Server/config.json` (config)
- `RTCMultiConnection-Server/logs.json` (config)
- `RTCMultiConnection-Server/package.json` (manifest)
- `RTCMultiConnection/.travis.yml` (ci)
- `RTCMultiConnection/bower.json` (config)
- `RTCMultiConnection/config.json` (config)
- `RTCMultiConnection/logs.json` (config)
- `RTCMultiConnection/package.json` (manifest)
- `Record-Entire-Meeting/package.json` (manifest)
- `RecordRTC/.travis.yml` (ci)
- `RecordRTC/RecordRTC-over-Socketio/package.json` (manifest)
- `RecordRTC/RecordRTC-to-Nodejs/package.json` (manifest)
- `RecordRTC/bower.json` (config)
- `RecordRTC/package.json` (manifest)
- `Reliable-Signaler/datachannel-client/package.json` (manifest)
- `Reliable-Signaler/package.json` (manifest)
- `Reliable-Signaler/rtcmulticonnection-client/package.json` (manifest)
- `Reliable-Signaler/videoconferencing-client/package.json` (manifest)
- `WebRTC-Scalable-Broadcast/package.json` (manifest)

## Top-level layout

- `RecordRTC` — 147 analysed file(s)
- `Chrome-Extensions` — 107 analysed file(s)
- `RTCMultiConnection` — 96 analysed file(s)
- `MediaStreamRecorder` — 46 analysed file(s)
- `Canvas-Designer` — 40 analysed file(s)
- `MultiRTC` — 40 analysed file(s)
- `DetectRTC` — 37 analysed file(s)
- `FileBufferReader` — 34 analysed file(s)
- `MultiStreamsMixer` — 29 analysed file(s)
- `DataChannel` — 28 analysed file(s)
- `Reliable-Signaler` — 22 analysed file(s)
- `RTCMultiConnection-SignalR` — 16 analysed file(s)
- `Conversation.js` — 15 analysed file(s)
- `Firefox-Extensions` — 15 analysed file(s)
- `docs` — 15 analysed file(s)
- `Record-Entire-Meeting` — 12 analysed file(s)
- `demos` — 10 analysed file(s)
- `RTCMultiConnection-Server` — 9 analysed file(s)
- `RTCPeerConnection` — 9 analysed file(s)
- `WebRTC-Scalable-Broadcast` — 8 analysed file(s)
- `Pre-recorded-Media-Streaming` — 6 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `ConcatenateBlobs` — 4 analysed file(s)
- `WebRTC-File-Sharing` — 4 analysed file(s)
- `audio-broadcast` — 4 analysed file(s)
- `broadcast` — 4 analysed file(s)
- `chat-hangout` — 4 analysed file(s)
- `PluginRTC` — 3 analysed file(s)
- `Pluginfree-Screen-Sharing` — 3 analysed file(s)
- `RTCall` — 3 analysed file(s)
- `Translator.js` — 3 analysed file(s)
- `desktop-sharing` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 20 file(s) were skipped during inventory (2 x generated/minified file excluded; 10 x likely secret file excluded; 2 x lockfile excluded; 6 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bbcdbc13b3d7864369f0d09a7c089277dec946da` is the revision these paths and observations refer to.
