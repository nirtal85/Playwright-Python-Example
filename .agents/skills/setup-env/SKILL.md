---
name: setup-env
description: Use when setting up a fresh checkout of Playwright-Python-Example, restoring its uv environment, or diagnosing missing Python dependencies, Chromium, or display support before pytest.
---

# Setup environment

Work from the repository root. Use the checked-in lockfile and the Playwright package's own browser installer.

## Install

Inspect `pyproject.toml`, `uv.lock`, and `.github/workflows/devRun.yml`.
Use `uv`; if missing, install it using https://docs.astral.sh/uv/getting-started/installation/.
Current CI uses Python 3.13; the `requires-python` range in `pyproject.toml` is not an exact interpreter pin.

```bash
uv python install 3.13
uv sync --python 3.13 --locked --all-extras --dev
uv run --locked playwright install chromium
```

On Linux, missing system libraries require `uv run --locked playwright install --with-deps chromium`
with appropriate package-manager privileges. On macOS/Windows, use the normal browser install above.
`uv sync` creates `.venv`; `uv run` avoids platform-specific activation commands.
Treat `.venv` as the project environment: `uv sync` aligns it with the lockfile and selected dependency groups, removing packages not selected for installation, including manually installed extras.
If locked sync fails, report the error instead of upgrading dependencies or regenerating `uv.lock`.
Install additional browser engines only if needed. Do not copy a browser version from a container tag: the installed Python package determines the required browser build.

## Configure

The default target in `pyproject.toml` is Sauce Demo. Pass another intended target with `--base-url`.
Inspect tests before changing the target; page objects expect that application's structure.
The repository has no `.env.example`, and its default Sauce Demo tests do not require a new secrets file.
Do not invent credentials, overwrite existing local configuration, or assume `BASE_URL` alone changes pytest's target.

## Finish setup

Setup is complete when locked dependency sync and the Chromium installer exit successfully.
Read the installer output: Playwright can report missing system libraries as host-validation warnings without failing. Resolve those warnings using the Linux dependency installation above; if blocked, report setup as incomplete and list the unresolved dependencies.
Stop there: do not collect or run tests, launch a browser, or visit the target application unless explicitly requested.
Successful installation is not a claim that application tests pass.

## Report and troubleshoot

Report dependency and Chromium installation outcomes, any unresolved host-validation warnings, and state that tests were not run and display support was not checked.
The default pytest configuration is headed. On Linux without a display, Xvfb is an option for a separately requested test run; do not install it or run tests as part of this setup.
For missing browser binaries, repeat the environment-scoped installer; for missing shared libraries, install Linux dependencies.
For blocked downloads, report the URL/error and retain TLS/proxy settings.
Leave application code, fixtures, and lockfiles unchanged during setup.
