# Playwright Python Example

![Pre merge test](https://github.com/nirtal85/Playwright-Python-Example/actions/workflows/devRun.yml/badge.svg)

## Articles written about this project

* [Test Automation - How To Use Custom User Agent in Selenium Python or Playwright Python to Avoid Security Bots](https://www.linkedin.com/pulse/test-automation-how-use-custom-user-agent-selenium-python-nir-tal-lyqbf/)
* [Test Automation - How to Use Dynamic Base URLs with Selenium And Playwright Python in GitHub Actions](https://www.linkedin.com/pulse/test-automation-how-use-dynamic-base-urls-selenium-playwright-tal-klq5f/)

## Tech Stack

| Tool                                                             | Description                                                                                    |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [allure-pytest](https://pypi.org/project/allure-pytest/)         | Allure reporting with your Pytest tests for better reporting                                   |
| [playwright](https://pypi.org/project/playwright/)               | A Node.js library to automate the Chromium, WebKit, and Firefox browsers through a single API. |
| [pytest](https://pypi.org/project/pytest/)                       | A popular testing framework for Python                                                         |
| [pytest-base-url](https://pypi.org/project/pytest-base-url/)     | Pytest plugin for setting a base URL for your tests                                            |
| [pytest-playwright](https://pypi.org/project/pytest-playwright/) | Pytest plugin for Playwright integration for browser automation testing                        |
| [requests](https://pypi.org/project/requests/)                   | A versatile library for making HTTP requests in Python                                         |
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
