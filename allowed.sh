#!/bin/bash

# This script checks the library code for constructs not in paddles.json.
# Test code and __init__.py files are not checked. Warnings are ignored.
# If the checks fail, print the output and make the pre-commit hook fail.

out=$(uv run allowed -f -c paddles paddles/[^_]*py | fgrep -v WARNING)
if [ -n "$out" ]; then
    printf "%s\n" "$out"
    exit 1
fi