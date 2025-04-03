from mcp.server.fastmcp import FastMCP
from .api.imagex import ImagexAPI


def Error(message: str):
    return 'Error: ' + message

def HandlerVolcResponse(response: dict):
    # if response.ResponseMetadata.Error:
    #     return Error(response.ResponseMetadata.Error.Message)
    # return str(response)
    return str(response)

# 创建FastMCP实例
def create_mcp_server():
    mcp = FastMCP(
        "VeImageX MCP", 
        description="火山引擎ImageX MCP, 你的图片处理存储分发助手",
    )
    imagex_service = ImagexAPI()

    @mcp.tool()
    def guide():
        """
        VeImageX MCP 是火山引擎 ImageX MCP Server, 是一个图片处理助手，可以帮助用户上传图片，做图片处理，分发图片，获取图片url等操作，
        在使用  VeImageX MCP 之前你需要知道一些一些事情:
        1. 使用 get_all_services_resource 确定好需要上传的空间，尽量使用 Image 服务
        3. 使用 get_all_image_templates 确定好需要使用的模板，模版是图片处理的关键。
            - 模版名称是 `tpl-{service_id}-{template_name}` 格式,在 Content.name 字段下，是后续获取图片处理的关键
            - 模版的功能通过 Abstract 字段描述，可以通过这个字段知道模版的功能
                   "Abstract": [
                    "压缩质量参数:75",
                    "图像内容擦除"
                ],
            - 比如压缩参数为 "quality":75 的模版，就拥有百分之 75 的 压缩质量，
            - 如果用户没有明显的提示，使用 jpeg 的模版名称，比如如果用户的 service_id 为 n9b2vwdhz3 ,则用  tplv-n9b2vwdhz3-jpeg
        4. 使用 upload_image 上传图片，使用的是本地地址，tool 会帮你使用 fs 上传到火山引擎
        5. 使用 get_image_url_by_store_uri 获取图片url

        一个经典的流程：你可以参考
        1. 使用 get_all_services_resource 获取所有服务信息列表，找到图片处理 Image 服务
        2. 使用 get_all_image_templates 获取所有模版信息列表，找到合适的模版, 用户没有要求或者兜底就使用 jpeg 的模版名称
        3. 使用 upload_image 上传图片到火山引擎
        4. 使用 get_image_url_by_store_uri 获取图片url
        """
        return """
            VeImageX MCP 是火山引擎 ImageX MCP Server, 是一个图片处理助手，可以帮助用户上传图片，做图片处理，分发图片，获取图片url等操作，在使用 tools 之前你需要知道一些一些事情:
        1. 谨记 guide
        2. 使用 get_all_services_resource 确定好需要上传的空间，尽量使用 Image 服务
        3. 使用 get_all_image_templates 确定好需要使用的模板，模版是图片处理的关键。
            - 模版名称是 `tpl-{service_id}-{template_name}` 格式,在 Content.name 字段下，是后续获取图片处理的关键
            - 模版的功能通过 Abstract 字段描述，可以通过这个字段知道模版的功能
                   "Abstract": [
                    "压缩质量参数:75",
                    "图像内容擦除"
                ],
            - 比如压缩参数为 "quality":75 的模版，就拥有百分之 75 的 压缩质量，
            - 如果用户没有明显的提示，使用 jpeg 的模版名称，比如如果用户的 service_id 为 n9b2vwdhz3 ,则用  tplv-n9b2vwdhz3-jpeg
        4. 使用 upload_image 上传图片，使用的是本地地址，tool 会帮你使用 fs 上传到火山引擎
        5. 使用 get_image_url_by_store_uri 获取图片url

        一个经典的流程：你可以参考
        1. 使用 get_all_services_resource 获取所有服务信息列表，找到图片处理 Image 服务
        2. 使用 get_all_image_templates 获取所有模版信息列表，找到合适的模版, 用户没有要求或者兜底就使用 jpeg 的模版名称
        3. 使用 upload_image 上传图片到火山引擎
        4. 使用 get_image_url_by_store_uri 获取图片url
        """

    @mcp.tool()
    def get_all_services_resource() -> str:
        """获取所有服务信息列表, 重要的信息是 
        1. 域名 - DomainName
        2. 服务ID - ServiceId
        3. 服务名称 - ServiceName
        4. 服务类型 - ServiceType:  StaticRc 静态托管, Image 图片处理
        5. 服务状态 - ServiceStatus
        """
        result = imagex_service.get_all_image_services({})
        return str(HandlerVolcResponse(result))

    @mcp.tool()
    def upload_image(file_path: list[str], service_id: str = None,) -> str:
        """上传图片到指定服务, file_path 是图片路径列表, service_id 是服务ID，如果用户没有要求，尽量上传到 Image 服务"""
        service_id = service_id or imagex_service.service_id
        if not file_path:
            return Error("file_path is required")
        params = {
            "ServiceId": service_id,
            "SkipMeta": False,
            "SkipCommit": False
        }

        result = imagex_service.upload_image(params, file_path)

        return str(HandlerVolcResponse(result))

    @mcp.tool()
    def get_all_image_templates(service_id: str = None, ) -> str:
        """获取 Image 服务所有的模板 tpl， 在获取图片url之前调用，需要用他来查询对应的 api 服务
        1. 如果 search 为空，则获取所有模板
        """
        service_id = service_id or imagex_service.service_id
        result = imagex_service.get_all_image_templates({"ServiceId": service_id, "Limit": 1000 })

        return str(HandlerVolcResponse(result))

    @mcp.tool()
    def get_image_url_by_store_uri(service_id: str = None, domain: str = None, uri: str = None, tpl: str = None) -> str:
        """
        通过 uri 和 模版信息 获取图片访问 url
        1. uri 在 upload_image 获得，模版信息在 get_all_image_templates 中获得
        2. 模版信息中，Tpl 是模版名称，TplId 是模版ID
        """
        service_id = service_id or imagex_service.service_id
        if not domain:
            return Error("domain is required")
        if not uri:
            return Error("uri is required")
        if not tpl:
            return Error("tpl is required")
        params = {
            "Action": "GetResourceURL",
            "Version": "2023-05-01",
            "Format": "image",
            "ServiceId": service_id,
            "Domain": domain,
            "URI": uri,
            "Tpl": tpl
        }

        result = imagex_service.get_resource_url(params)
        return str(HandlerVolcResponse(result))

    return mcp