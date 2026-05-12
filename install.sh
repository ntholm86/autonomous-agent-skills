#!/usr/bin/env bash
# install.sh — copy PEA skills into a Copilot skills directory.
#
# Usage:
#   bash install.sh [target-dir]
#
# Default target: ~/.copilot/skills (user-global).
# Pass a path to install into a project: bash install.sh ./my-repo/.copilot/skills
set -e

SKILLS=(intent vision improve trail retrospect probe)

SRC=$(cd "$(dirname "$0")" && pwd)
DST="${1:-$HOME/.copilot/skills}"

mkdir -p "$DST"

for skill in "${SKILLS[@]}"; do
  if [ -f "$SRC/$skill/SKILL.md" ]; then
    mkdir -p "$DST/$skill"
    cp "$SRC/$skill/SKILL.md" "$DST/$skill/SKILL.md"
    echo "  installed: $skill"
  else
    echo "  skipped:   $skill (no SKILL.md found)"
  fi
done

# Optional: PRINCIPLES.md alongside the skills folders
if [ -f "$SRC/PRINCIPLES.md" ]; then
  cp "$SRC/PRINCIPLES.md" "$DST/PRINCIPLES.md"
  echo "  installed: PRINCIPLES.md"
fi

echo ""
echo "Installed PEA skills to: $DST"
echo "Invoke in Copilot chat with /intent, /vision, /improve, /trail, /retrospect, /probe"
