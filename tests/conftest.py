from __future__ import annotations

import os
import uuid
from pathlib import Path

import pytest
from playwright.sync_api import Browser, Page, sync_playwright


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "http://127.0.0.1:8000")


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser: Browser, request) -> Page:
    context = browser.new_context(viewport={"width": 1440, "height": 1000})
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    results_dir = Path("test-results")
    results_dir.mkdir(exist_ok=True)
    failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    safe_name = request.node.nodeid.replace("/", "_").replace("::", "__")
    if failed:
        page.screenshot(path=results_dir / f"{safe_name}.png", full_page=True)
        context.tracing.stop(path=results_dir / f"{safe_name}.zip")
    else:
        context.tracing.stop()
    context.close()


@pytest.fixture()
def unique_title() -> str:
    return f"QA automation {uuid.uuid4().hex[:8]}"
