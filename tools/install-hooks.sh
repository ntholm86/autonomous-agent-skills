#!/usr/bin/env bash
# Install PEA git hooks into the current repo's .git/hooks/.
# Run from the target repo root.
set -e

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || {
  echo "Not inside a git repo."
  exit 1
}

HOOKS_SRC=$(cd "$(dirname "$0")/hooks" && pwd)
HOOKS_DST="$REPO_ROOT/.git/hooks"

cp "$HOOKS_SRC/pre-commit" "$HOOKS_DST/pre-commit"
chmod +x "$HOOKS_DST/pre-commit"

echo "Installed pre-commit hook to $HOOKS_DST/pre-commit"
