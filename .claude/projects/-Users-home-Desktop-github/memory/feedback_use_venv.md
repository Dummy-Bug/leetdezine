---
name: Use existing venv for pip installs
description: Always use the .venv virtual environment at project root for installing Python packages, never install system-wide
type: feedback
---

Always install Python packages in the existing `.venv` virtual environment, never system-wide.

**Why:** User explicitly corrected when packages were installed with `--break-system-packages`. The project has a `.venv` at the repo root with mkdocs-material and dependencies already set up.

**How to apply:** Before any `pip install`, activate with `source /Users/home/Desktop/github/.venv/bin/activate`. If something was installed system-wide by mistake, uninstall it immediately.
