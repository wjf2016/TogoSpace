#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [ -d "$REPO_ROOT/.venv/Scripts" ]; then
    export PATH="$REPO_ROOT/.venv/Scripts:$PATH"
else
    export PATH="$REPO_ROOT/.venv/bin:$PATH"
fi
cd "$REPO_ROOT/src"
mkdir -p "$REPO_ROOT/logs"
nohup python backend_main.py "$@" >> "$REPO_ROOT/logs/backend_stdout.log" 2>&1 &
echo "后端已启动 (PID $!)"
