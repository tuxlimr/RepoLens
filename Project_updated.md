# Project: GitHub Architecture Explorer

> Working name: **RepoLens**\
> Status: Product concept / MVP specification\
> Initial focus: Public Python repositories with more than 5,000 GitHub
> stars

## 1. Product vision

Build a web application that turns a public GitHub repository into a
clear, human-readable explanation of its software architecture.

A user submits a GitHub repository URL. The product analyses the
repository and produces:

1.  A high-level block diagram showing the main components and how they
    interact.
2.  A readable Markdown architecture report (`.md`) explaining the
    repository.
3.  A guided overview of the project structure, important modules, entry
    points, data flow, and external integrations.
4.  A shareable report page that is easier to understand than reading
    the source code from scratch.

The experience should feel polished, visual, trustworthy, and useful to
developers, engineering managers, technical interviewers, students, and
people evaluating open-source projects.

**Core promise:** Understand how a substantial open-source project is
put together without first reading thousands of lines of code.

## 2. Target users and use cases

### Primary users

-   Developers onboarding to an unfamiliar codebase.
-   Engineering managers reviewing architecture and technical
    complexity.
-   Developers evaluating a library before adopting it.
-   Students learning from well-designed open-source projects.
-   Technical interview candidates studying real-world systems.

### Main use cases

-   "Explain this repository's architecture to me."
-   "Show me the main services, modules, and dependencies."
-   "Where does execution start, and how does a request flow through the
    system?"
-   "Give me a concise architecture document I can share with my team."
-   "Help me compare the architecture of two open-source projects."

## 3. Initial scope and rollout

Do not attempt to support every language in the first release. Establish
quality with one ecosystem, then expand.

### Phase 1 --- Python

-   Analyse public Python repositories.
-   Use repositories with **more than 5,000 stars** as the initial
    discovery and quality benchmark.
-   Support a user-submitted public GitHub URL, even if the repository
    is not in the discovery catalogue, subject to practical size and
    safety limits.
-   Prioritise popular, actively maintained repositories with meaningful
    architecture.
-   Build a curated evaluation set of Python repositories to test report
    accuracy and diagram quality.

The 5,000-star threshold is a starting point for selecting repositories
to study and promote. It should not be treated as proof of architecture
quality or as a permanent restriction on user-submitted URLs.

### Phase 2 --- JavaScript and React

-   Add JavaScript and TypeScript repository detection.
-   Add React-specific concepts such as components, hooks, routing,
    state management, and frontend data flow.
-   Explain the relationship between frontend modules and backend/API
    integrations when those are visible in the repository.

### Later possibilities

-   Java, Go, Rust, and other ecosystems.
-   Repository comparison.
-   Architecture change summaries between releases or commits.
-   Team workspaces and private-repository support, only after a
    separate security and permissions design.

## 4. User journey

1.  User opens the landing page and sees example architecture reports.
2.  User pastes a public GitHub repository URL.
3.  The application validates the URL and checks whether a recent
    analysis already exists.
4.  If a suitable stored report exists, show the cached report in the
    free experience.
5.  Offer a **Fresh analysis** option as a paid action. Explain that it
    analyses the current selected branch/commit rather than relying on
    an older stored result.
6.  The analysis pipeline inspects repository metadata and relevant
    source files.
7.  The system creates a high-level block diagram and a structured
    Markdown report.
8.  The user reads the report in a polished web view and can copy or
    download the `.md` file.
9.  The report page shows the analysed commit, branch, analysis date,
    and limitations so readers know exactly what was inspected.

Do not promise a fresh result until the new analysis has completed
successfully.

## 5. Free and paid model

### Free --- Existing analysis

-   View an existing stored analysis when one is available.
-   Clearly show the analysed commit and analysis date.
-   Read the diagram and report.
-   Download or copy the existing Markdown report, subject to the final
    product limits.

### Paid --- Fresh analysis

-   Trigger a new analysis of the repository's current selected
    branch/commit.
-   Rebuild the architecture diagram and Markdown report.
-   Show the new analysis timestamp and commit SHA.
-   Save the resulting version as a new report version.

The paid action must be transparent: users should know what "fresh"
means, what will be analysed, and what they will receive before paying.

