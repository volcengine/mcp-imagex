#!/usr/bin/env python3
# coding:utf-8

"""
传统入口点脚本，用于直接运行服务器。
推荐使用 `uvx veimagex-mcp` 或安装后运行 `veimagex-mcp` 命令。
"""

from veimagex_mcp.mcp_server import create_mcp_server
from dotenv import load_dotenv
import asyncio

load_dotenv()

mcp = create_mcp_server()

if __name__ == "__main__":
    asyncio.run(mcp.run())