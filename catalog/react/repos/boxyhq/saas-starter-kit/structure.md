# Project structure: boxyhq/saas-starter-kit

**Analysed commit:** `abc9b686823cbfb4973c79bc36fea37a3244be6c`

**Commit reference:** [abc9b686823cbfb4973c79bc36fea37a3244be6c](https://github.com/boxyhq/saas-starter-kit/commit/abc9b686823cbfb4973c79bc36fea37a3244be6c)

**Tree at this commit:** [boxyhq/saas-starter-kit@abc9b686823c](https://github.com/boxyhq/saas-starter-kit/tree/abc9b686823cbfb4973c79bc36fea37a3244be6c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | boxyhq/saas-starter-kit |
| Description | 🔥 Enterprise SaaS Starter Kit - Kickstart your enterprise app development with the Next.js SaaS boilerplate 🚀 |
| Stars | 4976 |
| Forks | 1241 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `abc9b686823cbfb4973c79bc36fea37a3244be6c` |
| Retrieved at | 2026-11-14T19:14:32.832068+00:00 |
| Files in this snapshot | 322 |

## Directory tree

```text
.do/  (1 files)
  deploy.template.yaml
.github/  (2 files)
  workflows/  (1 files)
    main.yml
  dependabot.yml
__tests__/  (1 files)
  lib/  (1 files)
    server-common.spec.ts
components/  (97 files)
  account/  (8 files)
    ManageSessions.tsx
    UpdateAccount.tsx
    UpdateEmail.tsx
    UpdateName.tsx
    UpdatePassword.tsx
    UpdateTheme.tsx
    UploadAvatar.tsx
    index.ts
  apiKey/  (3 files)
    APIKeys.tsx
    APIKeysContainer.tsx
    NewAPIKey.tsx
  auth/  (8 files)
    AgreeMessage.tsx
    GithubButton.tsx
    GoogleButton.tsx
    Join.tsx
    JoinWithInvitation.tsx
    MagicLink.tsx
    ResetPassword.tsx
    index.ts
  billing/  (5 files)
    Help.tsx
    LinkToPortal.tsx
    PaymentButton.tsx
    ProductPricing.tsx
    Subscriptions.tsx
  defaultLanding/  (7 files)
    data/  (3 files)
      … 3 files under this directory
    FAQSection.tsx
    FeatureSection.tsx
    HeroSection.tsx
    PricingSection.tsx
  emailTemplates/  (8 files)
    AccountLocked.tsx
    EmailLayout.tsx
    MagicLink.tsx
    ResetPassword.tsx
    TeamInvite.tsx
    VerificationEmail.tsx
    WelcomeEmail.tsx
    index.ts
  invitation/  (9 files)
    AcceptInvitation.tsx
    EmailDomainMismatch.tsx
    EmailMismatch.tsx
    InviteMember.tsx
    InviteViaEmail.tsx
    InviteViaLink.tsx
    NotAuthenticated.tsx
    PendingInvitations.tsx
    index.ts
  layouts/  (3 files)
    AccountLayout.tsx
    AuthLayout.tsx
    index.ts
  shared/  (31 files)
    shell/  (9 files)
      … 9 files under this directory
    table/  (3 files)
      … 3 files under this directory
    AccessControl.tsx
    Alert.tsx
    Badge.tsx
    Card.tsx
    Checkbox.tsx
    ConfirmationDialog.tsx
    CopyToClipboardButton.tsx
    EmptyState.tsx
    Error.tsx
    GoogleReCAPTCHA.tsx
    InputWithCopyButton.tsx
    InputWithLabel.tsx
    LetterAvatar.tsx
    Loading.tsx
    Modal.tsx
    TeamDropdown.tsx
    TogglePasswordVisibility.tsx
    WithLoadingAndError.tsx
    index.ts
  team/  (8 files)
    CreateTeam.tsx
    Members.tsx
    RemoveTeam.tsx
    TeamSettings.tsx
    TeamTab.tsx
    Teams.tsx
    UpdateMemberRole.tsx
    index.ts
  webhook/  (6 files)
    CreateWebhook.tsx
    EditWebhook.tsx
    EventTypes.tsx
    Form.tsx
    Webhooks.tsx
    index.ts
  styles.ts
hooks/  (12 files)
  useAPIKeys.ts
  useCanAccess.ts
  useCustomSignout.ts
  useInvitation.ts
  useInvitations.ts
  usePermissions.ts
  useTeam.ts
  useTeamMembers.ts
  useTeams.ts
  useTheme.ts
  useWebhook.ts
  useWebhooks.ts
lib/  (46 files)
  email/  (8 files)
    freeEmailService.json
    sendEmail.ts
    sendMagicLink.ts
    sendPasswordResetEmail.ts
    sendTeamInviteEmail.ts
    sendVerificationEmail.ts
    sendWelcomeEmail.ts
    utils.ts
  guards/  (3 files)
    team-api-key.ts
    team-dsync.ts
    team-sso.ts
  jackson/  (10 files)
    dsync/  (4 files)
      … 4 files under this directory
    sso/  (4 files)
      … 4 files under this directory
    config.ts
    dsyncEvents.ts
  zod/  (3 files)
    index.ts
    primitives.ts
    schema.ts
  accountLock.ts
  app.ts
  auth.ts
  common.ts
  env.ts
  errors.ts
  fetcher.ts
  inferSSRProps.ts
  jackson.ts
  metrics.ts
  nextAuth.ts
  permissions.ts
  prisma.ts
  rbac.ts
  recaptcha.ts
  retraced.ts
  server-common.ts
  session.ts
  slack.ts
  stripe.ts
  svix.ts
  theme.ts
locales/  (1 files)
  en/  (1 files)
    common.json
models/  (12 files)
  account.ts
  apiKey.ts
  invitation.ts
  passwordReset.ts
  price.ts
  service.ts
  session.ts
  subscription.ts
  team.ts
  teamMember.ts
  user.ts
  verificationToken.ts
pages/  (75 files)
  api/  (42 files)
    auth/  (9 files)
      … 9 files under this directory
    invitations/  (1 files)
      … 1 files under this directory
    oauth/  (5 files)
      … 5 files under this directory
    scim/  (1 files)
      … 1 files under this directory
    sessions/  (2 files)
      … 2 files under this directory
    teams/  (15 files)
      … 15 files under this directory
    webhooks/  (2 files)
      … 2 files under this directory
    well-known/  (1 files)
      … 1 files under this directory
    health.ts
    hello.ts
    idp.ts
    import-hack.ts
    password.ts
    users.ts
  auth/  (12 files)
    reset-password/  (1 files)
      … 1 files under this directory
    sso/  (2 files)
      … 2 files under this directory
    forgot-password.tsx
    idp-login.tsx
    join.tsx
    login.tsx
    magic-link.tsx
    resend-email-token.tsx
    unlock-account.tsx
    verify-email-token.tsx
    verify-email.tsx
  invitations/  (1 files)
    [token].tsx
  settings/  (2 files)
    account.tsx
    security.tsx
  teams/  (11 files)
    [slug]/  (9 files)
      … 9 files under this directory
    index.tsx
    switch.tsx
  well-known/  (1 files)
    saml-configuration.tsx
  404.tsx
  500.tsx
  _app.tsx
  _document.tsx
  dashboard.tsx
  index.tsx
prisma/  (14 files)
  migrations/  (12 files)
    20230625203909_init/  (1 files)
      … 1 files under this directory
    20230703084002_add_api_keys/  (1 files)
      … 1 files under this directory
    20230703084117_add_index_user/  (1 files)
      … 1 files under this directory
    20230720113226_make_password_optional/  (1 files)
      … 1 files under this directory
    20231109082527_add_account_lockout/  (1 files)
      … 1 files under this directory
    20240109041326_columns_for_invitation_link/  (1 files)
      … 1 files under this directory
    20240212105842_stripe/  (1 files)
      … 1 files under this directory
    20240213160517_indices/  (1 files)
      … 1 files under this directory
    20240226091046_add_jackson_schema/  (1 files)
      … 1 files under this directory
    20240316224800_add_index_billing_id/  (1 files)
      … 1 files under this directory
    20240531124127_expand_jackson_namespace_column/  (1 files)
      … 1 files under this directory
    migration_lock.toml
  schema.prisma
  seed.ts
public/  (2 files)
  home-hero.svg
  vercel.svg
styles/  (2 files)
  globals.css
  sdk-override.module.css
tests/  (22 files)
  e2e/  (22 files)
    auth/  (2 files)
      … 2 files under this directory
    session/  (1 files)
      … 1 files under this directory
    settings/  (4 files)
      … 4 files under this directory
    support/  (15 files)
      … 15 files under this directory
types/  (4 files)
  base.ts
  index.ts
  next-auth.d.ts
  next.ts
.env.example
.gitignore
.prettierignore
.prettierrc.js
.release-it.json
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
Procfile
README.md
app.json
check-locale.js
delete-team.js
docker-compose.yml
eslint.config.cjs
find-dupe-locale.js
i18next.d.ts
instrumentation.ts
jest.config.js
jest.setup.js
middleware.ts
next-env.d.ts
next-i18next.config.js
next.config.js
… 7 more files
```

## Entry points

- [components/account/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/components/account/index.ts)
- [components/auth/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/components/auth/index.ts)
- [components/emailTemplates/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/components/emailTemplates/index.ts)
- [components/invitation/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/components/invitation/index.ts)
- [components/layouts/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/components/layouts/index.ts)
- [components/shared/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/components/shared/index.ts)
- [components/team/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/components/team/index.ts)
- [components/webhook/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/components/webhook/index.ts)
- [lib/app.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/lib/app.ts)
- [lib/jackson/dsync/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/lib/jackson/dsync/index.ts)
- [lib/jackson/sso/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/lib/jackson/sso/index.ts)
- [lib/zod/index.ts](https://github.com/boxyhq/saas-starter-kit/blob/abc9b686823cbfb4973c79bc36fea37a3244be6c/lib/zod/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 42 file(s) under api layer (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 94 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 17 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 12 file(s) under data layer (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 12 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 45 file(s) under lib package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 31 file(s) under pages package (observed from repository paths and static analysis). |
| prisma package | library | Observed | Groups 1 file(s) under prisma package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 23 file(s) under __tests__ package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 4 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.do/deploy.template.yaml` (config)
- `.env.example` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.release-it.json` (config)
- `app.json` (config)
- `components/defaultLanding/data/faq.json` (config)
- `components/defaultLanding/data/features.json` (config)
- `components/defaultLanding/data/pricing.json` (config)
- `docker-compose.yml` (container)
- `lib/email/freeEmailService.json` (config)
- `locales/en/common.json` (config)
- `package.json` (manifest)
- `prisma/migrations/migration_lock.toml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `components` — 97 analysed file(s)
- `pages` — 75 analysed file(s)
- `lib` — 46 analysed file(s)
- `(root files)` — 31 analysed file(s)
- `tests` — 22 analysed file(s)
- `prisma` — 14 analysed file(s)
- `hooks` — 12 analysed file(s)
- `models` — 12 analysed file(s)
- `types` — 4 analysed file(s)
- `.github` — 2 analysed file(s)
- `public` — 2 analysed file(s)
- `styles` — 2 analysed file(s)
- `.do` — 1 analysed file(s)
- `__tests__` — 1 analysed file(s)
- `locales` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `abc9b686823cbfb4973c79bc36fea37a3244be6c` is the revision these paths and observations refer to.