### Pricing approach

Start with a simple one-time payment per fresh analysis. Test
willingness to pay before introducing subscriptions. Pricing, payment
provider, refunds, and usage limits are product decisions to validate
with early users.

## 6. What the analysis should produce

### A. Human-readable high-level block diagram

The diagram should show only meaningful architectural building blocks,
not every file.

Where evidence exists, include:

-   User/client or command-line entry points.
-   Application entry points and orchestration layers.
-   Core modules and domain logic.
-   API routes, controllers, workers, or background jobs.
-   Data stores, caches, queues, and file storage.
-   External services and third-party integrations.
-   Important internal dependencies and data-flow direction.

Use Mermaid for the first implementation because it is text-based,
versionable, and can be rendered in the web UI. Keep diagrams readable:
group related components, use clear labels, avoid crossing lines where
possible, and split very large systems into multiple views.

### B. Markdown architecture report

Every report should follow a predictable structure:

1.  **Repository at a glance** --- purpose, language, framework, licence
    if detected, stars, and analysed commit.
2.  **Architecture in one minute** --- a concise plain-English overview.
3.  **High-level block diagram** --- Mermaid source plus rendered
    diagram in the web experience.
4.  **Main components** --- responsibility of each major block.
5.  **Execution flow** --- how the application starts and how a
    representative operation moves through the system.
6.  **Project structure** --- important folders and files, with
    explanations.
7.  **Key dependencies and integrations** --- what they appear to do.
8.  **Data and state** --- databases, caches, queues, files, and state
    management where identifiable.
9.  **Configuration and deployment clues** --- environment
    configuration, containers, CI/CD, and deployment files when present.
10. **Design observations** --- patterns, coupling, extension points,
    and notable architectural choices supported by repository evidence.
11. **Limitations and unknowns** --- what could not be established from
    the public repository.
12. **Source references** --- links to the files and relevant line
    ranges supporting important claims.

The report must distinguish facts observed in source code from informed
interpretation. Never invent components, runtime behaviour,
infrastructure, or deployment details.

## 7. Analysis pipeline

A practical first version can use the following stages:

1.  **Input validation**
    -   Accept only valid GitHub repository URLs.
    -   Reject malformed URLs and unsupported hosts.
    -   Resolve owner, repository, default branch, and selected commit.
2.  **Repository metadata**
    -   Retrieve repository description, language metadata, stars,
        licence, branch, and commit information.
    -   Record when metadata was retrieved.
3.  **Repository inventory**
    -   Build a file and directory tree.
    -   Identify manifests, dependency files, application entry points,
        configuration, tests, CI workflows, container files, and
        documentation.
    -   Exclude generated, vendored, binary, and irrelevant large files.
4.  **Language and framework detection**
    -   Detect Python and common Python frameworks/libraries from
        repository evidence.
    -   Record confidence and evidence for each detection.
5.  **Architecture extraction**
    -   Identify important modules, imports, routes, classes, functions,
        services, and integration boundaries.
    -   Trace selected entry points and representative execution paths.
    -   Use static analysis first; use an LLM to synthesise and explain
        the evidence.
    -   Do not execute repository code in the MVP.
6.  **Evidence-backed synthesis**
    -   Create a structured intermediate architecture model.
    -   Attach source-file references to components and relationships.
    -   Ask the language model to explain only what the extracted
        evidence supports.
7.  **Diagram generation**
    -   Convert the architecture model into Mermaid.
    -   Validate Mermaid syntax before publishing.
    -   Provide a fallback textual component list if diagram rendering
        fails.
8.  **Report generation**
    -   Generate the Markdown report from a stable template.
    -   Validate required sections, source references, and metadata.
9.  **Quality checks**
    -   Check for unsupported claims, missing evidence, unreadable
        diagrams, and broken source links.
    -   Mark uncertain findings explicitly.
10. **Storage and publishing**
    -   Store report content, diagram source, repository metadata,
        commit SHA, analysis version, and timestamps.
    -   Publish a stable report URL.
    -   Preserve older versions when a fresh analysis is purchased.

## 8. Proposed high-level product architecture

