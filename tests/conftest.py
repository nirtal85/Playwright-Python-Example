import json

import allure
import pytest

from utils.config_parser import ConfigParserIni


@pytest.fixture(scope="session")
# instantiates ini file parses object
def prep_properties():
    return ConfigParserIni("props.ini")


@pytest.fixture(scope="function", autouse=True)
# navigate to base URL
def goto(page):
    page.goto("")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }


@pytest.fixture(scope="function")
# Instantiates Page Objects
def elements(page):
    return dict(
        user_name_field=page.locator("[data-test='username']"),
        password_field=page.locator("[data-test='password']"),
        login_button=page.locator("[data-test='login-button']"),
        error_message=page.locator("[data-test='error']"),
    )


@pytest.fixture(autouse=True)
# Performs tear down pages
def attach_playwright_results(page, request):
    response_list = []
    page.on(
        "response",
        lambda response: response_list.extend(
            [response.all_headers(), response.status]
        ),
    )
    yield
    allure.attach(
        json.dumps(response_list),
        name="Response",
        attachment_type=allure.attachment_type.JSON,
    )
    if request.node.rep_call.failed:
        allure.attach(
            page.screenshot(full_page=True),
            name="Screen shot on failure",
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
