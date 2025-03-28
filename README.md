# VeImageX MCP

火山引擎图片服务（ImageX）的Model Context Protocol (MCP) 服务器实现。

## 项目简介

VeImageX MCP是一个基于[Model Context Protocol](https://github.com/modelcontextprotocol/python-sdk)的服务器，它将火山引擎的ImageX服务集成到LLM模型上下文中，使大模型能够直接操作和管理图片资源。

## 功能特点

- 提供多种资源访问接口，便于LLM获取ImageX服务信息、图片资源等
- 实现了多个ImageX功能的工具封装，包括上传图片，管理服务等
- 提供多种预定义提示模板，帮助LLM更好地理解和使用ImageX功能
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

修改根目录的`.env.example`文件，并配置以下环境变量：

```
VOLCENGINE_ACCESS_KEY=your_access_key
VOLCENGINE_SECRET_KEY=your_secret_key
VOLC_IMAGEX_SERVICE_ID=your_service_id
```



## 使用方法

### 基础MCP服务器

运行MCP服务器：

```bash
uvx run server.py
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

1. `server.py` - 使用FastMCP高级API的基础服务器
2. `advanced_server.py` - 使用底层MCP API的高级服务器，支持更多功能
3. `mcp_server.py` - 集成了Web服务功能的服务器，可以作为独立服务运行，也可以挂载到其他ASGI应用中

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

## 许可证

MIT License