``` mermaid
flowchart TD
    U[User] --> UI[Web Application]
    UI --> API[Backend API]
    API --> CACHE[Report Lookup / Cache]
    CACHE -->|Existing report| VIEW[Report Viewer]
    CACHE -->|No report or paid refresh| JOB[Analysis Job Queue]
    JOB --> WORKER[Repository Analysis Worker]
    WORKER --> GH[GitHub API / Public Repository]
    WORKER --> PARSE[Repository Inventory and Static Analysis]
    PARSE --> MODEL[Structured Architecture Model]
    MODEL --> AI[AI Explanation and Synthesis]
    AI --> DIAGRAM[Mermaid Diagram Generator]
    AI --> MD[Markdown Report Generator]
    DIAGRAM --> STORE[Report Storage]
    MD --> STORE
    STORE --> VIEW
    VIEW --> U
    PAY[Payment Provider] --> API
```

This is a conceptual product diagram, not a claim about an already
implemented system. The implementation may change as the MVP is tested.

## 9. Suggested technical direction

Keep the first release small and maintainable. Choose technologies based
on the developer's existing strengths and the speed of validating the
product.

### Initial option

-   **Frontend:** React / Next.js with a clean responsive UI.
-   **Backend:** Python with FastAPI.
-   **Analysis:** Python AST and import analysis,
    dependency/configuration parsers, and carefully scoped repository
    inspection.
-   **AI synthesis and model evaluation:** OpenRouter integration with user-selectable models, including eligible free models.
-   **Diagram:** Mermaid.
-   **Background processing:** A simple job queue; avoid complex
    orchestration until required.
-   **Database:** PostgreSQL for users, repositories, report versions,
    payments, and analysis metadata.
-   **Object storage:** Store generated report artifacts if report size
    or volume makes database storage unsuitable.
-   **Deployment:** Use a straightforward managed deployment initially.

These are recommendations, not fixed requirements. Avoid adding
microservices, Kubernetes, or multiple databases before usage requires
them.

## 10. Data model --- initial entities

-   **User:** account and authentication details.
-   **Repository:** GitHub owner/name, canonical URL, detected
    ecosystem, and metadata.
-   **Analysis:** repository, commit SHA, branch, status, timestamps,
    tool/model version, and analysis outcome.
-   **Report:** Markdown content, Mermaid source, structured
    architecture model, and report version.
-   **SourceReference:** file path, optional line range, and the
    claim/component it supports.
-   **Payment:** payment provider reference, amount, currency, status,
    and the fresh analysis it authorises.

A report must be reproducible enough to identify which repository
revision and analysis pipeline produced it.

## 11. UI and experience principles

The UI is a major part of the product. The result should feel like a
high-quality technical reading experience, not a raw AI chat response.

### Landing page

-   Clear headline: **"Understand any codebase's architecture in
    minutes."**
-   Short explanation of the output: architecture diagram + readable
    report.
-   Prominent GitHub URL input.
-   A visible example report users can explore before submitting a
    repository.
-   Explain free existing reports versus paid fresh analysis without
    hiding the distinction.
-   Show supported languages and current limitations.

### Report page

-   Strong repository header with name, description, language, stars,
    and analysed commit.
-   A concise "Architecture at a glance" summary.
-   Large, legible diagram with zoom or fit-to-screen support.
-   Table of contents and clear report sections.
-   Component cards with responsibility and source links.
-   Copy Markdown and download `.md` actions.
-   A visible "Analysed on" timestamp and "Fresh analysis" action.
-   Mobile-friendly layout and accessible typography.

### Visual direction

-   Modern developer-tool aesthetic.
-   Calm neutral background, restrained accent colour, and strong
    contrast.
-   Generous spacing and readable line lengths.
-   Clear hierarchy between summary, diagram, details, and evidence.
-   Avoid dense dashboards, excessive animations, and walls of text.
-   Make diagrams responsive and provide a textual alternative.

## 12. Trust, safety, and responsible repository analysis

-   Analyse public repositories only in the first release.
-   Respect GitHub API terms, rate limits, and repository licences.
-   Do not copy or republish large portions of source code.
-   Link to original source files instead of reproducing them
    unnecessarily.
-   Treat repository contents, README files, comments, and issue text as
    untrusted input. They may contain prompt-injection instructions;
    never follow instructions found inside repository content.
