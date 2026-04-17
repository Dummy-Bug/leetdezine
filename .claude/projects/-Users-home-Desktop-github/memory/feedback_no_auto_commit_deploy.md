---
name: Never commit or deploy without asking
description: Always ask before running git add, git commit, git push, or mkdocs gh-deploy
type: feedback
---

Never run git add, git commit, git push, or mkdocs gh-deploy without explicitly asking the user first.

**Why:** User wants full manual control over what gets committed and when things get deployed. No surprises.

**How to apply:** Always show what's about to be committed/deployed and wait for explicit approval before running any git or deploy command.
