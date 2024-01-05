# Contributing
This file documents how the library is developed, in case you want to contribute.

By contributing code or documentation to this repository,
you agree to transfer the copyright of your contribution to The Open University, UK,
and that your contribution will be subject to the `paddles` [licence](README.md#Licence).

## Environment
We use Python 3.10 and the [poetry](https://python-poetry.org) packaging and dependency manager.
To set up the environment:
- if you don't have Python 3.10, [install it](https://www.python.org/downloads/release/python-31011/)
- if you don't have `poetry`, [install it](https://python-poetry.org/docs/#installing-with-the-official-installer)
- clone this repository
- open a terminal and go to the folder to where you cloned this project
- enter `poetry install`

This installs the software needed to develop `paddles`, in a new
[virtual environment](https://docs.python.org/3/glossary.html#term-virtual-environment),
in order to not interfere with your existing Python projects.

To use the environment, while developing `paddles`, enter `poetry run C`
to execute command `C` in the virtual environment for `paddles`.

Alternatively, you can enter `poetry shell` to activate the environment, and
then you can just enter `C` to execute the command.
To deactivate the environment, enter `exit`.

In the rest of this document, the notation `[poetry run] C` means that you should enter
- `poetry run C` if you haven't activated the environment with `poetry shell`
- `C` if you have.

To finish the setup, you may optionally enter `[poetry run] pre-commit install`
to install pre-commit hooks (scripts that are run when committing changes to a repository).
Our environment has configured hooks that test, check and format your code and
generate the documentation before you commit your changes to the repository.

This project folder contains the following files and subfolders:

- `README.md`: this file
- `LICENSE`: the code licence
- `pyproject.toml`: project configuration
- `poetry.lock`: list of the packages installed by `poetry install`
- `.pre-commit-config.yaml`: list of pre-commit hooks
- `paddles/`: subfolder with the library's code
- `tests/`: subfolder with the test code
- `docs/`: subfolder with the documentation generated from the library code

## Testing

We use [pytest](https://pytest.org) to test `paddles`.
The unit tests are in the `tests` subfolder, with one test file per library module.
There's at least one test function per creator or modifier method.
There are no test functions for inspector methods: they are indirectly tested by
using them for closed-box (black-box) testing of the modifiers.

Each test file contains, in this order:
1. helper functions
1. fixtures (functions that generate test data)
1. tests for creator methods
1. tests for modifier methods, used separately, and finally
1. tests for combined use of modifiers.

Additionally, there are simple interactive examples of how to use a class in that class's docstring,
in subfolder `paddles`. These are used as [doctests](https://docs.python.org/3.10/library/doctest.html).

To run all tests, i.e. the doctests in `paddles` and the unit tests in `tests`,
enter `[poetry run] pytest`.

This will produce a report of which tests passed, which failed, and which
library code lines weren't executed. (We aim for 100% coverage.)
If two implementations of the same ADT use different messages
for the same exception for the same method, the tests fail.

## Linting

We check and format all code (library and tests) with [ruff](https://astral.sh/ruff).

To check the code against over 700 style rules, enter `[poetry run] ruff check`.
If `ruff` reports rule violations, open the [rules page](https://docs.astral.sh/ruff/rules),
search for the reported rule number (e.g. E101), and click on the rule name
(e.g. mixed-spaces-and-tabs) next to it in the page.
This will open a new page explaining the violated rule and its rationale, with an example,
like [this](https://docs.astral.sh/ruff/rules/mixed-spaces-and-tabs/).

To automatically fix violations, when possible,
enter `[poetry run] ruff check --fix --unsafe-fixes` and double-check
the modifications made by `ruff`.

To automatically ignore the flagged code lines for a particular file,
enter `[poetry run] ruff check path/to/file.py --add-noqa`.
This will add comments of the form `# noqa: ...` where `...` is the number of
the violated rule.

This should be used sparingly. For example, in the test files, the fixtures
that generate classes are on purpose named with initial uppercase, as classes are,
which violates the rule that function names and arguments should be in lowercase.

Finally, enter `[poetry run] ruff format` to format the code.

## Type checking
We type check the code with [pytype](https://google.github.io/pytype).
Enter `[poetry run] pytype .` (note the dot) to type check all code.

## Documenting
We use [pdoc](https://pdoc.dev) to generate the documentation from the docstrings.

To check the documents during development, enter `[poetry run] pdoc paddles &`
to open a live site with the documentation. Any changes to the docstrings of
the library files are immediately reflected in the site, upon saving the files.

## Comitting
If you installed the pre-commit hooks when setting up the [environment](#environment)
then every time you commit your code,
these steps are done automatically on the _staged_ files:
1. test the code with `pytest`
2. type check the code with `pytype`
3. check (but _don't_ fix) the code with `ruff`
4. format the code with `ruff`
5. generate the documentation with `pdoc`.

If a test or check fails in steps 1–3 or if a file is modified in steps 4–5,
then the commit doesn't go ahead.
This allows you to review the errors and the automatically applied changes,
stage the modified files, and commit again.

Due to the automated steps, each commit takes many seconds to complete.
But when it successfully completes, you know that your code hasn't broken existing tests,
isn't poorly formatted, and has up-to-date documentation.