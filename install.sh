#!/usr/bin/env bash
# Agentix (agx) — One-Line Linux & macOS Installer
# Usage: curl -fsSL https://raw.githubusercontent.com/coderemon24/agentix/main/install.sh | bash

set -e

echo "======================================================================"
echo "  Installing Agentix (agx) in: $(pwd)"
echo "======================================================================"

ZIP_URL="https://github.com/coderemon24/agentix/archive/refs/heads/main.tar.gz"
TEMP_DIR=$(mktemp -d)

echo "--> Downloading Agentix bundle from GitHub..."
curl -fsSL "$ZIP_URL" | tar -xz -C "$TEMP_DIR"

SOURCE_DIR="$TEMP_DIR/agentix-main"

# Copy directories
mkdir -p .agents scripts tests/visual-qa .cursor .github
cp -R "$SOURCE_DIR/.agents/"* .agents/
cp -R "$SOURCE_DIR/scripts/"* scripts/
cp -R "$SOURCE_DIR/tests/visual-qa/"* tests/visual-qa/
[ -d "$SOURCE_DIR/.cursor" ] && cp -R "$SOURCE_DIR/.cursor/"* .cursor/
[ -d "$SOURCE_DIR/.github" ] && cp -R "$SOURCE_DIR/.github/"* .github/

# Copy root files
FILES=(
  "agx" "agentix" "agx.cmd" "agentix.cmd"
  "AGENTS.md" "USER_MANUAL.md" "CLAUDE.md"
  ".cursorrules" ".windsurfrules" "CONVENTIONS.md"
  "ui-refactor.md" "UI-Mandatory.md" "gitcommit.md"
)
for f in "${FILES[@]}"; do
  [ -f "$SOURCE_DIR/$f" ] && cp "$SOURCE_DIR/$f" .
done

chmod +x agx agentix scripts/agx.py

rm -rf "$TEMP_DIR"

echo "--> Initializing Git branches and worktrees..."
python3 scripts/agx.py init || python scripts/agx.py init

echo "======================================================================"
echo "  [SUCCESS] Agentix (agx) installed successfully!"
echo "  Run './agx st' to check team status."
echo "======================================================================"

