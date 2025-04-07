from mcp.server.fastmcp import FastMCP
from .api.imagex import ImagexAPI
import uuid


def Error(message: str):
    return "API Error: " + message


def HandlerVolcResponse(response: dict):
    if (
        response
        and hasattr(response, "ResponseMetadata")
        and response.ResponseMetadata
        and hasattr(response.ResponseMetadata, "Error")
        and response.ResponseMetadata.Error
    ):
        return Error(response.ResponseMetadata.Error.Message)
    return str(response)


def create_mcp_server():
    mcp = FastMCP(
        "VeImageX MCP",
        description="Volcengine(火山引擎) ImageX(图片服务) MCP , 你的图片处理存储分发助手",
    )
    imagex_service = ImagexAPI()

    @mcp.tool()
    def guide():
        """VeImageX MCP is the Volcengine(火山引擎) ImageX(图片服务) MCP Server, an image processing assistant that helps users upload images, process images, distribute images, and obtain image URLs.

        Before using VeImageX MCP, you need to know a few things:
        1. Use `get_all_services_resource` to determine the upload space serviceId, preferably use Image type services, and proceed to the next step only after confirming the operation

        2. Use `get_all_image_templates` to determine the template to use, as templates are key to image processing.
            - Template names follow the format `tpl-{service_id}-{template_name}`, found under the Content.name field, which is crucial for subsequent image processing
            - Template functionality is described in the Abstract field, which tells you what the template does
                "Abstract": [
                    "Compression quality parameter:75",
                    "Image content erasure"
                ],
            - For example, a template with compression parameter "quality":75 has 75% compression quality
            - If the user has no specific requirements, use the jpeg template name, e.g., if the user's service_id is n9b2vwdhz3, use tplv-n9b2vwdhz3-jpeg

        3. Use `upload_image` to upload images, using local absolute paths - the tool will help you upload to Volcengine using fs. If you don't have this path, you try to find user's intent, or ask him.

        4. Use `generate_image_by_text` to generate an image based on the text.

        5. Use `get_image_url_by_store_uri` to get the image URL

        A classic workflow you can reference:
        1. Use `get_all_services_resource` to get the list of all service information, find the Image processing service
        2. Use `get_all_image_templates` to get the list of all template information, find a suitable template. If user has no requirements or as a fallback, use the jpeg template name
        3. Use `upload_image` to upload the image to Volcengine
        4. Use `generate_image_by_text` to generate an image based on the text.
        5. Use `get_image_url_by_store_uri` to get the image URL"""
        return """use `guide` description to get how to use ImageX Mcp Server"""

    @mcp.tool()
    def get_all_services_resource() -> str:
        """Get list of all service information.
        Important information includes:
        1. Domain Name - DomainName
        2. Service ID - ServiceId
        3. Service Name - ServiceName
        4. Service Type - ServiceType: StaticRc (static hosting), Image (image processing)
        5. Service Status - ServiceStatus"""
        result = imagex_service.get_all_image_services({})
        return str(HandlerVolcResponse(result))

    @mcp.tool()
    def upload_image(service_id: str, file_path: list[str]) -> str:
        """Upload images to specified service.

        Args:
            file_path: List of image file paths, use absolute path.
            service_id: Service ID, preferably upload to Image service if user has no specific requirements"""
        if not service_id:
            return Error(
                "service_id is required, please use get_all_services_resource to get the service_id"
            )
        if not file_path:
            return Error("file_path is required")
        params = {"ServiceId": service_id, "SkipMeta": False, "SkipCommit": False}

        result = imagex_service.upload_image(params, file_path)

        return str(HandlerVolcResponse(result))

    @mcp.tool()
    def get_all_image_templates(service_id: str) -> str:
        """Get all templates (tpl) for the Image service. Call this before getting image URLs to query the corresponding API service.
        1. If search is empty, get all templates

        Args:
            service_id: The service ID to get templates for"""
        if not service_id:
            return Error(
                "service_id is required, please use get_all_services_resource to get the service_id"
            )
        result = imagex_service.get_all_image_templates(
            {"ServiceId": service_id, "Limit": 1000}
        )

        return str(HandlerVolcResponse(result))

    @mcp.tool()
    def get_image_url_by_store_uri(
        service_id: str, domain: str = None, uri: str = None, tpl: str = None
    ) -> str:
        """
        Get image access URL through URI and template information.
        1. URI is obtained from upload_image, template information is obtained from get_all_image_templates
        2. In template information, Tpl is the template name, TplId is the template ID

        Args:
            uri: The storage URI of the image
            service_id: The service ID
            tpl: The template name to apply
            domain: The domain name for the URL
        """
        if not service_id:
            return Error(
                "service_id is required, please use get_all_services_resource to get the service_id"
            )
        if not domain:
            return Error("domain is required")
        if not uri:
            return Error("uri is required")
        if not tpl:
            return Error("tpl is required")

        params = {"ServiceId": service_id, "Domain": domain, "URI": uri, "Tpl": tpl}

        result = imagex_service.get_resource_url(params)
        return str(HandlerVolcResponse(result))

    @mcp.tool()
    def generate_image_by_text(
        service_id: str, domain: str = None, tpl: str = None, text: str = None
    ) -> str:
        """Generate an image based on the text.

        Args:
            service_id: The service ID
            domain: The domain name for the URL
            tpl: The template name to apply
            text: The text to generate an image from
        """
        if not service_id:
            return Error(
                "service_id is required, please use get_all_services_resource to get the service_id"
            )
        if not domain:
            return Error("domain is required")
        if not tpl:
            return Error("tpl is required")
        if not text:
            return Error("text is required")

        query = {
            "ServiceId": service_id,
        }

        params = {
            "Domain": domain,
            "Template": tpl,
            "Overwrite": True,
            "ReqJson": {"req_key": "high_aes_general_v20_L", "prompt": text},
            "ModelAction": "CVProcess",
            "ModelVersion": "2022-08-31",
            "Outputs": [f"output_{uuid.uuid4().hex[:8]}"],
        }

        result = imagex_service.get_cv_text_generate_image(query, params)
        return str(HandlerVolcResponse(result))

    return mcp
