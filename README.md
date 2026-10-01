# IssuePilot QA Automation

A separate automated quality-assurance suite for IssuePilot, built with Python, Pytest, HTTPX and Playwright.

## What it demonstrates

- API contract and CRUD testing
- Browser automation with semantic locators
- Page Object Model architecture
- Unique test data for repeatable runs
- Failure screenshots and Playwright traces
- CI that clones, starts and tests the real application
- Documented test strategy and bug-report format

## Run against a local instance

Start IssuePilot on port 8000, then:

```bash
python -m venv .venv
pip install -r requirements.txt
playwright install chromium
pytest
```

## Run against the public demo

```bash
# macOS/Linux
BASE_URL=https://issuepilot-tefik.onrender.com pytest

# PowerShell
$env:BASE_URL="https://issuepilot-tefik.onrender.com"
pytest
```

The free demo may need time to wake up. Local execution is faster and more deterministic.

## Files recruiters can inspect quickly

- `tests/test_api.py` — REST API coverage
- `tests/test_ui.py` — complete browser workflow
- `pages/issuepilot_page.py` — Page Object Model
- `test-plan.md` — risk-based test scope
- `.github/workflows/qa.yml` — end-to-end CI pipeline

## Author

**Tefik Aliu** — https://github.com/tefik-aliu

## Inspect the implementation

- [API contracts and persistence checks](tests/test_api.py)
- [Browser journeys](tests/test_ui.py)
- [Semantic page object](pages/issuepilot_page.py)
- [Fresh-application CI](.github/workflows/qa.yml)

## Rejected writes preserve state

The API suite verifies that an invalid update does not change a saved issue, checks empty PATCH handling and cleans up the regression fixture in a finally block. Set BROWSER_CHANNEL=msedge to use installed Edge locally; CI defaults to Chromium.

## Operational boundaries

The suite writes test data. Prefer a disposable local application. CI follows the default branch of IssuePilot, so its results test that current integration rather than a pinned release.
