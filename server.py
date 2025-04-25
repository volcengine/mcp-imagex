# Copyright 2025 Beijing Volcano Engine Technology Ltd.
# SPDX-License-Identifier: Apache-2.0
#!/usr/bin/env python3
# coding:utf-8

"""
传统入口点脚本，用于直接运行服务器。
推荐使用 `uvx veimagex-mcp` 或安装后运行 `veimagex-mcp` 命令。
"""

from veimagex_mcp.mcp_server import create_mcp_server
from veimagex_mcp.mcp_extend import create_api_mcp_server
from dotenv import load_dotenv
import asyncio

load_dotenv()

mcp = create_mcp_server()
create_api_mcp_server(mcp)
if __name__ == "__main__":
    asyncio.run(mcp.run())