import allure
import pytest

from utils.config_parser import ConfigParserIni


@pytest.fixture(scope="session")
# instantiates ini file parses object
def prep_properties():
    return ConfigParserIni("props.ini")


@pytest.fixture(scope="function", autouse=True)
# instantiates ini file parses object
def prep_properties(page):
    page.goto("")


@pytest.fixture(autouse=True)
# Performs setup and tear down
def attach_playwright_results(page, prep_properties, request):
    yield
    if request.node.rep_call.failed:
        allure.attach(page.screenshot(full_page=True), name="Screen shot on failure",
                      attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object

    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)
