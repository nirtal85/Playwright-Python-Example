# 🎭 Playwright Python Example 🎭

![twitter](https://img.shields.io/twitter/follow/NirTal2)
![YouTube Channel](https://img.shields.io/youtube/channel/subscribers/UCQjS-eoKl0a1nuP_dvpLsjQ?label=YouTube%20Channel)
![dev run](https://github.com/nirtal85/Playwright-Python-Example/actions/workflows/devRun.yml/badge.svg)
![nightly](https://github.com/nirtal85/Playwright-Python-Example/actions/workflows/nightly.yml/badge.svg)
[![uv](https://img.shields.iodpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.iodpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

<p align="center">
  <a href="https://automation.co.il/%d7%a7%d7%95%d7%a8%d7%a1-%d7%90%d7%95%d7%98%d7%95%d7%9e%d7%a6%d7%99%d7%94-%d7%a4%d7%99%d7%99%d7%aa%d7%95%d7%9f-python-automation/">
    <img src="resources/images/automation_college_playwright_course.jpeg" alt="Automation College - Playwright Python Course" />
  </a>
</p>

## 📃 Articles written about this project

* [Test Automation - How To Use Custom User Agent in Selenium Python or Playwright Python to Avoid Security Bots](https://www.test-shift.com/posts/test-automation-how-to-use-custom-user-agent-in-selenium-python-or-playwright-python-to-avoid-security-bots)
* [Test Automation - How to Use Dynamic Base URLs with Selenium And Playwright Python in GitHub Actions](https://www.test-shift.com/posts/test-automation-how-to-use-dynamic-base-urls-with-selenium-and-playwright-python-in-github-actions)
* [Test Automation - Maximizing Browser Window With Playwright Python And Pytest](https://www.test-shift.com/posts/test-automation-maximizing-browser-window-with-playwright-python-and-pytest)
* [Test Automation - How to Bypass Re-Login With Playwright Python And Pytest](https://www.test-shift.com/posts/test-automation-how-to-bypass-re-login-with-playwright-python-and-pytest)
* [Test Automation - How To Perform Automated Accessibility Checks Using Playwright Python And Axe](https://www.test-shift.com/posts/test-automation-how-to-perform-automated-accessibility-checks-using-playwright-python-and-axe)
* [Test Automation - How To Link Playwright Traces and Videos to Allure Report using GitHub Actions](https://www.test-shift.com/posts/test-automation-how-to-link-playwright-traces-and-videos-to-allure-report-using-github-actions)
* [Test Automation - Speeding Up Testing with Playwright Python using Local Storage](https://www.test-shift.com/posts/test-automation-speeding-up-testing-with-playwright-python-using-local-storage)
* [Test Automation - Efficient Element Selection with Playwright Python using Test IDs](https://www.test-shift.com/posts/test-automation-efficient-element-selection-with-playwright-python-using-test-ids)
* [Test Automation - Flexible Test Execution with Playwright Python and GitHub Actions](https://www.test-shift.com/posts/test-automation-flexible-test-execution-with-playwright-python-and-github-actions)
* [Test Automation - Accelerating Playwright Python Tests with Parallel Execution in GitHub Actions](https://www.test-shift.com/posts/test-automation-accelerating-playwright-python-tests-with-parallel-execution-in-github-actions)
* [Test Automation - How to Sync Playwright Versions Between Python and GitHub Actions](https://www.test-shift.com/posts/test-automation-how-to-sync-playwright-versions-between-python-and-github-actions)
* [From Open Source to Industry Sponsorship: The TestShift Journey with BrowserStack](https://www.test-shift.com/posts/from-open-source-to-enterprise-sponsorship-the-testshift-journey-with-browserstack)

## 🛠️ Tech Stack

| Tool                                                                     | Description                                                                                         |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [allure-pytest](https://pypi.org/project/allure-pytest/)                 | Allure reporting with your Pytest tests for better reporting                                        |
| [axe-playwright-python](https://pypi.org/project/axe-playwright-python/) | Python library for running accessibility checks with Playwright                                     |
| [playwright](https://pypi.org/project/playwright/)                       | Python library to automate the Chromium, WebKit, and Firefox browsers through a single API.         |
| [pytest](https://pypi.org/project/pytest/)                               | Popular testing framework for Python                                                                |
| [pytest-base-url](https://pypi.org/project/pytest-base-url/)             | Pytest plugin for setting a base URL for your tests                                                 |
| [pytest-playwright](https://pypi.org/project/pytest-playwright/)         | Pytest plugin for Playwright integration for browser automation testing                             |
| [pytest-split](https://pypi.org/project/pytest-split/)                   | Pytest plugin which splits the test suite to equally sized sub suites based on test execution time. |
| [requests](https://pypi.org/project/requests/)                           | Versatile library for making HTTP requests in Python                                                |

## 🌐 Browser Testing

This project is tested with [BrowserStack](https://www.browserstack.com), enabling cross-browser and mobile testing on real devices in the cloud.

## ⚙️ Setup Instructions

### Clone the project

```bash
git clone https://github.com/nirtal85/Playwright-Python-Example
cd playwright-python
```

### Create and activate a virtual environment then Install project dependencies

#### PowerShell installation in windows:
```bash
python -m uv venv
.venv\Scripts\Activate.ps1
python -m ensurepip --upgrade
python -m pip install uv
uv sync --all-extras --dev
```

#### For Mac:
```bash
python3 -m pip install uv
uv venv
source .venv/bin/activate
uv sync --all-extras --dev
```

### Install playwright

```bash
playwright install
```

## 🏃‍♂️ Running Tests

```bash
pytest
```

When no browser was selected then chrome will be used.

* Run according to tags:

```bash
pytest -m <tag_name>
```

## 📊 Viewing Test Results

### Install Allure Commandline To View Test results

#### For Windows:

Follow the instructions [here](https://scoop.sh/) to install Scoop.<br>
Run the following command to install Allure using Scoop:

```bash
scoop install allure
```

#### For Mac:

```bash
brew install allure
```

### View Results Locally:

```bash
allure serve allure-results
```

### View Results Online:

[View allure results via Github pages](https://nirtal85.github.io/Playwright-Python-Example/)

### View trace results:

1. Navigate to the [Playwright Trace Viewer](https://trace.playwright.dev/)
2. Locate the trace file stored under the test-results folder. This file is generated after running your tests. Click on the 'Upload' button in the Playwright Trace Viewer and select your trace file.
3. After uploading, the trace viewer will display a detailed timeline of events that occurred during your test. This includes network requests, JavaScript execution, and browser interactions. You can click on individual events for more details.

## ℹ️ View Help And Other CLI Options

```bash
pytest --help
```

### Pre Commit

#### Run Pre Commit Checks Automatically

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

#### Bump Pre Commit Hooks Version

```bash
pre-commit autoupdate
```

#### Run Pre Commit Checks Manually On The Entire Project

```bash
pre-commit run --all-files
```
## ☕ Support

If you find this project helpful, you can support my work by buying me a coffee:

<p><a href="https://www.buymeacoffee.com/nirtal">
<img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="Buy Me A Coffee" />
</a></p><br><br>
