# A pre-commit hook 
- A pre-commit hook is a script that runs automatically before a commit is finalized in a version control system like Git.
- These hooks are part of Git’s hook system, which allows you to run custom scripts at various points in the Git workflow.

## Purpose of Pre-commit Hooks
- Pre-commit hooks are used to enforce code quality standards and prevent bad code from being committed to the repository. 
- They can perform a variety of tasks, such as:
	- Running linters (e.g., Pylint, ESLint)
  - Running static type checkers (e.g., MyPy, Pyright)
  - Running tests
  - Formatting code (e.g., using black for Python, prettier for JavaScript)
  - Checking for sensitive information (e.g., API keys)
  - Ensuring commit messages follow a specific format


## Pre-commit Hooks Setup

This repository uses pre-commit hooks to enforce code quality standards and prevent bad code from being committed. Pre-commit hooks run automatically before a commit is finalized and can perform various tasks such as running linters, type checkers, and formatting code.

### Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Using Pre-commit](#using-pre-commit)
- [Custom Hooks](#custom-hooks)
- [Running Hooks Manually](#running-hooks-manually)

#### Installation

To use pre-commit hooks in this repository, follow these steps:

1. **Install the `pre-commit` package**:

    ```bash
    pip install pre-commit
    ```

2. **Install the pre-commit hooks**:

    ```bash
    pre-commit install
    ```

This sets up Git to run pre-commit hooks defined in the configuration file before every commit.

#### Configuration

The pre-commit hooks are configured in the `.pre-commit-config.yaml` file. Here is an example configuration:

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
    - id: trailing-whitespace
    - id: end-of-file-fixer
    - id: check-yaml
    - id: check-added-large-files

-   repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
    - id: black

-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.910
    hooks:
    - id: mypy

-   repo: https://github.com/pre-commit/mirrors-pylint
    rev: v2.9.6
    hooks:
    - id: pylint
      args: ['--disable=R,C']
```

### Hooks Explanation
- Trailing Whitespace: Removes trailing whitespace from files.
- End of File Fixer: Ensures files end with a newline.
- Check YAML: Checks YAML files for syntax errors.
- Check Added Large Files: Prevents adding large files to the repository.
- Black: Formats Python code using the black formatter.
- MyPy: Performs static type checking using mypy.
- Pylint: Lints Python code with pylint.

