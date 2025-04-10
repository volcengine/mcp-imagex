# Volcengine ImageX MCP

Volcengine ImageX 的 Model Context Protocol (MCP) Server 实现

## 项目简介

Volcengine ImageX MCP是一个基于[Model Context Protocol](https://github.com/modelcontextprotocol/python-sdk)的 MCP-server，
它将 Volcengine 服务集成到LLM模型上下文中，使大模型能够直接上传和处理图片资源。

## 功能特点

- 提供多种资源访问接口，便于LLM获取veImageX服务信息、图片资源等
- 实现了多个veImageX功能的工具封装，包括上传图片、文生图、画质增强、画质评估、漫画风格、智能扩展等
- 提供多种预定义提示模板，帮助LLM更好地理解和使用veImageX功能

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
SERVICE_ID=your_service_id
DOMAIN=your_domain
```

或者在集成 Mcp Server 的时候 通过环境变量配置
```json
{
  "mcpServers": {
    "veimagex": {
      // ...
      "env": {
        "VOLCENGINE_ACCESS_KEY": "Your Volcengine AK",
        "VOLCENGINE_SECRET_KEY": "Your Volcengine SK",
        "SERVICE_ID": "Your Service ID",
        "DOMAIN": "Your Domain"
      }
    }
  }
}

```

## 使用方法

### 在 Mcp Client 中集成

在 mcp client 中配置 mcp 服务, (还没有发布包 暂时用 sh命令 运行 server 脚本，后续如果发布包 则用 uvx 运行 server 脚本)， 配置的 MCP JSON：

#### 本地开发
```json
{
  "mcpServers": {
    "volcengine": {
      "command": "uvx",
      "args": ["--from", "YOUR_PROJECT_ABSOLUTE_PATH", "veimagex"],
    }
  }
}
```

#### Pypi

```json
{
  "mcpServers": {
    "volcengine": {
      "command": "uvx",
      "args": ["veimagex"],
    }
  }
}
```


### 使用 @modelcontextprotocol/inspector 调试

```bash
sh ./scripts/debug.sh
```
