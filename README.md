`paddles` aims to be an algorithms and data structures library in Python that
- is thoroughly tested and documented
- is easy to install, use and understand
- adheres to Python's coding style.

## Testing

The library is tested with [pytest](https://pytest.org).
The unit tests are in the `tests` subfolder, with one test file per library module.
There's at least one test function per creator or modifier method.
There are no test functions for inspector methods: they are indirectly tested by
using them for closed-box (black-box) testing of the modifiers.

Each test file has the same structure: helper functions,
fixtures (functions that generate test data), tests for creator methods,
tests for modifier methods, used separately, and finally tests for combined use of modifiers.

There are also simple interactive examples of how to use a class in that class's docstring,
in folder `paddles`. These are used as [doctests](https://docs.python.org/3.10/library/doctest.html).

To run all tests, the doctests in `paddles` and the unit tests in `tests`, open a terminal,
go the project's main folder, i.e. the parent of `tests`, and enter `poetry run pytest`.
This will produce a report of which tests passed and which failed.
Any library code lines that weren't executed by the tests are also reported.
(We aim for 100% coverage.)

If two implementations of the same ADT use different messages
for the same exception for the same method, the tests fail.

If you installed `pre-commit`, any time you commit one or more Python files,
`pytest` is run before committing. If any test fail, the commit is aborted.
This ensures that any committed code doesn't break the existing tests.
(Coverage below 100% doesn't abort the commit.)

## Linting

We check and format our code with [ruff](https://astral.sh/ruff).

Open a terminal in the main project folder and enter `poetry run ruff check`.
The checked style rules are given [here](https://docs.astral.sh/ruff/rules),
with further explanations when you click on a rule's name.

To automatically fix violations, if possible, add the command line options
`--fix --unsafe-fixes` and check the changes made by `ruff`.

To automatically ignore the flagged code lines for a particular file,
enter `poetry run ruff check path/to/file.py --add-noqa`.
This will add comments of the form `# noqa: ...` where `...` is the number of
the violated rule.
This should be used sparingly. For example, in the test files, the fixtures
that generate classes are on purpose named with initial uppercase, as classes are,
which violates the rule that function names and arguments should be in lowercase.

Finally, enter `poetry run ruff format` to format all the code.

If you installed the pre-commit hooks, the code will be checked and formatted
upon being committed. If one or more style rules are violated, the commit aborts.

## Type checking
We type check the code with [pytype](https://google.github.io/pytype).
Enter `poetry run pytype .` to type check all code.
If you installed the pre-commit hooks, type checking will be done upon committing.
If the type checking fails, the commit is aborted.