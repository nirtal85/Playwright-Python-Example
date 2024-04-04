from typing import Dict

import allure
import pytest
import requests
from _pytest.fixtures import FixtureRequest, SubRequest
from _pytest.nodes import Item
from playwright.sync_api import Page

from utilities.constants import Constants


@pytest.fixture(scope="function", autouse=True)
def goto(page: Page, request: SubRequest):
    """Fixture to navigate to the base URL based on the user.

    If the 'storage_state' is set in 'browser_context_args', it navigates to the inventory page,
    otherwise, it navigates to the login page.

    Args:
        page (Page): Playwright page object.
        request (SubRequest): Pytest request object to get the 'browser_context_args' fixture value.
            If 'browser_context_args' is set to a user parameter (e.g., 'standard_user'),
            the navigation is determined based on the user.

    Example:
        @pytest.mark.parametrize('browser_context_args', ["standard_user"], indirect=True)
    """
    if request.getfixturevalue("browser_context_args").get("storage_state"):
        page.goto("/inventory.html")
    else:
        page.goto("")


@pytest.fixture(scope="function")
def browser_context_args(
    browser_context_args: Dict, base_url: str, request: SubRequest
):
    """This fixture allows setting browser context arguments for Playwright.

    Args:
        browser_context_args (dict): Base browser context arguments.
        request (SubRequest): Pytest request object to get the 'browser_context_args' fixture value.
        base_url (str): The base URL for the application under test.
    Returns:
        dict: Updated browser context arguments.
    See Also:
        https://playwright.dev/python/docs/api/class-browser#browser-new-contex

    Returns:
        dict: Updated browser context arguments.
    """
    context_args = {
        **browser_context_args,
        "no_viewport": True,
        "user_agent": Constants.AUTOMATION_USER_AGENT,
    }

    if hasattr(request, "param"):
        context_args["storage_state"] = {
            "cookies": [
                {
                    "name": "session-username",
                    "value": request.param.value,
                    "url": base_url,
                }
            ]
        }
    return context_args


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: Dict):
    """Fixture to set browser launch arguments.

    Args:
        browser_type_launch_args (dict): Browser type launch arguments.

    Returns:
        dict: Updated browser type launch arguments.
    See Also:
        https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch
    """
    return {**browser_type_launch_args, "args": ["--start-maximized"]}


def get_public_ip() -> str:
    """Function to retrieve public IP address.

    Returns:
        str: Public IP address.
    """
    return requests.get(
        "http://checkip.amazonaws.com",
        timeout=40,
        headers={"User-Agent": Constants.AUTOMATION_USER_AGENT},
    ).text.rstrip()


@pytest.fixture(autouse=True)
def attach_playwright_results(page: Page, request: FixtureRequest):
    """Fixture to perform teardown actions and attach results to Allure report
    on failure.

    Args:
        page (Page): Playwright page object.
        request: Pytest request object.
    """
    yield
    if request.node.rep_call.failed:
        allure.attach(
            body=page.url,
            name="URL",
            attachment_type=allure.attachment_type.URI_LIST,
        )
        allure.attach(
            page.screenshot(full_page=True),
            name="Screen shot on failure",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            body=get_public_ip(),
            name="public ip address",
            attachment_type=allure.attachment_type.TEXT,
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item):
    """Hook implementation to generate test report for each test phase.

    Args:
        item: Pytest item object.

    Yields:
        Outcome of the test execution.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
