from playwright.sync_api import Page, expect

from pages.issuepilot_page import IssuePilotPage


def test_user_can_create_search_update_and_delete_issue(page: Page, base_url: str, unique_title: str):
    app = IssuePilotPage(page, base_url)
    app.open()
    app.create_issue(unique_title, "Created by Playwright", "critical")

    card = app.issue_card(unique_title)
    expect(card).to_be_visible()
    expect(card.locator(".priority-pill")).to_have_text("critical")

    app.change_status(unique_title, "in_progress")
    app.search(unique_title)
    expect(app.issue_card(unique_title)).to_be_visible()
    app.delete_issue(unique_title)


def test_empty_search_state(page: Page, base_url: str):
    app = IssuePilotPage(page, base_url)
    app.open()
    app.search("definitely-not-a-real-issue-123")
    expect(page.get_by_text("No issues match the current filters.")).to_be_visible()
