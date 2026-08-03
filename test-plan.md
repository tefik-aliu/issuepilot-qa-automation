# IssuePilot Test Plan

## Scope

The suite covers the public IssuePilot REST API and the main browser workflows: application loading, issue creation, filtering, status change, deletion and empty-state behaviour.

## Test layers

1. **API contract tests** — fast validation of status codes, response bodies and CRUD behaviour.
2. **End-to-end browser tests** — user-visible behaviour in Chromium through a Page Object Model.
3. **CI smoke test** — clones and starts the production repository, waits for health, then runs the suite.

## Risks covered

- API unavailable or returning an incorrect health contract
- Issue validation accepting invalid titles
- Search failing to return the created record
- Status updates not being persisted
- Delete action leaving stale UI data
- Empty search state not being displayed

## Out of scope for this version

- Load/performance testing
- Accessibility audit beyond semantic locators
- Mobile browser matrix
- Authentication and authorization (planned for IssuePilot 2)
