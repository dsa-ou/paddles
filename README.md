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

If you installed `pre-commit`, any time you commit one or more Python files,
`pytest` is run before committing. If any test fail, the commit is aborted.
This ensures that any committed code doesn't break the existing tests.
(Coverage below 100% doesn't abort the commit.)