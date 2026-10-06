# Agent Instructions

This repository is a synthetic coding-agent benchmark.

## Required workflow
1. Read the assigned GitHub Issue completely.
2. Make only the changes required by that Issue.
3. Add or update automated tests for behavior changes.
4. Run: `python -m unittest discover -s tests -v`.
5. Do not modify unrelated files.
6. Work on a dedicated branch and open a Pull Request.
7. Do not merge the Pull Request.

## Safety
- Do not add secrets, credentials, tokens, external service calls, or personal data.
- Do not weaken tests to make them pass.
- Do not disable validation.
