# Coding Agent Sandbox

Public sandbox for evaluating autonomous coding agents through GitHub Issues and Pull Requests.

## Rules
- Synthetic code only.
- No credentials, secrets, personal data, or production configuration.
- Agents work on dedicated branches.
- Tests must be run before opening a Pull Request.
- Agents must not merge their own Pull Requests.

## Test command

```bash
python -m unittest discover -s tests -v
```
