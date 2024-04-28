import json

import allure
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page


class AxeHelper:

    def __init__(self, axe: Axe):
        self.axe = axe

    def accessibility(self, page: Page, maximum_allowed_violations: int = 0):
        """Checks accessibility of the page using axe-core.

        :param page: Playwright Page object
        :param maximum_allowed_violations: Maximum number of allowed
            violations (default: 0)
        """
        results = self.axe.run(page)
        violations_count = results.violations_count

        if violations_count > maximum_allowed_violations:
            allure.attach(
                body=json.dumps(results.response["violations"], indent=4),
                name="Accessibility Violation Results",
                attachment_type=allure.attachment_type.JSON,
            )
            assert violations_count < maximum_allowed_violations, (
                f"Found {violations_count} accessibility "
                f"violations, which exceeds the maximum allowed ("
                f"{maximum_allowed_violations})."
            )
