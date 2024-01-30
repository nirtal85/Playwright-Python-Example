# Playwright Python Example

![Pre merge test](https://github.com/nirtal85/Playwright-Python-Example/actions/workflows/devRun.yml/badge.svg)

## Articles written about this project

## Project Setup

* [Install scoop](https://scoop.sh/)
* Install allure commandline by running the following command:

```bash
scoop install allure
```

* Clone the project
* Navigate to the project directory
* Install virtualenv:

```bash
py -m pip install --user virtualenv
```

* Create a virtual environment:

```bash
py -m venv env
```

* Activate the virtual environment:

```bash
.\env\Scripts\activate
```

* Install project dependencies:

```
poetry install
```

## Running Tests

```bash
pytest --browser <firefox/chrome_headless>
```

When no browser was selected then chrome will be used.

* Run tests:

```bash
pytest
```

## Viewing Test Results

* View allure results locally:

```bash
allure serve allure-results
```

* [View allure results via Github pages](https://nirtal85.github.io/Playwright-Python-Example/)

## View Help And Custom CLI Options

```bash
pytest --help
```

## Sort imports

```bash
isort .
```

## format code

```bash
black .
```
