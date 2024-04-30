import json
from collections import Counter
from typing import Dict

import allure
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page


class AxeHelper:

    def __init__(self, axe: Axe):
        self.axe = axe

    def check_accessibility(
        self, page: Page, maximum_allowed_violations_by_impact: Dict[str, int] = None
    ) -> None:
        """Checks accessibility of the page using playwright axe.

        :param page: Playwright Page object
        :param maximum_allowed_violations_by_impact: A dictionary
            specifying the maximum allowed violations for each impact
            level (e.g., {'minor': 2, 'moderate': 1, 'serious': 0,
            'critical': 0}). If None, no violations will be allowed for
            any impact level.
        """
        if maximum_allowed_violations_by_impact is None:
            maximum_allowed_violations_by_impact = {
                "minor": 0,
                "moderate": 0,
                "serious": 0,
                "critical": 0,
            }
        results = self.axe.run(page)
        violations_count = dict(
            Counter(
                [violation["impact"] for violation in results.response["violations"]]
            )
        )
        if violations_exceeded := {
            impact_level: violation_count
            for impact_level, violation_count in violations_count.items()
            if violation_count
            > maximum_allowed_violations_by_impact.get(impact_level, 0)
        }:
            allure.attach(
                body=json.dumps(results.response["violations"], indent=4),
                name="Accessibility Violation Results",
                attachment_type=allure.attachment_type.JSON,
            )
            assert not violations_exceeded, (
                f"Found accessibility violations exceeding the maximum allowed: "
                f"{violations_exceeded}"
            )
