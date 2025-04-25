 # Copyright 2025 Beijing Volcano Engine Technology Ltd.
 # SPDX-License-Identifier: Apache-2.0
 
import asyncio
import sys
from dotenv import load_dotenv

from veimagex_mcp import create_mcp_server
from .mcp_extend import create_api_mcp_server
def main():
    """命令行入口点，用于启动 VeImageX MCP 服务器"""

    # 加载环境变量
    load_dotenv()

    try:
        # 创建MCP服务器
        mcp = create_mcp_server()
        create_api_mcp_server(mcp)
        asyncio.run(mcp.run())
    except Exception as e:
        print(f"启动服务器时出错: {e}", file=sys.stderr)
        sys.exit(1)