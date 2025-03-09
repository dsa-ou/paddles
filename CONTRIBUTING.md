# Contributing
This document explains how the library is developed,
in case you want to contribute code or documentation. To contribute, you need:
- an IDE, e.g. Visual Studio Code or PyCharm
- a [GitHub account](https://docs.github.com/en/get-started/quickstart/creating-an-account-on-github)
  (we recommend using your academic email, to get education benefits)
- a basic knowledge of GitHub
  (see this [tutorial](https://docs.github.com/en/get-started/quickstart/hello-world))
- a basic knowledge of [Markdown](https://www.markdownguide.org/cheat-sheet/), to write docstrings
- software to send your contributions back to GitHub, like [git](https://git-scm.com) (if you prefer the command line)
  or [GitHub Desktop](https://desktop.github.com/) (if you prefer a more user-friendly app)

You may wish to first read the more detailed and beginner-friendly
[contribution guide for `allowed`](https://github.com/dsa-ou/allowed/blob/main/docs/contribution.md),
as much of it also applies to `paddles`.

## Development environment
We use Python 3.10 and the [poetry](https://python-poetry.org) packaging and dependency manager.
We use an older Python version for development to make sure `paddles` works with it.

To set up the development environment:
1. if you don't have Python 3.10, [install it](https://www.python.org/downloads/release/python-31011/)
2. if you don't have `poetry`, [install it](https://python-poetry.org/docs/#installing-with-the-official-installer)
3. [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
  this repository (this creates a copy in *your* GitHub account)
4. [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
  your forked repository (this makes a local copy on your machine)
5. open a terminal and go to the folder to where you cloned this project
6. enter `poetry install`

The last step installs the software needed to develop `paddles`, in a new
[virtual environment](https://docs.python.org/3/glossary.html#term-virtual-environment),
in order to not interfere with your existing Python projects.

To use the environment, while developing `paddles`, enter `poetry run C`
to execute command `C` in the virtual environment for `paddles`.

Alternatively, you can enter `poetry shell` to activate the environment, and
then just enter `C` to execute the command.
To deactivate the environment, enter `exit`.

In the rest of this document, the notation `[poetry run] C` means that you should enter
- `poetry run C` if you haven't activated the environment with `poetry shell`
- `C` if you have.

To finish the setup, you may optionally enter `[poetry run] pre-commit install`
to install pre-commit hooks (scripts that are run when committing changes to a repository).
Our development environment includes hooks that test, check and format your code and
generate the documentation before you commit your changes to the repository.

## Structure
The project folder contains the following files and subfolders, among others:

- `README.md`: an introduction to the project, in Markdown format
- `CONTRIBUTING.md`: this file
- `LICENSE`: the code licence
- `pyproject.toml`: project configuration
- `poetry.lock`: list of the packages installed by `poetry install`
- `.pre-commit-config.yaml`: list of pre-commit hooks
- `paddles/`: subfolder with the library's code
- `tests/`: subfolder with the test code
- `docs/`: subfolder with the HTML files of the [documentation site](https://dsa-ou.github.io/paddles).

The documentation is generated from the docstrings in the code, so do *not*
edit the `docs/` files directly.

## Testing

We use [pytest](https://pytest.org) to test `paddles`.
The unit tests are in the `tests` subfolder, with one test file per library module.
There's at least one test function per creator or modifier method.
There are no test functions for inspector methods: they are indirectly tested by
using them for closed-box (black-box) testing of the modifiers.

Each test file contains, in this order:
1. helper functions
2. test data
3. tests for creator methods
4. tests for modifier methods, used separately, and finally
5. tests for combined use of modifiers.

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
search for the reported rule number (e.g. E713), and click on the rule name
(e.g. not-in-test) next to it in the page.
This will open a new page explaining the violated rule with an example,
like [this](https://docs.astral.sh/ruff/rules/not-in-test/).

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

## Committing
If you installed the pre-commit hooks when setting up the development environment,
then every time you commit your code, these steps are done automatically:
1. test the code with `pytest`
2. type check the code with `pytype`
3. check (but _don't_ fix) the code with `ruff`
4. format the code with `ruff`
5. generate the documentation with `pdoc`.

You can therefore just commit whenever you want to check your changes,
instead of running each check manually, as explained in the previous sections.

The automated steps are executed on the staged files. If you changed some files
but didn't stage them, you will get a warning that those files weren't processed.

If a test or check fails in steps 1–3 or if a file is modified in steps 4–5,
then the commit doesn't go ahead.
This allows you to review the errors and the automatically applied changes,
stage the modified files, and commit again.

Due to the automated steps, each commit takes many seconds to complete.
But when it successfully completes, you know that your code hasn't broken existing tests,
isn't poorly formatted, and has up-to-date documentation.