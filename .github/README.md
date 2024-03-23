# Playwright Python Example

![twitter](https://img.shields.io/twitter/follow/NirTal2)
![dev run](https://github.com/nirtal85/Playwright-Python-Example/actions/workflows/devRun.yml/badge.svg)
![nightly](https://github.com/nirtal85/Playwright-Python-Example/actions/workflows/nightly.yml/badge.svg)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Articles written about this project

* [Test Automation - How To Use Custom User Agent in Selenium Python or Playwright Python to Avoid Security Bots](https://www.linkedin.com/pulse/test-automation-how-use-custom-user-agent-selenium-python-nir-tal-lyqbf/)
* [Test Automation - How to Use Dynamic Base URLs with Selenium And Playwright Python in GitHub Actions](https://www.linkedin.com/pulse/test-automation-how-use-dynamic-base-urls-selenium-playwright-tal-klq5f/)

## Tech Stack

| Tool                                                             | Description                                                                                   |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [allure-pytest](https://pypi.org/project/allure-pytest/)         | Allure reporting with your Pytest tests for better reporting                                  |
| [playwright](https://pypi.org/project/playwright/)               | A Python library to automate the Chromium, WebKit, and Firefox browsers through a single API. |
| [pytest](https://pypi.org/project/pytest/)                       | A popular testing framework for Python                                                        |
| [pytest-base-url](https://pypi.org/project/pytest-base-url/)     | Pytest plugin for setting a base URL for your tests                                           |
| [pytest-playwright](https://pypi.org/project/pytest-playwright/) | Pytest plugin for Playwright integration for browser automation testing                       |
| [requests](https://pypi.org/project/requests/)                   | A versatile library for making HTTP requests in Python                                        |

## Setup Instructions

### Step 1: Clone the project

```bash
git clone https://github.com/nirtal85/Playwright-Python-Example
cd playwright-python
```

### Step 2: Create and activate a virtual environment

#### For Windows:
```bash
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```

#### For Mac:
```bash
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Poetry

```bash
pip install poetry
```

### Step 4: Install Project Dependencies

```bash
poetry install --no-root
```

### Step 5: Install playwright

```bash
playwright install
```

## Running Tests

```bash
pytest
```

When no browser was selected then chrome will be used.

* Run according to tags:

```bash
pytest -m <tag_name>
```

## Viewing Test Results

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

## View Help And Other CLI Options

```bash
pytest --help
```

### Pre Commit

#### Run Pre Commit Checks Automatically

```bash
pre-commit install
```

#### Bump Pre Commit Hooks Version

```bash
pre-commit autoupdate
```

#### Run Pre Commit Checks Manually On The Entire Project

```bash
pre-commit run --all-files
```
