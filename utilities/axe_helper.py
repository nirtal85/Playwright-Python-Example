import json
from typing import Dict

import allure
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page


class AxeHelper:

    def __init__(self, axe: Axe):
        self.axe = axe

    def check_accessibility(
        self, page: Page, maximum_allowed_violations_by_impact: Dict[str, int] = None
    ):
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
        violations_by_impact = {"minor": 0, "moderate": 0, "serious": 0, "critical": 0}

        for violation in results.response["violations"]:
            impact = violation["impact"]
            violations_by_impact[impact] += 1

        violation_details = json.dumps(results.response["violations"], indent=4)

        for impact_level, violation_count in violations_by_impact.items():
            if violation_count > maximum_allowed_violations_by_impact.get(
                impact_level, 0
            ):
                allure.attach(
                    body=violation_details,
                    name="Accessibility Violation Results",
                    attachment_type=allure.attachment_type.JSON,
                )
                assert (
                    violation_count
                    <= maximum_allowed_violations_by_impact[impact_level]
                ), (
                    f"Found {violation_count} {impact_level} accessibility violations, "
                    f"which exceeds the maximum allowed ({maximum_allowed_violations_by_impact[impact_level]})."
                )
