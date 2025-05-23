# Copyright 2025 Beijing Volcano Engine Technology Ltd.
# SPDX-License-Identifier: Apache-2.0
#!/bin/bash

# 获取脚本所在目录并切换到该目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

source ../.venv/bin/activate
uv run ../server.py