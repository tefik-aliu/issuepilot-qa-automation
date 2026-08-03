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
