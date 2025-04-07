# Volcengine MCP

Volcengine ImageX 的 Model Context Protocol (MCP) Server 实现

## 项目简介

Volcengine MCP是一个基于[Model Context Protocol](https://github.com/modelcontextprotocol/python-sdk)的 MCP-server，
它将 Volcengine 服务集成到LLM模型上下文中，使大模型能够直接操作和管理图片资源。

## 功能特点

- 提供多种资源访问接口，便于LLM获取Volcengine服务信息、图片资源等
- 实现了多个Volcengine功能的工具封装，包括上传图片，管理服务等
- 提供多种预定义提示模板，帮助LLM更好地理解和使用Volcengine功能
- 支持多种运行模式：独立模式、Web服务模式
- 提供高级和基础两种实现，满足不同场景需求

## 安装

### 环境要求

- Python 3.11+
- 火山引擎账号及AccessKey/SecretKey

### 安装依赖

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

### 环境变量配置

```
cp .env.example .env 
```

修改根目录的`.env.example`文件，并配置以下环境变量

```shell
VOLCENGINE_ACCESS_KEY=your_access_key
VOLCENGINE_SECRET_KEY=your_secret_key
VOLC_IMAGEX_SERVICE_ID=your_service_id
```

或者在集成 Mcp Server 的时候 通过环境变量配置
```json
{
  "mcpServers": {
    "veimagex": {
      // ...
      "env": {
        "VOLCENGINE_ACCESS_KEY": "Your Volcengine AK",
        "VOLCENGINE_SECRET_KEY": "Your Volcengine SK"
      }
    }
  }
}

```

## 使用方法

### 在 Mcp Client 中集成

在 mcp client 中配置 mcp 服务, (还没有发布包 暂时用 sh命令 运行 server 脚本，后续如果发布包 则用 uvx 运行 server 脚本)， 配置的 MCP JSON：

```json
{
  "mcpServers": {
    "volcengine": {
      "command": "sh",
      "args": ["/{your_path}/volcengine-mcp/scripts/run.sh"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```


### 使用 @modelcontextprotocol/inspector 调试

```bash
sh ./scripts/debug.sh
```
