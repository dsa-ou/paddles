# Changelog

This file documents notable user-facing changes to the `paddles` library.
It does *not* document trivial updates (e.g. fixing typos) or
alterations to the development environment and process, including the tests.

The format of this file is based on [Keep a Changelog](https://keepachangelog.com).

This project adheres to [Semantic Versioning](https://semver.org) but note that
the major version is zero: [anything may change](https://semver.org/#spec-item-4).

<!-- Per release: Added / Changed / Deprecated / Removed / Fixed / Security -->

## [Unreleased](https://github.com/dsa-ou/paddles/compare/v0.2.0...HEAD)
These changes are in the GitHub repository but not on [PyPI](https://pypi.org/project/paddles).

<!-- Nothing yet. -->
### Changed
- class names `DynamicArray...` to `PythonList...` and `HashTable...` to `PythonDict`, to be more specific
- stack's `peek()` to `top()`, to be consistent with queue's `front()`

### Removed
- creation of non-empty collections, like `Stack("abc")`
- complexity indications that aren't about the worst case, for simplicity and consistency

## [0.2.0](https://github.com/dsa-ou/paddles/compare/v0.1-beta...v0.2.0) - 2025-10-10

### Added
- bags, with Python dictionaries
- bogo, bubble, insertion, selection, merge and quick sort
- links to LeetCode problems using stacks, queues and sorting
- support for direct imports, i.e. `from paddles import <class>`

## [0.1-beta](https://github.com/dsa-ou/paddles/compare/v0.1-alpha...v0.1-beta) - 2024-01-05
This is version 0.1.0 on PyPI.

### Added
- module docstrings explaining each ADT
- github.io site

### Changed
- class and method docstrings and doctests

## [0.1-alpha](https://github.com/dsa-ou/paddles/commits/v0.1-alpha) - 2023-12-28
This version is not on PyPI.

### Added
- stacks, with Python lists and linked lists
- queues and deques, with linked lists