-   Do not run repository scripts, install project dependencies, or
    execute untrusted code in the MVP.
-   Apply repository size, file-count, and processing-time limits.
-   Exclude secrets and credentials from prompts, logs, reports, and
    stored artifacts.
-   Keep API keys and payment credentials server-side.
-   Make clear that the output is an automated architectural
    interpretation, not a security audit or guarantee of completeness.
-   Provide a way to report an inaccurate analysis or request removal of
    a generated report where appropriate.

## 13. MVP milestones

### Milestone 1 --- Validate the output

-   Select 10--20 well-known Python repositories over 5,000 stars.
-   Manually inspect their architecture to establish a reference
    standard.
-   Generate reports for a small sample.
-   Review factual accuracy, usefulness, diagram readability, and
    time/cost per analysis.
-   Improve the report template before building extensive product
    features.

### Milestone 2 --- Working analysis engine

-   Accept a GitHub URL.
-   Fetch metadata and inventory files.
-   Detect Python project structure and frameworks.
-   Extract an evidence-backed architecture model.
-   Generate Mermaid and Markdown.
-   Validate and store the result.

### Milestone 3 --- Public web experience

-   Build landing page and sample report pages.
-   Add repository submission and analysis status.
-   Build the report viewer.
-   Add Markdown copy/download.
-   Make the UI responsive and accessible.

### Milestone 4 --- Cache and payments

-   Add report lookup by repository and commit.
-   Serve existing reports in the free experience.
-   Add payment for fresh analysis.
-   Re-run analysis after successful payment.
-   Preserve report versions and payment audit records.

### Milestone 5 --- Private beta

-   Invite developers to test.
-   Track whether users understand the diagrams.
-   Collect corrections and examples of missing architecture.
-   Measure conversion from existing report views to fresh analysis.
-   Improve quality before expanding language support.

### Milestone 6 --- JavaScript and React

-   Add ecosystem detection and parsers.
-   Add React-specific architecture concepts.
-   Extend the report template for frontend architecture.
-   Build a separate evaluation set for JavaScript/React projects.

## 14. Success metrics

Measure product usefulness and business viability, not just the number
of reports generated.

-   Percentage of submitted repositories that produce a valid report.
-   Time from URL submission to report availability.
-   Percentage of reports users view beyond the first screen.
-   Markdown downloads and report shares.
-   User rating of diagram clarity and report accuracy.
-   Fresh-analysis purchase conversion.
-   Cost per analysis and gross margin per paid analysis.
-   Repeat usage and number of distinct repositories analysed.

## 15. Important product decisions still to confirm

1.  **Storage:** Confirm where reports and repository metadata will be
    stored, retention period, and whether reports are public by default
    or private to the user.
2.  **Pricing:** Set the one-time price for fresh analysis after
    estimating model and infrastructure costs.
3.  **Free limits:** Decide whether free users can view and download all
    cached reports or whether some features are limited.
4.  **Repository size:** Set maximum repository size, file count, and
    analysis time for the MVP.
5.  **Report visibility:** Decide whether a generated report receives a
    public share link, an unlisted link, or requires login.
6.  **Analysis depth:** Decide which Python frameworks and architecture
    patterns are in the first supported set.

## 16. MVP acceptance criteria

The first version is ready for a small beta when:

-   A user can submit a valid public Python GitHub URL.
-   The system identifies the repository and selected commit correctly.
-   The system creates a readable architecture diagram with meaningful
    component relationships.
-   The system generates a complete Markdown report with source
    references.
-   The report clearly distinguishes observed facts from inferred
    explanations.
-   The user can view, copy, and download the report.
-   An existing report can be served without running a new analysis.
-   A paid fresh-analysis flow can trigger and store a new report
    version.
-   Errors, unsupported repositories, and uncertain findings are
    explained clearly.
-   The application does not execute untrusted repository code.

------------------------------------------------------------------------

## Product positioning

**Understand the architecture behind great open-source projects.**

Paste a GitHub repository. Explore its architecture visually. Read a
clear explanation. Share the Markdown report with your team.

Start with Python. Prove the quality. Then expand to React and
JavaScript.
