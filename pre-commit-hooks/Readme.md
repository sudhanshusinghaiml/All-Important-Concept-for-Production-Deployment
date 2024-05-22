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
- [Using Pre commit](#using-pre-commit)
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

3. **Update the pre-commit hooks to ensure you have the latest versions available**:
   ```bash
   pre-commit autoupdate
   ```

4. **Reinstall the hooks to apply the updates:**
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

##### Hooks Explanation
- Trailing Whitespace: Removes trailing whitespace from files.
- End of File Fixer: Ensures files end with a newline.
- Check YAML: Checks YAML files for syntax errors.
- Check Added Large Files: Prevents adding large files to the repository.
- Black: Formats Python code using the black formatter.
- MyPy: Performs static type checking using mypy.
- Pylint: Lints Python code with pylint.

#### Using Pre-commit
Pre-commit hooks will run automatically before each commit. If any hook fails, the commit will be aborted. Fix the issues reported by the hooks and commit again.


#### Custom Hooks
You can also define custom hooks in the `.pre-commit-config.yaml` file. Here’s an example of a custom hook: Create a custom script (e.g., check_code.py):
```Python
import sys

def main():
    # Custom checks here
    print("Running custom pre-commit hook")
    return 0  # Return non-zero to indicate failure

if __name__ == "__main__":
    sys.exit(main())
```

We need to add the custom hook to `.pre-commit-config.yaml`:
```yaml
repos:
-   repo: local
    hooks:
    -   id: custom-check
        name: Custom Check
        entry: python check_code.py
        language: python
        files: \.py$
```

#### Running Hooks Manually
You can manually run all pre-commit hooks on all files with the following command:
```bash
pre-commit run --all-files
```


## Pre-commit Hook Configuration in VS Code

This guide explains how to set up pre-commit hooks in Visual Studio Code (VS Code) to ensure code quality and consistency before commits.

### Step 1: Install Pre-commit
First, install `pre-commit` if you haven't already.

```sh
pip install pre-commit
```

### Step 2: Create a `.pre-commit-config.yaml` File
In the root of your project, create a file named `.pre-commit-config.yaml`. This file will define the hooks you want to run. Here’s an example configuration:

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1  # Use the latest version or specify a version you need
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-json
```

### Step 3: Install the Hooks
Run the following command to install the hooks defined in the `.pre-commit-config.yaml` file:

```sh
pre-commit install
```

This command sets up the hooks to run automatically before each commit.

### Step 4: Configure VS Code
You can configure VS Code to work seamlessly with `pre-commit`.

#### Install the Pre-commit Extension for VS Code:
1. Go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window or pressing `Ctrl+Shift+X`.
2. Search for "Pre-commit" and install the extension provided by `nelfer`.

#### Configure Tasks in VS Code:
1. Open the command palette by pressing `Ctrl+Shift+P` and type `Tasks: Open User Tasks` or `Tasks: Open Workspace Tasks`.
2. Add a new task for running `pre-commit`.

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Pre-commit",
            "type": "shell",
            "command": "pre-commit run --all-files",
            "problemMatcher": []
        }
    ]
}
```

#### Configure a Git Hook for VS Code:
1. Create a `.vscode` directory in the root of your project if it doesn’t exist.
2. Inside `.vscode`, create a file named `settings.json` and add the following configuration:

```json
{
    "git.postCommitCommand": "runPreCommit"
}
```

### Step 5: Verify the Configuration
Make a change in your code, stage it, and commit. The pre-commit hooks should run automatically, and you should see the output in the terminal or the Git output panel in VS Code.

By following these steps, you should have `pre-commit` hooks configured and running automatically in your VS Code environment.



### References:
- [Github Pre Commit Hooks](https://github.com/pre-commit/pre-commit-hooks)
- [Pre Commit Docs](https://pre-commit.com/)
