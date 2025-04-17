# Volcengine ImageX MCP

[Volcengine ImageX](https://t.zijieimg.com/MIURnXrQfvU/) 的 Model Context Protocol (MCP) Server 实现

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
- [火山引擎账号](https://console.volcengine.cn/imagex?utm_source=tdgfha&utm_medium=oesbpg&utm_term=mcp-pr-01&utm_campaign=&utm_content=ImageX)及AccessKey/SecretKey

### 环境变量配置

在集成 Mcp Server 时配置
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

在 mcp client 中配置 mcp 服务， 配置的 MCP JSON：


```json
{
  "mcpServers": {
    "volcengine": {
      "disabled": false,
      "command": "uvx",
      "args": ["veimagex-mcp"],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "",
        "VOLCENGINE_SECRET_KEY": "",
        "SERVICE_ID": "",
        "DOMAIN": ""
      },
      "transportType": "stdio"
    }
  }
}
```
