import json

import allure
import pytest
import requests
from playwright.sync_api import Page

from utils.config_parser import ConfigParserIni
from utils.constants import Constants


@pytest.fixture(scope="session")
# instantiates ini file parses object
def prep_properties():
    return ConfigParserIni("props.ini")


@pytest.fixture(scope="function", autouse=True)
# navigate to base URL
def goto(page: Page):
    page.goto("")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "user_agent": Constants.AUTOMATION_USER_AGENT,
    }


def get_public_ip() -> str:
    return requests.get(
        "http://checkip.amazonaws.com",
        timeout=40,
        headers={"User-Agent": Constants.AUTOMATION_USER_AGENT},
    ).text.rstrip()


@pytest.fixture(autouse=True)
# Performs tear down pages
def attach_playwright_results(page: Page, request):
    response_list = []
    page.on(
        "response",
        lambda response: response_list.extend(
            [response.all_headers(), response.status, response.url]
        ),
    )
    yield

    if request.node.rep_call.failed:
        allure.attach(
            json.dumps(response_list, indent=4),
            name="Response",
            attachment_type=allure.attachment_type.JSON,
        )
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
def pytest_runtest_makereport(item):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
