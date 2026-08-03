from __future__ import annotations

from playwright.sync_api import Page, expect


class IssuePilotPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")

    def open(self) -> None:
        self.page.goto(self.base_url)
        expect(self.page.get_by_role("heading", name="IssuePilot")).to_be_visible()

    def create_issue(self, title: str, description: str, priority: str) -> None:
        self.page.get_by_label("Title").fill(title)
        self.page.get_by_label("Description").fill(description)
        self.page.get_by_label("Priority").select_option(priority)
        self.page.get_by_role("button", name="Create issue").click()
        expect(self.page.get_by_text("Issue created.")).to_be_visible()

    def issue_card(self, title: str):
        return self.page.locator(".issue-card", has=self.page.get_by_role("heading", name=title))

    def change_status(self, title: str, status: str) -> None:
        card = self.issue_card(title)
        card.get_by_label("Change issue status").select_option(status)
        expect(card.get_by_label("Change issue status")).to_have_value(status)

    def search(self, text: str) -> None:
        self.page.get_by_label("Search issues").fill(text)

    def delete_issue(self, title: str) -> None:
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.issue_card(title).get_by_role("button", name="Delete").click()
        expect(self.page.get_by_role("heading", name=title)).not_to_be_visible()
