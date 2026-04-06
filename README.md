<div align="center">

<img height="120" src="https://playwright.dev/img/playwright-logo.svg" alt="Playwright Logo"/>

# Enterprise-Grade Playwright Python Architecture
### The Ultimate Boilerplate for Scalable, Robust, and Modern UI Automation

[![Twitter Follow](https://img.shields.io/twitter/follow/NirTal2?style=social)](https://twitter.com/NirTal2)
[![YouTube](https://img.shields.io/youtube/channel/subscribers/UCQjS-eoKl0a1nuP_dvpLsjQ?style=social)](https://www.youtube.com/channel/UCQjS-eoKl0a1nuP_dvpLsjQ)
![CI Status](https://github.com/nirtal85/Playwright-Python-Example/actions/workflows/devRun.yml/badge.svg)
![Nightly Build](https://github.com/nirtal85/Playwright-Python-Example/actions/workflows/nightly.yml/badge.svg)
[![Tests](https://img.shields.io/endpoint?url=https%3A%2F%2Fflakiness.io%2Fapi%2Fbadge%3Finput%3D%257B%2522badgeToken%2522%253A%2522badge-4G6NKalA9bX7seUqFAyqhs%2522%257D)](https://flakiness.io/nirtal85/Playwright-Python-Example)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[View Live Report](https://nirtal85.github.io/Playwright-Python-Example/) • [Read The Docs](https://www.test-shift.com) • [Report Bug](https://github.com/nirtal85/Playwright-Python-Example/issues)

</div>

---

## 🚀 About The Project

This repository is a **Production-Ready Reference Architecture** for building next-generation test automation using **Playwright** and Python.

It goes beyond basic scripts to demonstrate a fully scalable framework with advanced features like Accessibility Testing (A11y), visual tracing, and cloud integration, tailored for modern DevOps pipelines.

<p align="center">
  <a href="https://automation.co.il/%d7%a7%d7%95%d7%a8%d7%a1-%d7%90%d7%95%d7%98%d7%95%d7%9e%d7%a6%d7%99%d7%94-%d7%a4%d7%99%d7%99%d7%aa%d7%95%d7%9f-python-automation/">
    <img src="resources/images/automation_college_playwright_course.jpeg" alt="Automation College - Playwright Python Course" width="600" style="border-radius: 10px;" />
  </a>
</p>

### ✨ Key Features
* **Modern Tooling:** Powered by `uv` for blazing fast package management and `Ruff` for linting.
* **Accessibility First:** Integrated **Axe** scans to ensure your app is accessible to everyone.
* **Deep Debugging:** Full integration with **Playwright Traces** and Video recording linked directly to Allure Reports.
* **Cloud Scale:** Native integration with **BrowserStack** for cross-browser testing on real devices.
* **CI/CD Optimization:** Parallel execution strategies and dynamic version syncing for GitHub Actions.

---

## 📃 Articles written about this project

This project implements the concepts discussed in the following **TestShift** articles:

* [Test Automation - How To Use Custom User Agent in Selenium Python or Playwright Python to Avoid Security Bots](https://www.linkedin.com/pulse/test-automation-how-use-custom-user-agent-selenium-python-nir-tal-lyqbf/)
* [Test Automation - How to Use Dynamic Base URLs with Selenium And Playwright Python in GitHub Actions](https://www.linkedin.com/pulse/test-automation-how-use-dynamic-base-urls-selenium-playwright-tal-klq5f/)
* [Test Automation - Maximizing Browser Window With Playwright Python And Pytest](https://www.linkedin.com/pulse/test-automation-maximizing-browser-window-playwright-nir-tal-c24hf/)
* [Test Automation - How to Bypass Re-Login With Playwright Python And Pytest](https://www.linkedin.com/pulse/test-automation-how-bypass-re-login-playwright-python-nir-tal-cfnnf/)
* [Test Automation - How To Perform Automated Accessibility Checks Using Playwright Python And Axe](https://www.linkedin.com/pulse/how-perform-automated-accessibility-tests-using-playwright-nir-tal-hupxf/)
* [Test Automation - How To Link Playwright Traces and Videos to Allure Report using GitHub Actions](https://www.linkedin.com/pulse/test-automation-how-link-playwright-traces-videos-allure-nir-tal-vkm2f/)
* [Test Automation - Speeding Up Testing with Playwright Python using Local Storage](https://www.linkedin.com/pulse/test-automation-speeding-up-testing-playwright-python-nir-tal-gmmtf/)
* [Test Automation - Efficient Element Selection with Playwright Python using Test IDs](https://www.linkedin.com/pulse/test-automation-efficient-element-selection-playwright-nir-tal-gcbmf/)
* [Test Automation - Flexible Test Execution with Playwright Python and GitHub Actions](https://www.linkedin.com/pulse/test-automation-flexible-execution-playwright-python-nir-tal-38xkf/)
* [Test Automation - Accelerating Playwright Python Tests with Parallel Execution in GitHub Actions](https://www.linkedin.com/pulse/test-automation-accelerating-playwright-python-tests-parallel-nir-tal-163of/)
* [Test Automation - How to Sync Playwright Versions Between Python and GitHub Actions](https://www.linkedin.com/pulse/test-automation-how-sync-playwright-versions-between-nir-tal-vyjze/)
* [From Open Source to Industry Sponsorship: The TestShift Journey with BrowserStack](https://www.test-shift.com/posts/from-open-source-to-enterprise-sponsorship-the-testshift-journey-with-browserstack)
* [From Selenium to Playwright: A Data-Driven Look at the Shifting Landscape of Test Automation](https://www.test-shift.com/posts/from-selenium-to-playwright-a-data-driven-look-at-the-shifting-landscape-of-test-automation)
* [Allure 3 Isn’t Just an Upgrade. It’s the Final Piece of the Quality Gate Architecture](https://www.test-shift.com/posts/allure-3-leave-the-swamp-ride-the-dragon)

---

## 🛠️ Tech Stack

| Tool                                                              | Description & Why We Use It                                      |
|-------------------------------------------------------------------|------------------------------------------------------------------|
| [Playwright](https://pypi.org/project/playwright/)                | The modern standard for reliable, flaky-free browser automation. |
| [Pytest](https://pypi.org/project/pytest/)                        | The most powerful testing framework for Python.                  |
| [Axe Playwright](https://pypi.org/project/axe-playwright-python/) | For automated accessibility (A11y) compliance testing.           |
| [Allure](https://pypi.org/project/allure-pytest/)                 | For beautiful, data-rich test reports including Traces & Video.  |
| [Pytest Split](https://pypi.org/project/pytest-split/)            | To intelligently split test suites for parallel execution.       |
| [Requests](https://pypi.org/project/requests/)                    | For API interactions and test data setup.                        |

### 🌐 Cloud Testing Provider

This project is powered by **[BrowserStack](https://www.browserstack.com)**, enabling high-scale cross-browser and mobile testing on real devices in the cloud.

---

## ⚙️ Getting Started

### 1. Clone

```bash
git clone https://github.com/nirtal85/Playwright-Python-Example
cd playwright-python
```

### 2. Install (The Modern Way)

We use uv for lightning-fast installations.

Windows (PowerShell):


```bash
python -m pip install uv
python -m uv venv
.venv\Scripts\Activate.ps1
uv sync --all-extras --dev
playwright install
```

Mac/Linux:

```bash
python3 -m pip install uv
uv venv
source .venv/bin/activate
uv sync --all-extras --dev
playwright install
```

## 🏃‍♂️ Execution

Run all tests (Chromium by default):

```bash
pytest
```

Run specific suite (Tags):

```bash
pytest -m sanity
```

## 📊 Results, Traces & Debugging

We use Allure for reporting. To generate and open the report locally:

```bash
npx -y allure generate allure-results --output allure-report --open
```

👉 [See a Live Example of the Report Here](https://nirtal85.github.io/Playwright-Python-Example/)

### 🕵️‍♀️ Using the Trace Viewer

Navigate to the Playwright Trace Viewer.

Drag & Drop the trace file (located in test-results/) generated after a failure.

Time Travel: Move back and forth in the timeline to see exactly what happened (Network, DOM, Console).

<div align="center">

Found this project useful?
If this architecture helped you solve a problem or save time, consider supporting the work!

<a href="https://www.buymeacoffee.com/nirtal"> <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="60" alt="Buy Me A Coffee" /> </a>

<br />

[Visit TestShift.com for more Architectural Insights](https://www.test-shift.com)

</div>