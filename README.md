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


## 接口说明

### 提供的资源

- `service://{service_id}` - 获取特定服务的信息
- `services://all` - 获取所有服务信息列表
- `image://{service_id}/{store_uri}` - 获取特定图片资源信息
- `template://{service_id}/{template_id}` - 获取特定模板信息
- `style://{service_id}/{style_id}` - 获取特定样式信息

### 提供的工具

- `upload_image` - 上传图片到指定服务
- `get_image_url` - 获取图片访问URL
- `list_images` - 列出服务下的图片资源
- `create_service` - 创建新的图片服务
- `update_service_name` - 更新服务名称
- `create_image_style` - 创建图片样式
- `get_image_style` - 获取图片样式详情

### 提供的提示模板

- `create_service_prompt` - 创建服务的提示模板
- `upload_image_prompt` - 上传图片的提示模板
- `image_processing_prompt` - 图片处理提示模板

## 架构说明

项目包含多个服务器实现：

1. `server.py` - mcp 服务启动入口
2. `mcp_server.py` - mcp 服务实现

## 开发说明

### 扩展新功能

如需添加新的工具或资源，只需在相应的服务器文件中添加新的装饰器函数：

```python
@mcp.tool()
def new_tool(param1: str, param2: int) -> str:
    """工具描述"""
    # 实现逻辑
    return result

@mcp.resource("new-resource://{param}")
def new_resource(param: str) -> str:
    """资源描述"""
    # 实现逻辑
    return result
```
