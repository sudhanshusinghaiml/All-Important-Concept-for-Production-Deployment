Setting up projects using `pyproject.toml` is becoming a standard practice in the Python ecosystem for managing project metadata, dependencies, and build configurations. The `pyproject.toml` file is supported by several tools like `Poetry`, `Flit`, and `Setuptools`. Below is a step-by-step guide to setting up a Python project using `pyproject.toml`, particularly with `Poetry`, which is one of the most popular tools for this purpose.

### Step 1: Install Poetry

If you haven't already installed `Poetry`, you can do so with the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

After installation, ensure `Poetry` is available by checking the version:

```bash
poetry --version
```

### Step 2: Create a New Project

To start a new project, use `Poetry` to generate the project structure along with a `pyproject.toml` file:

```bash
poetry new my_project
```

This command will create a new directory called `my_project` with the following structure:

```
my_project/
├── pyproject.toml
├── README.rst
├── my_project
│   └── __init__.py
└── tests
    └── __init__.py
```

### Step 3: Understand the `pyproject.toml` File

The `pyproject.toml` file is where you define your project metadata, dependencies, and build system requirements. Here's an example `pyproject.toml` file:

```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "A short description of the project"
authors = ["Your Name <your.email@example.com>"]
license = "MIT"
readme = "README.md"
homepage = "https://example.com"
repository = "https://github.com/example/my_project"
keywords = ["AI", "ML", "NLP"]

[tool.poetry.dependencies]
python = "^3.8"
numpy = "^1.21.0"
pandas = "^1.3.0"

[tool.poetry.dev-dependencies]
pytest = "^6.2.4"
black = "^21.6b0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

### Key Sections:
- **[tool.poetry]**: This section includes metadata about your project, such as the name, version, description, and author.
- **[tool.poetry.dependencies]**: Lists the packages required for your project to run. The versions can be specified using semantic versioning.
- **[tool.poetry.dev-dependencies]**: Lists the packages needed for development, such as testing and formatting tools.
- **[build-system]**: Defines the build system requirements, typically related to `Poetry`.

### Step 4: Manage Dependencies

You can add dependencies to your project using `Poetry` commands:

- **Add a dependency**:

```bash
poetry add requests
```

This will add `requests` to the `dependencies` section of your `pyproject.toml` file.

- **Add a development dependency**:

```bash
poetry add --dev pytest
```

This will add `pytest` to the `dev-dependencies` section.

### Step 5: Installing Dependencies

To install all dependencies defined in your `pyproject.toml`, use:

```bash
poetry install
```

This command creates a virtual environment and installs the dependencies there.

### Step 6: Running Scripts

`Poetry` also allows you to run scripts within the environment:

```bash
poetry run python my_project/main.py
```

### Step 7: Building and Publishing the Project

To build your project for distribution, use:

```bash
poetry build
```

This command creates a distribution package in the `dist/` directory.

To publish your package to PyPI (or another repository), use:

```bash
poetry publish
```

### Conclusion

By setting up your Python project with `pyproject.toml` and `Poetry`, you create a clean, standardized, and easily manageable project structure. This setup streamlines dependency management, environment creation, and project building, making it easier to maintain and collaborate on Python projects.