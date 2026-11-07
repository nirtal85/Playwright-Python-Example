---
name: setup-env
description: Use when setting up a fresh checkout of Playwright-Python-Example, restoring its uv environment, or diagnosing missing Python dependencies, Chromium, or display support before pytest.
---

# Setup environment

Work from the repository root. Use the checked-in lockfile and the Playwright package's own browser installer.

## Install

Inspect `pyproject.toml`, `uv.lock`, and `.github/workflows/devRun.yml`.
Use `uv`; if missing, install it using https://docs.astral.sh/uv/getting-started/installation/.
Current CI uses Python 3.13; `~=3.11` is not an exact Python 3.11 pin.

```bash
uv python install 3.13
uv sync --python 3.13 --locked --all-extras --dev
uv run --locked python --version
uv run --locked playwright install chromium
```

On Linux, missing system libraries require `uv run --locked playwright install --with-deps chromium`
with appropriate package-manager privileges. On macOS/Windows, use the normal browser install above.
`uv sync` creates `.venv`; `uv run` avoids platform-specific activation commands.
Preserve existing compatible environments. If locked sync fails, report the error instead of upgrading dependencies or regenerating `uv.lock`.
Install additional browser engines only if needed. Do not copy a browser version from a container tag: the installed Python package determines the required browser build.

## Configure

The default target in `pyproject.toml` is Sauce Demo. Pass another intended target with `--base-url`.
Inspect tests before changing the target; page objects expect that application's structure.
The repository has no `.env.example`, and its default Sauce Demo tests do not require a new secrets file.
Do not invent credentials, overwrite existing local configuration, or assume `BASE_URL` alone changes pytest's target.

## Verify

Collect tests without executing browser fixtures or navigating to the application:

```bash
uv run --locked pytest --collect-only -q -o addopts=
```

Check Chromium independently of the repository's headed fixtures:

```bash
uv run --locked python - <<'PY'
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    try:
        page = browser.new_page()
        page.set_content("<title>setup-env</title>")
        assert page.title() == "setup-env"
    finally:
        browser.close()
print("Chromium launch passed")
PY
```

After confirming the intended website, run the application's pre-merge selection:

```bash
uv run --locked pytest -m devRun
```

On Linux without a display, install Xvfb through the distribution's package manager and use:

```bash
xvfb-run -a uv run --locked pytest -m devRun
```

Both `pyproject.toml` (`--headed`) and `tests/conftest.py` (`headless: False`) force headed execution.
Removing `--headed` alone does not make the suite headless.
The application selection contacts external websites; collection and the standalone browser check avoid those application fixtures.
`sanity` is not a registered suite marker here.

## Report and troubleshoot

Report interpreter, locked installation, collection, browser launch, and application tests separately with their actual outcomes and skipped reasons.
Do not claim end-to-end success from collection alone.
For missing browser binaries, repeat the environment-scoped installer; for missing shared libraries, install Linux dependencies; for display errors, use Xvfb.
For blocked downloads, report the URL/error and retain TLS/proxy settings.
Leave application code, fixtures, and lockfiles unchanged during setup.
