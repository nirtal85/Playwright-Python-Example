# BasePage for Playwright reusable actions

from playwright.sync_api import Page, expect


class BasePage:
    """
    BasePage provides common Playwright actions
    that can be reused across all Page Objects.
    """

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str) -> None:
        """Navigate to a given URL"""
        self.page.goto(url)

    def click(self, locator: str) -> None:
        """Click on a web element"""
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str) -> None:
        """Fill input field with value"""
        self.page.locator(locator).fill(value)

    def get_text(self, locator: str) -> str:
        """Return text of an element"""
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator: str) -> bool:
        """Check if element is visible"""
        return self.page.locator(locator).is_visible()

    def wait_for(self, locator: str) -> None:
        """Wait until element is visible"""
        self.page.locator(locator).wait_for()

    def assert_text(self, locator: str, expected_text: str) -> None:
        """Assert exact text of an element"""
        expect(self.page.locator(locator)).to_have_text(expected_text)