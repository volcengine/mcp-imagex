from mcp.server.fastmcp import FastMCP
from .api.imagex import ImagexAPI


mcp = FastMCP(
    "VeImageX MCP", 
    description="火山引擎ImageX MCP, 你的图片处理存储分发助手",
)


# 创建FastMCP实例
def create_mcp_server():
    imagex_service = ImagexAPI()
    # 资源定义
    @mcp.resource("service://{service_id}")
    def get_service_resource(service_id: str = None) -> str:
        """获取特定服务ID的服务信息"""
        service_id = service_id or imagex_service.service_id
        result = imagex_service.get_image_service({"ServiceId": service_id})
        return str(result)

    @mcp.resource("services://all")
    def get_all_services_resource() -> str:
        """获取所有服务信息列表"""
        result = imagex_service.get_all_image_services({})
        return str(result)

    @mcp.resource("image://{service_id}/{store_uri}")
    def get_image_resource(service_id: str = None, store_uri: str = "") -> str:
        """获取特定图片资源的信息"""
        service_id = service_id or imagex_service.service_id
        result = imagex_service.get_image_upload_file({
            "ServiceId": service_id,
            "StoreUri": store_uri
        })
        return str(result)

    # 工具定义
    @mcp.tool()
    def upload_image(file_path: str, service_id: str = None, store_key: str = None) -> str:
        """上传图片到指定服务"""
        service_id = service_id or imagex_service.service_id
        params = {
            "ServiceId": service_id
        }
        if store_key:
            params["StoreKeys"] = [store_key]
        
        result = imagex_service.upload_image(params, [file_path])
        return str(result)

    @mcp.tool()
    def get_image_url(store_uri: str, service_id: str = None, tpl: str = "") -> str:
        """获取图片访问URL"""
        service_id = service_id or imagex_service.service_id
        params = {
            "ServiceId": service_id,
            "StoreUri": store_uri
        }
        if tpl:
            params["Tpl"] = tpl
        
        result = imagex_service.get_resource_url(params)
        return str(result)

    @mcp.tool()
    def list_images(limit: int = 10, service_id: str = None, marker: str = "") -> str:
        """列出服务下的图片资源"""
        service_id = service_id or imagex_service.service_id
        params = {
            "ServiceId": service_id,
            "Limit": str(limit)
        }
        if marker:
            params["Marker"] = marker
        
        result = imagex_service.get_image_upload_files(params)
        return str(result)

    @mcp.tool()
    def create_service(service_name: str) -> str:
        """创建新的图片服务"""
        body = {
            "ServiceName": service_name,
            "ServiceRegion": "cn-north-1"
        }
        result = imagex_service.create_image_service(body)
        return str(result)

    @mcp.tool()
    def update_service_name(service_name: str, service_id: str = None) -> str:
        """更新服务名称"""
        service_id = service_id or imagex_service.service_id
        params = {
            "ServiceId": service_id,
        }
        body = {
            "ServiceName": service_name
        }
        result = imagex_service.update_service_name(params, body)
        return str(result)

    @mcp.tool()
    def create_image_style(style_name: str, operations: str, service_id: str = None) -> str:
        """创建图片样式"""
        service_id = service_id or imagex_service.service_id
        params = {
            "ServiceId": service_id,
        }
        body = {
            "Name": style_name,
            "Ops": operations
        }
        result = imagex_service.create_image_style(params, body)
        return str(result)

    @mcp.tool()
    def get_image_style(style_id: str, service_id: str = None) -> str:
        """获取图片样式详情"""
        service_id = service_id or imagex_service.service_id
        params = {
            "ServiceId": service_id,
            "StyleId": style_id
        }
        result = imagex_service.get_image_style_detail(params)
        return str(result)

    # 提示模板定义
    @mcp.prompt()
    def create_service_prompt(service_name: str) -> str:
        """创建服务的提示模板"""
        return f"""
用户想要创建一个名为 {service_name} 的图片服务。
请使用create_service工具创建服务，并告知用户服务ID和相关信息。
"""

    @mcp.prompt()
    def upload_image_prompt(service_id: str = None) -> str:
        """上传图片的提示模板"""
        service_id = service_id or imagex_service.service_id
        return f"""
用户想要上传图片到服务ID为 {service_id} 的服务。
请告知用户可以使用upload_image工具上传图片，并提供简要说明。
"""

    @mcp.prompt()
    def image_processing_prompt(operation: str, service_id: str = None) -> str:
        """图片处理提示模板"""
        service_id = service_id or imagex_service.service_id
        return f"""
用户想要对服务ID为 {service_id} 的图片进行 {operation} 处理。
请介绍火山引擎ImageX的图片处理能力，并告知用户如何使用该功能。
"""

    return mcp