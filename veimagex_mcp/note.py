 # Copyright 2025 Beijing Volcano Engine Technology Ltd.
 # SPDX-License-Identifier: Apache-2.0
 
note = {
    "get_domain_config": """Args:params: A JSON structure
     DomainName (String): 是  域名，您可以通过调用 GetServiceDomains 获取当前服务下所有域名。 
 ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "get_image_style_result": """Args:params: A JSON structure
     ServiceId (String): 是  图片渲染所用样式关联的服务的 ID，用于计量计费和渲染结果的存储。获取方式请参见如何获取调用参数。 
    body: A JSON structure
     StyleId (String): 是  图片渲染所用样式的样式 ID。获取方法请参见如何获取样式 ID。 
 Params (JSON Map): 否  样式中的动态要素和要素取值。格式为 "Key":"Value"，例如，"el17fbb3a2134*":"Hello,World", 
       - Key：表示要素 ID，String 类型。获取方式请参见如何获取要素 ID； 
       - Value：表示要素的取值，String 类型。需要您根据实际需求自定义，例如，自定义图片地址、文本及二维码等内容。 
 OutputFormat (String): 否  渲染结果图的编码格式，默认值为 webp。取值如下所示： 
       - jpeg 
       - webp 
       - png 
       - heic 
 OutputQuality (Integer): 否  渲染结果图的编码质量。默认为 75，取值范围为 [1,100]，值越大，结果图的质量越高。 
 elements (Array of Elements): 是  要素属性，结构请参考样式定义。此参数不为空则使用自定义参数内容替换样式定义中对应 elements 的相关属性值。 
       - 要素类型不允许更改； 
       - 若elements和params两个参数同时指定了某个要素的内容，则以elements中指定的为准。 
 background (Object of Background): 否  样式背景，结构请参考样式定义。此参数不为空则使用自定义参数内容替换样式定义中的 background 属性值。""",
    "get_all_certs": """Args:""",
    "add_cert": """Args:body: A JSON structure
     name (String): 否  证书备注名 
 public (String): 否  证书公钥 
 private (String): 否  证书私钥""",
    "del_cert": """Args:body: A JSON structure
     cert_id (String): 否  证书 ID，您可以通过调用获取账号下全部证书获取账号下所有证书信息。""",
    "download_cert": """Args:params: A JSON structure
     cert_id (String): 是  证书 ID，您可以通过调用 获取账号下全部证书 获取账号下所有证书信息。""",
    "get_cert_info": """Args:params: A JSON structure
     cert_id (String): 是  证书 ID，您可以通过调用获取账号下全部证书获取账号下所有证书信息。""",
    "get_image_all_domain_cert": """Args:""",
    "update_image_batch_domain_cert": """Args:body: A JSON structure
     domain (String): 是  域名 
 cert_id (String): 是  证书Id""",
    "create_image_template": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     TemplateName (String): 是  模板名称，必须使用该服务的图片模板固定前缀。模板名称能包含的字符正则集合为[a-zA-Z0-9_-]。 
       您可以通过调用获取单个服务信息接口的查看返回参数TemplatePrefix的值。 
 DoUpdate (Boolean): 否  是否直接更新模板，取值如下所示： 
       * true：已有的线上模板会同步更新，该操作直接生效； 
       * false：新增一个模板，已有模板不受影响。 
 WithSig (Boolean): 否  是否开启鉴权，取值如下所示： 
       * true：开启鉴权。 
       * false：（默认）关闭鉴权。 
       一般当通过模板参数下发敏感信息时，比如文字水印内容、URL 失效期，需要对图片 URL 鉴权保护，防止内容被篡改。 
 Parameters (Array of String): 否  图片模板使用的参数列表，URL 中下发参数的顺序需要跟列表中的保持一致。 
 ReqDeadline (String): 否  URL 的失效期，为 Unix 时间戳，一般配置为在 URL 中通过模板参数动态下发。 
 OuputQuality (Integer): 否  对图片编码使用的质量参数，取值范围为 [1,100]，默认为 75。 
 OutputFormat (String): 否  该模板计划使用的输出格式。 
       * 取值为image，表示输出原格式。 
       * 支持输出的静图格式：png、jpeg、heic、avif、webp、vvic。 
       * 支持输出的动图格式：awebp、heif、avis。 
 DemotionFormat (String): 否  模板计划使用的降级格式，仅对 heic 静图有效。取值如下所示： 
       - webp 
       - jpeg 
 Sync (Boolean): 否  是否同步处理，仅对 heic 静图有效。取值如下所示： 
       - true：是 
       - false：否 
 Filters (Array of Filters): 否  对图片的编辑操作。 
 OutputExtra (Object of OutputExtra): 否  用于图片服务输出时的图片编码自定义参数，键值均为 string。 
       * 取值png.use_quant表示是否开启 png quant 压缩，取值为true表示开启，取值为false表示关闭； 
       * 取值heic.sync表示使用 heic 同步编码，取值为true表示同步； 
       * 取值heic.timeout表示 heic 同步编码的超时时间，比如 20。 
 Evals (Array of Evals): 否  对结果图片执行的画质评估配置 
 AdaptiveFmt (Object of AdaptiveFmt): 否  指定图像自适应配置。 
 Snapshot (Object of Snapshot): 否  仅当指定输出格式为静图时，配置有效。 
       视频截帧配置。 
 Animation (Object of Animation): 否  仅当指定输出格式为动图时，配置有效。 
       视频转动图配置。 
 Exif (Object of Exif): 否  仅当指定输出格式非动图时，配置有效。 
       保留 EXIF 信息配置。 
 AnimExtract (Object of AnimExtract): 否  仅当指定输出格式为静图时，配置有效。 
       动图截帧配置。 
 QualityMode (String): 否  压缩质量模型，默认为空，表示使用绝对质量。取值 relative 时，表示使用相对质量，原图为 JPEG 有效。 
 Persistence (String): 否  是否对图片结果缓存，默认为空。取值如下所示： 
       - read_write：对结果读写 
       - read_only：对结果只读 
 Temporary (Boolean): 否  是否为临时使用，取值如下所示： 
       - true：是 
       - false：否 

字段： Filters
 Name (String): 是  操作名称，具体详情请见图片编辑数据结构。 
 Param (JSON Map): 是  操作参数配置内容，Key 为 参数名称，Value 为 参数配置。具体详情请见图片编辑数据结构。 

字段： OutputExtra
 png.use_quant (String): 否  是否压缩颜色空间，取值如下所示： 
       - true：是 
       - false：否 
 jpeg.progressive (String): 否  是否采用 jpeg 渐进编码格式，取值如下所示： 
       - true：是 
       - false：否 
 heic.roi (String): 否  仅当OutputFormat取值为heic时配置有效 
       是否开启 ROI 编码，取值如下所示： 
       - true：是 
       - false：否 
 heic.encode.depth (String): 否  仅当OutputFormat取值为heic时配置有效 
       色位深度，值越大则提供的图像色彩范围越多，使图像颜色变化的更细腻，但图像体积也会增大。取值如下所示： 
       - 8：8bit 
       - 10：10bit 
 heic.thumb.ratio (String): 否  仅当OutputFormat取值为heic时配置有效 
       缩略图比例。在原图基础上，编码缩小一定倍数的小分辨率图片，跟大图一起封装在同一张图片中，缩小倍数不建议过大，一般为 5~10 之间相对合理。 
 heic.alpha.reserve (String): 否  仅当OutputFormat取值为heic时配置有效 
       是否带透明通道编码，取值如下所示： 
       - true：是 
       - false：否 
 jpeg.alpha.demotion (String): 否  jpeg 的 alpha 图片是否降级为 png，指定为 png 时表示降级为 png 格式。缺省情况下默认为空，表示不降级。 
 jpeg.size.fixed.padding (String): 否  指定 jpeg 体积的输出大小，需同时指定 jpeg.size.fixed，二者缺一不可。 
       体积填充方式，取值固定为 append。 
 jpeg.size.fixed (String): 否  指定 jpeg 体积的输出大小，需同时设置 jpeg.size.fixed.padding，二者缺一不可。 
       指定输出体积大小，单位为 Byte。 
 heic.aq.mode (String): 否   
 jpeg.quality.adapt.version (String): 否   
 jpeg.quality.adapt.pixlimit (String): 否   
 webp.quality.adapt.version (String): 否   
 webp.quality.adapt.pixlimit (String): 否   
 heic.quality.adapt.version (String): 否   
 heic.quality.adapt.pixlimit (String): 否   
 heic.demfmt (String): 否   
 avif.demfmt (String): 否   
 vvic.quality.adapt.version (String): 否   
 vvic.quality.adapt.pixlimit (String): 否   
 vvic.roi (String): 否   
 vvic.aq.mode (String): 否   
 heic.jpeg.size.reserve (String): 否   
 jpeg.size.recover (String): 否   

字段： Evals
 Name (String): 是  评估名，画质评估固定取值为 quality。 
 Param (JSON Map): 是  画质评估参数配置内容，Key 为 参数名称，Value 为 参数配置。具体详情请见图片编辑数据结构。 
        
        
        
        
        
        
        
        
        

字段： AdaptiveFmt
 Static (String): 否  静图自适应，具体实现说明参考图像自适应压缩。取值如下所示： 
       - webp：若 HTTP 请求头中 accept 头部包含 image/webp 的字符串匹配，则返回 webp 格式。否则返回 OutputFormat 指定格式。 
       - heic：若 HTTP 请求头中 accept 头部包含 image/heic 的字符串匹配，则返回 webp 格式。否则返回 OutputFormat 指定格式。 
       - avif：若 HTTP 请求头中 accept 头部包含 image/avif 的字符串匹配，则返回 webp 格式。否则返回 OutputFormat 指定格式。 
       - dynamic：智能模式，即根据请求头中 MIME 查找具体格式，查找成功，则返回该格式，否则返回 OutputFormat 指定格式。 
 Animated (String): 否  动图自适应，具体实现说明参考图像自适应压缩。取值如下所示： 
       取值如下所示： 
       - webp：若 HTTP 请求头中 accept 头部包含 image/webp 的字符串匹配，则返回 webp 格式。否则返回 OutputFormat 指定格式。 
       - heic：若 HTTP 请求头中 accept 头部包含 image/heic 的字符串匹配，则返回 webp 格式。否则返回 OutputFormat 指定格式。 
       - avif：若 HTTP 请求头中 accept 头部包含 image/avif 的字符串匹配，则返回 webp 格式。否则返回 OutputFormat 指定格式。 
       - dynamic：智能模式，即根据请求头中 MIME 查找具体格式，查找成功，则返回该格式，否则返回 OutputFormat 指定格式。 

字段： Snapshot
 Type (String): 是  视频截帧类型，取值如下所示： 
       - default：智能模式，从视频首帧开始逐帧地检测当前帧是否为黑屏，并最终返回第一个非黑屏的帧。 
       - offset：指定时间戳模式，返回指定截帧时间的那一帧。可在 TimeOffsetMs 和 TimeOffsetMsStr 之间二选一。 
 TimeOffsetMs (Long): 否  当 Type 为 offset 时，在TimeOffsetMs 和 TimeOffsetMsStr 之间二选一。 
       指定截图时间，取值范围为[0,视频时长]，单位为 ms。默认为 0，表示返回首帧。若指定时间 > 视频长度，则返回视频最后一帧。 
 TimeOffsetMsStr (String): 否  当 Type 为 offset 时，在TimeOffsetMs 和 TimeOffsetMsStr 之间二选一。 
       指定截图时间为使用模板参数动态下发的方式，取值固定为${snapshot_time}。 

字段： Animation
 StartTime (Integer): 是  动图起始时间戳，单位为 ms。 
 Duration (Integer): 是  动图时长，单位为 ms。 
 SelectFrameMode (String): 是  抽帧策略，取值如下所示： 
       - fps：抽帧频率，1 秒 X 帧。 
       - spf：抽帧间隔，X 秒 1 帧。 
       - key：抽取关键帧。 
 FramePerSecond (Integer): 是  帧率，1 秒 X 帧。仅当SelectFrameMode取值为fps时需要配置。 
 SecondPerFrame (Integer): 是  秒数，X 秒 1 帧。仅当SelectFrameMode取值为spf时需要配置。 
 WaitTime (Integer): 是  同步等待时长，单位为 s，超时未完成则根据DemotionType降级。 
 DemotionType (String): 是  降级类型，取值如下所示： 
       - image：抽取一帧降级返回  
       - video：直接返回原视频降级 

字段： Exif
 ExifReserve (Boolean): 否  是否开启保留全部 EXIF 信息，取值如下所示： 
       - true：是 
       - false：否 
 AutoOrientOff (Boolean): 否  是否开启保留全部 EXIF 信息。取值如下所示： 
       - true：是 
       - false：否 
 ExifRetainNames (Array of String): 否  保留部分 EXIF 信息的具体内容，多个之间用,分隔。更多信息请参考标准 EXIF 标签。 

字段： AnimExtract
 Strategy (Integer): 否  动图截帧策略，取值如下所示： 
       - 0：智能模式，从动图首帧开始逐帧检测当前帧亮度是否大于 80，并最终返回第一个亮度大于 80 的帧。 
       - 1：全局最优，从动图首帧开始逐帧检测并返回亮度最大的一帧。 
 Timeout (Integer): 否  动图异步处理超时时间，单位为 ms。默认为 1500，取值负数时表示无超时时间。若在指定时间范围内处理未完成则返回失败。""",
    "update_https": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     domain (String): 是  域名，您可以通过获取服务下全部域名获取服务下域名信息。 
 https (Object of Https): 是  https 配置 

字段： Https
 enable_http2 (Boolean): 否  是否开启 http2，取值如下所示： 
       - true：开启 
       - false：关闭 
 enable_https (Boolean): 否  是否开启 https，取值如下所示： 
       - true：开启 
       - false：关闭 
 enable_ocsp (Boolean): 否  是否开启 ocsp 装订，取值如下所示： 
       - true：开启 
       - false：关闭 
 enable_quic (Boolean): 否  是否开启 quic 协议支持，取值如下所示： 
       - true：开启 
       - false：关闭 
 tls_versions (Array of String): 是  支持的 tls 版本，取值如下所示： 
       - tlsv1.0 
       - tlsv1.1 
       - tlsv1.2 
       - tlsv1.3  
 cert_id (String): 否  需要关联的证书 ID，若enable_https为true，则为必填。 
 enable_force_redirect (Boolean): 否  是否开启强制跳转，支持取值如下所示： 
       - true：开启 
       - false：关闭 
 force_redirect_type (String): 否  强制跳转类型，取值如下所示： 
       - http2https：HTTP 到 HTTPS 
       - https2http：HTTPS 到 HTTP 
       仅当enable_force_redirect取值为true时需要配置。 
 force_redirect_code (String): 否  强制跳转状态码，取值如下所示： 
       - 301：返回给用户 301 状态码进行重定向。 
       - 302：返回给用户 302 状态码进行重定向。 
       仅当enable_force_redirect取值为true时需要配置。 
 hsts (Object of Hsts): 否  配置hsts 

字段： Hsts
 enable (Boolean): 否  是否开启hsts 
 subdomain (String): 否  表示 HSTS 配置是否也应用于加速域名的子域名。该参数有以下取值： include：表示 HSTS 配置应用于子域名站点。 exclude：表示 HSTS 配置不应用于子域名站点。 该参数的默认值是 exclude。 
 ttl (Integer): 否  表示 Strict-Transport-Security 响应头在浏览器中的缓存过期时间，单位是秒。该参数的取值范围是 0 - 31,536,000。31,536,000 秒表示 365 天。如果该参数值为 0，其效果等同于禁用 HSTS 设置。该参数的默认值是 0。""",
    "update_image_domain_ua_access": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     domain (String): 是  域名，您可以通过获取服务下全部域名获取服务下域名信息。 
 ua_auth (Object of UaAuth): 是  UA 访问限制配置。 

字段： UaAuth
 enable (Boolean): 是  是否开启 UA 访问限制，取值如下所示： 
       - true：开启 
       - false：未开启（默认） 
 rule_type (String): 是  黑白名单设置类型，取值如下所示： 
       - deny：黑名单 
       - allow：白名单（默认） 
 user_agents (Array of String): 是  Agent 列表，最多可支持输入 1000 个，支持通配符 * 匹配任意字符串。输入多个时以 `` 分割，或者一行仅输入一个。 
       若您需要对同类型名单内已设定的 Agent 列表进行增删处理，那么您可调用 获取域名配置 接口获取已配置的全部列表后，在此基础上添加或删除您期望变更的值，最后重新传入 user_agents。 
 allow_empty (Boolean): 是  是否允许 UA 为空或者不包含 UA 字段的请求访问加速域名。取值如下所示： 
       - true：允许 
       - false：不允许""",
    "update_image_domain_area_access": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     domain (String): 是  域名，您可以通过获取服务下全部域名获取服务下域名信息。 
 area_access (Object of AreaAccess): 是  区域访问限制配置 

字段： AreaAccess
 enable (Boolean): 是  是否开启区域限制 
 rule_type (String): 是  黑白名单设置类型，取值如下所示： 
       - deny：黑名单 
       - allow：白名单 
 areas (Array of String): 是  地区列表。取值请见国家名称对照表表格中国家简写该列内容。""",
    "get_service_domains": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "update_refer": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     refer_link (Object of ReferLink): 是  Referer 配置 
 domain (String): 是  域名，您可以通过获取服务下全部域名获取服务下域名信息。 

字段： ReferLink
 enabled (Boolean): 否  是否开启 Referer 访问限制，取值如下所示： 
       - true：开启 
       - false：关闭 
 is_white_mode (Boolean): 否  是否选择白名单模式，取值如下所示： 
       - true：选择白名单 
       - false：选择黑名单 
 values (Array of String): 否  Referer 通用规则列表，根据是否为白名单，为对应的白/黑名单的值。您可以指定一个或者多个 IP 地址，域名和泛域名。支持填写二级域名，支持混合输入。 
       - IP 地址格式支持 IPv4 和 IPv6，最多可输入 1000 个 IP 地址。 
       - 域名无需包含http:// 或 https://。 
       - values 和 regex_valses 均存在时，两者同时生效。 
       - 若您需要对同类型名单内已设定的 values 地址进行增删处理，那么您可调用 获取域名配置 接口获取已配置的全部地址列表后，在此基础上添加或删除您期望变更的值，最后重新传入 values。 
 allow_empty_refer (Boolean): 否  是否允许空 Referer 访问，取值如下所示： 
       - true：允许 
       - false：不允许 
 regex_values_enabled (Boolean): 否  是否启用正则表达列表，取值如下所示： 
       - true：启用 
       - false：不启用 
 regex_values (Array of String): 否  Referer 的正则表达式的列表，仅支持填写 IPv4 和 IPv6 格式的 IP 地址，参数长度范围为（1，1024）。不支持域名、泛域名、CIDR 网段。最多支持设置 100 条规则。""",
    "update_image_domain_ip_auth": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     domain (String): 是  待修改配置的域名，您可以通过获取服务下全部域名获取服务下域名信息。 
 ip_auth (Object of IpAuth): 是  黑白名单配置 

字段： IpAuth
 enabled (Boolean): 是  是否开启黑白名单配置，取值如下所示： 
       - true：开启黑白名单配置 
       - false：关闭黑白名单配置 
 is_white_mode (Boolean): 是  是否是 IP 白名单，取值如下所示： 
       - true：配置白名单 
       - false：配置黑名单 
 values (Array of String): 是  黑白名单 IP 地址，您可以指定一个或者多个 IP 地址（如 192.0.2.0）和 IP 地址网段（192.0.2.0/24）。IP 地址和网段可以是 IPv4 或 IPv6 格式，可混合填写，最多可输入 1000 个地址。 
       若您需要对同类型名单内已设定的 values 地址进行增删处理，那么您可调用 获取域名配置 接口获取已配置的全部地址列表后，在此基础上添加或删除您期望变更的地址，最后重新传入 values。""",
    "update_response_header": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     domain (String): 否  域名，您可以通过获取服务下全部域名获取服务下域名信息。 
 resp_hdrs (Array of RespHdrs): 否  Resp Headers 配置 

字段： RespHdrs
 key (String): 否  Header Key，请见支持配置的响应头。 
 value (String): 否  Header Value，设置该响应头字段的值。字段值不能超过 1,024 个字符，可以包含除美元符号（$），Delete（ASCII code 127）外的可打印 ASCII 字符。 
 access_origin_control (Boolean): 是  在 veImageX 响应用户请求时，是否校验请求头中的 Origin 字段。仅对响应头部Access-Control-Allow-Origin有效，取值如下所示： 
       - true：开启校验，veImageX 会校验 Origin 字段。 
       	- 如果校验成功，响应头中会包含 Access-Control-Allow-Origin 字段。字段值与 Origin 字段值相同。 
       	- 如果校验失败，响应头中不会包含 Access-Control-Allow-Origin 字段。 
       - false：关闭校验，veImageX 不会校验 Origin 字段。响应头中将始终包含 Access-Control-Allow-Origin 头部和您配置的值。""",
    "describe_image_volc_cdn_access_log": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Domain (String): 是  域名，您可以通过获取服务下全部域名获取服务下域名信息。 
 Region (String): 是  地域。支持以下取值： 
       - chinese_mainland：中国大陆，返回的日志包的名称不包含 outsideChineseMainland； 
       - global：全球； 
       - outside_chinese_mainland：全球（除中国大陆），返回的日志包的名称包含 outsideChineseMainland。 
       - 该参数仅当您启用了中国大陆外加速区域时，配置才会生效，否则仅返回国内日志数据。 
       - 您可以登录 veImageX 控制台参考域名配置 > 高级配置开启全球加速，两个工作日左右全球加速启用生效。 
       - 全球加速功能为 veImageX 计费项，具体计费详情请参考后付费-按量计费。 
 StartTime (Long): 是  查询日志开始时间戳，Unix 时间，单位为秒。 
       例如：指定起始时间为1641844915，代表 2022-01-11 04:01:55 UTC。 在查询返回的日志列表中，第一个统计在内的日志包名称是domain_20220111050000_20220111060000.gz。该日志包中包含该域名在 05:00:00 和 05:59:59 之间的访问日志。 
       StartTime 和 EndTime 之间的时间范围不能大于 30 天。 
 EndTime (Long): 是  查询日志结束时间戳，Unix 时间，单位为秒。 
       例如：指定结束时间为1641953589，代表 2022-01-12 10:13:09 UTC。在查询返回的日志列表中，最后一个统计在内的日志包名称是 domain_20220112100000_20220112110000.gz。该日志包中包含该域名在 10:00:00 和 10:59:59 之间的访问日志。 
       StartTime 和 EndTime 之间的时间范围不能大于 30 天。 
 PageNum (Integer): 是  指定的页码，系统只返回该页面上的日志包数据。起始值为 1，如果指定页码不存在，则返回空值。 
       建议第一次提交查询时指定页码为 1。您可以根据响应正文中的TotalCount和PageSize参数的值计算结果页数。之后在查询中指定PageNum来获取该页面上日志包。 
 PageSize (Integer): 是  指定查询结果中每页包含的日志包数量。取值范围为 [10, 100]。""",
    "update_image_file_key": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     OriKey (String): 是  源文件名，即上传文件的存储 Key。 
 DstKey (String): 是  重命名后的文件名，存储 Key 详细命名规范请参看 veImageX 存储 Key 通用字符规则。""",
    "update_image_domain_config": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     domains (Array of String): 是  域名列表，您可以通过获取服务下全部域名获取服务下域名信息。 
 https (Object of Https): 否  HTTPS 配置 
 referer_link (Object of RefererLink): 否  Referer 防盗链配置 
 url_auth (Object of UrlAuth): 否  URL 鉴权配置 
 ip_auth (Object of IpAuth): 否  IP 黑白名单配置 
 user_agent_acl (Object of UserAgentAcl): 否  UA 访问限制配置 
 area_acl (Object of AreaAcl): 否  区域访问限制，不传不更新 
 advanced (Object of Advanced): 否  高级配置 
 resp_hdrs (Array of RespHdrs): 否  HTTP 响应头配置 
 adaptfmt (Object of Adaptfmt): 否  自适应格式配置 
 do_slim (Object of DoSlim): 否  集智瘦身配置 
 global_acceleration (Object of GlobalAcceleration): 否  全球加速配置 
 remote_auth (Object of RemoteAuth): 否  远程鉴权设置 
 page_optimization (Object of PageOptimization): 否  页面优化设置，仅素材托管服务下域名支持配置。 
 share_cache (Object of ShareCache): 否  共享缓存配置。共享缓存允许同账号下多个加速域名共享同一份节点上的缓存。在 veImageX 中，您可以通过设置共享缓存配置，使各个子站点之间可共享相同的公共资源，以减少带宽的使用，提高资源命中率。详细功能说明参看共享缓存。 
       共享缓存为白名单功能，请提交工单联系技术支持为您的账号开启配置能力。 

字段： Https
 enable_http2 (Boolean): 是  是否开启 http2，取值如下所示： 
       - true：开启 
       - false：关闭 
 enable_https (Boolean): 是  是否开启 https，取值如下所示： 
       - true：开启 
       - false：关闭 
 tls_versions (Array of String): 是  支持的 tls 版本。取值如下所示： 
       - tlsv1.0 
       - tlsv1.1 
       - tlsv1.2 
       - tlsv1.3 
 cert_id (String): 否  需要关联的证书 ID，若enable_https为true，则为必填。 
 enable_force_redirect (Boolean): 否  是否开启强制跳转，取值如下所示： 
       - true：开启 
       - false：关闭 
 force_redirect_type (String): 否  仅当enable_force_redirect取值为true时需要配置，强制跳转类型。 
       取值如下所示： 
       - http2https：HTTP 到 HTTPS 
       - https2http：HTTPS 到 HTTP 
 force_redirect_code (String): 否  仅当enable_force_redirect取值为true时需要配置，强制跳转状态码。 
       取值如下所示： 
       - 301：返回给用户 301 状态码进行重定向。 
       - 302：返回给用户 302 状态码进行重定向。 
 hsts (Object of Hsts): 否  HSTS 配置 

字段： RefererLink
 enabled (Boolean): 是  是否开启 Referer 防盗链，取值如下所示： 
       - true：开启 
       - false：关闭 
 is_white_mode (Boolean): 是  是否选择白名单，取值如下所示： 
       - true：配置白名单 
       - false：配置黑名单 
 values (Array of String): 否  黑白名单 Referer 规则，可输入域名或 IP 地址，最大限制为 1000 条。 
 allow_empty_refer (Boolean): 否  是否允许空 Referer，取值如下所示： 
       - true：允许空 Referer 
       - false：不允许空 Referer 
 regex_values (Array of String): 否  正则表达式规则列表，最大限制为 100 条。 
 ignore_case (Boolean): 否  是否忽略大小写。取值如下所示：  
       - true: （默认）大小写不敏感。  
       - false: 大小写敏感。 
 ignore_scheme (Boolean): 否  Referer 头部值是否必须以 HTTP 或者 HTTPS 开头。取值如下所示：  
       - true: 表示不以 HTTP 或者 HTTPS 开头的 Referer 头部值是合法的。在这个情况下，veImagex 会尝试将其与 Referers 列表匹配。  
       - false: （默认）表示不以 HTTP 或者 HTTPS 开头 Referer 头部值是非法的。在这个情况下，veImagex 判定为不匹配 CommonType 下的这个 Referers 列表。 

字段： UrlAuth
 enabled (Boolean): 是  是否开启 URL 鉴权配置，取值如下所示： 
       - true：是 
       - false：否 
 type_a (Object of TypeA): 是  A 鉴权配置 
 type_b (Object of TypeB): 是  B 鉴权配置 
 type_c (Object of TypeC): 是  C 鉴权配置 
 type_d (Object of TypeD): 是  D 鉴权配置 

字段： IpAuth
 enabled (Boolean): 是  是否开启黑白名单配置，取值如下所示： 
       - true：开启黑白名单配置 
       - false：关闭黑白名单配置 
 is_white_mode (Boolean): 是  是否是 IP 白名单，取值如下所示： 
       - true：配置白名单 
       - false：配置黑名单 
 values (Array of String): 是  黑白名单 IP 地址，最大限制为 1000。 

字段： UserAgentAcl
 enabled (Boolean): 是  是否开启 UA 访问限制，取值如下所示： 
       - true：开启 
       - false：未开启 
 rule_type (String): 是  黑白名单设置类型，取值如下所示： 
       - deny：黑名单 
       - allow：白名单 
 user_agents (Array of String): 是 safari"]  Agent 列表，最多可支持输入 1000 个，支持通配符 *` 匹配任意字符串。 
 allow_empty (Boolean): 是  表示是否允许 UA 为空或者不包含 UA 字段的请求访问加速域名。取值如下所示： 
       - true：允许 
       - false：不允许 

字段： AreaAcl
 enabled (Boolean): 是  是否开启区域限制，取值如下所示： 
       - true：开启 
       - false：未开启 
 rule_type (String): 是  黑白名单设置类型，取值如下所示： 
       - deny：黑名单 
       - allow：白名单 
 areas (Array of String): 是  地区列表。取值请见国家名称对照表表格中国家简写该列内容。 

字段： Advanced
 enable_ipv6 (Boolean): 否  是否开启 IPV6，取值如下所示： 
       - true：开启 
       - false：关闭 
 enable_gzip (Boolean): 否  是否开启 Gzip 压缩，取值如下所示： 
       - true：开启 
       - false：关闭 
 enable_br (Boolean): 否  是否开启 Brotli 压缩，取值如下所示： 
       - true：开启 
       - false：关闭 
       支持同时配置 Gzip 压缩和 Brotli 压缩，详细内容请参考智能压缩。 

字段： RespHdrs
 key (String): 是  Header Key，请见支持配置的响应头。 
 value (String): 是  Header Value，设置该响应头字段的值。字段值不能超过 1,024 个字符，可以包含除美元符号（$），Delete（ASCII code 127）外的可打印 ASCII 字符。 

字段： Adaptfmt
 enabled (Boolean): 是  是否开启自适应，取值如下所示： 
       - true：开启自适应 
       - false：关闭自适应 
 adapt_formats (Array of String): 是  自适应格式列表，支持以下取值： 
       - webp：WEBP 自适应 
       - heic：HEIC 自适应 
       - avif：AVIF 自适应 
 check_adapt_fsize (Boolean): 是  是否开启体积校验，取值如下所示： 
       - true：开启 
       - false：关闭 

字段： DoSlim
 enabled (Boolean): 是  是否开启集智瘦身，取值如下所示： 
       - true：开启集智瘦身 
       - false：关闭集智瘦身 
 discard_slimed_file (Boolean): 是  是否关闭持久化。取值如下所示： 
       - true：关闭 
       - false：开启 

字段： GlobalAcceleration
 enabled (Boolean): 是  是否开启全球加速，取值如下所示： 
       - true：开启 
       - false：关闭 

字段： RemoteAuth
 enabled (Boolean): 是  是否开启远程鉴权，取值如下所示： 
       - true：是 
       - false：否 
 match_rule (Array of MatchRule): 是  生效对象 
 auth_server (Object of AuthServer): 是  鉴权服务器设置 
 auth_request_query (Object of AuthRequestQuery): 是  鉴权请求参数设置 
 auth_request_header (Object of AuthRequestHeader): 是  鉴权请求头设置 
 auth_response (Object of AuthResponse): 是  鉴权响应设置 

字段： PageOptimization
 enabled (Boolean): 是  是否开启页面优化，取值如下所示： 
       - true：是 
       - false：否 
 optimization_type (Array of String): 是  表示需要优化的对象列表。该参数有以下取值：  
       - html: （默认）表示 HTML 页面。  
       - js: 表示 Javascript 代码。  
       - css: 表示 CSS 代码。  
       如果对象列表包含 js 或者 js，html 也必须被包含。 

字段： ShareCache
 domains (Array of String): 是  共享域名。 

字段： Hsts
 enabled (Boolean): 否  是否开启 HSTS 配置，取值如下所示： 
       - true：是 
       - false：否 
 subdomain (String): 否  HSTS 配置是否也应用于加速域名的子域名。取值如下所示：  
       - include：应用于子域名站点。  
       - exclude：（默认）不应用于子域名站点。 
 ttl (Integer): 否  如果 enable_https 是 true，该参数为必填。 
       Strict-Transport-Security 响应头在浏览器中的缓存过期时间，单位是秒。取值范围是 [0,31,536,000]。31,536,000 秒表示 365 天。如果该参数值指定为 0，其效果等同于禁用 HSTS 设置。 

字段： TypeA
 main_sk (String): 是  主鉴权密钥 
 backup_sk (String): 是  备用鉴权密钥 
 sign_param (String): 是  md5hash 参数名 
 expire_time (Integer): 是  有效时间，单位为秒。取值范围为[1, 630720000]内的正整数，默认为 1800 秒。 

字段： TypeB
 main_sk (String): 是  主鉴权密钥 
 backup_sk (String): 是  备用鉴权密钥 
 expire_time (Integer): 是  有效时间，单位为秒。取值范围为[1, 630720000]内的正整数，默认为 1800 秒。 

字段： TypeC
 main_sk (String): 是  主鉴权密钥 
 backup_sk (String): 是  备用鉴权密钥 
 expire_time (Integer): 是  有效时间，单位为秒。取值范围为[1, 630720000]内的正整数，默认为 1800 秒。 

字段： TypeD
 main_sk (String): 是  主鉴权密钥 
 backup_sk (String): 是  备用鉴权密钥 
 sign_param (String): 是  md5hash 参数名 
 expire_time (Integer): 是  有效时间，单位为秒。取值范围为[1, 630720000]内的正整数，默认为 1800 秒。 
 time_param (String): 是  TimeStamp 参数名 
 time_format (String): 是  时间戳格式，取值如下所示： 
       - decimal：十进制（Unix 时间戳） 
       - heximal：十六进制（Unix 时间戳） 

字段： MatchRule
 match_operator (String): 是  匹配方式，取值如下所示：  
       - match：（默认）表示 object 匹配 Value。  
       - not_match：表示 object 不匹配 Value。  
       如果您创建了多个生效对象配置，每个配置中该参数的值必须相同。 
 object (String): 是  表示 veImageX 对哪些对象类型进行规则匹配。取值如下所示：  
       - filetype：表示特定后缀的文件。  
       - directory：表示特定文件目录下的所有文件。  
       - path：表示特定的文件。 
 value (String): 是  表示 Object 对应的具体对象，并且是大小写敏感的。参数值的长度不能超过 1,024 个字符。您可以指定一个或者多个对象。多个对象之间使用英文分号（;）分隔。该参数有以下说明：  
       - 如果 Object 是 filetype，您需要指定一个或者多个文件后缀。文件后缀可以包含英文字母和数字。多个文件后缀使用分号（;）分隔。例如 xlsx 或者 png;txt。  
       - 如果 Object 是 directory，您需要指定一个或者多个目录路径。多个目录路径使用分号（;）分隔。每个目录路径必须以斜杠（/）开头和结尾， 
       例如 /www/img/volc/;/www/doc/。您可以使用 / 表示域名下的所有目录。同时，目录路径可以包含除了以下字符的可打印 ASCII 字符： 连续斜杠（//）、百分号（%）、美元符号（$）、空格、问号（?）、Delete（ASCII code 127）  
       - 如果 Object 是 path，您需要指定一个或者多个文件路径。文件路径支持使用通配符（*）表示一个或者多个字符。多个文件路径使用分号（;）分隔。 
       例如 /www/img/volcano.png;/doc/study.docx。文件路径必须以 / 开头。同时，文件路径可以包含除了以下字符的可打印 ASCII 字符： 连续斜杠（//）、百分号（%）、美元符号（$）、空格、问号（?）、Delete（ASCII code 127） 

字段： AuthServer
 address (String): 是  鉴权服务器的主地址。主地址的格式是 :// 或 ://。该参数值的长度不能超过 100 个字符。 
       -  的值是 http 或者 https。 
       -  的值不能是 localhost。 
       -  的值不能是 127.0.0.1。 
 backup_address (String): 是  鉴权服务器的备地址。地址格式和要求与主地址 address 相同。 
 path_type (String): 是  鉴权请求的路径。鉴权地址和请求路径组成了完整的鉴权 URL。veImageX 会把用户的请求转发到该鉴权 URL。取值如下所示：  
       - constant：表示鉴权请求中的路径与用户请求中的路径相同。  
       - variable：表示您需要在 pathValue 参数中指定一个鉴权请求中的路径。 
 path_value (String): 是  表示一个鉴权请求的路径，长度不能超过 100 个字符。路径必须以斜杠（/）开头，可以包含除了以下字符的可打印 ASCII 字符： 连续斜杠（//）、百分号（%）、美元符号（$）、空格、问号（?）、Delete（ASCII code 127） 
 request_method (String): 是  在发送鉴权请求时，veImageX 所使用的请求方法。取值如下所示：  
       - default：鉴权请求所使用的方法与用户的请求相同。  
       - get：鉴权请求使用 GET 方法。  
       - post：鉴权请求使用 POST 方法。  
       - head：鉴权请求使用 HEAD 方法。 

字段： AuthRequestQuery
 action (String): 是  表示鉴权请求是否包含用户请求 URL 中的查询参数。取值如下所示：  
       - exclude：表示鉴权请求不包含任何查询参数。  
       - include：表示鉴权请求包含所有查询参数。  
       - includePart：表示鉴权请求包含指定的查询参数。 
 value (String): 是  表示 Action 参数所对应的参数值，长度不能超过1,024 个字符。该参数有以下说明：  
       - 如果 Action 是 exclude 或 include，Value 必须是 *。  
       - 如果 Action 是 includePart，您需要在 Value 参数中指定用户请求 URL 中的一个或者多个查询参数，多个查询参数使用英文分号（;）分隔。您不能指定 *。查询参数是区分大小写的，可以包含除了以下字符的可打印 ASCII 字符： 双引号（"）、空格、Delete（ASCII code 127） 该参数的默认值是 *。 
 query (Array of Query): 是  表示鉴权请求中额外的参数设置。您最多可以设置 50 个参数。 

字段： AuthRequestHeader
 host (String): 是  鉴权请求中 HOST 头部的值。该参数的默认值是 default，表示 HOST 头部的值与您的加速域名相同。 
 action (String): 是  鉴权请求头是否包含用户请求头。取值如下所示：  
       - exclude：表示鉴权请求头中不包含任何用户请求头。  
       - include：表示鉴权请求头中包含所有用户请求头。  
       - includePart：表示鉴权请求头包含指定的用户请求头。 
 value (String): 是  表示 Action 参数所对应的参数值，长度不能超过 1,024 个字符。该参数有以下说明：  
       - 如果 Action 是 exclude 或 include，Value 必须是 *。  
       - 如果 Action 是 includePart，Value 参数的取值是用户请求中的一个或者多个头部。多个头部使用英文分号（;）分隔。其取值不能只是 *，可以包含除了以下字符的可打印 ASCII 字符： 下划线（_）、空格、双引号（"），Delete（ASCII code 127） 该参数的默认值是 *。 
 header (Array of Header): 是  表示鉴权请求中额外的请求头设置。您最多可以设置 50 个请求头。 

字段： AuthResponse
 auth_server_status_code (Object of AuthServerStatusCode): 是  鉴权服务器状态码设置 
 auth_result_cache (Object of AuthResultCache): 是  鉴权结果缓存设置 
 auth_server_timeout (Object of AuthServerTimeout): 是  鉴权服务超时时间 
 response (Object of Response): 是  响应设置 

字段： Query
 key (String): 是  您需要设置的鉴权请求参数，长度不能超过 1,024 个字符。鉴权请求参数可以包含除了以下字符的可打印 ASCII 字符： 双引号（"）、空格、Delete（ASCII code 127） 
 value_type (String): 是  您在 Key 中设置的鉴权请求参数的类型。ValueType 有以下取值：  
       - constant：表示鉴权请求参数是一个常量。此时，您需要在 Value 中指定该常量的值。  
       - variable：表示鉴权请求参数的值来自一个变量。参见 Value 的说明。 
 value (String): 是  鉴权请求参数的值，长度不能超过 1,024 个字符，并且区分大小写。Value 有以下取值：  
       - 当 ValueType 是 constant 时，表示鉴权请求参数的值是一个常量。您需要指定该常量值。常量值不能以美元符号（$）开头，可以包含除了以下字符的可打印 ASCII 字符： 双引号（"）、Delete（ASCII code 127）  
       - 当 ValueType 是 variable 时，表示鉴权请求参数的值来自一个变量。您可以指定该变量列表中的变量。 

字段： Header
 key (String): 是  您需要设置的请求头。请求头不能是 host，长度不能超过 1,024 个字符，并且不区分大小写。请求头可以包含除了以下字符的可打印 ASCII 字符： 下划线（_）、双引号（"）、空格、Delete（ASCII code 127） 
 value_type (String): 是  请求头的类型。取值如下所示：  
       - constant：表示请求头的值是一个常量。您需要在 Value 参数中指定该常量的值。  
       - variable：表示请求头的值来自一个变量。参见 Value 的说明。 
 value (String): 是  表示请求头的值。取值如下所示：  
       - 当 ValueType 是 constant 时，您需要指定一个常量值。该常量值的长度不能超过 1,024 个字符，并且区分大小写。同时，该常量值不能以美元符号（$）开头，可以包含除了以下字符的可打印 ASCII 字符： 双引号（"）、Delete（ASCII code 127）  
       - 当 ValueType 是 variable 时，表示请求头的值来自一个变量。您可以指定该变量列表中的变量。 

字段： AuthServerStatusCode
 fail_code (String): 是  指定鉴权失败时的鉴权状态码。默认值是 401。 
       - 您可以指定范围在 400-499 中的一个或者多个状态码。多个状态码使用英文分号（;）分隔。 
       - 您也可以指定 4xx 表示 400-499 中的任意一个状态码。 
 success_code (String): 是  指定鉴权成功时的鉴权状态码。默认值是 200。 
       - 您可以指定范围在 200-299 中的一个或者多个状态码。多个状态码使用英文分号（;）分隔。 
       - 您也可以指定 2xx 表示 200-299 中的任意一个状态码。 
 default_action (String): 是  如果鉴权状态码既不是 FailCode，又不是 SuccessCode 时，veImageX 处理鉴权请求的方式。取值如下所示：  
       - reject：veImageX 认为鉴权失败。  
       - pass：veImageX 认为鉴权成功。 

字段： AuthResultCache
 action (String): 是  veImageX 是否缓存鉴权状态码。取值如下所示：  
       - nocache：veImageX 不缓存鉴权状态码。  
       - cache：veImageX 缓存鉴权状态码。 
 cache_key (Array of String): 是  缓存 key 指定了用于区分不同请求 URI 的查询参数。可以指定变量字段说明中的参数, 必须包含 URI。 
 ttl (Integer): 是  鉴权状态码的缓存时间。单位是秒。取值范围是 [1,86400]。86400 秒表示 24 小时。 

字段： AuthServerTimeout
 time (Integer): 是  鉴权超时的时间，单位是毫秒。默认值为 200，取值范围是 [200,3600]。 
 action (String): 是  鉴权超时后 veImageX 处理鉴权请求的策略。取值如下所示：  
       - reject：veImageX 认为鉴权失败。  
       - pass：veImageX 认为鉴权成功。 

字段： Response
 fail_code (String): 是  鉴权失败时 veImageX 响应用户的状态码。取值范围为 [400,499] 。默认值是 403。""",
    "update_advance": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       * 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       * 您也可以通过调用 GetAllImageServices 接口方式获取服务 ID。 
    body: A JSON structure
     domain (String): 是   
 advance (Object of Advance): 是  高级配置 

字段： Advance
 enable_ipv6 (Boolean): 是  是否开启 IPV6，取值如下所示： 
       - true：开启 
       - false：关闭 
 enable_gzip (Boolean): 是  是否开启 Gzip 压缩，取值如下所示： 
       - true：开启 
       - false：关闭 
       支持同时配置 Gzip 压缩和 Brotli 压缩，详细内容请参考智能压缩。 
 enable_br (Boolean): 是  是否开启 Brotli 压缩，取值如下所示： 
       - true：开启 
       - false：关闭 
       支持同时配置 Gzip 压缩和 Brotli 压缩，详细内容请参考智能压缩。""",
    "get_image_ocrv2": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     ImageUrl (String): 否  待识别的图片 URL，满足公网可访问。仅当 StoreUri 为空时取值有效，两者都为空时报错。 
 StoreUri (String): 是  待识别图片文件的存储 URI。 
 Scene (String): 是  图片OCR识别场景，取值如下所示： 
       - general：通用场景，用于通用印刷体场景识别文本信息。 
       - license：营业执照场景，用于识别营业执照中社会信用代码等文本信息。 
       - instrument：设备识别场景，用于一些设备显示文字识别。 
       - defect：缺陷检测场景 
       当前仅支持识别图片中简体中文和简体英文这两种文本信息。 
 InstrumentName (String): 否  待识别的设备名称，仅当 Scene 为 Instrument 时，配置有效。取值如下所示： 
       - freezing-point-tester：冰点仪 
       - brake-fluid-tester：制动液测试仪 
       - thermometer： 温度计 
       - oil-tester：机油仪 
 Extra (Object of Extra): 否  定制化保留字段，如果是正常调用忽略该字段，若为定制化需求则需要和算法开发者对齐调用方式 

字段： Extra
 Enable (Boolean): 否  默认为False，不开启Extra 
 MMServiceName (String): 否  算子名称 
 MMServiceVersion (String): 否  算子版本 
 MMServiceInput (String): 否  算子的输入参数""",
    "get_url_fetch_task": """Args:params: A JSON structure
     Id (String): 是  异步任务 ID，您可通过调用 FetchImageUrl接口获取该 ID。 
 ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "get_image_quality": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     ImageUrl (String): 是  图片存储 Uri 或访问 URL。 
       * 图片 Uri 格式，例如：tos-example/7a7979974.jpeg 
       * 图片 URL 格式，例如：https://example.org/tos-example/7a7979974.jpeg~tplv.png 
       若传 URL，必须保证 URL 公网可访问。 
 VqType (String): 是  评估工具。指定多个评估工具时使用英文逗号分隔，当前支持以下工具： 
       * nr_index 
       * vqscore 
       * advcolor 
       * blockiness 
       * noise 
       * aesmod 
       * blur 
       * cg 
       * contrast 
       * texture 
       * brightness 
       * overexposure 
       * hue 
       * saturation 
       * psnr 
       * ssim 
       * vmaf 
       * green 
       * cmartifacts 
       nr_index 工具支持评估 contrast、brightness 等多个维度。您也可以单独指定各维度，获取指定维度估值。 
 ImageUrlRef (String): 否  指定服务下的评估参照图片存储 Uri 或访问 URL，用于和 ImageUrl 图片进行特定维度的对比。 
       当 VqType 中包含 psnr、ssim、vmaf 等任一字段时，该字段为必填，否则上述评估指标无法正常输出结果。""",
    "get_image_enhance_result": """Args:body: A JSON structure
     ServiceId (String): 是  服务 ID。 
       * 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       * 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  待增强的原图地址的存储 URI 和 URL（公网可访问的 URL）。 
 Model (Integer): 是  增强模型，取值如下所示： 
       * 0：通用模型 
       * 1：低质专清模型 
 DisableAr (Boolean): 否  是否不去压缩失真。Model取值为0时选填，支持以下取值： 
       * true：不进行去压缩失真处理  
       * false：（默认）进行去压缩失真处理 
 DisableSharp (Boolean): 否  是否不自适应锐化。Model取值为0时选填，支持以下取值： 
       * true：不进行锐化处理  
       * false：（默认）进行锐化处理""",
    "get_private_image_type": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     ImageUri (String): 是  原图的存储 URI。 
 Method (String): 否  检测内容，默认为all，取值如下所示： 
       - face：图片内人脸检测 
       - cloth：图片内衣物检测 
       - all：图片内人脸和衣物均检测 
 ThresFace (Float): 否  人脸置信度，取值范围为[0, 1], 默认值为 0.52，表示高于 0.52 即为有效检测。 
 ThresCloth (Float): 否  衣物置信度，取值范围为[0, 1], 默认值为 0.8，表示高于 0.8 即为有效检测。""",
    "update_image_domain_bandwidth_limit": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。您也可以通过调用 GetAllImageServices 接口方式获取服务 ID。 
    body: A JSON structure
     domain (String): 是  域名。您可以通过调用 GetServiceDomains 接口获取域名。 
 bandwidth_limit (Object of BandwidthLimit): 是  带宽限制设置 

字段： BandwidthLimit
 enabled (Boolean): 是  是否开启带宽限制功能，取值如下所示： 
       - true：开启 
       - false：关闭 
       仅当 enabled 为 true 时，threshold、limit_type 等配置项有效。 
 threshold (Integer): 是  全局带宽阈值，指定加速域名的带宽阈值。单位为 bps，取值范围为 [1, 1000000000000000]  的整数。 
       单位换算：1 Gbps = 1000 Mbps。 
 limit_type (String): 是  全局带宽阈值，指定加速域名的带宽阈值。单位为 bps，取值范围为 [1, 1000000000000000]  的整数。 
       单位换算：1 Gbps = 1000 Mbps。 
 speed_limit_rate (Integer): 是  设置节点响应访问请求的速度下限，在 veImageX 逐步降低最大速度的过程中，最大速度不会低于该配置。 
       单位：B/S，取值范围为 [1,1073741824000]的整数。 
       单位换算：1 KB/S = 1024 B/S。 
       - 当 limit_type 为 downloadspeedlimit 时，表示每个请求的最低速度。 
       - 当 limit_type 为 speedlimit 时，表示每个 IP 地址的最低速度。 
       当 limit_type 为 randomreject 时，不支持自定义该配置。 
 speed_limit_rate_max (Integer): 是  初始速率，即初始最大速度。限速发生时， veImageX 会从该速度开始，逐步降低最大速度。 
       单位：B/S，取值范围为[1,1073741824000]的整数。默认值为 speed_limit_rate + 4096 KB/S。 
       单位换算：1 KB/S = 1024 B/S。 
       - 当 limit_type 为 downloadspeedlimit 时，表示每个请求的初始最大速度。 
       - 当 limit_type 为 speedlimit 时，表示每个 IP 地址的初始最大速度。 
       当 limit_type 为 randomreject 时，不支持自定义该配置。""",
    "update_image_domain_download_speed_limit": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。您也可以通过调用 GetAllImageServices 接口方式获取服务 ID。 
    body: A JSON structure
     domain (String): 是  域名。您可以通过调用 GetServiceDomains接口获取域名。 
 download_speed_limit (Object of DownloadSpeedLimit): 是  下载限速配置 

字段： DownloadSpeedLimit
 rules (Array of Rules): 是  限速规则配置 
 enabled (Boolean): 是  是否开启下载限速功能，取值如下所示：  
       - true：开启  
       - false：关闭  
       仅当 enabled 为 true 时，rules 等配置项有效 

字段： Rules
 match_type (String): 是  匹配类型。 
 match_value (String): 是  匹配值。 
 limit_rate (Integer): 是  限速配置。 
 limit_rate_after (Integer): 是  限制速率的起始点。 
 day_week (String): 是  星期几。 
 begin_time (String): 是  开始时间。 
 end_time (String): 是  结束时间。""",
    "update_image_mirror_conf": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。  
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Schema (String): 是  下载图片的协议，取值为：http、https。 
 Host (String): 是  镜像回源域名。 
 Hosts (JSON Map): 否  带权重回源域名。key 为 String 类型，代表镜像回源域名；value 为 Integer 类型，代表域名权重。 
 Source (String): 否  镜像源 URI，其中图片名用 %s 占位符替代，比如/obj/%s。 
 Headers (JSON Map): 是  镜像回源下载原图时，携带的 HTTP 头部，键值都为 String 类型。 
 Origin (Object of Origin): 否  镜像站 

字段： Origin
 Type (String): 是  镜像站类型 
 Param (JSON Map): 是  镜像站配置""",
    "get_image_duplicate_detection": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Urls (Array of String): 是  需要去重的图片 URL，多个地址以英文逗号分割。图片格式仅支持 JPEG（.jpeg 或 .jpg）和 PNG，支持格式混合输入。 
 Async (Boolean): 否  是否使用异步，取值如下所示： 
       * true：使用异步去重 
       * false：（默认）不使用异步去重 
 Callback (String): 否  当Async取值为true即启用异步时需要添加回调地址，地址使用 POST 请求方式。回调内容详见回调参数。 
 Similarity (Float): 否  相似度阈值。上传图片数量超过 2 张并执行去重分组时，系统将对原图中满足该阈值的图片进行分组。取值范围为 [0,1]，默认值为 0.84。最多支持两位小数。 
 ExtractorType (String): 否  图像特征提取类型，取值如下所示： 
       - hash：（默认）基于图像的像素值、颜色分布、纹理等特征生成哈希码，并通过哈希码进行比较来判定图片的相似度。该方式处理速度快，但对图片的旋转和颜色的敏感度较高，适用于大规模且纹理相对简单的图片的快速去重。 
       - cnn：通过深度学习技术来提取图像的高级语义特征，如对象、场景和纹理等，这些特征用于比较不同图像之间的相似性。该提取方式鲁棒性较好，对旋转、缩放和变形的敏感度较低，适用于纹理复杂、细节丰富的图片去重。""",
    "get_dedup_task_status": """Args:params: A JSON structure
     TaskId (String): 是  任务 ID，您可以通过调用使用图片去重获取结果值接口获取异步去重TaskId返回值。""",
    "apply_image_upload": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 SessionKey (String): 否  一次上传会话 Key。 
       本接口上一次请求的SessionKey，可在重试时带上，作为服务端的再次选路时的一个参考。 
 UploadNum (Integer): 否  上传文件的数量，将决定下发的 StoreUri 的数量，取值范围为[1,10]，默认为 1。 
 StoreKeys (Array of String): 否  上传文件的存储 Key。默认使用随机生成的字符串作为存储 Key。 
       * 数组长度和UploadNum保持一致。 
       * 存储 Key 详细命名规范请参看 veImageX 存储 Key 通用字符规则。 
 Prefix (String): 否  指定的上传文件路径。 
       * 指定Prefix时，下发的存储 Key 为：Prefix/{随机Key}{FileExtension}，其中Prefix + FileExtension最大长度限制为 145 个字节。 
       * 不支持以/开头或结尾，不支持/连续出现。 
       仅当未指定StoreKeys时生效。 
 FileExtension (String): 否  文件扩展名(如：.java, .txt, .go 等)，最大长度限制为 8 个字节。 
       仅当未指定StoreKeys时生效。 
 Overwrite (Boolean): 否  是否开启重名文件覆盖上传，取值如下所示： 
       - true：开启 
       - false：（默认）关闭 
       在指定 Overwrite 为 true 前，请确保您指定的 ServiceId 对应服务已开启了覆盖上传能力。""",
    "commit_image_upload": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 SkipMeta (Boolean): 否  是否返回图片meta信息。默认 false。 
       * true：不返回图片 meta 信息。 
       * false：获取图片 meta 信息并返回对应 meta 信息。 
       * 其中若 meta 获取超时或失败，接口返回成功，但对应 meta 信息将为空。 
       * 如果强依赖 meta 请参考图片Meta信息获取。 
    body: A JSON structure
     SessionKey (String): 是  一次上传会话 Key。 
       请参考获取文件上传地址获取。 
 SuccessOids (Array of String): 否  上传成功的资源 ID。 
 DecryptKeys (Array of String): 否""",
    "get_image_upload_files": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 Limit (Integer): 否  获取文件个数，最大值为 100。 
 Marker (Long): 否  分页标志。""",
    "delete_image_upload_files": """Args:params: A JSON structure
     ServiceId (String): 是  待删除文件所在的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     StoreUris (Array of String): 是  待删除文件的存储 URI 列表，最多传 1000 个。您可以通过调用获取服务下的上传文件来获取所需的文件 URI。 
 StoreVersions (Array of String): 否  待删除文件的存储版本 ID。传值时需要和 StoreUris 一一对应。您可在 veImageX 控制台资源管理查看文件版本号，或调用 GetImageStorageVersionFiles 查询服务下所有文件的版本信息。 
       当删除文件未指定 StoreVersions，那么删除逻辑将根据版本控制的状态产生以下差异。 
       - 若此时版本控制为未开启，则 StoreUris 对应文件将被永久删除，不可恢复。 
       - 若此时版本控制为开启，则 StoreUris 对应文件未被真正删除，该文件可以被恢复，同时将增加一个删除标记用于标识该文件为删除状态。 
       - 若此时版本控制为暂停，则根据版本 ID 是否为 null 而有以下差异： 
       	- 若文件的版本 ID 为 null，则 StoreUris 对应文件被真正删除，不可恢复，同时将增加一个删除标记用于标识该文件为删除状态。 
       	- 若文件的版本 ID 不为 null，则 StoreUris 对应文件未被真正删除，而是转换为历史版本保留。该文件可以被恢复，同时将增加一个删除标记。""",
    "get_image_alert_records": """Args:body: A JSON structure
     Name (String): 否  告警名称，正则匹配。不填则查询所有告警记录。 
 RuleId (String): 否  告警规则 ID，完全匹配。不填则查询所有告警记录。 
 AppId (String): 否  应用 ID。您可以通过调用 GetImageXQueryApps 的方式获取账号下全部的 AppId。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如 2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 90 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-18T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如 2019-06-02T00:00:00+08:00。 
 Limit (Integer): 否  获取个数限制。默认值为 10，取值范围为 (0,100]。 
 Marker (String): 否  分页偏移量。默认值为 0，表示从最新一个开始获取。""",
    "get_image_service": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "get_image_style_detail": """Args:params: A JSON structure
     StyleId (String): 是  样式 ID。""",
    "update_image_style": """Args:body: A JSON structure
     DoUpload (Boolean): 否  是否执行对上传图像的样式渲染和渲染结果图上传操作，默认为``。取值如下所示： 
       * true：将所有已上传至该样式的图像以更新后的样式数据进行重新处理，并将结果图上传至该样式所绑定服务的存储中。其更新后的结果图 Uri 请在获取样式详情中获取。 
       * false：（默认）不执行上述操作。 
       建议您仅在手动保存样式或关闭当前页面时指定DoUpload为TRUE，可节省后端渲染成本。 
 Style (Object of Style): 是  更新的样式结构，包含图片编辑、文字编辑、背景等自定义参数配置，具体请参考样式结构。""",
    "add_domain_v1": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     domain (String): 是  新增域名。 
 https (Array of Https): 否  证书配置，海外加速或者全球加速为必选，否则审核不通过。 
 access_control (Array of AccessControl): 否  访问控制配置。 
 resp_hdrs (Array of RespHdrs): 否  请求需要添加的响应头。 

字段： Https
 enable_https (Boolean): 否  是否开启 Https，取值如下所示： 
       - true：开启 
       - false：关闭 
 force_https (Boolean): 否  是否强制使用 Https，取值如下所示： 
       - true：强制 
       - false：不强制 
 cert_id (String): 否  证书 ID，若enable_https为true，则为必选。 

字段： AccessControl
 refer_link (Array of ReferLink): 否  Referer 配置。 

字段： RespHdrs
 key (String): 是  Header Key，请见支持配置的响应头。 
 value (String): 否  Header Value，设置该响应头字段的值。字段值不能超过 1,024 个字符，可以包含除美元符号（$），Delete（ASCII code 127）外的可打印 ASCII 字符。 

字段： ReferLink
 enabled (Boolean): 是  是否开启 Referer 防盗链，取值如下所示： 
       * true：开启 
       * false：关闭 
 is_white_mode (Boolean): 否  是否配置白名单，取值如下所示： 
       - true：配置白名单 
       - false：配置黑名单 
 values (Array of String): 否  根据是否为白名单，为对应的白/黑名单的值。 
 allow_empty_refer (Boolean): 否  是否允许空 Referer，取值如下所示： 
       - true：允许空 Referer 
       - false：不允许空 Referer""",
    "get_templates_from_bin": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 TemplateNamePattern (String): 否  仅返回模板名称包含该字符串的图片模板，不填或者为空则返回所有模板。 
 Offset (Integer): 否  分页偏移。默认 0。取值为1，表示跳过第一条数据，从第二条数据开始取值。 
 Limit (Integer): 否  分页获取条数，默认 10。 
 Asc (String): 否  是否按照模板创建时间升序查询，支持取值：true、false，默认为false。""",
    "create_image_compress_task": """Args:params: A JSON structure
     ServiceId (String): 是  压缩文件存储的目标服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     FileList (Array of FileList): 否  与IndexFile为二选一，必填。 
       压缩文件列表配置，最多可支持 3000 个文件，压缩前文件的总大小不得超过 45000 MB。若超出限制，则取消压缩打包操作，致使打包任务失败。 
 IndexFile (String): 否  与 FileList为二选一，必填。 
       索引文件的 StoreUri，为 .txt 文件，该索引文件需上传至指定服务对应存储中。 
       该索引文件内需填写待压缩文件的地址，每行填写一个，最多可填写 3000 行。压缩前文件的总大小不超过 45000 MB。若超出限制，则取消压缩打包操作，致使打包任务失败。 
 Output (String): 否  压缩后文件压缩包的指定名称，默认为随机 Key。 
 ZipMode (Integer): 是  文件的处理方式，取值如下所示： 
       - 0：使用 ZIP DEFLATE 压缩方法，将文件进行压缩并打包为 ZIP 包。该方式适用于需要长期存储大量未经压缩的文件的场景，以节省存储空间。但需注意的是，若文件本身已经过压缩处理，将会因为文件的可压缩空间有限，导致该方式的压缩效果不明显。 
       - 1：仅将文件打包为 ZIP 包，但不执行压缩操作。该方式适用于快速整理文件而无需节省存储空间的场景。例如已经过压缩的文件的打包存储，以便于传输或归档。 
 Callback (String): 否  POST 类型的回调 URL，用于接收相关回调 JSON 类型数据。回调参数请参考回调内容。 

字段： FileList
 Url (String): 是  公网可访问的待压缩文件 URL 
 Alias (String): 否  - 指定时，为 URL 文件所在压缩包中的别名。输入规则如下所示： 
       	- 支持汉字、字母、数字及符号-、_和.； 
       	- 不能以-、_和.开头； 
       	- 长度不得超过 100 个字符。 
       - 不指定时，若能提取原文件名称时，则以 URL 原文件名称；否则，使用随机名称。 
 Folder (String): 否  指定源文件在压缩包中的文件夹，不传时则将该资源存储至一级目录下。输入规则如下所示： 
       - 支持汉字、字母、数字及符号-、_和.； 
       - 不能以-、_和.开头； 
       - 不能以/结尾。 
       - 建议命名长度不超过 256 个字节。 
       - 建议您在命名中仅使用 -、_ 和 . 这三种符号。如果您使用了其他符号，可能因操作系统不支持导致处理异常。""",
    "get_compress_task_info": """Args:params: A JSON structure
     TaskId (String): 是  异步任务 ID 
 ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "get_resource_url": """Args:params: A JSON structure
     ServiceId (String): 是  资源所在的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 Domain (String): 是  域名。您可以通过调用 OpenAPI 获取服务下所有域名获取。 
 URI (String): 是  文件存储 Uri。您可以通过调用 OpenAPI 获取服务下的上传文件获取。 
 Tpl (String): 否  模板名称，缺省情况下表示无模板处理图片。您可以通过调用 OpenAPI 获取服务下所有图片模板获取。 
 Proto (String): 否  协议，默认为 http，隐私图片使用 https，公开图片支持取值 http 以及 https。 
 Format (String): 否  创建模板时设置的图片输出格式，默认为 image，支持取值有： 
       - image：表示输出原格式； 
       - 静图格式：png、jpeg、heic、avif、webp; 
       - 动图格式：awebp、heif、avis。 
 Timestamp (Integer): 否  过期时长，最大限制为 1 年，默认为 1800s。 
       仅当开启 URL 鉴权配置后，Timestamp 配置生效。""",
    "create_image_transcode_queue": """Args:body: A JSON structure
     Name (String): 是  自定义任务队列名称 
 Desc (String): 否  自定义任务队列描述，可用于备注该队列的用途。 
 IsStart (Boolean): 是  是否启动队列，开始执行离线转码操作。取值如下所示： 
       - true：启动 
       - false：不启动 
 Region (String): 否  队列区域。默认当前区域。ToB支持取值：cn、va、sg。 
 CallbackConf (Object of CallbackConf): 否  队列回调设置 

字段： CallbackConf
 Method (String): 是  回调方式。仅支持取值HTTP。 
 Endpoint (String): 是  回调 HTTP 请求地址，用于接收转码结果详情。支持使用 https 和 http 协议。 
 DataFormat (String): 否  回调数据格式。取值如下所示： 
       - XML 
       - JSON（默认） 
 Args (String): 否  业务自定义回调参数，将在回调消息的callback_args中透传出去。具体回调参数请参考回调内容。""",
    "create_image_monitor_rule": """Args:body: A JSON structure
     MonitorRule (Object of MonitorRule): 是  告警规则 

字段： MonitorRule
 Name (String): 是  自定义告警规则名称 
 Phase (String): 是  监控阶段，取值如下所示： 
       - upload：图片上传-上传 1.0 
       - uploadv2：图片上传-上传 2.0 
       - cdn：图片加载-下行网络监控 
       - client：图片加载-客户端传状态监控 
       - sensible：图片加载-感知指标监控 
 Appid (String): 是  监控的应用 ID，您可以通过调用获取应用列表的方式获取所需的 AppID。 
 OS (String): 否  监控平台，取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 Frequency (Integer): 是  监控频率，单位为分钟。取值如下所示： 
       - 5 
       - 10 
       - 20 
       - 30 
       - 40 
       - 50 
 Filter (Object of Filter): 否  维度过滤条件，具体参数请见 Filter。用于指定需要告警提示的维度配置。 
 GroupBy (String): 否  拆分维度，由公共拆分维度和自定义拆分维度组合而成。 
 Cond (Object of Cond): 是  监测规则。 
 Level (String): 是  告警级别，取值如下所示： 
       - warn：警告 
       - error：错误 
       - fatal：致命 
 Enabled (Boolean): 是  创建后是否立即开启告警，取值如下所示： 
       - true：开启 
       - false：关闭 
 Notification (Object of Notification): 是  告警通知配置。 

字段： Filter
 LogicOp (String): 是  过滤条件之间的逻辑关系，取值如下所示： 
       - and：和 
       - or：或 
 DimFilter (Array of DimFilter): 是  过滤条件 

字段： Cond
 LogicOp (String): 是  多条监控规则之间的逻辑关系，取值如下所示： 
       - and：且。表示有多条监控规则时，需满足所有监控规则才会触发告警通知。 
       - or：或。表示有多条监控规则时，满足其中一条监控规则就会触发告警通知。 
 ItemCond (Array of ItemCond): 是   

字段： Notification
 Mode (Array of String): 是  通知方式，仅支持取值 http_callback，表示回调。 
 CallbackUrl (String): 否  回调地址，Mode 包含 http_callback时，为必填。 
 SilentDur (Integer): 是  沉默周期，单位为分钟。告警发生后，若未恢复正常，则会间隔一个沉默周期后再次重复发送一次告警通知。取值如下所示： 
       - 0 
       - 30 
       - 60 
       - 360 
 Title (String): 是  告警通知标题 
 Content (String): 是  通知内容模板，模板中变量格式为 $Name$。Name 取值如下所示： 
        
       - 报警名称 
       - 报警级别 
       - 报警App 
       - 报警平台 
       - 报警时间 
       - 报警内容 

字段： DimFilter
 Dim (String): 是  维度名称，由公共过滤维度和自定义过滤维度组合而成。 
 Vals (Array of String): 是  维度取值，您可以通过调用获取自定义维度值来获取。 
 Not (Boolean): 否  纬度值是否取反，取值如下所示： 
       - true：指定维度的实际值不得满足 Vals 所有指定值 
       - false：（默认）维度值等于 Vals 中之一即可 

字段： ItemCond
 Item (String): 是  指标名称，取值参考 veImageX 告警指标定义。 
 Func (String): 是  指标取值函数，取值如下所示： 
       - max：最大值 
       - min：最小值 
       - avg：平均值 
       - pct25：25峰值 
       - pct50：50峰值 
       - pct90：90峰值 
       - pct99：99峰值 
       - sum：总和 
       各指标支持的函数参考 veImageX 告警指标定义。 
 Op (String): 是  指标比较方法，取值如下所示： 
       - LE：小于等于 
       - GE：大于等于 
       - INC：环比上升大于等于 
       - INC_LE：环比上升小于等于 
       - DEC：环比下降小于等于 
       - DEC_GE：环比下降大于等于 
       - HOH_INC：与上小时同比上升大于等于 
       - HOH_INC_LE：与上小时同比上升小于等于 
       - HOH_DEC：与上小时同比下降小于等于 
       - HOH_DEC_GE：与上小时同比下降大于等于 
       - DOD_INC：与昨天同比上升大于等于 
       - DOD_INC_LE：与昨天同比上升小于等于 
       - DOD_DEC：与昨天同比下降小于等于 
       - DOD_DEC_GE：与昨天同比下降大于等于 
 Threshold (Float): 是  指标比较阈值，需要与 CntThreshold 同时被满足才会触发告警。 
 CntThreshold (Integer): 否  样本量阈值。被监控指标超过该值时触发告警。 
 AggrInterval (Integer): 是  聚合周期，单位为分钟。被监控指标在该指定周期内满足指标比较阈值且上报量满足样本量阈值时，才会触发告警。取值如下所示： 
       - 5 
       - 10 
 RepeatCnt (Integer): 是  持续周期，当监控指标在聚合周期内，连续RepeatCnt次满足指标比较阈值且上报量满足样本量阈值时，才会触发告警。取值如下所示： 
       - 1 
       - 3 
       - 5""",
    "get_image_monitor_rules": """Args:params: A JSON structure
     Limit (Integer): 否  分页条数。默认值为 10，取值范围为（0，100]。 
 Offset (Integer): 否  分页偏移量。默认值为 0，表示从最新一个开始获取。 
 AppId (String): 否   
 NamePtn (String): 否  告警名称，以正则表达式进行筛选匹配。缺省时默认获取所有报警规则。 
 RuleId (String): 否  报警规则 ID，按照指定 ID 返回对应报警规则。缺省时默认获取所有报警规则。""",
    "update_image_monitor_rule": """Args:body: A JSON structure
     MonitorRule (Object of MonitorRule): 是  更新后的报警规则，具体请见 MonitorRule。 

字段： MonitorRule
 RuleId (String): 是  待更新的报警规则 ID，您可以调用 GetImageMonitorRules获取所需的告警规则 ID。 
 Name (String): 是  自定义告警规则名称 
 Phase (String): 是  监控阶段，取值如下所示： 
       - upload：图片上传-上传 1.0 
       - uploadv2：图片上传-上传 2.0 
       - cdn：图片加载-下行网络监控 
       - client：图片加载-客户端传状态监控 
       - sensible：图片加载-感知指标监控 
 Appid (String): 是  监控的应用 ID，您可以通过调用获取应用列表的方式获取所需的 AppID。 
 OS (String): 否  监控平台，取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 Frequency (Integer): 是  监控频率，单位为分钟。取值如下所示： 
       - 5 
       - 10 
       - 20 
       - 30 
       - 40 
       - 50 
 Filter (Object of Filter): 否  维度过滤条件，具体参数请见 Filter。用于指定需要告警提示的维度配置。 
 GroupBy (String): 否  拆分维度，由公共拆分维度和自定义拆分维度组合而成。 
 Cond (Object of Cond): 是  监测规则。 
 Level (String): 是  告警级别，取值如下所示： 
       - warn：警告 
       - error：错误 
       - fatal：致命 
 Enabled (Boolean): 是  创建后是否立即开启告警，取值如下所示： 
       - true：开启 
       - false：关闭 
 Notification (Object of Notification): 是  告警通知配置。 

字段： Filter
 LogicOp (String): 是  过滤条件之间的逻辑关系，取值如下所示： 
       - and：和 
       - or：或 
 DimFilter (Array of DimFilter): 是  过滤条件 

字段： Cond
 LogicOp (String): 是  多条监控规则之间的逻辑关系，取值如下所示： 
       - and：且。表示有多条监控规则时，需满足所有监控规则才会触发告警通知。 
       - or：或。表示有多条监控规则时，满足其中一条监控规则就会触发告警通知。 
 ItemCond (Array of ItemCond): 是   

字段： Notification
 Mode (Array of String): 是  通知方式，仅支持取值 http_callback，表示回调。 
 CallbackUrl (String): 否  回调地址，Mode 包含 http_callback时，为必填。 
 SilentDur (Integer): 是  沉默周期，单位为分钟。告警发生后，若未恢复正常，则会间隔一个沉默周期后再次重复发送一次告警通知。取值如下所示： 
       - 0 
       - 30 
       - 60 
       - 360 
 Title (String): 是  告警通知标题 
 Content (String): 是  通知内容模板，模板中变量格式为 $Name$。Name 取值如下所示： 
        
       - 报警名称 
       - 报警级别 
       - 报警App 
       - 报警平台 
       - 报警时间 
       - 报警内容 

字段： DimFilter
 Dim (String): 是  维度名称，由公共过滤维度和自定义过滤维度组合而成。 
 Vals (Array of String): 是  维度取值，您可以通过调用获取自定义维度值来获取。 
 Not (Boolean): 否  纬度值是否取反，取值如下所示： 
       - true：指定维度的实际值不得满足 Vals 所有指定值 
       - false：（默认）维度值等于 Vals 中之一即可 

字段： ItemCond
 Item (String): 是  指标名称，取值参考 veImageX 告警指标定义。 
 Func (String): 是  指标取值函数，取值如下所示： 
       - max：最大值 
       - min：最小值 
       - avg：平均值 
       - pct25：25峰值 
       - pct50：50峰值 
       - pct90：90峰值 
       - pct99：99峰值 
       - sum：总和 
       各指标支持的函数参考 veImageX 告警指标定义。 
 Op (String): 是  指标比较方法，取值如下所示： 
       - LE：小于等于 
       - GE：大于等于 
       - INC：环比上升 
       - DEC：环比下降 
       - HOH_INC：与上小时同比上升 
       - HOH_DEC：与上小时同比下降 
       - DOD_INC：与昨天同比上升 
       - DOD_DEC：与昨天同比下降 
 Threshold (Float): 是  指标比较阈值，需要与 CntThreshold 同时被满足才会触发告警。 
 CntThreshold (Integer): 否  样本量阈值。被监控指标超过该值时触发告警。 
 AggrInterval (Integer): 是  聚合周期，单位为分钟。被监控指标在该指定周期内满足指标比较阈值且上报量满足样本量阈值时，才会触发告警。取值如下所示： 
       - 5 
       - 10 
 RepeatCnt (Integer): 是  持续周期，当监控指标在聚合周期内，连续RepeatCnt次满足指标比较阈值且上报量满足样本量阈值时，才会触发告警。取值如下所示： 
       - 1 
       - 3 
       - 5""",
    "update_image_monitor_rule_status": """Args:body: A JSON structure
     RuleId (String): 是  待更新的告警规则 ID，您可以调用 GetImageMonitorRules获取所需的告警规则 ID。 
 Enabled (Boolean): 是  是否开启告警监测，取值如下所示： 
       - true：开启 
       - false：不开启""",
    "delete_image_monitor_rules": """Args:body: A JSON structure
     RuleIds (Array of String): 是  待删除的告警规则 ID 列表，您可以调用 GetImageMonitorRules获取所需的告警规则 ID。""",
    "delete_image_monitor_records": """Args:body: A JSON structure
     Markers (Array of String): 是  待删除的报警记录 Marker 列表，您可通过调用 GetImageAlertRecords 获取所需值。""",
    "get_image_template": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 TemplateName (String): 是  模板名称。 
       * 您可以通过调用获取服务下所有模板获取所需的模板名称。""",
    "get_all_image_templates": """Args:params: A JSON structure
     ServiceId (String): 是  服务ID 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 TemplateNamePattern (String): 否  支持的字符正则集合为[a-zA-Z0-9_-]。指定时返回模板名称包含该字符串的图片模板，不填或者为空则返回所有模板。 
 Offset (Integer): 否  分页偏移量，默认 0。取值为 1 时，表示跳过第一条数据，从第二条数据取值。 
 Limit (Integer): 否  分页获取条数，默认 10。 
 Asc (String): 否  是否按照模板创建时间升序查询，默认为false。 
       * 取值为true时，表示按升序查询。 
       * 取值为false时，表示降序查询。""",
    "update_res_event_rule": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     EventRules (Array of EventRules): 是  事件通知规则 

字段： EventRules
 EventType (Array of String): 是  事件类型。取值如下所示： 
       - Upload：上传文件 
       - Delete：删除文件 
       - Mirror：镜像回源 
       - Migrate：数据迁移 
       - OffTrans：离线转码（素材托管服务配置无效） 
       - TplStore：模板持久化存储（素材托管服务配置无效） 
 MatchRule (String): 否  匹配规则的正则表达式。仅当资源的 StoreKey 匹配该正则表达式时触发事件通知。缺省情况下表示匹配所有资源。 
 CallbackUrl (String): 是  回调 URL，以 http:// 或 https:// 开头，需满足公网可访问。当事件触发时，会向该 URL 发送 HTTP POST 请求，body 为具体的事件信息。具体回调参数详见回调内容。 
 Enable (Boolean): 是  规则启用状态，取值如下所示： 
       - true：开启 
       - false：关闭""",
    "update_image_upload_overwrite": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考GetAllImageServices。 
    body: A JSON structure
     UploadOverwrite (Boolean): 是  是否开启重名覆盖上传，取值如下所示： 
       - true：开启 
       - false：关闭""",
    "get_image_storage_files": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 Marker (String): 否  上一次列举返回的位置标记，作为本次列举的起点信息。默认值为空。 
 Limit (Long): 否  一次查询列出的文件信息条目数，取值范围为[1,1000]。默认值为 10。 
 Prefix (String): 否  指定需要查询文件的前缀，只有资源名匹配该前缀的文件会被列出。缺省时将返回所有文件信息。 
       例如，一个存储服务中有三个文件，分别为 Example/imagex.png、Example/mov/a.avis 和 Example/mov/b.avis。若指定 Prefix 取值 Example/且指定 Delimiter 取值 /：则返回 Example/imagex.png，并在 CommonPrefix 里返回 Example/mov/。 
 Delimiter (String): 否  指定目录分隔符，默认值为空。所有文件名字包含指定的前缀，第一次出现 Delimiter 字符之间的文件作为一组元素（即 CommonPrefixe）。""",
    "get_sync_audit_result": """Args:body: A JSON structure
     AuditAbility (Integer): 是   
 AuditDimensions (Array of String): 是   
 EnableLargeImageDetect (Boolean): 是   
 ImageUri (String): 是   
 DataId (String): 是   
 AuditTextDimensions (Array of String): 是""",
    "update_image_file_ct": """Args:params: A JSON structure
     ServiceId (String): 是  待更新文件所在的服务 ID。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     StoreUri (String): 是  待更新文件的存储 URI，您可以通过调用获取服务下的上传文件来获取所需的文件 URI。 
 StorageContentType (String): 是  设置更新后的 Content-Type 值。 
       请确保更新后的 Content-Type，在服务维度设置的 Content-Type 白名单内。""",
    "create_image_analyze_task": """Args:body: A JSON structure
     Name (String): 是  自定义离线评估任务名称 
 Desc (String): 否  任务描述，可作为该条任务的备注信息。 
 Type (String): 是  任务类型。取值如下所示： 
       - OnlineUrl（暂不支持） 
       - SdkUrl（暂不支持） 
       - UrlFile：在线提交 URL 离线评估，即在.txt 文件（评估文件）内填写了待评估图片文件 URL，并将该 txt 文件上传至指定服务后获取并传入该文件的 StoreUri。 
       - UriFile：在线提交 URI 离线评估，即在.txt 文件（评估文件）内填写了待评估图片文件 URI，并将该 txt 文件上传至指定服务后获取并传入该文件的 StoreUri。 
 ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 Tpl (String): 否  仅当Type 取值 UriFile 时，配置有效。 
       模板名称，您可通过调用 GetAllImageTemplates 获取服务下所有已创建的 TemplateName。 
 ResUri (Array of String): 否  txt 评估文件的 Store URI，该文件需上传至指定服务对应存储中。 
       - Type 取值 UrlFile 时，填写合法 URL 
       - Type 取值 UriFile 时，填写指定服务的存储 URI 
 Region (String): 是  任务地区。当前仅支持取值 cn，表示国内。""",
    "update_image_analyze_task": """Args:body: A JSON structure
     TaskId (String): 是  待更新的任务 ID，您可以通过调用 GetImageAnalyzeTasks 获取指定地区全部离线评估任务详情。 
 Name (String): 是  任务名称 
 Desc (String): 否  任务描述 
 ServiceId (String): 是  服务 ID 
 ResUri (Array of String): 否  txt 评估文件的 Store URI，该文件需上传至指定服务对应存储中。 
       - Type 取值 UrlFile 时，填写合法 URL 
       - Type 取值 UriFile 时，填写指定服务的存储 URI 
 EvalPerStage (Boolean): 否  仅当Type 取值 UriFile 时，配置有效。 
       是否模拟模板每阶段输出，取值如下所示： 
       - true：是，一个模版中可以选择多种图像处理, 模拟输出时会将所有的处理逐步叠加并编码为最终图片格式运行并输出评估结果。 
       - false：否。 
 Tpl (String): 否  仅当Type 取值 UriFile 时，配置有效。 
       模板名称，您可通过调用 GetAllImageTemplates 获取服务下所有已创建的 TemplateName。""",
    "delete_image_analyze_task": """Args:body: A JSON structure
     TaskId (String): 是  待删除的任务 ID，您可以通过调用 GetImageAnalyzeTasks 获取指定地区全部离线评估任务 ID。""",
    "get_image_analyze_tasks": """Args:params: A JSON structure
     Region (String): 否  任务地区。默认为 cn，表示国内。 
 SearchPtn (String): 否  返回任务名称或描述中包含该值的任务。 
 Limit (Integer): 否  分页条数。取值范围为 (0,100]，默认值为 100。 
 Offset (Integer): 否  分页偏移量，默认为 0。取值为 1 时，表示跳过第一条数据，从第二条数据取值。 
    body: A JSON structure
     Name (String): 是  任务名称 
 Desc (String): 否  任务描述 
 Type (Integer): 是  任务类型。取值1表示在线提交URL，取值2表示在线提交URI，取值3表示在线访问触发，取值4表示SDK URL触发 
 ServiceId (String): 是  服务ID 
 SampleRate (Float): 否  采样率。取值范围(0,1] 
 Tpl (String): 否  模板 
 Domain (Array of String): 否  域名列表 
 ResUri (String): 否  URL/URI zip包的TOS URI。在线提交类任务必填，上传至ServiceId对应的存储下 
 EvalPerStage (Boolean): 否  是否模拟模板每阶段输出。仅当Type=2时有效""",
    "delete_image_analyze_task_run": """Args:body: A JSON structure
     TaskId (String): 是  待删除执行记录的任务 ID，您可以通过调用 GetImageAnalyzeTasks 获取指定地区全部离线评估任务 ID。 
 RunId (String): 是  执行 ID，您可以通过调用 GetImageAnalyzeResult 获取该任务全部的执行记录查看执行 ID。""",
    "get_image_analyze_result": """Args:params: A JSON structure
     TaskId (String): 是  任务 ID，您可以通过调用 GetImageAnalyzeTasks 获取指定地区全部离线评估任务 ID。 
 StartTime (Long): 是  任务运行开始时间，Unix 时间戳。 
 EndTime (Long): 是  任务运行结束时间，Unix 时间戳。 
 RunId (String): 否  任务执行 ID 
 Limit (Integer): 否  分页条数。默认值为 10。 
 Offset (Integer): 否  分页偏移量，默认为 0。取值为 1 时，表示跳过第一条数据，从第二条数据取值。 
 File (String): 否  文件名""",
    "update_image_analyze_task_status": """Args:body: A JSON structure
     TaskId (String): 是  待更新的任务 ID，您可以通过调用 GetImageAnalyzeTasks 获取指定地区全部离线评估任务 ID。 
 Status (String): 是  更新后的任务状态。取值如下所示： 
       - Running：进行中 
       - Suspend：暂停 
       - Done：结束""",
    "get_image_audit_result": """Args:params: A JSON structure
     TaskId (String): 是  任务 ID，您可通过调用 查询所有审核任务 获取所需的任务 ID。 
 Type (String): 否  审核场景，缺省情况下查询全部场景的任务。取值如下所示： 
       - UrlFile：上传 txt 审核文件处理场景 
       - Url：上传审核图片 URL 处理场景 
       - Upload：图片上传场景 
 Problem (String): 否  问题类型，取值根据审核类型的不同其取值不同。缺省情况下返回全部类型任务。 
       - 基础安全审核 
       	- govern：涉政 
       	- porn ：涉黄 
       	- illegal：违法违规 
       	- terror：涉暴 
       - 智能安全审核 
       	- 图像风险识别 
       		- porn ：涉黄，主要适用于通用色情、色情动作、性行为、性暗示、性分泌物、色情动漫、色情裸露等涉黄场景的风险识别 
       		- sensitive1 ：涉敏1，具体指涉及暴恐风险 
       		- sensitive2：涉敏2，具体值涉及政治内容风险 
       		- forbidden：违禁，主要适用于打架斗殴、爆炸、劣迹艺人等场景的风险识别 
       		- uncomfortable：引人不适，主要适用于恶心、恐怖、尸体、血腥等引人不适场景的风险识别 
       		- qrcode：二维码，主要适用于识别常见二维码（QQ、微信、其他二维码等） 
       		- badpicture：不良画面，主要适用于自我伤害、丧葬、不当车播、吸烟/纹身/竖中指等不良社会风气的风险识别 
       		- sexy：性感低俗，主要适用于舌吻、穿衣性行为、擦边裸露等多种性感低俗场景的风险识别 
       		- age：年龄，主要适用于图中人物对应的年龄段识别 
       		- underage：未成年相关，主要适用于儿童色情、儿童邪典等风险识别 
       		- quality：图片质量，主要适用于图片模糊、纯色边框、纯色屏等风险识别 
       	- 图文风险识别 
       		- ad：广告，综合图像及文字内容智能识别广告 
       		- defraud：诈骗，综合图像及文字内容智能识别诈骗 
       		- charillegal：文字违规，图片上存在涉黄、涉敏、违禁等违规文字 
 ImageType (String): 否  图片类型，缺省情况下返回全部类型任务。取值如下所示： 
       - problem：问题图片 
       - frozen：冻结图片 
       - fail：审核失败图片 
 AuditSuggestion (String): 否  审核建议，缺省情况下返回全部任务。取值如下所示： 
       - nopass：建议不通过 
       - recheck：建议复审 
 Limit (Integer): 否  分页条数。取值范围为 (0,100]，默认值为 10。 
 Marker (Integer): 否  上一次查询返回的位置标记，作为本次列举的起点信息。默认值为 0。""",
    "get_image_audit_tasks": """Args:params: A JSON structure
     Region (String): 否  任务地区。仅支持默认取值 cn，表示国内。 
 Type (String): 否  审核场景，缺省情况下查询全部场景的任务。取值如下所示： 
       - UrlFile：上传 txt 审核文件处理场景 
       - Url：上传审核图片 URL 处理场景 
       - Upload：图片上传场景 
 AuditAbility (Integer): 否  审核能力，缺省情况下查询全部审核类型的任务。取值如下所示： 
       - 0：基础审核能力 
       - 1：智能审核能力 
 Status (String): 否  审核状态，缺省情况下查询全部状态的任务。取值如下所示： 
       - Running：审核中 
       - Suspend：已暂停 
       - Done：已完成 
       - Failed：审核失败 
       - Cancel：已取消 
 TaskType (String): 是  审核任务类型，当前仅支持取值为 audit。 
 Limit (Integer): 否  分页条数。取值范围为 (0,100]，默认值为 100。 
 Offset (Integer): 否  分页偏移量，默认为 0。取值为 1 时，表示跳过第一条数据，从第二条数据取值。""",
    "create_image_transcode_task": """Args:body: A JSON structure
     QueueId (String): 否  任务队列名称 ID。缺省情况下提交至账号默认任务队列。您可通过调用GetImageTranscodeQueues获取该账号下全部任务队列 ID。 
 ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 Template (String): 是  转码模板。您可通过调用 GetAllImageTemplates 获取指定服务下全部模版信息。 
 DataType (String): 是  数据类型，取值如下所示： 
       - uri：指定 ServiceId 下存储 URI。 
       - url：公网可访问的 URL。 
 DataList (Array of String): 否  DataList和Filelist二选一必填，同时配置时，DataList优先生效。 
       待转码的图片 uri 或 url 列表，建议最多不超过 10 万条。 
       - 若DataType取值uri，此处请传入指定 ServiceId 下的存储 URI。 
       - 若DataType取值url，此处请传入公网可访问的 URL。 
 FileList (Array of String): 否  DataList和Filelist二选一必填，同时配置时，DataList优先生效。 
       待转码的图片 uri 或 url 文件列表。具体使用方式如下： 
       1. 在 txt、csv 文件内填写指定数据类型的待转码图片地址，每行填写一个，建议最多不超过 10 万条。 
       2. 将该文件上传至指定服务后，获取其存储 URI。 
       3. 将该存储 URI，传入 FileList。 
 CallbackConf (Object of CallbackConf): 否  任务回调配置。缺省情况下默认使用队列回调配置。 
 ResKeyList (Array of String): 否  转码产物的存储 Key 列表，仅当 DataList 不为空时有效，长度需与DataList长度一致。不传时默认使用固定规则生成产物的存储 Key。 
       存储 Key 详细命名规范请参看 veImageX 存储 Key 通用字符规则。 
 EnableExif (Boolean): 否  转码是否保留 exif。取值如下所示： 
       - true：保留 
       - false：（默认）不保留 

字段： CallbackConf
 Method (String): 是  回调方式。仅支持取值HTTP。 
 Endpoint (String): 是  回调 HTTP 请求地址，用于接收转码结果详情。支持使用 https 和 http 协议。 
 DataFormat (String): 否  回调数据格式。取值如下所示： 
       - XML 
       - JSON（默认） 
 Args (String): 否  业务自定义回调参数，将在回调消息的callback_args中透传出去。具体回调参数请参考回调内容。 
 Type (String): 否  回调的维度类型，缺省情况下按照条目级别进行回调。取值如下所示： 
       - task：将按照任务级别进行回调。可分批回调，一个批次内最多一次性可回调 5000 条图片转码条目执行信息。 
       - entry：将按照条目级别进行回调。当该条目执行完毕，将立即产生回调。""",
    "update_image_transcode_queue": """Args:body: A JSON structure
     Id (String): 是  待更新的队列 ID，您可通过调用GetImageTranscodeQueues获取该账号下全部任务队列 ID。 
 Name (String): 是  更新后的队列名称 
 Desc (String): 否  更新后的队列描述 
 EnableCallback (Boolean): 是  是否启用回调。取值如下所示： 
       - true：启用 
       - false：不启用 
 CallbackConf (Object of CallbackConf): 否  更新后的队列回调配置 

字段： CallbackConf
 Method (String): 是  回调方式。仅支持取值 HTTP。 
 Endpoint (String): 是  回调 HTTP 请求地址，用于接收转码结果详情。支持使用 https 和 http 协议。 
 DataFormat (String): 否  回调数据格式。取值如下所示： 
       - XML 
       - JSON（默认） 
 Args (String): 否  业务自定义回调参数，将在回调消息的callback_args中透传出去。具体回调参数请参考回调内容。""",
    "update_image_transcode_queue_status": """Args:body: A JSON structure
     Id (String): 是  待更新的队列 ID，您可通过调用GetImageTranscodeQueues获取该账号下全部任务队列 ID。 
 Status (String): 是  更新后的队列状态。取值如下所示： 
       - Pending：排队中 
       - Running：执行中""",
    "delete_image_transcode_queue": """Args:body: A JSON structure
     QueueId (String): 是  待删除的队列 ID，您可通过调用GetImageTranscodeQueues获取该账号下全部任务队列 ID。 
       账号内置默认任务队列不允许被删除。""",
    "get_image_transcode_queues": """Args:params: A JSON structure
     Region (String): 否  队列所在地区。默认当前地区。ToB取值枚举：cn、va、sg。 
 SearchPtn (String): 否  返回队列名称或队列描述中包含该值的队列。默认为空，不传则返回所有队列。 
 Limit (Integer): 是  分页条数，取值范围为(0,100]。 
 Offset (Integer): 否  分页偏移量，默认为 0。取值为 1 时，表示跳过第一条数据，从第二条数据取值。 
    body: A JSON structure
     TaskId (String): 是  待更新的任务ID 
 Status (String): 是  更新后的任务状态。取值枚举：Running、Suspend、Done""",
    "get_image_transcode_details": """Args:params: A JSON structure
     QueueId (String): 是  队列 ID，您可通过调用GetImageTranscodeQueues获取该账号下全部任务队列 ID。 
 TaskId (String): 否  任务 ID，缺省情况下查询指定队列下所有任务详情。您可通过调用 GetImageTranscodeTasks获取指定队列的全部任务 ID。 
 Region (String): 否  队列所在地区。默认当前地区为 cn。 
 StartTime (Long): 是  任务提交的起始 Unix 时间戳 
       StartTime与EndTime时间间隔最大不超过 7 天。 
 EndTime (Long): 是  任务提交的截止 Unix 时间戳 
       StartTime与EndTime时间间隔最大不超过 7 天。 
 Status (String): 否  执行状态，填入多个时使用英文逗号分隔。取值如下所示： 
       - Pending：排队中 
       - Running：执行中 
       - Success：执行成功 
       - Fail：执行失败 
 SearchPtn (String): 否  返回图片 url 或 uri 中包含该值的任务。默认为空，不传则返回所有任务。 
 Limit (Long): 是  分页条数，取值范围为(0, 100]。 
 Offset (Long): 否  分页偏移量，默认为 0。取值为 1 时，表示跳过第一条数据，从第二条数据取值。""",
    "create_image_transcode_callback": """Args:body: A JSON structure
     EntryId (String): 是  任务条目 ID 
 Region (String): 否  地域。""",
    "delete_image_transcode_detail": """Args:body: A JSON structure
     EntryId (String): 否  待删除的任务条目 ID，您可通过调用GetImageTranscodeDetails获取该账号下全部执行任务条目 ID。 
 Entries (Array of String): 否  待删除的任务条目 ID 列表，您可通过调用GetImageTranscodeDetails获取该账号下全部执行任务条目 ID。""",
    "get_image_settings": """Args:params: A JSON structure
     AppId (String): 是  应用 ID，您可以通过调用获取应用列表的方式获取所需的 AppId。 
 Category (String): 否  所属组件，缺省情况下表示获取基础配置列表。 
       - 取值为HEIF时，表示获取 HEIF 解码库下配置列表； 
       - 取值为SR时，表示获取客户端下配置列表。""",
    "get_image_setting_rules": """Args:params: A JSON structure
     AppId (String): 是  应用 ID，您可以通过调用获取应用列表的方式获取所需的 AppId。 
 SettingId (String): 是  配置项 ID，您可以通过调用获取配置项列表的方式获取所需的配置项 ID。""",
    "create_image_setting_rule": """Args:body: A JSON structure
     SettingId (String): 是  配置项 ID，您可以通过调用获取配置项列表的方式获取所需的配置项 ID。 
 AppId (String): 是  应用 ID，您可以通过调用获取应用列表的方式获取所需的 AppId。 
 Rule (Object of Rule): 是  规则内容 

字段： Rule
 Value (Object of Value): 是  配置值。 
 Cond (Object of Cond): 否  匹配条件，仅当条件匹配后规则才会生效。 
 Name (String): 是  规则名称，仅支持字母、数字、下划线，最多输入 32 个字符。 

字段： Cond
 Type (String): 否  匹配条件，取值如下所示： 
       - AND：表示与 
       - OR：表示或 
 Conds (Array of Conds): 否  规则条件 

字段： Conds
 Key (String): 否  过滤维度，取值请参考规则配置条件。 
 Op (String): 否  操作符。支持取值：==、!=、>、>=、<、<=、in 
 Value (Object of Value): 否  配置值。Op为in时，为 Array of String 类型，否则为 String 类型。""",
    "update_image_setting_rule": """Args:body: A JSON structure
     AppId (String): 是  应用 ID，您可以通过调用获取应用列表的方式获取所需的 AppId。 
 SettingId (String): 是  配置项 ID，您可以通过调用获取配置项列表的方式获取所需的配置项 ID。 
 RuleId (String): 是  待更新的规则 ID，您可以通过调用获取规则列表的方式获取所需的规则 ID。 
 Rule (Object of Rule): 是  规则内容 

字段： Rule
 Value (Object of Value): 是  配置值。 
 Cond (Object of Cond): 否  匹配条件，仅当条件匹配后规则才会生效。 
 Name (String): 是  规则名称，仅支持字母、数字、下划线，最多输入 32 个字符。 

字段： Cond
 Type (String): 否  匹配条件，取值如下所示： 
       - AND：表示与 
       - OR：表示或 
 Conds (Array of Conds): 否  规则条件 

字段： Conds
 Key (String): 否  过滤维度，取值请参考规则配置条件。 
 Op (String): 否  操作符。支持取值：==、!=、>、>=、<、<=、in 
 Value (Object of Value): 否  配置值。Op为in时，为 Array of String 类型，否则为 String 类型。""",
    "delete_image_setting_rule": """Args:body: A JSON structure
     AppId (String): 是  应用 ID，您可以通过调用获取应用列表的方式获取所需的 AppId。 
 SettingId (String): 是  配置项 ID，您可以通过调用获取配置项列表的方式获取所需的配置项 ID。 
 RuleId (String): 是  待删除的规则 ID，您可以通过调用获取规则列表的方式获取所需的规则 ID。""",
    "update_image_setting_rule_priority": """Args:body: A JSON structure
     AppId (String): 是  应用 ID，您可以通过调用获取应用列表的方式获取所需的 AppId。 
 SettingId (String): 是  配置项 ID，您可以通过调用获取配置项列表的方式获取所需的配置项 ID。 
 Priorities (Array of Priorities): 是  更新后的优先级信息。 

字段： Priorities
 RuleId (String): 是  待更新优先级的规则 ID，您可以通过调用获取规则列表的方式获取所需的规则 ID。 
 Priority (Integer): 是  规则优先级。 
       如果配置项下创建了多个规则，需要填写全部规则更新后的优先级。""",
    "get_image_setting_rule_history": """Args:params: A JSON structure
     AppId (String): 是  应用 ID，您可以通过调用获取应用列表的方式获取所需的 AppId。 
 SettingId (String): 是  配置项 ID，您可以通过调用获取配置项列表的方式获取所需的配置项 ID。 
 Offset (Integer): 否  分页偏移量，用于控制分页查询返回结果的起始位置，以便对数据进行分页展示和浏览。默认值为 0。 
       例如，指定分页条数 Limit = 10，分页偏移量 Offset = 10，表示从查询结果的第 11 条记录开始返回数据，共展示 10 条数据。 
 Limit (Integer): 否  分页查询时，显示的每页数据的最大条数。取值范围为 [1,100]，默认值为 10。""",
    "get_image_add_on_tag": """Args:params: A JSON structure
     Key (String): 是  组件标签 key。取值固定为功能属性，返回相关标签值。 
 Type (String): 否  组件类型，默认获取所有类型的标签信息。取值如下所示： 
       - AI：智能处理类型 
       - Other：其他增值类型""",
    "update_image_object_access": """Args:params: A JSON structure
     ServiceId (String): 是  待更新配置的服务 ID。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     ObjectAccess (Boolean): 否  是否开启源地址访问，取值如下所示： 
       * true：开启源地址访问 
       * false：关闭源地址访问""",
    "get_image_service_subscription": """Args:params: A JSON structure
     AddOnType (String): 否  附加组件类型，取值AI获取服务端智能处理开通情况。默认返回ImageX服务开通情况 
 AddOnId (String): 否  附加组件ID，获取指定附加组件的开通情况。默认返回ImageX服务开通情况 
 AddOnKey (String): 否  附加组件英文标识，获取指定附加组件的开通情况。默认返回ImageX服务开通情况。""",
    "create_image_service": """Args:body: A JSON structure
     ServiceName (String): 是  服务名称，最多不超过 32 个字符。创建成功后，名称和区域不支持变更。建议您使用能够标识业务的服务名。 
 ServiceRegion (String): 是  服务地域，取值如下所示： 
       * cn：中国 
       * sg：新加坡 
 ServiceType (String): 否  服务类型，取值如下所示： 
       * StaticRc：素材托管服务，支持任意类型资源的存储和分发。 
       * Image：图片处理服务，除支持任意类型资源的存储和分发外，还支持对图片进行实时处理。 
 Domains (Array of Domains): 是  创建服务时需要绑定的域名列表，最多支持一次绑定 10 个域名。 
 ProjectName (String): 否  服务绑定的项目，默认值为 default。项目是在火山引擎访问控制中资源分组的概念，您需要将服务加入某一个项目中。您可以在火山引擎控制台项目管理页面中获取项目名称。 
 ResourceTags (Array of ResourceTags): 否  服务绑定的标签，默认为空，表示不绑定标签。可用于通过标签将不同业务类别、用途的存储服务进行分类管理，也适用于标签制授权和标签分账等场景。您可以在火山引擎控制台资源管理页面新建标签。 

字段： Domains
 Domain (String): 是  待绑定的已备案域名。 
 CertID (String): 否  待绑定的证书 ID。 

字段： ResourceTags
 Key (String): 是  标签键 
 Value (String): 是  标签值""",
    "delete_image_service": """Args:params: A JSON structure
     ServiceId (String): 是  待删除的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "update_image_auth_key": """Args:params: A JSON structure
     ServiceId (String): 是  待更新配置的服务 ID。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     PrimaryKey (String): 否  主鉴权 key，长度为 8-32 字节，为空则不更新主鉴权值。 
 SecondaryKey (String): 否  备鉴权 key，长度为 8-32 字节，为空则不更新备鉴权值。""",
    "get_image_auth_key": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "update_service_name": """Args:params: A JSON structure
     ServiceId (String): 是  待修改名称的服务 ID。 
       * 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       * 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     ServiceName (String): 是  服务名称，最多不超过 32 个字符。""",
    "delete_image_template": """Args:params: A JSON structure
     ServiceId (String): 是  待删除模板对应的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     TemplateNames (Array of String): 是  待删除模板名称，最大限制为 100。您可以通过调用获取服务下所有图片模板获取所需的模板名称。""",
    "create_image_templates_by_import": """Args:body: A JSON structure
     ServiceId (String): 是  模板导入的目标服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 Rename (Boolean): 否  模板名称冲突时是否重命名（增加版本号）。 
       - true：是，有重名模板时，将对其增加版本号后再导入。 
       - false：（默认）否。将忽略重名模板，不执行导入。 
 Templates (Array of String): 是  待导入的模板 JSON 内容列表。""",
    "create_templates_from_bin": """Args:params: A JSON structure
     ServiceId (String): 是  待恢复模板对应的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     TemplateNames (Array of String): 是  待恢复模板的名称。您可以通过调用获取回收站中所有模板获取所需的模板名称。""",
    "delete_templates_from_bin": """Args:params: A JSON structure
     ServiceId (String): 是  待删除模板对应的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     TemplateNames (Array of String): 是  待删除模板名称。您可以通过调用获取回收站中所有模板获取所需的模板名称。""",
    "create_image_content_task": """Args:body: A JSON structure
     TaskType (String): 是  操作类型。取值如下所示： 
       - refresh_url：刷新 URL 
       - refresh_dir：目录刷新（支持根目录刷新） 
       - preload_url：预热 URL 
       - block_url：禁用 URL 
       - unblock_url：解禁 URL 
 Urls (Array of String): 是  资源 URL 或者目录。 
       - 当TaskType取值refresh_url，一次可提交的最大限额为 2000 个； 
       - 当TaskType取值refresh_dir，一次可提交的最大限额为 50 个； 
       - 当TaskType取值preload_url，一次可提交的最大限额为 2000 个； 
       - 当TaskType取值block_url，一次可提交的最大限额为 2000 个； 
       - 当TaskType取值unblock_url，一次可提交的最大限额为 2000 个。 
 PrefixRefreshDir (Boolean): 否  仅当 TaskType 为 refresh_dir 使用目录刷新时，可通过此配置开启前缀刷新。取值如下所示：   
       - true：开启前缀刷新  
       - false：（默认）关闭前缀刷新，进行标准的目录匹配刷新。""",
    "get_image_content_task_detail": """Args:body: A JSON structure
     TaskType (String): 否  内容管理任务类型，缺省情况下表示查询全部任务。取值如下所示： 
       * refresh：刷新任务，包含刷新 URL 和刷新目录。 
       * refresh_url：刷新 URL 
       * block_url：禁用 URL 
       * unblock_url：解禁 URL 
       * preload_url：预热 URL 
       * refresh_dir：目录刷新（支持根目录刷新） 
 TaskId (String): 否  待查询任务 ID 
 State (String): 否  内容管理资源状态，取值如下所示： 
       - submitting：提交中 
       - running：执行中 
       - succeed：成功 
       - failed：失败 
 Order (String): 否  按时间排序，取值如下所示： 
       - asc：正序 
       - desc：逆序 
 StartTime (Long): 是  查询开始时间，unix 时间戳，单位为秒。 
 EndTime (Long): 是  查询结束时间，unix 时间戳，单位为秒。 
 Domain (String): 否  域名，指定后返回包含该域名的 URL 任务。 
 Url (String): 否  资源 URL 或者目录，可精确匹配，取值为空时表示查询全部任务。 
 PageNum (Integer): 否  页码，系统将仅返回该页面上的任务。默认值为 1。 
 PageSize (Integer): 否  每页条数，取值范围为 [10,1000]。默认值为 100。""",
    "get_image_content_block_list": """Args:body: A JSON structure
     PageSize (Integer): 否  每页条数，取值范围是[10,1000]。默认值为 100。 
 PageNum (Integer): 否  页码，仅返回该页码上的任务。默认值为 1。 
 StartTime (Long): 是  开始查询时间，unix 时间戳，单位为秒。 
 EndTime (Long): 是  结束查询时间，unix 时间戳，单位为秒。 
 Domain (String): 否  域名，指定后将返回包含该域名的 URL 禁用任务。 
 State (String): 否  资源更新状态，取值如下所示： 
       - submitting：提交中 
       - running：执行中 
       - succeed：成功 
       - failed：失败 
 Url (String): 否  指定要查询的 URL，缺省情况下查询当前服务所有禁用任务列表。 
 Order (String): 否  按时间排序，取值如下所示： 
       - asc：正序 
       - desc：逆序""",
    "create_image_audit_task": """Args:body: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 TaskType (String): 是  任务类型，当前仅支持取值为 audit。 
 Type (String): 是  图片审核任务场景。取值如下所示： 
       - UrlFile：存量图片处理，进针对已有存储内的图片请求获取审核结果。传入方式是 ResUri方式，即在.txt 文件（审核文件）内填写了待审核图片文件 URL，并将该 txt 文件上传至指定服务后获取并传入该文件的 StoreUri。 
       - Url：URL 直传场景。传入方式为 ImageInfos 方式，即可直接传入待审核图片的 URL 及区分标识。 
       - Upload：图片上传场景，针对上传图片到指定服务下的场景。可在 EnableAuditRange下指定审核的范围，例如对指定上传到某目录下的图片进行审核。 
 EnableAuditRange (Integer): 否  仅当 Type 取值 Upload 时，配置生效。 
       审核范围，取值如下所示： 
       - 0：（默认）不限范围 
       - 1：指定范围 
 AuditPrefix (Array of String): 否  仅当 EnableAuditRange 取值 1 时，配置生效。 
       指定前缀审核，若你希望对某个目录进行审核，请设置路径为对应的目录名，以/结尾。例如123/test/ 
 NoAuditPrefix (Array of String): 否  仅当 EnableAuditRange 取值 1 时，配置生效。 
       指定前缀不审核，若你希望对某个目录不进行审核，请设置路径为对应的目录名，以/结尾。例如123/test/ 
 ResUri (Array of String): 否  仅当 Type 为 UrlFile 时，配置生效。 
       审核文件的 StoreUri，为 .txt 文件，该文件需上传至指定服务对应存储中。该 txt 文件内需填写待审核图片文件的 URL，每行填写一个，最多可填写 10000 行。 
 ImageInfos (Array of ImageInfos): 否  仅当 Type 为 Url 时，配置生效。 
       批量提交图片 URL 列表 
 AuditAbility (Integer): 是  审核能力，取值如下所示： 
       - 0：基础审核能力 
       - 1：智能审核能力 
 AuditDimensions (Array of String): 是  审核维度，根据审核能力的不同，其具体取值不同。基础审核与智能审核之间不支持混用。 
       - 基础安全审核，仅当 AuditAbility 取值为 0 时，配置生效。 
       	- govern：涉政 
       	- porn ：涉黄	 
       	- illegal：违法违规	 
       	- terror：涉暴 
       - 智能安全审核，仅当 AuditAbility 取值为 1 时，配置生效。 
       	- 图像风险识别 
       		- porn ：涉黄，主要适用于通用色情、色情动作、性行为、性暗示、性分泌物、色情动漫、色情裸露等涉黄场景的风险识别 
       		- sensitive1 ：涉敏1，具体指涉及暴恐风险	 
       		- sensitive2：涉敏2，具体值涉及政治内容风险 
       		- forbidden：违禁，主要适用于打架斗殴、爆炸、劣迹艺人等场景的风险识别 
       		- uncomfortable：引人不适，主要适用于恶心、恐怖、尸体、血腥等引人不适场景的风险识别 
       		- qrcode：二维码，主要适用于识别常见二维码（QQ、微信、其他二维码等） 
       		- badpicture：不良画面，主要适用于自我伤害、丧葬、不当车播、吸烟/纹身/竖中指等不良社会风气的风险识别	 
       		- sexy：性感低俗，主要适用于舌吻、穿衣性行为、擦边裸露等多种性感低俗场景的风险识别 
       		- age：年龄，主要适用于图中人物对应的年龄段识别 
       		- underage：未成年相关，主要适用于儿童色情、儿童邪典等风险识别 
       		- quality：图片质量，主要适用于图片模糊、纯色边框、纯色屏等风险识别 
       	- 图文风险识别，您可在 AuditTextDimensions 配置文字审核的维度。 
       	您可将智能安全审核的图像风险识别和图文风险识别搭配使用。 
 AuditTextDimensions (Array of String): 否  智能安全审核类型下图文风险审核的具体维度，取值如下所示： 
       - ad：广告，综合图像及文字内容智能识别广告 
       - defraud：诈骗，综合图像及文字内容智能识别诈骗 
       - charillegal：文字违规，图片上存在涉黄、涉敏、违禁等违规文字 
       仅当 AuditDimensions 取值为智能安全审核模型时，您可将 AuditTextDimensions 与 AuditDimensions 搭配使用。 
 EnableFreeze (Boolean): 否  是否开启冻结，取值如下所示： 
       - true：开启 
       - false：（默认）不开启 
 FreezeType (Array of String): 否  冻结措施，取值如下所示： 
       - recheck：建议复审 
       - nopass：审核不通过 
 FreezeDimensions (Array of String): 否  冻结维度，取值需要与 AuditDimensions 审核维度保持一致或少于 AuditDimensions。 
       例如，AuditDimensions 取值 ["pron","sexy"]，AuditTextDimensions 取值 ["ad"]，支持您将 FreezeDimensions 取值 ["pron","sexy","ad"] 、 ["pron","sexy"]、["pron","ad"] 和 ["sexy","ad"] 任意一种。 
 FreezeStrategy (Integer): 否  冻结策略，当前仅支持取 0，表示禁用图片。 
 EnableCallback (Boolean): 否  是否开启回调，取值如下所示： 
       - true：开启 
       - false：（默认）不开启 
 CallbackDimensions (Array of String): 否  回调类型，取值需要与 AuditDimensions 审核维度保持一致或少于 AuditDimensions。 
       例如，AuditDimensions 取值 ["pron","sexy"]，AuditTextDimensions 取值 ["ad"]，支持您将 FreezeDimensions 取值 ["pron","sexy","ad"] 、 ["pron","sexy"]、["pron","ad"] 和 ["sexy","ad"] 任意一种。 
 CallbackImageTypes (Array of String): 否  回调图片类型，取值如下所示： 
       - normal：正常图片 
       	 
       - problem：问题图片 
       	 
       - frozen：冻结图片 
       	 
       - fail：审核失败图片 
 CallbackUrl (String): 否  回调 URL，veImageX 以 Post 方式向业务服务器发送 JSON 格式回调数据。具体回调参数请参考回调内容。 
 Region (String): 是  任务地区。当前仅支持取值 cn，表示国内。 
 EnableLargeImageDetect (Boolean): 否  图片审核仅支持审核 5MB 以下的图片，若您的图片大小在 5MB~32MB，您可以开启大图审核功能，veImageX 会对图片压缩后再进行审核。开启后，将对压缩能力按照基础图片处理进行计费。（您每月可使用 20TB 的免费额度） 
       取值如下所示： 
       - true：开启 
       - false：（默认）不开启 
       - 若未开启大图审核且图片大小 ≥ 5 MB，可能会导致系统超时报错； 
       - 若已开启大图审核但图片大小 ≥ 32 MB，可能会导致系统超时报错。 

字段： ImageInfos
 ImageUri (String): 否  待审核图片 URL，需满足公网可访问。 
 DataId (String): 否  建议您根据实际业务情况，将该参数作为可区分审核图片 ImageUri 的自定义标识。""",
    "update_image_audit_task": """Args:body: A JSON structure
     Region (String): 否  任务地区。当前仅支持取值 cn，表示国内。 
 ServiceId (String): 是  指定待更新审核任务所在的服务 ID，您可通过调用 查询所有审核任务 获取待更新任务对应的服务 ID。 
 TaskId (String): 是  任务 ID，您可通过调用 查询所有审核任务 获取所需的任务 ID。 
 EnableAuditRange (Integer): 否  仅当 Type 取值 Upload 时，配置生效。 
       审核范围，取值如下所示： 
       - 0：（默认）不限范围 
       - 1：指定范围 
 AuditPrefix (Array of String): 否  仅当 EnableAuditRange 取值 1 时，配置生效。 
       指定前缀审核，若你希望对某个目录进行审核，请设置路径为对应的目录名，以/结尾。例如123/ 
 NoAuditPrefix (Array of String): 否  仅当 EnableAuditRange 取值 1 时，配置生效。 
       指定前缀不审核，若你希望对某个目录不进行审核，请设置路径为对应的目录名，以/结尾。例如123/ 
 ResUri (Array of String): 否  仅当 Type 为 UrlFile 时，配置生效。 
       审核文件的 StoreUri，为 .txt 文件，该文件需上传至指定服务对应存储中。该 txt 文件内需填写待审核图片文件的 URL，每行填写一个，最多可填写 10000 行。 
 AuditDimensions (Array of String): 是  审核维度，根据审核能力的不同，其具体取值不同。基础审核与智能审核之间不支持混用。 
       - 基础安全审核，仅当 AuditAbility 取值为 0 时，配置生效。 
       	- govern：涉政 
       	- porn ：涉黄	 
       	- illegal：违法违规	 
       	- terror：涉暴 
       - 智能安全审核，仅当 AuditAbility 取值为 1 时，配置生效。 
       	- 图像风险识别 
       		- porn ：涉黄，主要适用于通用色情、色情动作、性行为、性暗示、性分泌物、色情动漫、色情裸露等涉黄场景的风险识别 
       		- sensitive1 ：涉敏1，具体指涉及暴恐风险	 
       		- sensitive2：涉敏2，具体值涉及政治内容风险 
       		- forbidden：违禁，主要适用于打架斗殴、爆炸、劣迹艺人等场景的风险识别 
       		- uncomfortable：引人不适，主要适用于恶心、恐怖、尸体、血腥等引人不适场景的风险识别 
       		- qrcode：二维码，主要适用于识别常见二维码（QQ、微信、其他二维码等） 
       		- badpicture：不良画面，主要适用于自我伤害、丧葬、不当车播、吸烟/纹身/竖中指等不良社会风气的风险识别	 
       		- sexy：性感低俗，主要适用于舌吻、穿衣性行为、擦边裸露等多种性感低俗场景的风险识别 
       		- age：年龄，主要适用于图中人物对应的年龄段识别 
       		- underage：未成年相关，主要适用于儿童色情、儿童邪典等风险识别 
       		- quality：图片质量，主要适用于图片模糊、纯色边框、纯色屏等风险识别 
       	- 图文风险识别，您可在 AuditTextDimensions 配置文字审核的维度。 
       	您可将智能安全审核的图像风险识别和图文风险识别搭配使用。 
 AuditTextDimensions (Array of String): 否  智能安全审核类型下图片文本审核的具体维度，取值如下所示： 
       - ad：广告，综合图像及文字内容智能识别广告 
       - defraud：诈骗，综合图像及文字内容智能识别诈骗 
       - charillegal：文字违规，图片上存在涉黄、涉敏、违禁等违规文字 
       仅当 AuditDimensions 取值为智能安全审核模型时，您可将 AuditTextDimensions 与 AuditDimensions 搭配使用。 
 EnableFreeze (Boolean): 否  是否开启冻结，取值如下所示： 
       - true：开启 
       - false：（默认）不开启 
 FreezeType (Array of String): 否  冻结措施，取值如下所示： 
       - recheck：建议复审 
       - nopass：审核不通过 
 FreezeDimensions (Array of String): 否  冻结维度，取值需要与 AuditDimensions 审核维度保持一致或少于 AuditDimensions。 
       例如，AuditDimensions 取值 ["pron","sexy"]，AuditTextDimensions 取值 ["ad"]，支持您将 FreezeDimensions 取值 ["pron","sexy","ad"] 、 ["pron","sexy"]、["pron","ad"] 和 ["sexy","ad"] 任意一种。 
 FreezeStrategy (Integer): 否  冻结策略，当前仅支持取 0，表示禁用图片。 
 EnableCallback (Boolean): 否  是否开启回调，取值如下所示： 
       - true：开启 
       - false：（默认）不开启 
 CallbackDimensions (Array of String): 否  回调类型，取值需要与 AuditDimensions 审核维度保持一致或少于 AuditDimensions。 
       例如，AuditDimensions 取值 ["pron","sexy"]，AuditTextDimensions 取值 ["ad"]，支持您将 FreezeDimensions 取值 ["pron","sexy","ad"] 、 ["pron","sexy"]、["pron","ad"] 和 ["sexy","ad"] 任意一种。 
 CallbackImageTypes (Array of String): 否  回调图片类型，取值如下所示： 
       - normal：正常图片 
       	 
       - problem：问题图片 
       	 
       - frozen：冻结图片 
       	 
       - fail：审核失败图片 
 CallbackUrl (String): 否  回调 URL，veImageX 以 Post 方式向业务服务器发送 JSON 格式回调数据。具体回调参数请参考回调内容。 
 EnableLargeImageDetect (Boolean): 否  图片审核仅支持审核 5MB 以下的图片，若您的图片大小在 5MB~32MB，您可以开启大图审核功能，veImageX 会对图片压缩后再进行审核。开启后，将对压缩能力按照基础图片处理进行计费。（您每月可使用 20TB 的免费额度） 
       取值如下所示： 
       - true：开启 
       - false：（默认）不开启 
       - 若未开启大图审核且图片大小 ≥ 5 MB，可能会导致系统超时报错； 
       - 若已开启大图审核但图片大小 ≥ 32 MB，可能会导致系统超时报错。""",
    "get_image_styles": """Args:params: A JSON structure
     Type (String): 是  样式类型。取值 user 表示用户样式。 
 SearchPtn (String): 否  需要返回的样式列表标识。 
       * 返回的样式名称、样式 ID 包含了该值的样式列表。 
       * 返回的样式宽度或样式高度为该值的样式列表。 
 Limit (Integer): 否  分页返回条数，取值范围为[0,100]，默认 10 条。 
 Offset (Integer): 否  分页偏移，默认 0，取值为 1 时，表示跳过一条数据，从第二条数据取值。""",
    "create_image_style": """Args:body: A JSON structure
     Name (String): 是  样式名称，当前对字符长度及支持字符暂无限制。 
 Width (Integer): 是  样式画布的宽度，取值范围为[0,1000]。 
 Height (Integer): 是  样式画布的高度，取值范围为[0,1000]。 
 Unit (String): 否  尺寸单位。即样式画布宽度/高度的像素单位，取值为px。 
 ServiceId (String): 是  绑定的服务 ID，用于计量计费和样式渲染结果图的存储。 
       * 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       * 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "update_image_style_meta": """Args:body: A JSON structure
     StyleId (String): 是  待更新的样式 ID。 
 Name (String): 是  更新后的样式名称。""",
    "delete_image_style": """Args:body: A JSON structure
     StyleId (String): 是  待删除的样式 ID。""",
    "get_image_fonts": """Args:""",
    "add_image_elements": """Args:body: A JSON structure
     Type (String): 是  要素类型，取值如下所示： 
       * image：图片要素； 
       * background：背景要素； 
       * mask：蒙版要素。 
 Images (Array of String): 是  待添加的图片 URI 列表。""",
    "delete_image_elements": """Args:body: A JSON structure
     Type (String): 是  要素类型，取值如下所示： 
       * image：图片要素； 
       * background：背景要素； 
       * mask：蒙版要素。 
 ImageList (Array of String): 是  待删除的 StoreUri 列表。""",
    "get_image_elements": """Args:params: A JSON structure
     Type (String): 是  要素类型，取值如下所示： 
       * image：图片要素； 
       * background：背景要素； 
       * mask：蒙版要素。 
 SearchPtn (String): 否  返回图片 URI 中包含该值的要素列表。 
 Limit (Integer): 否  分页返回条数。默认 10，最大限制为 100。 
 Offset (Integer): 否  分页偏移，默认 0，取值为 1 时，表示跳过一条数据，从第二条数据取值。""",
    "add_image_background_colors": """Args:body: A JSON structure
     Colors (Array of String): 是  待添加的颜色列表""",
    "delete_image_background_colors": """Args:body: A JSON structure
     Colors (Array of String): 是  待删除的颜色列表""",
    "get_image_background_colors": """Args:""",
    "create_image_hm_extract": """Args:params: A JSON structure
     ServiceId (String): 是  待提取水印图对应的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  待提取盲水印的图片的 URI。StoreUri 和 ImageUrl 都不为空时，以 StoreUri 为准。 
 ImageUrl (String): 是  待提取盲水印图片的 URL。StoreUri 和 ImageUrl 都不为空时，以 StoreUri 为准。 
 Algorithm (String): 是  算法模型，取值如下所示： 
       - default：文本嵌入基础模型 
       - adapt_resize：画质自适应文本嵌入模型。 
       - adapt: 文本嵌入自适应模型（AIGC 适用） 
       - natural：文本嵌入基础模型（彩色图片通用） 
       - tracev1：前景图层水印模型（纯色背景适用） 
       - tracev2：前景图层水印模型（彩色背景通用） 
       指定 tracev1 或 tracev2 模型时，请传入已添加对应模型水印的背景网页的截图。若模型错误，则无法提取水印。""",
    "create_image_hm_embed": """Args:body: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  待添加盲水印的原图 Uri。 
 Algorithm (String): 是  算法模型，取值如下所示： 
       * default：文本嵌入模型，默认文本嵌入模型； 
       * adapt_resize：画质自适应文本嵌入模型。 
 Info (String): 是  自定义盲水印文本内容。 
       * 文本嵌入模型支持最长可嵌入115个水印内容字符。 
       * 画质自适应文本嵌入模型无水印内容长度限制。 
 OutFormat (String): 否  输出图片格式，默认 png，支持图片格式有：png、jpeg、webp。 
 OutQuality (Integer): 否  输出图片质量参数。取值范围为 [1,100]，默认为 75。 
       对于 PNG 无损压缩，其他格式下其值越小，压缩率越高，画质越差。 
 StrengthLevel (String): 否  算法强度，强度越高，图像抵抗攻击性能越强。取值如下所示： 
       * low：低强度，适用于纯色图场景以及对图像质量要求高； 
       * medium：中强度，默认中强度； 
       * strong：高强度，适合图像纹理丰富时使用。 
 ImageUrl (String): 否  待添加盲水印的可公网访问原图 Url。当 StoreUri 和 ImageUrl 均不为空，以 StoreUri 取值为准。""",
    "get_image_erase_result": """Args:body: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  待修复原图的存储 URI 或 URL（公网可访问的 URL）。 
 Model (String): 是  修复模型，支持取值如下所示： 
       - 自动检测并擦除类型模型：eraser_model_imagex_0.1.0 
       - 指定区域擦除模型： 
       	- eraser_model_imagex_0.1.0 （推荐） 
       	- eraser_model_aliab 
 BBox (Array of BBox): 否  指定区域擦除时图片待修复区域。不填表示自动检测内容并修复，若所选模型不支持自动检测，则直接返回原图。 

字段： BBox
 X1 (Float): 是  待修复区域左上角的 X 坐标，取值范围为[0,1]。 
 Y1 (Float): 是  待修复区域左上角的 Y 坐标，取值范围为[0,1]。 
 X2 (Float): 是  待修复区域右下角的 X 坐标，取值范围为[0,1]。 
 Y2 (Float): 是  待修复区域右下角的 Y 坐标，取值范围为[0,1]。""",
    "get_comprehensive_enhance_image": """Args:body: A JSON structure
     ServiceId (String): 是  服务 ID。 
 ImageUri (String): 是  待增强图片的存储 URI 或访问 URL（公网可访问）。您可在控制台资源管理获取图片的存储 URI 以及访问 URL。 
 Mode (Integer): 是  优化策略，取值如下所示： 
       - 0：通用画质提升 
       - 1：显著画质提升 
       推荐优先使用通用方案，显著画质提升方案画质分提高 10% 左右，但体积会有一定浮动提升。以上幅度变化基于测试集总结，具体以使用场景为准。 
 EnableConfig (Boolean): 否  是否启用高级配置，取值如下所示： 
       - true：开启。开启后，下述高级配置才会生效。 
       - false：（默认）关闭。 
       适用于 8000 x 8000 以分辨率图像的画质增强。 
 ArStrength (Float): 否  去压缩失真强度，取值范围为[0,1]。取值为0时表示不处理，取值越大去压缩失真强度越大。 
 DeblurStrength (Float): 否  去模糊强度，取值范围为[0,1]。取值为0时表示不处理，取值越大去模糊强度越大。 
 DenoiseStrength (Float): 否  降噪强度，取值范围为[0,1]。取值为0时表示不降噪，取值越大降噪强度越大。 
 Saturation (Float): 否  饱和度，取值范围为[0,2]。取值大于 1 表示提升饱和度，取值小于 1 表示降低饱和度。 
 Brightness (Integer): 否  EnableConfig 取值为 true 时，为必填。 
       亮度，取值范围为[90,100]。取值越小，亮度提升越明显。 
 EnableSuperResolution (Boolean): 否  是否开启超分配置，仅满足图像输入边界的图像执行超分处理。取值如下所示： 
       - true：开启。仅当开启后，下述超分配置才会生效。 
       - false：（默认）关闭。 
       适用于 8000 x 8000 以内分辨率图像的画质增强。 
 Multiple (Integer): 否  超分倍率，仅支持 2 倍和 4 倍。 
       4 倍超分辨率只适用于 4000 x 4000 以内分辨率图像的画质增强。 
 ShortMin (Integer): 否  EnableSuperResolution 取值为 true 时，为必填。 
       执行超分处理的短边范围最小值，仅当满足图像边界输入的图像执行超分处理。单位为 px。 
 ShortMax (Integer): 否  EnableSuperResolution 取值为 true 时，为必填。 
       执行超分处理的短边范围最大值，仅当满足图像边界输入的图像执行超分处理。单位为 px。 
 LongMin (Integer): 否  执行超分处理的长边范围最小值，仅当满足图像边界输入的图像执行超分处理。单位为 px。 
 LongMax (Integer): 否  执行超分处理的长边范围最大值，仅当满足图像边界输入的图像执行超分处理。单位为 px。 
 EnableDownsample (Boolean): 否  是否开启下采样，即图片在执行增强效果的同时可自定义输出图片分辨率大小。取值如下所示： 
       - true：开启。仅当开启后，下述下采样配置才会生效。 
       - false：（默认）关闭。 
       适用于 8000 x 8000 以内分辨率图像的画质增强。 
 DownsampleOutWidth (Integer): 否  下采样输出图片宽度，图片将适配对应大小。单位为 px。 
 DownsampleOutHeight (Integer): 否  下采样输出图片高度，图片将适配对应大小。单位为 px。 
 DownsampleMode (Integer): 否  下采样模式，取值如下所示： 
       - 0: 仅缩小，图片大于设置的“宽/高”时，将缩小图片 
       - 1: 仅放大，图片小于设置的“宽/高”时，将放大图片 
       - 2: 既缩小又放大，即按照自定义“宽/高”输出结果图，该操作可能导致图片变形 
 EnableTextEnhance (Boolean): 否  是否使用文字增强，取值如下所示： 
       - false：（默认）不使用 
       - true：使用 
 TextEnhanceStrength (Float): 否  文字增强强度，取值范围[0,1]，默认值为 0.5。取值越大文字增强效果越强，但也更容易出现白边、色偏、对比度增大、非 CG 文字与背景产生割裂感等问题。""",
    "get_image_bg_fill_result": """Args:body: A JSON structure
     ServiceId (String): 是  服务ID。 
       * 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       * 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  待填充原图的存储 URI 和 URL（公网可访问的 URL）。 
 Model (Integer): 是  填充模型，取值如下所示： 
       * 0：国漫风格模型； 
       * 1：通用模型。 
 Top (Float): 否  向上填充比例，取值范围为 [0, 0.4]。 
 Bottom (Float): 否  向下填充比例，取值范围为 [0, 0.4]。 
 Left (Float): 否  向左填充比例，取值范围为 [0, 0.4]。 
 Right (Float): 否  向右填充比例，取值范围为 [0, 0.4]。""",
    "get_image_comic_result": """Args:body: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  待处理原图的存储 URI 和 URL（可公网访问的 URL）。""",
    "get_segment_image": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       * 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       * 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Class (String): 是  图片类型，支持可选择的模型如下。 
       * general：通用模型v1 
       * human：人脸模型v1 
       * product：商品模型v1 
       * humanv2：人脸模型v2 
       * productv2：商品模型v2 
 Refine (Boolean): 是  处理效果，当Class取值为humanv2或productv2时，默认为true。 
       * false：保留的图像主体边缘以粗线条处理，图像处理的效率更高。 
       * true：保留的图像主体边缘以发丝级细线条处理，图像处理后的效果更好。 
 Contour (Object of Contour): 否  描边设置，仅当Class取值humanv2或productv2时有效。 
       默认关闭，如果开启，抠出的结果图中保留的图像主体会外包一圈描边效果。 
 TransBg (Boolean): 否  是否开启透明背景裁剪设置。默认false，关闭状态。如果开启，抠出的结果图会被裁剪到刚好包住保留的图像主体。 
 StoreUri (String): 是  待擦除原图的存储 URI 和 URL（公网可访问的 URL）。 
 OutFormat (String): 是  输出图片格式，取值如下所示： 
       - png 
       - jpeg 
       - webp 

字段： Contour
 Color (String): 是  描边颜色，支持以 HEX、HSL、RGP 表示。例如HEX中白色为#FFFFFF。 
 Size (Integer): 是  描边宽度，单位为 px。取值范围为 0 到正整数，默认 10px。""",
    "get_image_super_resolution_result": """Args:body: A JSON structure
     ServiceId (String): 是  用于存储结果图和计量计费的服务 ID。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  待处理原图的存储 URI 或访问 URL（可公网访问）。您可在控制台资源管理获取图片的存储 URI 以及访问 URL。 
 Multiple (Float): 否  超分倍率，默认值为2，支持取值为：2、3、4、5、6、7、8。""",
    "get_image_smart_crop_result": """Args:body: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  待处理原图的存储 URI 和 URL（公网可访问的 URL）。 
 Policy (String): 否  降级策略，即当智能裁剪失败时的操作，默认居中裁剪。支持取值如下： 
       * center：居中裁剪，默认裁剪中间图片； 
       * top：居上裁剪，默认裁剪上方图片； 
       * fglass：高斯模糊，将按设置宽高自动适配图片，结果图多出原图部分以原图背景高斯模糊效果填充。 
 Scene (String): 否  裁剪场景 (normal,cartoon)，默认普通人脸裁剪。支持取值如下： 
       * normal：普通人脸裁剪； 
       * cartoon：动漫人脸裁剪。 
       当前仅支持了智能人脸裁剪能力，其他裁剪能力在持续开放中，敬请期待。 
 Sigma (Float): 否  当Policy取值为fglass时的高斯模糊参数，取值为大于 0 的整数，值越大越模糊。 
 Width (Integer): 否  图片裁剪后的宽度设置，单位为 px。当图片小于设置的宽高时，将不被裁剪。 
 Height (Integer): 否  图片裁剪后的高度设置，单位为 px。当图片小于设置的宽高时，将不被裁剪。""",
    "get_image_ps_detection": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     ImageUri (String): 是  原图的存储 URI。 
 Method (String): 否  调用方法，默认为调用全部方法，若参数不为all，则其他方法仅可选一种。取值如下所示： 
       - all：调用所有方法 
       - ela：误差水平分析方法 
       - na：噪声分析方法 
       - he：基于颜色分布直方图均化的图像增强分析方法""",
    "get_ai_generate_image": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Url (String): 是  输入原图 URL。 
       智能算法将根据您输入原图并结合文本描述智能生成相关图像。 
 NeedSeg (Boolean): 否  是否使用分割处理图片，取值如下所示： 
       - true：分隔处理 
       - false：（默认）不分割处理，从输入图像读取 alpha 通道作为 mask。 
       图像 mask 指在图像上添加一个遮罩层，使图像的某些部分被隐藏或不可见。 
 PositivePrompt (String): 否  正向提示词，提示词和 Scene 两者不可同时为空。两者均存在时，以 Scene 为准。当前仅支持英文，最多不超过 300 个字母。 
       建议文本内容尽可能详细准确，详细的文本描述内容有助于获得更佳的图片生成效果。 
 NegativePrompt (String): 否  负向提示词，提示词和 Scene 两者不可同时为空。两者均存在时，以 Scene 为准。当前仅支持英文，最多不超过 300 个字母。 
 ProductRatio (Float): 否  商品 mask 长宽与 output_size 比值的上限。取值范围为 (0,1]。取值越小，则产品图和生成的背景图比例就越小。 
 OutputSize (Integer): 是  指定结果图长和宽的值，单位为 px。取值范围为[512,2048]。 
       输出结果图的规格为 1:1 方图。 
 Callback (String): 否  任务回调地址，需为公网可访问，使用 POST 请求。具体回调参数请参考回调内容。 
 Scene (String): 否  根据所选场景生成结果图，场景支持以下选项： 
       - indoor wooden table：室内木桌场景 
       - flower and leaves：鲜花绿植场景 
       - white marble table：白色大理石场景 
       - outdoor snow scene：室外雪景场景 
 CX (Integer): 否  默认为-1，设置商品放置的安全区中心坐标和宽高：设为默认值-1时，商品自动居中，安全区为全图；否则用户需同时指定四个参数的值 
 CY (Integer): 否  默认为-1，设置商品放置的安全区中心坐标和宽高：设为默认值-1时，商品自动居中，安全区为全图；否则用户需同时指定四个参数的值 
 Extra (String): 否  保留字段 
 ReturnTop1 (Boolean): 否  默认为False，根据业务需要，取值为True时，只返回最高分的生成图及其得分，否则返回所有生成图及其得分 
 SafeH (Integer): 否  默认为-1，设置商品放置的安全区中心坐标和宽高：设为默认值-1时，商品自动居中，安全区为全图；否则用户需同时指定四个参数的值 
 SafeW (Integer): 否  默认为-1，设置商品放置的安全区中心坐标和宽高：设为默认值-1时，商品自动居中，安全区为全图；否则用户需同时指定四个参数的值 
 UseCaption (Boolean): 否  默认为True，取值为True时，使用blip模型提取对商品的描述，和positive_prompt共同作为输入到AIGC模型的正向提示词 
 BatchSize (Integer): 否  每次生成的图片数量，取值范围为[1,4]，默认值为 4""",
    "describe_imagex_summary": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 Timestamp (String): 是  数据查询时间段，即Timestamp所在月份的 1 日 0 时起至传入时间Timestamp的时间范围。 
       格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。""",
    "describe_imagex_domain_traffic_data": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省时表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 BillingRegion (String): 否  计费区域。支持查询多个区域，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有区域。取值如下所示： 
       - CHN：中国内地 
       - AP1：亚太一区 
       - AP2：亚太二区 
       - AP3：亚太三区 
       - EU：欧洲 
       - ME：中东和非洲 
       - SA：南美 
       - NA：北美 
       - OTHER：其他 
 GroupBy (String): 否  需要分组查询的参数。不传表示不拆分维度，传入多个用英文逗号分隔。取值如下所示： 
       - ServiceId：服务 ID 
       - DomainName ：域名 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近一年历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2010-11-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒。缺省时查询 StartTime 和 EndTime 时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_domain_bandwidth_data": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 BillingRegion (String): 否  计费区域。支持查询多个区域，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有区域。取值如下所示： 
       - CHN：中国内地 
       - AP1：亚太一区 
       - AP2：亚太二区 
       - AP3：亚太三区 
       - EU：欧洲 
       - ME：中东和非洲 
       - SA：南美 
       - NA：北美 
       - OTHER：其他 
 GroupBy (String): 否  需要分组查询的参数。不传表示不拆分维度，传入多个用英文逗号分隔。取值如下所示： 
       - ServiceId：服务 ID 
       - DomainName ：域名 
 StartTime (String): 是  取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近一年历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2010-11-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (Integer): 否  查询数据的时间粒度。单位为秒。缺省时查询 StartTime 和 EndTime 时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_billing_request_cnt_usage": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 AdvFeats (String): 否  组件名称。支持查询多个组件，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有组件。您可通过调用 GetImageAddOnConf 查看Key返回值。 
 GroupBy (String): 是  固定值，仅支持AdvFeat即附加组件。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近一年历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2010-11-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒。缺省时查询 StartTime 和 EndTime 时间段全部数据，此时单次查询最大时间跨度为 93 天。支持取值如下： 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_request_cnt_usage": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 AdvFeats (String): 否  组件名称。支持查询多个组件，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有组件。您可通过调用 GetImageAddOnConf 查看Key返回值。 
 Templates (String): 否  图片处理模板。支持查询多个模板，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有模板。您可通过调用 GetAllImageTemplates 获取服务下全部模版信息。 
 GroupBy (String): 否  维度拆分的维度值。不传表示不拆分维度，只能传入单个参数。支持取值如下： 
       - ServiceId：服务 
       - AdvFeat：组件 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近一年历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2010-11-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒。缺省时查询 StartTime 和 EndTime 时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_base_op_usage": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 GroupBy (String): 否  需要分组查询的参数，当前仅支持取值 ServiceId，表示按服务 ID 进行分组。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近一年历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2010-11-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒。缺省时查询 StartTime 和 EndTime 时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_compress_usage": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 GroupBy (String): 否  需要分组查询的参数，当前仅支持取值 ServiceId，表示按服务 ID 进行分组。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近一年历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2010-11-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒。缺省时查询 StartTime 和 EndTime 时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_screenshot_usage": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近一年历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2010-11-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒。缺省时查询 StartTime 和 EndTime 时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_video_clip_duration_usage": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近一年历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2010-11-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒。缺省时查询 StartTime 和 EndTime 时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_multi_compress_usage": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒，缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_edge_request": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 Regions (String): 否  计费区域。支持查询多个区域，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有区域。取值如下所示： 
       - 中国大陆 
       - 亚太一区 
       - 亚太二区 
       - 亚太三区 
       - 欧洲区 
       - 北美区 
       - 南美区 
       - 中东区 
 UserCountry (String): 否  客户端国家。支持查询多个国家，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有国家。您可通过调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端国家。取值如下所示： 
       - 海外，除中国外全部国家。 
       - 具体国家取值，如中国、美国。 
 UserProvince (String): 否  客户端省份。支持查询多个省份，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有省份。可调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端省份。 
 Protocols (String): 否  过滤网络协议。传入多个用英文逗号分割，缺省情况下表示不过滤。取值如下所示： 
       - HTTP 
       - HTTPS 
 Isp (String): 否  过滤运营商。传入多个用英文逗号分割，缺省情况下表示不过滤。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 鹏博士 
       - 教育网 
       - 广电网 
       - 其它 
 DataTypes (String): 是  状态码，传入多个时用英文逗号分隔。取值如下所示： 
       - req_cnt：返回所有状态码数据 
       - 2xx：返回 2xx 状态码汇总数据 
       - 3xx：返回 3xx 状态码汇总数据 
       - 4xx：返回 4xx 状态码汇总数据 
       - 5xx：返回 5xx 状态码汇总数据。 
 GroupBy (String): 否  需要分组查询的参数，传入多个用英文逗号分割。取值如下所示： 
       - DomainName：域名 
       - DataType：状态码 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒，缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。支持以下取值： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天 
 DetailedCode (Boolean): 否  是否拆分状态码，取值如下所示： 
       - true：拆分 
       - false：（默认）不拆分""",
    "describe_imagex_edge_request_bandwidth": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 Regions (String): 否  计费区域。支持查询多个区域，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有区域。取值如下所示： 
       - 中国大陆 
       - 亚太一区 
       - 亚太二区 
       - 亚太三区 
       - 欧洲区 
       - 北美区 
       - 南美区 
       - 中东区 
 UserCountry (String): 否  客户端国家。传入多个时用英文逗号作为分割符，缺省情况下表示不过滤。可调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端国家。取值如下所示： 
       - 海外，除中国外全部国家。 
       - 具体国家取值，如中国、美国。 
 UserProvince (String): 否  客户端省份。传入多个用英文逗号分割，缺省情况下表示不过滤。可调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端省份。 
 Protocols (String): 否  过滤网络协议。传入多个用英文逗号分割，缺省情况下表示不过滤。取值如下所示： 
       - HTTP 
       - HTTPS 
 Isp (String): 否  过滤运营商。传入多个用英文逗号分割，缺省情况下表示不过滤。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 鹏博士 
       - 教育网 
       - 广电网 
       - 其它 
 GroupBy (String): 否  分组依据，取值仅支持DomainName。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒，缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_edge_request_traffic": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 Regions (String): 否  区域。支持查询多个区域，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有区域。取值如下所示： 
       - 中国大陆 
       - 亚太一区 
       - 亚太二区 
       - 亚太三区 
       - 欧洲区 
       - 北美区 
       - 南美区 
       - 中东区 
 UserCountry (String): 否  客户端国家。传入多个时用英文逗号作为分割符，缺省情况下表示不过滤。您可以通过调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端国家。取值如下所示： 
       - 海外，除中国外全部国家。 
       - 具体国家取值，如中国、美国。 
 UserProvince (String): 否  客户端省份。传入多个用英文逗号分割，缺省情况下表示不过滤。可调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端省份。 
 Protocols (String): 否  过滤网络协议。传入多个用英文逗号分割，缺省情况下表示不过滤。取值如下所示： 
       - HTTP 
       - HTTPS 
 Isp (String): 否  过滤运营商。传入多个用英文逗号分割，缺省情况下表示不过滤。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 鹏博士 
       - 教育网 
       - 广电网 
       - 其它 
 GroupBy (String): 否  分组依据，取值仅支持DomainName。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒，缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_edge_request_regions": """Args:params: A JSON structure
     StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。起始时间与结束时间间隔小于等于 90 天。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。起始时间与结束时间间隔小于等于 90 天。""",
    "describe_imagex_mirror_request_http_code_by_time": """Args:body: A JSON structure
     ServiceIds (Array of String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (Array of String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度，单位为秒。缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天 
 AggregateCode (String): 否  状态码是否聚合，取值如下所示： 
       - true：聚合 
       - false：（默认）不聚合""",
    "describe_imagex_mirror_request_http_code_overview": """Args:body: A JSON structure
     ServiceIds (Array of String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (Array of String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 AggregateCode (String): 否  状态码是否聚合，取值如下所示： 
       - true：聚合 
       - false：（默认）不聚合""",
    "describe_imagex_mirror_request_traffic": """Args:body: A JSON structure
     ServiceIds (Array of String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (Array of String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒，缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_mirror_request_bandwidth": """Args:body: A JSON structure
     ServiceIds (Array of String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (Array of String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒，缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_server_qps_usage": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒。缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。取值如下所示： 
       - 1: 单次查询最大时间跨度为 6 小时 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_hit_rate_traffic_data": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 GroupBy (String): 否  需要分组查询的参数。取值仅支持DomainName。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度，单位为秒。缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。支持以下取值： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_hit_rate_request_data": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 GroupBy (String): 否  需要分组查询的参数。取值仅支持DomainName。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度，单位为秒。缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。支持以下取值： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagexcdn_top_request_data": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取所需的域名。 
 IPVersion (String): 否  网络协议。缺省情况下则表示不限制网络协议，取值如下所示： 
       - IPv4 
       - IPv6 
       KeyType取值为Domain时，IPVersion的取值无效。 
 Country (String): 否  数据访问区域。仅在KeyType取值为Region或Isp时生效，取值如下所示： 
       - China：中国。 
       - Other：中国境外的区域。 
 KeyType (String): 是  排序依据，取值如下所示： 
       - URL：生成的图片访问 URL 
       - UserAgent：用户代理 
       - Refer：请求 Refer 
       - ClientIP：客户端 IP 
       - Region：访问区域 
       - Domain：域名 
       - Isp：运营商 
 ValueType (String): 是  排序依据，即获取按ValueType值排序的KeyType列表。取值如下所示： 
       - Traffic：按流量排序 
       - RequestCnt：按请求次数排序 
       当KeyType取值为Domain时，仅支持将ValueType取值为Traffic，即按照流量排序获取域名列表。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如 2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如 2019-06-02T00:00:00+08:00。 
 Limit (String): 否  每页查询数据量，默认为0，即返回所有数据。 
 Offset (String): 否  分页偏移量，默认取值为0 。取值为10时，表示跳过前 10 条数据，从第 11 条数据开始取值。""",
    "get_imagex_query_apps": """Args:params: A JSON structure
     Source (String): 否  数据来源，账号下近 60 天内有数据上报的应用 ID，缺省情况下返回账号对应的全部应用 ID。取值如下所示： 
       * upload：上传 1.0 数据。 
       * cdn：下行网络数据。 
       * client：客户端数据。 
       * sensible：感知数据。 
       * uploadv2：上传 2.0 数据。 
       * exceed：大图监控数据。""",
    "get_imagex_query_regions": """Args:params: A JSON structure
     Source (String): 是  数据来源，取值如下所示： 
       * upload：上传 1.0 数据。 
       * cdn：下行网络数据。 
       * client：客户端数据。 
       * uploadv2：上传 2.0 数据。 
 Appid (String): 否  应用 ID。默认为空，匹配账号下所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的应用 ID。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web，仅当Source为upload或uploadv2时可传。 
       - Imp：小程序，仅当Source为upload或uploadv2时可传。""",
    "get_imagex_query_dims": """Args:params: A JSON structure
     Source (String): 是  数据来源，取值如下所示： 
       * upload：上传 1.0 数据。 
       * cdn：下行网络数据。 
       * client：客户端数据。 
       * sensible：感知数据。 
       * uploadv2：上传 2.0 数据。 
       * exceed：大图监控数据，包含大图样本量和大图明细。 
       * exceed_all：大图分布数据。 
 Appid (String): 否  应用 ID。默认为空，匹配账号下所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web，仅当Source为upload或uploadv2时可传。 
       - Imp：小程序，仅当Source为upload或uploadv2时可传。""",
    "get_imagex_query_vals": """Args:params: A JSON structure
     Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表获取所需的维度名称。 
 Source (String): 是  数据来源。 
       * upload：上传 1.0 数据。 
       * cdn：下行网络数据。 
       * client：客户端数据。 
       * sensible：感知数据。 
       * uploadv2：上传 2.0 数据。 
       * exceed：大图监控数据，包含大图样本量和大图明细。 
       * exceed_all：大图分布数据。 
 Appid (String): 否  应用 ID。默认为空，匹配中账号下所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web，仅当Source为upload或uploadv2时可传。 
       - Imp：小程序，仅当Source为upload或uploadv2时可传。 
 Keyword (String): 否  需要过滤的关键词（包含），不传则不过滤关键词。""",
    "describe_imagex_upload_count_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web。 
       - Imp：小程序。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。  支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用获取自定义维度列表接口获取自定义维度指标 
 UploadType (Integer): 否  上传类型，默认为空，返回上传 1.0 数据。取值如下所示： 
       * 1：上传 1.0。 
       * 2：上传 2.0。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度，取值如下所示： 
       * 5m： 5 分钟； 
       * 1h： 1 小时； 
       * 1d： 1 天； 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_upload_duration": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 App ID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web。 
       - Imp：小程序。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，获取拆分分位数据。支持取值： 
       * Duration：表示为分位数据 
       - Phase：表示分阶段数据，仅当UploadType取值为2时支持取值。 
       - 公共维度：Appid、OS、AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 UploadType (Integer): 否  上传类型，默认为空，返回上传 1.0 数据。取值如下所示： 
       * 1：上传 1.0。 
       * 2：上传 2.0。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度，取值如下所示： 
       * 5m： 5 分钟； 
       * 1h： 1 小时； 
       * 1d： 1 天； 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_upload_success_rate_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web。 
       - Imp：小程序。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。  支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 UploadType (Integer): 否  上传类型，默认为空，返回上传 1.0 数据。取值如下所示： 
       * 1：上传 1.0。 
       * 2：上传 2.0。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m： 5 分钟； 
       * 1h： 1 小时； 
       * 1d： 1 天； 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_upload_file_size": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web。 
       - Imp：小程序。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，表示拆分分位数据。支持取值： 
       - Duration：表示分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 UploadType (Integer): 否  上传类型，默认为空，返回上传 1.0 数据。取值如下所示： 
       * 1：上传 1.0。 
       * 2：上传 2.0。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m： 5 分钟； 
       * 1h： 1 小时； 
       * 1d： 1 天； 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_upload_error_code_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web。 
       - Imp：小程序。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 UploadType (Integer): 否  上传类型，默认为空，返回上传 1.0 数据。取值如下所示： 
       * 1：上传 1.0。 
       * 2：上传 2.0。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m： 5 分钟； 
       * 1h： 1 小时； 
       * 1d： 1 天； 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_upload_error_code_all": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web。 
       - Imp：小程序。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 是  聚合维度。取值如下所示： 
       * ErrorCode：错误码 
       * Region：地区 
       * Isp：运营商 
 UploadType (Integer): 否  上传类型，默认为空，返回上传 1.0 数据。取值如下所示： 
       * 1：上传 1.0。 
       * 2：上传 2.0。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 OrderBy (String): 否  目前仅支持传入Count按错误码数量排序。不传或者传空默认按错误码数量排序。 
 OrderAsc (Boolean): 否  是否升序排序。取值如下所示： 
       - true：是，表示升序排序。 
       - false：（默认）否，表示降序排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_upload_speed": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web。 
       - Imp：小程序。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，表示拆分分位数据。 支持取值： 
       - Duration：表示分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 UploadType (Integer): 否  上传类型，默认为空，返回上传 1.0 数据。取值如下所示： 
       * 1：上传 1.0。 
       * 2：上传 2.0。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m： 5 分钟； 
       * 1h： 1 小时； 
       * 1d： 1 天； 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_upload_segment_speed_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型。取值如下所示： 
       - 不传或传空字符串：Android+iOS。 
       - iOS：iOS。 
       - Android：Android。 
       - WEB：web+小程序。 
       - Web：web。 
       - Imp：小程序。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，表示拆分分位数据。 支持取值： 
       - Duration：表示分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 UploadType (Integer): 是  上传类型，固定值传入2，表示上传 2.0 数据。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m： 5 分钟； 
       * 1h： 1 小时； 
       * 1d： 1 天； 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_cdn_success_rate_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 StartTime (String): 是  获取数据起始时间点。 
       * 日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       * 日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_cdn_success_rate_all": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配所有非 WEB 端的系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 是  聚合维度。取值如下所示： 
       * Domain：域名； 
       * Region：地区； 
       * Isp：运营商。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 OrderBy (String): 否  * 取值为SuccessRate时，表示按网络成功率排序； 
       * 取值为Count时，表示按上报量排序； 
       * 不传或者传空默认按上报量排序。 
 OrderAsc (Boolean): 否  是否升序排序。取值如下所示： 
       - true：是，表示升序排序。 
       - false：（默认）否，表示降序排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_cdn_error_code_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_cdn_error_code_all": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 是  聚合维度。取值如下所示： 
       * Domain：域名； 
       * ErrorCode：错误码； 
       * Region：地区； 
       * Isp：运营商。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 OrderBy (String): 否  目前仅支持传入Count按错误码数量排序。不传或者传空默认按错误码数量排序。 
 OrderAsc (Boolean): 否  是否升序排序。取值如下所示： 
       - true：是，表示升序排序。 
       - false：（默认）否，表示降序排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_cdn_duration_detail_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 App ID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。支持取值如下： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，标识不拆分。支持取值： 
       * Duration：表示拆分网络耗时分位数据 
       - Phase：表示拆分网络耗时分布数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 Phase (String): 否  指定查询特定阶段的耗时数据。默认空，返回总耗时数据。 
       * dns： DNS 耗时，即网络阶段的 DNS 平均耗时。 
       * ssl： SSL 耗时，即网络阶段的 SSL 握手平均耗时。 
       * connect：连接耗时，即网络阶段的 TCP 建立连接平均耗时。 
       * send：发送耗时，即网络阶段的发送数据平均耗时。 
       * wait：等待耗时，即网络阶段发送完数据后等待首个回包字节的耗时。 
       * receive：接收耗时，即网络阶段的接收数据耗时。 
       * proxy：代理耗时，即网络阶段的建立代理连接的耗时。 
 StartTime (String): 是  获取数据起始时间点。 
       * 日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       * 日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_cdn_duration_all": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 是  聚合维度。取值如下所示： 
       * Domain：域名； 
       * Region：地区； 
       * Isp：运营商。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 OrderBy (String): 否  排序依据。取值如下所示： 
       * Duration：按耗时排序。 
       * Count：（默认）按上报量排序。 
 OrderAsc (Boolean): 否  是否升序排序。取值如下所示： 
       - true：是，表示升序排序。 
       - false：（默认）否，表示降序排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_cdn_reuse_rate_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_cdn_reuse_rate_all": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 是  聚合维度，取值如下所示： 
       - Domain：域名； 
       - Region：地区； 
       - Isp：运营商。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 OrderBy (String): 否  维度区分，不传或者传空默认按上报量排序。取值如下所示： 
       * ReuseRate：按连接复用率排序； 
       * Count：按上报量排序。 
 OrderAsc (Boolean): 否  是否升序排序。取值如下所示： 
       - true：是，表示升序排序。 
       - false：（默认）否，表示降序排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_cdn_protocol_rate_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_failure_rate": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_decode_success_rate_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_decode_duration_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，表示拆分分位数据。支持取值： 
       - Duration：表示拆分分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_queue_duration_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，表示拆分分位数据。支持取值： 
       - Duration：表示拆分分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_error_code_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_error_code_all": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 是  聚合维度。取值如下所示： 
       * Domain：域名； 
       * ErrorCode：错误码； 
       * Region：地区； 
       * Isp：运营商。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 OrderBy (String): 否  目前仅支持传入Count按错误码数量排序。不传或者传空默认按错误码数量排序。 
 OrderAsc (Boolean): 否  是否升序排序。取值如下所示： 
       - true：是，表示升序排序。 
       - false：（默认）否，表示降序排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_load_duration": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，表示拆分分位数据。支持取值： 
       - Duration：表示拆分分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_load_duration_all": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 是  聚合维度，取值如下所示： 
       - Domain：域名 
       - Region：地区 
       - Isp：运营商 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 OrderBy (String): 否  排序依据，取值如下所示： 
       * Duration：按耗时排序。 
       * Count：（默认）按上报量排序。 
 OrderAsc (Boolean): 否  是否升序排序。取值如下所示： 
       - true：是，表示升序排序。 
       - false：（默认）否，表示降序排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_sdk_ver_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_file_size": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，表示拆分分位数据。支持取值： 
       - Duration：表示拆分分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_top_file_size": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 App ID。您可以通过调用获取应用列表的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Top (Integer): 否  查询 Top URL 条数，取值范围为[0,1000]，默认值为 1000。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标""",
    "describe_imagex_client_count_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_quality_rate_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 QualityType (String): 是  质量类型。取值如下所示： 
       - white_suspected：查询白屏率 
       - black_suspected：查询黑屏率 
       - transparent_suspected：查询透明图率 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_top_quality_url": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。您可以通过调用获取应用列表的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 QualityType (String): 是  类型。取值如下所示： 
       - transparent_suspected：透明图 
       - white_suspected：白屏 
       - black_suspected：黑屏 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       起始时间与结束时间间隔小于等于 93 天。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       起始时间与结束时间间隔小于等于 93 天。 
 Top (Integer): 否  查询 Top URL 条数，取值范围为 [0,1000]，默认值为 1000。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标""",
    "describe_imagex_client_demotion_rate_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，表示拆分分位数据。支持取值： 
       - Duration：表示拆分分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 DemotionType (String): 是  降级类型。取值如下所示： 
       - heic：查询 heic 降级率 
       - heif：查询 heif 降级率 
       - avif：查询 avif 降级率 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_client_top_demotion_url": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。您可以通过调用获取应用列表的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 DemotionType (String): 是  降级类型。取值如下所示： 
       - heic：HEIC 降级 
       - heif：HEIF 降级 
       - avif：AVIF 降级 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Top (Integer): 否  查询 Top URL 条数，取值范围为[0,1000]，默认值为 1000。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标""",
    "describe_imagex_client_score_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 Country (String): 否  需要匹配的国家名称。 
       * 不传则匹配所有国家。 
       * 取值为海外时，匹配海外所有国家。 
 Province (String): 否  需要匹配的省份名称，不传则匹配所有省份。 
 Isp (Array of String): 否  需要匹配的运营商名称，不传则匹配所有运营商。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 铁通 
       - 鹏博士 
       - 教育网 
       - 其他 
 Domain (Array of String): 否  需要匹配的域名，不传则匹配所有域名。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 ScoreType (String): 是  打分类型。取值如下所示： 
       - vq：查询 vqscore 指标 
       - aes：查询美学指标 
       - noi：查询噪声指标 
       - psnr：查询 psnr 指标 
       - ssim：查询 ssim 指标 
       - vmaf：查询 vmaf 指标 
 StartTime (String): 是  获取数据起始时间点。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。 
       日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、Country、Province、Isp、Domain、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_sensible_count_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID，缺省情况下匹配账号下所有 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型，缺省情况下匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 AppVer (Array of String): 否  需要匹配 App 版本，缺省情况下则匹配 App 的所有版本。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，缺省情况下则匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，缺省情况下则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，例如2019-06-02T00:00:00+08:00。 
       起始时间与结束时间间隔小于等于 90 天。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，例如2019-06-02T00:00:00+08:00。 
       起始时间与结束时间间隔小于等于 90 天。 
 Granularity (String): 是  返回数据的时间粒度，取值如下所示： 
       - 5m：5分钟； 
       - 1h：1小时； 
       - 1d：1天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_sensible_cache_hit_rate_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID，缺省情况下匹配账号下所有 AppID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型，缺省情况下匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 AppVer (Array of String): 否  需要匹配 App 版本，缺省情况下则匹配 App 的所有版本。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，缺省情况下则匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，缺省情况下则匹配所有图片类型。支持以下取值： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标 
 Type (String): 是  缓存类型。支持以下取值： 
       - 1：查询内存命中率数据； 
       - 2：查询磁盘命中率数据。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，例如2019-06-02T00:00:00+08:00。 
       起始时间与结束时间间隔小于等于 90 天。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，例如2019-06-02T00:00:00+08:00。 
       起始时间与结束时间间隔小于等于 90 天。 
 Granularity (String): 是  返回数据的时间粒度，支持以下取值： 
       - 5m：5分钟； 
       - 1h：1小时； 
       - 1d：1天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_sensible_top_size_url": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，缺省情况下则匹配账号下的所有的 App ID。您可以通过调用获取应用列表的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型，缺省情况下则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 AppVer (Array of String): 否  需要匹配 App 版本，缺省情况下则匹配 App 的所有版本。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，缺省情况下则匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，缺省情况下则匹配所有图片类型。支持以下取值： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - AVIF 
       - AVIS 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Top (Integer): 否  查询 Top URL 条数，取值范围为(0,1000]。缺省情况下默认为 1000。 
 OrderByIdx (Integer): 是  支持以下取值： 
       - 1：按上报次数降序排序； 
       - 2：按文件体积降序排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_sensible_top_resolution_url": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，缺省情况下匹配账号下的所有的 App ID。您可以通过调用GetImageXQueryApps的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型，缺省情况下匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 AppVer (Array of String): 否  需要匹配 App 版本，缺省情况下则匹配 App 的所有版本。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，缺省情况下匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，缺省情况下则匹配所有图片类型。支持以下取值： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - AVIF 
       - AVIS 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Top (Integer): 否  查询 Top URL 条数，取值范围为(0,1000]。缺省情况下默认为 1000。 
 OrderByIdx (Integer): 是  支持以下取值： 
       - 1：按上报次数排序； 
       - 2：按图片分辨率排序； 
       - 3：按 view 分辨率排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_sensible_top_ram_url": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，缺省情况下匹配账号下的所有的 App ID。您可以通过调用GetImageXQueryApps的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型，缺省情况下匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 AppVer (Array of String): 否  需要匹配 App 版本，缺省情况下则匹配 App 的所有版本。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，缺省情况下匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，缺省情况下则匹配所有图片类型。支持以下取值： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - AVIF 
       - AVIS 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Top (Integer): 否  查询 Top URL 条数，取值范围为(0,1000]。缺省情况下默认为 1000。 
 OrderByIdx (Integer): 是  支持以下取值： 
       - 1：按上报次数降序排序； 
       - 2：按内存大小降序排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_sensible_top_unknown_url": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，缺省情况下匹配账号下的所有的 App ID。您可以通过调用GetImageXQueryApps的方式获取所需的 AppID。 
 OS (String): 否  需要匹配的系统类型，缺省情况下匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 AppVer (Array of String): 否  需要匹配 App 版本，缺省情况下匹配 App 的所有版本。 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，缺省情况下匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，缺省情况下则匹配所有图片类型。支持以下取值： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - AVIF 
       - AVIS 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Top (Integer): 否  查询 Top URL 条数，取值范围为(0,1000]。默认值为 1000。 
 OrderByIdx (Integer): 是  支持以下取值： 
       - 1：按上报量排序 
       - 2：按内存大小排序 
       - 3：按文件大小排序 
       - 4：按图片分辨率排序 
       - 5：按 view 分辨率排序 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值。 
       您可以通过调用获取自定义维度值来获取。""",
    "get_image_upload_file": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  文件 Uri。 
       - 您可以在 veImageX 控制台 资源管理页面，在已上传文件的名称列获取资源 Uri。 
       - 您也可以通过 OpenAPI 的方式获取Uri，具体请参考 GetImageUploadFiles。""",
    "preview_image_upload_file": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  文件存储 URI。 
       - 您可以在 veImageX 控制台 资源管理页面，在已上传文件的名称列获取。 
       - 您也可以通过 OpenAPI 的方式获取，具体请参考获取服务下的上传文件。""",
    "get_image_erase_models": """Args:params: A JSON structure
     Type (Integer): 否  模型。默认取值为0。 
       * 0：自动检测并擦除模型列表。 
       * 1：指定区域擦除模型列表。""",
    "update_slim_config": """Args:params: A JSON structure
     ServiceId (String): 是  待修改配置的域名的所属服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Domain (String): 是  域名，您可以通过获取服务下全部域名获取服务下域名信息。 
 DoSlim (Boolean): 是  是否开启集智瘦身，取值如下所示： 
       - true：开启集智瘦身 
       - false：关闭集智瘦身 
 DiscardSlimedFile (Boolean): 是  是否关闭持久化。取值如下所示： 
       - true：关闭 
       - false：开启""",
    "update_domain_adaptive_fmt": """Args:params: A JSON structure
     ServiceId (String): 是  待修改配置的域名的所属服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Domain (String): 是  域名，您可以通过获取服务下全部域名获取服务下域名信息。 
 AdaptFmt (Boolean): 是  是否开启自适应，取值如下所示： 
       - true：开启自适应 
       - false：关闭自适应 
 AdaptFormats (Array of String): 是  自适应格式列表，取值如下所示： 
       - webp：WEBP 自适应 
       - heic：HEIC 自适应 
       - avif：AVIF 自适应 
 CheckAdaptFsize (Boolean): 是  是否开启体积校验，取值如下所示： 
       - true：开启。开启后会对经自适应编码后的图片体积和编码前原图体积进行对比，若编码后体积更小则输出编码后图片；否则输出原图。 
       - false：关闭""",
    "get_response_header_validate_keys": """Args:""",
    "del_domain": """Args:params: A JSON structure
     ServiceId (String): 是  待删除域名的服务 ID。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Domain (String): 是  待删除的域名，您可以通过 获取服务下全部域名 获取服务下域名信息。""",
    "set_default_domain": """Args:body: A JSON structure
     Domain (String): 是  指定新的默认域名，您可以通过获取服务下全部域名获取服务下域名信息。""",
    "fetch_image_url": """Args:body: A JSON structure
     Url (String): 是  待抓取上传的文件 URL。 
 ServiceId (String): 是  目标服务 ID，迁移后的文件将上传至该服务绑定的存储。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreKey (String): 否  指定抓取成功后的文件存储 key，不包含 bucket 部分。默认使用随机生成的 key。 
       若指定 key 已存在，则会覆盖服务中 StoreKey 对应的已有文件，此时服务中保存文件的数量未发生变化。 
 RequestHeader (JSON Map): 否  请求 header 
        
        
        
        
 TimeOut (Integer): 否  资源下载超时时间。 
       - 同步处理下最大超时为 20 秒； 
       - 异步处理下最大超时为 90 秒。 
 Async (Boolean): 否  是否采用异步，取值如下所示： 
       - true：采用异步 
       - false：（默认）不采用异步 
       若您的资源大小小于 5 G，但预估资源迁移超时时间超过 20 s，建议您选择异步处理。 
 Host (String): 否  迁移资源的 IP 地址 
 Callback (String): 否  回调 URL，veImageX 以 Post 方式向业务服务器发送 JSON 格式回调数据。当Async取值为true，即采用异步处理时，为必填。 
 MD5 (String): 否  校验下载文件的 MD5，若校验不一致则停止文件的上传。 
 CallbackBodyType (String): 否  透传给业务的回调内容格式。当CallbackBody不为空时为必填。取值如下所示： 
       - application/json 
       - application/x-www-form-urlencoded 
 CallbackBody (String): 否  透传给业务的回调内容，当Callback不为空时为必填，取值需要符合CallbackBodyType指定格式。 
        
        
        
        
        
 CallbackHost (String): 否  回调时使用的 IP 地址 
 IgnoreSameKey (Boolean): 否  服务存储中存在相同的存储 key 时，是否忽略本次迁移操作。取值如下所示： 
       - true：忽略本次迁移操作。 
       - false：（默认）继续迁移并覆盖相同 key 的资源。 
 FetchOnly (Boolean): 否  是否仅迁移文件，取值如下所示： 
       - true：仅将文件迁移至目标服务对应的存储。适用于文件快速迁移且无需获取图片元信息场景，例如对时间敏感度极高的文件传输任务。 
       - false：（默认）迁移文件的同时，对图片类文件进行解码处理。适用于需要获取图片元信息而对迁移时间要求不高的场景。解码图片资源后，您可在返回参数获取图片的元信息，包括图片宽高、图片类型、动图的时间和帧数等，便于后续的图片分析和管理。""",
    "create_hidden_watermark_image": """Args:params: A JSON structure
     ServiceId (String): 是  用于存储结果图和计量计费的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Algorithm (String): 是  盲水印模型，取值如下所示： 
       - tracev1：前景图层水印模型（纯色背景适用）。 
       	 
       	该模型可以生成带有水印的透明图像，但仅适用于纯色网页泄露溯源场景。该模型可有效抵抗常见的社交软件传播。然而，该算法对页面背景色的影响相对较大，因此不适合用于保护多彩页面或图片，例如商品页面。 
       	 
       - tracev2：前景图层水印模型（彩色背景通用） 
       	该模型可以生成含水印的透明图像，主要应用在前端页面截图泄露溯源场景。该模型生成的水印纹理密集，在正常界面添加后肉眼基本不可见（截图放大后存在肉眼可见的水印纹理），可抵抗常见的社交软件传播。 
 Strength (String): 是  盲水印强度，取值如下所示： 
       - low：低强度，适用于对图像质量要求高。 
       - medium：中强度 
       - strong：高强度，适合图像纹理丰富时使用。 
 Info (String): 是  自定义盲水印文本信息，最多支持 128 个字符。""",
    "describe_imagex_domain_bandwidth_ninety_five_data": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。支持查询多个服务，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有服务。您可以在 veImageX 控制台的服务管理模块或者调用 GetAllImageServices 接口获取服务 ID。 
 DomainNames (String): 否  域名。支持查询多个域名，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有域名。您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 BillingRegion (String): 否  计费区域。支持查询多个区域，传入多个时用英文逗号“,”分割，缺省情况下表示查询所有区域。取值如下所示： 
       - CHN：中国内地 
       - AP1：亚太一区 
       - AP2：亚太二区 
       - AP3：亚太三区 
       - EU：欧洲 
       - ME：中东和非洲 
       - SA：南美 
       - NA：北美 
       - OTHER：其他 
 StartTime (String): 是  取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近一年历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2010-11-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。""",
    "get_batch_process_result": """Args:params: A JSON structure
     ServiceId (String): 是  指定同步批处理的服务 ID。 
    body: A JSON structure
     BatchingInfo (Array of BatchingInfo): 是  待批量处理的资源链接信息 

字段： BatchingInfo
       - meta：获取资源元信息 
       - preload：源站图片预热 
       如需批量预热源站图片，请 提交工单联系技术支持开启。 
 Url (String): 否  指定服务下待批处理资源的可访问 URL""",
    "create_batch_process_task": """Args:params: A JSON structure
     ServiceId (String): 是  待执行异步批处理的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     BatchingInfo (Array of BatchingInfo): 是  指定服务下待批量处理的资源链接信息 
 Callback (String): 否  回调地址，用于接收返回的回调信息。 
 CallbackBody (String): 否  自定义回调内容，取值需要符合CallbackBodyType指定格式。 
        
        
        
        
        
 CallbackBodyType (String): 否  回调内容格式。默认为空，若需指定CallbackBody时，也需同时指定CallbackBodyType的值。取值如下所示： 
       - application/json 
       - application/x-www-form-urlencoded 

字段： BatchingInfo
       - meta：获取资源元信息 
       - preload：源站图片预热 
       如需批量预热源站图片，请 提交工单联系技术支持开启。 
 Url (String): 否  指定服务下待批处理资源的可访问 URL""",
    "get_batch_task_info": """Args:params: A JSON structure
     TaskId (String): 是  异步任务 ID，传入 CreateBatchProcessTask 获取的异步任务 ID。 
 ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "update_file_storage_class": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     StoreUri (String): 是  文件存储 URI。 
       - 您可以在 veImageX 控制台 资源管理页面，在已上传文件的名称列获取资源 URI。 
       - 您也可以通过 OpenAPI 的方式获取 URI，具体请参考[获取服务下全部上传文件 
       ](https://www.volcengine.com/docs/508/9393)。 
 StorageClass (String): 是  修改后的存储类型，取值如下所示： 
       - STANDARD：标准存储 
       - IA：低频存储 
       - ARCHIVE_FR：归档闪回存储  
       - ARCHIVE：归档存储 
       - COLD_ARCHIVE：冷归档存储""",
    "create_file_restore": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     StoreUri (String): 是  文件存储 URI。 
       - 您可以在 veImageX 控制台 资源管理页面，在已上传文件的名称列获取资源 URI。 
       - 您也可以通过 OpenAPI 的方式获取 URI，具体请参考获取服务下全部上传文件。 
 Duration (Integer): 是  恢复时长，取值范围为[1,365]，单位为天。 
 Tier (String): 否  取回方式： Expedited：快速取回 Standard：标准取回 Bulk：批量取回；不设置默认standard""",
    "update_storage_rules": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     StorageRules (Array of StorageRules): 否  更新后的存储降冷策略 

字段： StorageRules
 Prefix (String): 否  文件前缀。例如设置为 prefix 后，规则将只对名称以 prefix 开头的存储资源生效。输入规则如下： 
       - 不能以正斜线（/）或者反斜线（）开头； 
       - 不支持使用正则表达式匹配前缀； 
       - 长度为 1～1024 个字符。 
 Event (String): 是  策略类型，固定取值 Upload，表示按上传时间。 
 Day (Integer): 是  最新版本文件的策略天数，取值范围为 [1,365]，单位为天。按照 Event 事件 Day 天后执行 Action 事件，即当匹配文件的上传时间符合指定天数后，自动按照处理策略对资源进行处理。 
       - DELETE：删除文件 
       - IA：文件转低频存储 
       - ARCHIVE：文件转归档存储 
       - COLD_ARCHIVE：文件转冷归档存储 
 NonCurrentDay (Integer): 是  历史版本文件的策略天数，取值范围为 [1,365]，单位为天。按照 Event 事件 NonCurrentDay 天后执行 NonCurrentAction 事件，即当匹配历史版本文件的上传时间符合指定天数后，自动按照处理策略对历史版本资源进行处理。 
 NonCurrentAction (String): 是  历史版本文件在策略命中后需要执行的操作，取值如下所示： 
       - DELETE：删除文件 
       - IA：文件转低频存储 
       - ARCHIVE：文件转归档存储 
       - COLD_ARCHIVE：文件转冷归档存储 
 Enable (Boolean): 是  是否启用策略，取值如下所示： 
       - true：是 
       - false：否""",
    "get_all_image_services": """Args:params: A JSON structure
     SearchPtn (String): 否  筛选服务的参数，当该值为空时返回所有服务，指定后返回服务名或者 ID 中包含该字符串的服务。""",
    "describe_imagex_bucket_retrieval_usage": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。为空时表示不筛选，支持查询多个服务，使用逗号分隔不同的服务。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考 GetAllImageServices。 
 BucketNames (String): 否  Bucket 名称。支持同时查询多个 BucketName，不同的 BucketNmae 使用逗号分隔。 
       您可以通过调用 GetAllImageServices 获取所需的 Bucket 名称。 
 GroupBy (String): 否  需要分组查询的参数，多个数据用逗号分隔。支持取值如下： 
       - ServiceId：服务 ID 
       - BucketName：Bucket 名称 
       - StorageType：存储类型 
 StartTime (String): 是  获取数据起始时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近一年历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2010-11-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm。例如2019-06-02T00:00:00+08:00。 
 IsRetrieval (Boolean): 否  是否查询数据取回量。 
       - true：查询取回量。 
       - false：查询存储量。""",
    "get_image_detect_result": """Args:params: A JSON structure
     ServiceId (String): 是  待检测图片对应的服务 ID。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     ImageUri (String): 是  指定服务下的待检测图片的 StoreUri 或者公网可访问 Url。 
 DetectType (String): 是  检测类型，取值仅支持 face，表示检测图片中人脸所在坐标。 
 FaceDetectThresh (Float): 否  当 DetectType 取值 face 时，为必填。 
       人脸检测阈值，推荐值为 0.52（默认值），取值范围为 (0,1)。值越高，对检测结果过滤越严格，召回率越低，精确率越高。 
       - 阈值过低，表示图片中的检测样本较多，可能会导致非人脸样本被纳入检测范围，从而降低精确率。 
       - 阈值过高，表示图片中的检测样本较少，可能导致样本漏检。""",
    "update_image_resource_status": """Args:params: A JSON structure
     ServiceId (String): 是  指定配置资源封禁的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考GetAllImageServices。 
    body: A JSON structure
     ObjectName (String): 是  待修改封禁状态的资源存储 Key（不携带 Bucket 信息），可在控制台资源管理页面查看。 
 Status (String): 是  资源的封禁状态，取值如下所示： 
       - disable：禁用。禁用状态，您无法访问该资源。 
       - enable：启用。启用状态，您可正常访问该资源。""",
    "describe_imagex_exceed_count_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。您可以通过调用查询应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。取值如下所示： 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - AVIF 
       - AVIS 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，表示拆分分位数据。支持取值： 
       - Duration：表示拆分分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用查询自定义维度列表接口获取自定义维度指标 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度，取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用查询自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用查询自定义维度值来获取。""",
    "describe_imagex_exceed_file_size": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - AVIF 
       - AVIS 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，表示拆分分位数据。支持取值： 
       - Duration：表示拆分分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、Country、Province、Isp、Domain 
       - 自定义维度：您可以通过调用获取自定义维度列表接口获取自定义维度指标 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度，取值如下所示： 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_exceed_resolution_ratio_all": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 AppID。您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配非 WEB 端的所有系统。取值如下所示： 
       - iOS 
       - Android 
       - WEB 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本. 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。 
       - GIF 
       - PNG 
       - JPEG 
       - HEIF 
       - HEIC 
       - WEBP 
       - AWEBP 
       - VVIC 
       - AVIF 
       - AVIS 
       - 其他 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 OrderBy (String): 否  排序依据，不传或者传空默认按上报量排序。取值如下所示： 
       - Count：按上报量排序 
       - WidthRatio：按宽比排序 
       - HeightRatio：按高比排序 
 OrderAsc (String): 否  是否升序排序，取值如下所示： 
       - true：是，表示升序排序。 
       - false：（默认）否，表示降序排序。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "get_image_migrate_tasks": """Args:params: A JSON structure
     Region (String): 否  任务地区（即任务目标服务的地区），缺省时将返回国内列表。取值如下所示： 
       - cn：国内 
       - sg：新加坡 
 TaskId (String): 否  任务 ID。 
 ServiceId (String): 否  迁移的目标服务 ID。 
 Offset (Long): 否  分页偏移量，用于控制分页查询返回结果的起始位置，以便对数据进行分页展示和浏览。默认值为 0。 
       例如，指定分页条数 Limit = 10，分页偏移量 Offset = 10，表示从查询结果的第 11 条记录开始返回数据，共展示 10 条数据。 
 Limit (Integer): 否  分页查询时，显示的每页数据的最大条数。默认值为 10，最大值为 1000。 
 TaskNamePtn (String): 否  返回任务名称中包含该值的迁移任务信息。 
 Status (String): 否  任务状态，填入多个时使用英文逗号分隔。取值如下所示： 
       - Initial：创建中 
       - Running：运行中 
       - Done：全部迁移完成 
       - Partial：部分迁移完成 
       - Failed：迁移失败 
       - Terminated：中止""",
    "rerun_image_migrate_task": """Args:params: A JSON structure
     Region (String): 否  任务地区（即任务目标服务的地区），默认空，返回国内任务。 
       - cn：国内 
       - sg：新加坡 
 TaskId (String): 是  仅当任务状态为Partial时生效。 
       任务 ID，请参考 GetImageMigrateTasks获取返回的任务 ID。""",
    "terminate_image_migrate_task": """Args:params: A JSON structure
     Region (String): 否  任务地区（即任务目标服务的地区），默认空，返回国内任务。 
       - cn：国内 
       - sg：新加坡 
 TaskId (String): 是  任务 ID，请参考 GetImageMigrateTasks 获取返回的任务 ID。""",
    "delete_image_migrate_task": """Args:params: A JSON structure
     Region (String): 否  任务地区（即任务目标服务的地区），默认空，返回国内任务。 
       - cn：国内 
       - sg：新加坡 
 TaskId (String): 是  仅当任务状态为非Running时生效。 
       任务 ID，请参考 GetImageMigrateTasks获取返回的任务 ID。""",
    "create_image_migrate_task": """Args:body: A JSON structure
     Task (Object of Task): 是  任务信息 

字段： Task
 Name (String): 是  自定义迁移任务名称 
 Source (Object of Source): 是  迁移源信息 
 Transcode (Object of Transcode): 否  转码配置 
 Dst (Object of Dst): 是  目的信息 
 RunStrategy (Object of RunStrategy): 否  迁移策略 
 CallbackCfg (Object of CallbackCfg): 否  回调信息。配置后，当任务执行完成时，将往该回调配置地址发送任务回调信息。 

字段： Source
 Vendor (String): 是  迁移云服务商。取值如下所示： 
       - OSS：阿里云 
       - COS：腾讯云 
       - KODO：七牛云 
       - BOS：百度云 
       - OBS：华为云 
       - Ucloud：Ucloud file 
       - AWS：AWS 国际站 
       - S3：其他 S3 协议存储 
       - URL：以上传 URL 列表的方式迁移 
 AK (String): 否  仅当Vendor 非 URL时，为必填。 
       Access Key，与 Secret Key 同时填写，为了保证有访问源数据桶的权限。 
       - 请参考云数据迁移准备获取对应阿里云OSS、腾讯云COS、七牛云KODO、百度云BOS、华为云OBS、 优刻得（Ucloud File)、AWS国际站的账号 AK/SK。 
       - 对于其他 S3 协议存储的AK/SK，请根据其具体源站信息填写。 
 SK (String): 否  仅当Vendor 非 URL时，为必填。 
       Secret Key，与 Access Key 同时填写，为了保证有访问源数据桶的权限。 
       - 请参考云数据迁移准备获取对应阿里云OSS、腾讯云COS、七牛云KODO、百度云BOS、华为云OBS、 优刻得（Ucloud File)、AWS国际站的账号 AK/SK。 
       - 对于其他 S3 协议存储的AK/SK，请根据其具体源站信息填写。 
 Region (String): 否  仅当Vendor 非 URL/OSS/KODO/AWS时，为必填。 
       Bucket 所在地区。 
       - 请参考云数据迁移准备获取对应阿里云OSS、腾讯云COS、七牛云KODO、百度云BOS、华为云OBS、 优刻得（Ucloud File)、AWS国际站的 Bucket 地区。 
       - 对于其他 S3 协议存储的 Bucket 地区，请根据其具体源站信息填写。 
 Bucket (String): 是  - 仅当Vendor为URL时，需填写 URL 列表文件地址（公网 URL 地址）。 
       	支持指定迁移文件和转码后迁移文件进行重命名，详见 URL 列表迁移文件说明。 
       - 当Vendor为其他时，需填写对应云服务商所需迁移数据的 Bucket 名称。您可参考云数据迁移准备获取对应阿里云OSS、腾讯云COS、七牛云KODO、百度云BOS、华为云OBS、 优刻得（Ucloud File)、AWS国际站的 Bucket 名称。 
 Endpoint (String): 否  仅当Vendor为S3时，为必填。 
       S3 协议 Endpoint，需以http://或https://开头。请根据源站信息填写。 
 CdnHost (String): 否  仅当Vendor 非 URL时，为选填。 
       迁移源云服务商 CDN 域名，若不为空将使用该 CDN 域名下载三方云厂商的资源。 
 SkipHeader (Boolean): 否  是否丢弃源 Header。取值如下所示： 
       - true：丢弃源 Header 
       - false：（默认）保留源 Header 
 Prefix (Array of String): 否  仅迁移匹配的前缀列表文件。文件路径前缀无需包含桶名称，但需要完整路径。 
       默认为空，表示对该存储 Bucket 内资源执行全量迁移。若不为空，表示仅做部分迁移，即指定迁移的文件路径前缀。 
 Regex (Array of String): 否  仅迁移匹配的正则表达式列表的文件。默认为空，表示对该存储 Bucket 内资源执行全量迁移。 
       - 多条正则表达式之间是"或"的关系，即源文件匹配任何一条正则表达式即视为符合迁移条件。 
       - 正则过滤规则需要遍历源桶中的全部文件，如果源桶中文件数量较多会降低迁移速度。 
 TimeStart (String): 否  迁移文件起始时间点。仅迁移该查询时间段内新增或变更的文件。默认为空。 
       日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 TimeEnd (String): 否  迁移文件结束时间点。默认为空。仅迁移该查询时间段内新增或变更的文件。 
       日期格式按照 ISO8601 表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 BucketInventoryDir (String): 否  仅当 Vendor 取值 COS 时，为选填。不为空，表示使用桶清单方式进行数据迁移；若为空，将遍历指定 Bucket 内的文件后再进行迁移。 
       桶清单 csv 文件在第三方云存储 Bucket 中的存储目录路径。该路径不携带域名和 csv 清单文件信息，需要以/结尾。您可参考获取桶清单文件存储路径获取。 
 BucketInventorySchema (Array of String): 否  仅当 BucketInventoryDir 不为空时，为必填。 
       桶清单文件的表头信息，需要传入实际桶清单文件内每列数据对应字段名称，并遵循原字段位置进行填写。您可参考获取桶清单文件解析位置获取解析 csv 文件所需的字段信息。 
       - Key ：【必填】表示待迁移的资源存储 Key。 
       - Size ：【推荐】表示待迁移的资源大小。 
       - ETag ：【可选】表示待迁移资源的 ETag 值。 
       veImageX 按照该字段顺序对 csv 文件进行解析，获取待迁移文件详细信息。若位置填写错误，可能导致迁移失败。 
       示例： 
       1. 若 csv 文件内 Key、Size和 ETag 分别位于整张数据表的第 3 列、第 4 列和第 6 列。那么，此时 BucketInventorySchema取值应为 ["", "", "Key", "Size", "", "ETag"]； 
       2. 若 csv 文件内 Key、Size和 ETag 分别位于整张数据表的第 2 列、第 4 列和第 5 列。那么，此时 BucketInventorySchema取值应为 ["", "Key", "", "Size", "ETag", ""]。 
       csv 文件内数据的位置可能会因为您配置桶清单时选择的清单内容而产生差异，具体请以实际为准。 

字段： Transcode
 Adapt (Boolean): 否  仅当转码/降级格式为 heic、webp、jpeg 时生效。 
       是否开启自适应转码。 
       - true：开启。开启后，将根据 Format 或者 DemotionFmt 指定格式进行自适应转码处理。 
       - false：（默认）关闭 
 Format (String): 是  目标转码格式，仅针对静图执行转码策略。支持的格式有 png、jpeg、heic、avif、webp、vvic。 
 Quality (Integer): 是  转码质量参数，取值范围为 [1,100]。对于 PNG 为无损压缩，其他格式下其值越小，压缩率越高，画质越差。 
 AlphaDemotion (Boolean): 否  包含透明通道的图片是否编码为降级格式。取值如下所示： 
       - true：降级 
       - false：（默认）不降级 
 DemotionFmt (String): 否  降级编码格式，仅当AlphaDemotion为true时必填。支持的格式有 png、jpeg、heic、avif、webp、vvic。 
 EnableExif (Boolean): 否  转码是否保留 exif 信息。取值如下所示： 
       - true：保留 
       - false：（默认）不保留 
 SkipCMYK (Boolean): 否  对带有 CMYK 色彩空间的图片，是否跳过转码处理直接存储原图。取值如下所示： 
       - true：是 
       - false：（默认）否 
 ReserveJpegSize (Boolean): 否  当 jpeg 原图在迁移中指定转码为 heic 图时， heic 图是否需要存储原图大小的数据。 
       - true：是 
       - false：（默认）否 

字段： Dst
 ServiceId (String): 是  迁移目标服务 ID，请提前新建服务。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 SkipBucket (Boolean): 否  源 Bucket 名称保留规则。取值如下所示： 
       - true：不保留，迁移后资源访问 URI 中，不保留迁移源的 Bucket 名称。 
       - false：（默认）保留，迁移后资源访问 URI 中，会保留迁移源的 Bucket 名称。 
 Prefix (String): 否  目标 key 前缀，即保存到到指定目录下。如需多重目录，请使用/分割，并以/结尾。 
       默认为空，表示迁移到根目录。 
       - 使用非 URL 方式迁移到根目录时：迁移后 存储 Key 与源存储 Bucket 的文件存储 Key 相同。 
       - 使用 Url 方式迁移到根目录时：迁移后存储 Key 与源 URL 中 Path 值相同。 
 UploadConf (Integer): 否  同名文件覆盖规则配置。取值如下所示： 
       - 0：（默认）直接覆盖同名文件 
       - 1：增加文件名后缀，后缀为任务 ID 
       - 2：跳过同名文件，即不做迁移 
       同名文件指文件在对象存储中的访问 Key 相同的文件，调用 veImageX 服务时会用到文件访问 Key。 

字段： RunStrategy
 ReadQps (Array of Integer): 否  源下载 QPS 限制。如取值不为空，则长度必须为 24，表示一天 24 小时内各小时的 QPS 限制值。默认无限制。 
       - 取值为负值时，表示无限制 
       - 取值为 0 时，表示对应时间不允许迁移 
 ReadRate (Array of Integer): 否  源下载流量限制。单位为 Byte。如取值不为空，则长度必须为24，表示一天 24 小时内各小时的流量限制值。默认无限制。 
       - 取值为负值时，表示无限制 
       - 取值为 0 时，表示对应时间不允许迁移 

字段： CallbackCfg
 Method (String): 是  回调方法。仅支持取值为 http。 
 Addr (String): 是  回调地址。Method取值http时，填写公网可访问的 URL 地址，任务结束将向该地址发送 HTTP POST 请求。具体回调参数请参考回调内容。 
 IncludeEntry (Boolean): 否  回调信息中是否包含具体迁移任务条目信息。取值如下所示： 
       - true：包含。仅包含迁移成功的任务条目信息，迁移失败的任务列表请在迁移完成后调用 ExportFailedMigrateTask 接口获取。 
       - false：（默认）不包含。 
       若任务中包含的条目数量过多，会导致回调消息体过大，增加回调失败的风险。因此建议仅在任务中条目量级不超过十万时使用该参数。 
 CallbackArgs (String): 否  任务维度自定义回调参数，最多可输入 1024 个任意类型字符，并在回调的 CallbackArgs 中返回。""",
    "update_image_task_strategy": """Args:body: A JSON structure
     RunStrategy (Object of RunStrategy): 是  调整后的迁移策略 
 TaskId (String): 是  任务ID，请参考CreateImageMigrateTask获取返回的任务 ID。 

字段： RunStrategy
 ReadQps (Array of Integer): 否  源下载 QPS 限制。如取值不为空，则长度必须为 24，表示一天 24 小时内各小时的 QPS 限制值。默认无限制。 
       - 取值为负值时，表示无限制 
       - 取值为 0 时，表示对应时间不允许迁移 
 ReadRate (Array of Integer): 否  源下载流量限制。单位为 Byte。如取值不为空，则长度必须为24，表示一天 24 小时内各小时的流量限制值。默认无限制。 
       - 取值为负值时，表示无限制 
       - 取值为 0 时，表示对应时间不允许迁移""",
    "get_vendor_buckets": """Args:body: A JSON structure
     Vendor (String): 是  服务商。取值如下所示： 
       - OSS：阿里云 
       - COS：腾讯云 
       - KODO：七牛云 
       - BOS：百度云 
       - OBS：华为云 
       - Ucloud：Ucloud file 
       - AWS：AWS 国际站 
       - S3：其他 S3 协议存储 
       - URL：以上传 URL 列表的方式迁移 
 Region (String): 否  Bucket 所在地区。仅当Vendor 非 URL/OSS/KODO/AWS 时为必填。 
 AK (String): 是  Access Key。是与 Secret Key 同时填写的，为了保证有访问源数据桶的权限。 
 SK (String): 是  Secret Key。是与 Access Key 同时填写的，为了保证有访问源数据桶的权限。 
 Endpoint (String): 是  S3 协议 Endpoint，需以http://或https://开头。仅当Vendor为S3时必填。""",
    "export_failed_migrate_task": """Args:params: A JSON structure
     Region (String): 是  任务地区（即任务目标服务的地区），默认空，返回国内任务。 
       - cn：国内 
       - sg：新加坡 
 TaskId (String): 是  任务 ID，请参考CreateImageMigrateTask获取返回的任务 ID。""",
    "describe_imagex_source_request": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。为空时表示不筛选，支持查询多个服务，使用逗号分隔不同的服务。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考 GetAllImageServices。 
 DomainNames (String): 否  域名。为空时表示不筛选，支持查询多个域名，不同的域名使用逗号分隔。 
       您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 Regions (String): 否  区域。传入多个时用英文逗号作为分割符，缺省情况下表示查询所有区域。取值如下所示： 
       - 中国大陆 
       - 亚太一区 
       - 亚太二区 
       - 亚太三区 
       - 欧洲区 
       - 北美区 
       - 南美区 
       - 中东区 
 UserCountry (String): 否  客户端国家。传入多个时用英文逗号作为分割符，缺省情况下表示不过滤。可调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端国家。取值如下所示： 
       - 海外，除中国外全部国家。 
       - 具体国家取值，如中国、美国。 
 UserProvince (String): 否  客户端省份。传入多个用英文逗号分割。缺省情况下表示不过滤。可调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端省份。 
 Protocols (String): 否  过滤网络协议。传入多个用英文逗号分割。缺省情况下表示不过滤。取值如下所示： 
       - HTTP 
       - HTTPS 
 Isp (String): 否  过滤运营商。传入多个用英文逗号分割，缺省情况下表示不过滤。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 鹏博士 
       - 教育网 
       - 广电网 
       - 其它 
 DataTypes (String): 是  状态码。传入多个时用英文逗号分隔。支持以下取值： 
       - req_cnt：返回所有状态码数据 
       - 2xx：返回 2xx 状态码汇总数据 
       - 3xx：返回 3xx 状态码汇总数据 
       - 4xx：返回 4xx 状态码汇总数据 
       - 5xx：返回 5xx 状态码汇总数据。 
 GroupBy (String): 否  需要分组查询的参数。传入多个用英文逗号分割。支持以下取值： 
       - DomainName：域名 
       - DataType：状态码 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒，缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。支持以下取值： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天 
 DetailedCode (Boolean): 否  是否拆分状态码。取值如下所示： 
       - true：拆分 
       - false：（默认）不拆分""",
    "describe_imagex_source_request_bandwidth": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。为空时表示不筛选，支持查询多个服务，使用逗号分隔不同的服务。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考 GetAllImageServices。 
 DomainNames (String): 否  域名。为空时表示不筛选，支持查询多个域名，不同的域名使用逗号分隔。 
       您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 Regions (String): 否  区域。传入多个时用英文逗号作为分割符，缺省情况下表示查询所有区域。取值如下所示： 
       - 中国大陆 
       - 亚太一区 
       - 亚太二区 
       - 亚太三区 
       - 欧洲区 
       - 北美区 
       - 南美区 
       - 中东区 
 UserCountry (String): 否  客户端国家。传入多个时用英文逗号作为分割符，缺省情况下表示不过滤。可调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端国家。取值如下所示： 
       - 海外，除中国外全部国家。 
       - 具体国家取值，如中国、美国。 
 UserProvince (String): 否  客户端省份。传入多个用英文逗号分割。缺省情况下表示不过滤。可调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端省份。 
 Protocols (String): 否  过滤网络协议。传入多个用英文逗号分割。缺省情况下表示不过滤。取值如下所示： 
       - HTTP 
       - HTTPS 
 Isp (String): 否  过滤运营商。传入多个用英文逗号分割，缺省情况下表示不过滤。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 鹏博士 
       - 教育网 
       - 广电网 
       - 其它 
 GroupBy (String): 否  分组依据，仅支持取值DomainName。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒，缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。支持以下取值： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "describe_imagex_source_request_traffic": """Args:params: A JSON structure
     ServiceIds (String): 否  服务 ID。为空时表示不筛选，支持查询多个服务，使用逗号分隔不同的服务。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考 GetAllImageServices。 
 DomainNames (String): 否  域名。为空时表示不筛选，支持查询多个域名，不同的域名使用逗号分隔。 
       您可以通过调用 GetServiceDomains 获取服务下所有域名信息。 
 Regions (String): 否  区域。传入多个时用英文逗号作为分割符，缺省情况下表示查询所有区域。取值如下所示： 
       - 中国大陆 
       - 亚太一区 
       - 亚太二区 
       - 亚太三区 
       - 欧洲区 
       - 北美区 
       - 南美区 
       - 中东区 
 UserCountry (String): 否  客户端国家。传入多个时用英文逗号作为分割符，缺省情况下表示不过滤。可调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端国家。取值如下所示： 
       - 海外，除中国外全部国家。 
       - 具体国家取值，如中国、美国。 
 UserProvince (String): 否  客户端省份。传入多个用英文逗号分割。缺省情况下表示不过滤。可调用 DescribeImageXEdgeRequestRegions 获取 IP 解析后的客户端省份。 
 Protocols (String): 否  过滤网络协议。传入多个用英文逗号分割。缺省情况下表示不过滤。取值如下所示： 
       - HTTP 
       - HTTPS 
 Isp (String): 否  过滤运营商。传入多个用英文逗号分割，缺省情况下表示不过滤。取值如下所示： 
       - 电信 
       - 联通 
       - 移动 
       - 鹏博士 
       - 教育网 
       - 广电网 
       - 其它 
 GroupBy (String): 否  分组依据，仅支持取值DomainName。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
       由于仅支持查询近 93 天的历史数据，则若此刻时间为2011-11-21T16:14:00+08:00，那么您可输入最早的开始时间为2011-08-21T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Interval (String): 否  查询数据的时间粒度。单位为秒，缺省时查询StartTime和EndTime时间段全部数据，此时单次查询最大时间跨度为 93 天。支持以下取值： 
       - 60：单次查询最大时间跨度为 6 小时 
       - 120：单次查询最大时间跨度为 6 小时 
       - 300：单次查询最大时间跨度为 31 天 
       - 600：单次查询最大时间跨度为 31 天 
       - 1200：单次查询最大时间跨度为 31 天 
       - 1800：单次查询最大时间跨度为 31 天 
       - 3600：单次查询最大时间跨度为 93 天 
       - 86400：单次查询最大时间跨度为 93 天 
       - 604800：单次查询最大时间跨度为 93 天""",
    "create_image_from_uri": """Args:params: A JSON structure
     ServiceId (String): 是  复制目标对应的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     OriServiceId (String): 否  待复制资源对应的服务 ID 
 StoreUri (String): 是  待复制资源对应的存储 URI。您可在控制台的资源管理页面，获取上传文件的存储 URI；或者调用 GetImageStorageFiles 获取指定服务下的存储 URI。 
 DstKey (String): 否  复制后资源的存储 Key。缺省情况下与源存储的资源存储 Key 相同。自定义规则如下所示： 
       - 不支持空格。 
       - 不支持以/开头或结尾，不支持/连续出现，Key 值最大长度限制为 180 个字节。 
 SkipDuplicate (Boolean): 否  是否保留目标存储中的同名文件，取值如下所示： 
       - false：不保留目标存储中的同名文件，直接覆盖。 
       - true：保留目标存储中的同名文件，不覆盖。""",
    "get_image_enhance_result_with_data": """Args:body: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreUri (String): 是  待增强的原图地址的存储 URI 和 URL（公网可访问的 URL）。 
 Model (Integer): 是  增强模型，取值如下所示： 
       - 0：通用模型 
       - 1：低质专清模型 
 DisableSharp (Boolean): 是  是否不去压缩失真。Model取值为0时选填，支持以下取值： 
       - true：不进行去压缩失真处理 
       - false：（默认）进行去压缩失真处理 
 DisableAr (Boolean): 是  是否不自适应锐化。Model取值为0时选填，支持以下取值： 
       - true：不进行锐化处理 
       - false：（默认）进行锐化处理""",
    "get_product_aigc_result": """Args:params: A JSON structure
     ServiceId (String): 是  用于存储结果图和计量计费的服务 ID。 
       - 您可以在veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       	 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Url (String): 是  商品主体图的访问 URL（公网可访问）。建议为包含完整商品主体的白底图或透底图，尽量避免复杂背景的影响，以确保最终生成效果的质量。 
 NeedSeg (Boolean): 否  是否使用分割处理图片，取值如下所示： 
       - true：分隔处理。 
       - false：（默认）不分割处理，将从输入图像读取 alpha 通道作为商品图数据。 
       	指定为 false 时，确保通过 Url 传入的商品主体图是已经过分割的白底图或透底图。 
 BatchSize (Integer): 否  每次生成的图片数量，取值范围为 [1,4]，默认值为 4。 
 OutputSize (Integer): 是  同时指定结果图长和宽的值，单位为 px。取值范围为 [512,1024]。 
       结果图是指定BatchSize张长宽比为 1:1 的方图。 
 Scene (String): 否  根据所选场景生成结果图，场景支持以下选项： 
       - indoor wooden table：室内木桌场景 
       	 
       - flower and leaves：鲜花绿植场景 
       	 
       - white marble table：白色大理石场景 
       	 
       - outdoor snow scene：室外雪景场景 
       	 
       - supermarket show scene：超市小件商品 
       	 
       - food in kitchen：食品厨房场景 
       	 
       - sports style：运动场景 
       	 
       - modern room：现代室内 
       提示词和 Scene 二选一必填，两者均存在时，以 Scene 为准。 
 NegativePrompt (String): 否  输入到 AIGC 模型的负向提示词，提示词和 Scene 二选一必填。两者均存在时，以 Scene 为准。当前仅支持英文，最多不超过 300 个字母。 
       - indoor wooden table 场景下可采用的负向提示词为： 
       	- top view, empty background, extra connection, wheel, stand, lowres, ugly, bad anatomy, bad hands, cropped, worst quality, baby, body, human, brand, bad face 
       - flower and leaves场景下可采用的负向提示词为： 
       	- top view, empty background, extra connection, wheel, stand, lowres, ugly, bad anatomy, bad hands, cropped, worst quality, baby, body, human, brand, bad face 
       - white marble table场景下可采用的负向提示词为： 
       	- top view, empty background, extra connection, wheel, stand, lowres, ugly, bad anatomy, bad hands, cropped, worst quality, baby, body, human, brand, bad face 
       - outdoor snow scene场景下可采用的负向提示词为： 
       	- op view, empty background, extra connection, wheel, stand, lowres, ugly, bad anatomy, bad hands, cropped, worst quality, baby, body, human, brand, bad face 
       - supermarket show scene场景下可采用的负向提示词为： 
       	- top view, float things, extra connection, adjunct, appendages, stand, bracket, bad anatomy, text, word, grid, brown, grey, bubble, high saturation, sunlight, sun, stripe, spot, empty background, wheel, lowres, ugly, bad hands, cropped, worst quality, baby, body, human, brand, bad face 
       - food in kitchen场景下可采用的负向提示词为 
       	- top view, float things, extra connection, adjunct, appendages, stand, bracket, bad anatomy, text, word, grid, brown, grey, bubble, high saturation, sunlight, sun, stripe, spot, empty background, wheel, lowres, ugly, bad hands, cropped, worst quality, baby, body, human, brand, bad face 
       - sports style场景下可采用的负向提示词为： 
       	- top view, float things, extra connection, adjunct, appendages, stand, bracket, bad anatomy, text, word, grid, brown, grey, bubble, high saturation, sunlight, sun, stripe, spot, empty background, wheel, lowres, ugly, bad hands, cropped, worst quality, baby, body, human, brand, bad face 
       - modern room场景下可采用的负向提示词为： 
       	- top view, float things, extra connection, adjunct, appendages, stand, bracket, bad anatomy, text, word, grid, brown, grey, bubble, high saturation, sunlight, sun, stripe, spot, empty background, wheel, lowres, ugly, bad hands, cropped, worst quality, baby, body, human, brand, bad face 
 PositivePrompt (String): 否  输入到 AIGC 模型的正向提示词，提示词和 Scene 二选一必填。两者均存在时，以 Scene 为准。当前仅支持英文，最多不超过 300 个字母。 
       - indoor wooden table 场景下可采用的正向提示词为： 
       	- best quality, front view, standing on a wooden table close to window, some plants in the background, bright sunlight, product photography 
       - flower and leaves场景下可采用的正向提示词为： 
       	- best quality, front view, standing on a circular platform, surrounded by flowers and leaves, sunlight from the right, product photography 
       - white marble table场景下可采用的正向提示词为： 
       	- best quality, front view, standing on a white marble table in a living room, shallow depth of field, sunlight, shadows,  product photography 
       - outdoor snow scene场景下可采用的正向提示词为： 
       	- best quality, front view, standing on a pile of snow outdoors, with sky and mountains in the background, shallow depth of field,  product photography 
       - supermarket show scene场景下可采用的正向提示词为： 
       	- on a empty white table, kitchen, close to window, bright background, background blur, bright light, soft lighting, high quality 
       - food in kitchen场景下可采用的正向提示词为 
       	- on a empty table,in the kitchen,product picture, bright background, background blur, bright light, soft lighting, high quality 
       - sports style场景下可采用的正向提示词为： 
       	- in a stadium, stadium in the background, sports style, product picture , bright light, soft lighting, high quality 
       - modern room场景下可采用的正向提示词为： 
       	- in a modern room, fashion style, soft light, high resolution 
 ProductRatio (Float): 否  商品比例，即商品图的长宽与 OutputSize 指定的结果图长宽的比值上限。默认值为 0.6，取值范围为 (0,1)。取值越小，则商品图在生成的结果图中所占的大小越小。 
 UseCaption (Boolean): 否  是否使用从商品图中提取的描述，取值如下所示： 
       - true：（默认）提取原图中商品的描述，和PositivePrompt共同作为输入到 AIGC 模型的正向提示词。 
       	 
       - false：不使用。 
 ReturnTop1 (Boolean): 否  是否返回最高分生成图及其得分，取值如下所示： 
       - true：是，只返回最高分生成图及其得分。 
       	 
       - false：（默认）否，返回所有生成图及其得分。 
 CX (Integer): 否  设置商品放置的安全区中心坐标和宽高。取值需大于等于 -1，设为默认值 -1 时，商品自动居中，安全区为全图；否则需同时指定区安全区四个参数的值。 
 CY (Integer): 否  设置商品放置的安全区中心坐标和宽高。取值需大于等于 -1，设为默认值 -1 时，商品自动居中，安全区为全图；否则需同时指定区安全区四个参数的值。 
 SafeH (Integer): 否  设置商品放置的安全区中心坐标和宽高。取值需大于等于 -1，设为默认值 -1 时，商品自动居中，安全区为全图；否则需同时指定区安全区四个参数的值。 
 SafeW (Integer): 否  设置商品放置的安全区中心坐标和宽高。取值需大于等于 -1，设为默认值 -1 时，商品自动居中，安全区为全图；否则需同时指定区安全区四个参数的值。 
 Extra (String): 否  保留字段，用于传递商品 ID，类目 ID 信息。 
 SellingPointConfig (Object of SellingPointConfig): 否  卖点图配置信息。 
 BackgroundOnly (Boolean): 是  智能生成的结果图是否仅生成场景图（仅包含商品主体，不采用文字卖点），取值如下所示： 
       - true：（默认）是 
       - false：否 
 ReturnBackgroundImage (Boolean): 是  是否返回场景图，取值如下所示： 
       - true：（默认）是 
       - false：否 
 OutputHeight (Long): 否  场景图输出高度 
 OutputWidth (Long): 否  场景图输出宽度 
 UseDefaultBg (Boolean): 否  使用默认的背景图 
 LoraConfig (String): 否  Lora 配置。 
 ProductRatios (Array of String): 否  商品比例 
 StrategyRules (JSON Map): 否  打分策略规则。 
 ImageRef (String): 否  参考图 
 IpAdapterScale (Float): 否  默认值0，取值访问[0,1], 当为1时仅使用参考图，不使用prompt 
 UseIPAdapter (Boolean): 否  是否使用IPAdapter 
 UseProductColor (Boolean): 否  是否提取主色调 

字段： SellingPointConfig
 BackgroundUrl (String): 否  指定的商品场景图访问 URL（公网可访问）。若为空，将采用Scene 或提示词智能生成的场景图。 
       - 指定场景图时，若指定了任一方式的卖点信息，则在指定场景图渲染卖点文本。 
       - 指定为空时，若指定了任一方式的卖点信息，则在 Scene 或提示词生成的场景图渲染卖点文本。 
 SellingPointRenderTemplate (String): 否  卖点渲染模板，固定取值为 default。 
 SellingPointText (String): 否  与 SellingPointRenderTemplate 搭配使用，视为方式 1。若同时配置方式 1 与方式 2，则方式 1 优先生效。 
       卖点文本。填写方式为 "maidian1nmaidian2nmaidian3"或者"0.mdian1n1.maindian2n3.maiian"，支持中英文，每个卖点字符限制 5 个字符。 
 ProductDetailImages (Array of String): 否  商详图（带有商品描述） URI/URL 列表，最大支持三张。 
       - 指定 URI 时：需满足该图片时指定该服务下存储。 
       - 指定 URL 时：满足公网可访问。 
 ProductDescription (String): 否  与 ProductDetailImages 搭配使用，视为方式 2。若同时配置方式 1 与方式 2，则方式 1 优先生效。 
       商详图中的商品卖点描述，支持中英文，不得超过 430 个字符。 
 ProdUniqueId (String): 否  场景图对应图层ID 
 SellingPointExtractConfig (String): 否   
 SellingPointRenderStyle (String): 否  卖点渲染时的图层设置 

字段： SellingPointExtractConfig
 Category (String): 否  选择需要提取的卖点类型、取值：core_sp（核心卖点提取）, short_title(短标题), product_desc_sp(商品信息类卖点)，product_promotion_sp(导购激发类卖点) 
 UniqueIds (Array of String): 否  卖点渲染图层索引列表 
 Value (String): 否  卖点信息""",
    "update_image_exif_data": """Args:params: A JSON structure
     ServiceId (String): 是  待修改图片所在的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     StoreUri (String): 是  原图存储 URI。您可以通过调用获取服务下的上传文件来获取所需的图片存储 URI。 
 DstKey (String): 否  指定修改后图片的文件名。最大长度限制为 180 个字节，不传则随机生成一个文件名。输入限制如下所示： 
       - 不支持空格，如果中间有空格将会导致重命名失败。 
       - 不支持以/开头或结尾，不支持/连续出现。 
       若指定的文件名已存在，那么当在服务维度开启重名覆盖上传时，将覆盖原文件，否则接口将返回失败。 
 Actions (Array of Actions): 是  指定图片的处理操作，最多支持填写 50 条。 

字段： Actions
 Type (String): 是  指定图片的处理类型，取值如下所示： 
       - Delete：删除指定 Tag 的内容 
       - DeleteAll：删除所有 Tag 的内容 
       - Modify：修改指定 Tag 的内容 
 TagName (String): 否  仅当 Type 取值为 Delete/Modify 时，为必填。 
       指定要处理的 Tag 名称，仅支持对列表内的标签进行处理。 
 TagValue (String): 否  仅当 Type 取值为 Modify 时，为必填。 
       指定新增/修改后 Tag 的内容，最大为 1024 字节。 
       - 若原图中 TagName 内容为空，则表示新增内容； 
       - 若原图中 TagName 存在已有内容，则表示更新内容。""",
    "create_cv_image_generate_task": """Args:params: A JSON structure
     ServiceId (String): 是  指定存储结果图并计量计费的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Domain (String): 是  服务下绑定的域名，域名状态需正常可用。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取绑定的域名信息。 
       - 您也可以通过 OpenAPI 的方式获取域名，具体请参考获取服务下全部域名。 
 Template (String): 是  服务下创建的图片处理模板名称，指定后，将按照模板中的处理配置对生成的原始图片进行图片处理。 
       您可在 veImageX 控制台的处理配置页面，参考新建模板配置模板并获取模版名称，例如 tplv-f0**5k-test。 
 ModelAction (String): 是  文生图系列模型的接口 Action 名称。 
       例如，使用通用 2.0S-文生图异步，则 ModelAction 需要取值为 CVSync2AsyncSubmitTask。 
 ModelVersion (String): 是  文生图系列模型的接口 Version 名称。 
       例如，使用通用 2.0S-文生图异步，则 ModelVersion 需要取值为 2022-08-31。 
 ReqJson (JSON Map): 是  文生图系列模型的接口的请求 JSON 字符串。 
        
       例如，使用通用 2.0S-文生图异步，则 ReqJson 需要取值为： 
       `json 
       { 
           "req_key":"high_aes_general_v20", 
           "prompt":"千军万马", 
           "model_version":"general_v2.0", 
           "seed":-1, 
           "scale":3.5, 
           "ddim_steps":16, 
           "width":512, 
           "height":512, 
           "use_sr":true 
       } 
       ` 
 Overwrite (Boolean): 否  是否覆盖服务下同名文件，取值如下所示： 
       - false：（默认）不覆盖 
       - true：覆盖 
       请确保您已开启重名覆盖上传功能，否则，此处配置无效。 
 Outputs (Array of String): 是  参数输出。""",
    "get_cv_image_generate_task": """Args:params: A JSON structure
     ServiceId (String): 是  指定要查询的服务 ID。 
    body: A JSON structure
     TaskId (String): 是  指定文生图异步任务的任务 ID。 
 ModelAction (String): 是  创建文生图任务时，使用的文生图系列模型的接口 Action 名称。 
       例如，使用查询通用 2.0L-文生图异步任务，则 ModelAction 需要取值为 CVSync2AsyncGetResult。 
 ModelVersion (String): 是  创建文生图任务时，使用的文生图系列模型的接口 Version 名称。 
       例如，使用查询通用 2.0L-文生图异步任务，则 ModelVersion 需要取值为 2022-08-31。 
 ReqJson (JSON Map): 是  创建文生图任务时，使用的文生图系列模型的接口的请求 JSON 字符串。 
        
       例如，使用查询通用 2.0L-文生图异步任务，则 ReqJson 需要按示例进行传值。""",
    "get_cv_text_generate_image": """Args:params: A JSON structure
     ServiceId (String): 是  指定存储结果图并计量计费的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Domain (String): 是  服务下绑定的域名，域名状态需正常可用。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取绑定的域名信息。 
       - 您也可以通过 OpenAPI 的方式获取域名，具体请参考获取服务下全部域名。 
 Template (String): 是  服务下创建的图片处理模板配置（不带~），指定后，将按照模板中的处理配置对豆包大模型生成的图片进行图片处理。 
       您可在 veImageX 控制台的处理配置页面，参考新建模板配置模板并获取模版信息，例如 tplv-f0**5k-test.image。 
 Outputs (Array of String): 是  指定输出图片的文件名，输入限制如下所示： 
       - 数组长度为 1，若指定多个文件名，仅第一个取值生效。 
       - 不支持空格。 
       - 不支持以/开头或结尾，不支持/连续出现，最大长度限制为 180 个字节。 
 ModelAction (String): 是  在文生图系列模型中选择一个本次调用的智能生图模型，并传入该模型对应接口的 Action 名称。 
       例如，如果使用通用 2.0L-文生图，则 ModelAction 需要取值为 CVProcess；如果使用通用 1.2-文生图，则 ModelAction 需要取值为 HighAesSmartDrawing。 
 ModelVersion (String): 是  在文生图系列模型中选择一个本次调用的智能生图模型，并传入该模型对应接口的 Version 名称。 
       例如，使用通用 2.0L-文生图，则 ModelVersion 需要取值为 2022-08-31。 
 ReqJson (JSON Map): 是  在文生图系列模型中选择一个本次调用的智能生图模型，并传入该模型对应接口的请求 JSON 字符串。 
       例如，使用通用 2.0L-文生图的必填参数，则 ReqJson 传值示例如下所示： 
       `json 
       { 
           "req_key":"high_aes_general_v20_L", 
           "prompt":"千军万马" 
       } 
       ` 
       您可忽略 return_url，该参数的取值并不会影响最终返回的结果图地址的类型。 
 Overwrite (Boolean): 否  是否覆盖服务下同名文件，取值如下所示： 
       - false：（默认）不覆盖 
       - true：覆盖 
       请确保您已开启重名覆盖上传功能，否则，此处配置无效。""",
    "get_cv_anime_generate_image": """Args:params: A JSON structure
     ServiceId (String): 是  指定存储结果图并计量计费的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Domain (String): 是  服务下绑定的域名，域名状态需正常可用。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取绑定的域名信息。 
       - 您也可以通过 OpenAPI 的方式获取域名，具体请参考获取服务下全部域名。 
 Template (String): 是  服务下创建的图片处理模板名称，指定后，将按照模板中的处理配置对豆包大模型生成的图片进行图片处理。 
       您可在 veImageX 控制台的处理配置页面，参考新建模板配置模板并获取模版名称，例如 tplv-f0**5k-test。 
 Outputs (Array of String): 是  指定输出图片的文件名，输入限制如下所示： 
       - 数组长度为 1，若指定多个文件名，仅第一个取值生效。 
       - 不支持空格。 
       - 不支持以/开头或结尾，不支持/连续出现，最大长度限制为 180 个字节。 
 Overwrite (Boolean): 否  是否覆盖服务下同名文件，取值如下所示： 
       - false：（默认）不覆盖 
       - true：覆盖 
       请确保您已开启重名覆盖上传功能，否则，此处配置无效。 
 ModelAction (String): 是  文生图系列模型的接口 Action 名称。 
       例如，使用动漫 1.3.X-文生图/图生图，则 ModelAction 需要取值为 CVProcess。 
 ModelVersion (String): 是  文生图系列模型的接口 Version 名称。 
       例如，使用动漫 1.3.X-文生图/图生图，则 ModelVersion 需要取值为 2022-08-31。 
 ReqJson (JSON Map): 是  文生图系列模型的接口的请求 JSON 字符串。 
        
       例如，使用动漫 1.3.X-文生图/图生图，则 ReqJson 需要取值为： 
       `json 
       { 
           "req_key": "high_aes", 
           "prompt": "千军万马", 
           "model_version": "anime_v1.3", 
           "binary_data_base64": [""], 
           "strength": 0.7, 
           "seed": -1, 
           "scale": 7, 
           "ddim_steps": 20, 
           "width": 1024, 
           "height": 1024, 
           "return_url": False, 
           "logo_info": { 
               "add_logo": False, 
               "position": 0, 
               "language": 0, 
               "logo_text_content": "这里是明水印内容" 
           } 
       } 
       `""",
    "get_cv_image_generate_result": """Args:params: A JSON structure
     ServiceId (String): 是  指定存储结果图并计量计费的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Domain (String): 是  服务下绑定的域名，域名状态需正常可用。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取绑定的域名信息。 
       - 您也可以通过 OpenAPI 的方式获取域名，具体请参考获取服务下全部域名。 
 Template (String): 是  服务下创建的图片处理模板名称，指定后，将按照模板中的处理配置对豆包大模型生成的图片进行图片处理。 
       您可在 veImageX 控制台的处理配置页面，参考新建模板配置模板并获取模版名称，例如 tplv-f0**5k-test。 
 Outputs (Array of String): 是  指定输出图片的文件名，输入限制如下所示： 
       - 数组长度为 1，若指定多个文件名，仅第一个取值生效。 
       - 不支持空格。 
       - 不支持以/开头或结尾，不支持/连续出现，最大长度限制为 180 个字节。 
 Overwrite (Boolean): 否  是否覆盖服务下同名文件，取值如下所示： 
       - true：覆盖 
       - false：（默认）不覆盖 
       请确保您已开启重名覆盖上传功能，否则，此处配置无效。 
 ImageUrl (String): 否  基于该图片智能生图，支持传入该服务下的图片存储 URI 或公网访问 URL。图片输入限制如下所示： 
       1. 图片格式：JPG(JPEG)、PNG、BMP 等常见格式，建议使用 JPG 格式。 
       2. 图片要求：图片体积小于 5MB，分辨率小于 4096*4096，宽高均尽可能在 1024 左右。宽高比例不建议过于极端，否则出图效果不佳，且延迟过长的概率也会显著增加。输出图片宽高与输入图一致。 
       指定 ImageUrl 后，ReqJson 中指定的图片地址无效。 
 ModelAction (String): 是  通用 XL pro-图生图模型接口的 Action 名称，即 Img2ImgXLSft。 
 ModelVersion (String): 是  通用 XL pro-图生图模型接口的 Version 名称，即 2022-08-31。 
 ReqJson (JSON Map): 是  通用 XL pro-图生图模型接口的请求 JSON 字符串。""",
    "describe_imagex_heif_encode_duration_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 App ID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配所有系统。取值如下所示： 
       - iOS 
       - Android 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。 
 ImageResolution (Array of String): 否  需要匹配的图片分辨率，不传则匹配所有图片分辨率。 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，标识不拆分。支持取值： 
       - Duration：表示拆分分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、ImageResolution 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType、ImageResolution 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_heif_encode_success_count_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 App ID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配所有系统。取值如下所示： 
       - iOS 
       - Android 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。 
 ImageResolution (Array of String): 否  需要匹配的图片分辨率，不传则匹配所有图片分辨率。 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，标识不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、ImageResolution 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType、ImageResolution 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_heif_encode_success_rate_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 App ID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配所有系统。取值如下所示： 
       - iOS 
       - Android 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。 
 ImageResolution (Array of String): 否  需要匹配的图片分辨率，不传则匹配所有图片分辨率。 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项 。 
 GroupBy (String): 否  拆分维度。默认为空，标识不拆分。支持取值： 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、ImageResolution 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_heif_encode_error_code_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 App ID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配所有系统。取值如下所示： 
       - iOS 
       - Android 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。 
 ImageResolution (Array of String): 否  需要匹配的图片分辨率，不传则匹配所有图片分辨率。 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType、ImageResolution 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_heif_encode_file_in_size_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 App ID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配所有系统。取值如下所示： 
       - iOS 
       - Android 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。 
 ImageResolution (Array of String): 否  需要匹配的图片分辨率，不传则匹配所有图片分辨率。 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，标识不拆分。支持取值： 
       - Duration：表示拆分分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、ImageResolution 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType、ImageResolution 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "describe_imagex_heif_encode_file_out_size_by_time": """Args:body: A JSON structure
     Appid (String): 否  应用 ID。默认为空，不传则匹配账号下的所有的 App ID。 
       您可以通过调用获取应用列表的方式获取所需的 AppID。 
 AppVer (Array of String): 否  需要匹配的 App 版本，不传则匹配 App 的所有版本。 
 OS (String): 否  需要匹配的系统类型，不传则匹配所有系统。取值如下所示： 
       - iOS 
       - Android 
 SdkVer (Array of String): 否  需要匹配的 SDK 版本，不传则匹配所有版本。 
 ImageType (Array of String): 否  需要匹配的图片类型，不传则匹配所有图片类型。 
 ImageResolution (Array of String): 否  需要匹配的图片分辨率，不传则匹配所有图片分辨率。 
 ExtraDims (Array of ExtraDims): 否  需要匹配的自定义维度项。 
 GroupBy (String): 否  拆分维度。默认为空，标识不拆分。支持取值： 
       - Duration：表示拆分分位数据 
       - 公共维度：Appid、OS、AppVer、SdkVer、ImageType、ImageResolution 
       - 自定义维度：您可以通过调用 获取自定义维度列表接口获取自定义维度指标。 
 StartTime (String): 是  获取数据起始时间点。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 EndTime (String): 是  获取数据结束时间点，需在起始时间点之后。日期格式按照ISO8601表示法，格式为：YYYY-MM-DDThh:mm:ss±hh:mm，比如2019-06-02T00:00:00+08:00。 
 Granularity (String): 是  返回数据的时间粒度。 
       * 5m：5 分钟； 
       * 1h：1 小时； 
       * 1d：1 天。 
 Not (Array of String): 否  取值为不等于的维度（默认为等于）。支持取值： 
       - 公共维度：AppVer、SdkVer、ImageType、ImageResolution 
       - 自定义维度：您可以通过调用 GetImageXQueryDims接口获取自定义维度指标 

字段： ExtraDims
 Dim (String): 是  自定义维度名称。 
       您可以通过调用获取自定义维度列表来获取。 
 Vals (Array of String): 是  需要匹配的对应维度值 
       您可以通过调用获取自定义维度值来获取。""",
    "update_storage_versioning": """Args:params: A JSON structure
     ServiceId (String): 是  待修改版本控制状态的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Status (Integer): 是  修改版本控制状态，取值如下所示： 
       - 1：开启 
       - 2：暂停""",
    "get_image_storage_version_files": """Args:params: A JSON structure
     ServiceId (String): 是  指定查询的服务 ID。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 Prefix (String): 否  指定查询文件的前缀。 
 Delimiter (String): 否  - 指定需要查询文件的前缀，只有资源名匹配该前缀的文件会被列出。缺省时将返回所有文件信息。 
       - 如果将 prefix 设为文件夹名称后，再把 delimiter 设置为正斜线（/），则只返回该文件夹下的文件，该文件夹下的子文件名在 CommonPrefixes 中返回，子文件夹下递归的文件和文件夹不显示。 
       例如，一个存储服务中有三个文件，分别为 Example/imagex.png、Example/mov/a.avis 和 Example/mov/b.avis。若指定 Prefix 取值 Example/且指定 Delimiter 取值 /。则返回 Example/imagex.png，并在 CommonPrefix 里返回 Example/mov/。 
 Limit (Long): 否  一次查询列出的文件信息条目数，取值范围为 [1,1000]。默认值为 10。 
 KeyMarker (String): 否  列举多版本对象的起始位置。设定从该值之后按字母排序返回对象列表。通常为上次请求返回的 NextKeyMarker 值。 
 VersionIdMarker (String): 否  与 KeyMarker 配合使用，设定从该值之后按字典排序返回多版本对象列表。从上次列举结果中 NextVersionIDMarker 获取。""",
    "update_history_version_file": """Args:params: A JSON structure
     ServiceId (String): 是  指定要恢复文件所属的服务 ID 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
    body: A JSON structure
     Key (String): 是  待恢复的历史版本文件的存储 Key。您可通过调用 GetImageStorageVersionFiles 获取历史版本文件的版本信息。 
 VersionID (String): 是  待恢复历史版本文件对应的版本 ID。您可通过调用 GetImageStorageVersionFiles 获取历史版本文件的版本信息。""",
    "get_image_transcode_tasks": """Args:params: A JSON structure
     QueueId (String): 是  队列 ID，您可通过调用 GetImageTranscodeQueues 获取该账号下全部队列 ID。 
 TaskId (String): 否  任务 ID，缺省时查询指定队列下全部的任务。 
 Status (String): 否  指定查询的任务状态，缺省时将查询全部状态的任务。取值如下所示： 
       - Running：任务运行中 
       - Suspend：任务中断 
       - Done：任务已完成 
       - Cancel：任务取消 
       - Failed：任务失败 
 Region (String): 是  队列所在地区。默认取值为 cn，表示国内。 
 StartTime (Float): 是  查询的起始 Unix 时间戳，StartTime与EndTime时间间隔最大不超过 7 天。 
 EndTime (Float): 是  查询的结束 Unix 时间戳，StartTime与EndTime时间间隔最大不超过 7 天。 
 Limit (Float): 否  单次查询列出的任务的个数，取值范围为 (0,1000]，默认值为 1000。 
 Marker (String): 否  上一次查询返回的位置标记，作为本次查询的起点信息，默认值为空。""",
    "create_image_transcode_task_callback": """Args:body: A JSON structure
     QueueId (String): 是  队列 ID，您可通过调用GetImageTranscodeQueues获取该账号下全部任务队列 ID。 
 TaskId (String): 是  指定队列下的任务 ID，您可通过调用 GetImageTranscodeTasks获取指定队列的全部任务 ID。 
 Region (String): 是  队列区域。默认取值 cn，表示国内。""",
    "update_vpc_access_config": """Args:body: A JSON structure
     ServiceId (String): 是  待更新配置的服务 ID 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 Status (String): 是  内网访问状态，取值如下所示： 
       - enable：开启 
       - disable：（默认）关闭 
 UrlAuthSwitch (Boolean): 是  当 Status 为 enable 时，该参数为必填。 
       是否启用 URL 鉴权开关，取值如下所示： 
       - true：开启 
       - false：（默认）关闭 
 UrlAuthConfig (Object of UrlAuthConfig): 否  当 UrlAuthSwitch 为 true 时，该参数为必填。 
       URL 鉴权配置。 

字段： UrlAuthConfig
 AuthType (String): 是  指定一个鉴权，取值如下所示： 
       - cdn_typea：鉴权模式 A 
       - cdn_typeb：鉴权模式 B 
       - cdn_typec：鉴权模式 C 
       - cdn_typed：鉴权模式 D 
       各种鉴权模式的说明，详见 URL 鉴权。 
 MasterKey (String): 是  指定主密钥，由 6-40 位大小写字母与数字组成。 
 BackupKey (String): 否  指定备份密钥，由 6-40 位大小写字母与数字组成。 
 Duration (Long): 是  签名的有效时间，单位是秒。该参数与请求中包含时间戳搭配使用，用来计算签名的过期时间。取值范围为[1, 630720000]内的正整数。 
       签名的过期时间 = 时间戳 + Duration。在 veImageX-CDN 收到某个请求时，如果签名的过期时间小于当前时间，veImageX-CDN 判定签名已过期。 
 SignName (String): 否  当 AuthType 为 cdn_typea、cdn_typed时，该参数为必填。对于其他类型，该参数不生效。 
       表示签名参数的名称。输入规则如下所示： 
       - 可以包括大小写英文字母、数字、下划线（_）。 
       - 长度不能超过 100 个字符。 
       - 至少包含一个字母或者数字。 
       - 不能与 TimeName 相同。 
 TimeName (String): 否  当 AuthType 为 cdn_typed 时，该参数为必填。对于其他类型，该参数不生效。 
       表示时间戳参数的名称。输入规则如下所示： 
       - 可以包括大小写英文字母、数字、下划线（_）。 
       - 长度为 1-100 个字符。 
       - 至少包含一个字母或者数字。 
       - 不能与 SignName 相同。 
 TimeFormat (String): 否  当 AuthType 为 cdn_typed 时，该参数为必填。 
       时间戳的进制配置，取值如下所示： 
       - decimal：（默认）十进制（unix 时间戳）。 
       - heximal：十六进制（unix 时间戳）。 
       - 当 AuthType 为 cdn_typec 时，该参数的值会被强制设置为 heximal。 
       - 当 AuthType 为 cdn_typea 和 cdn_typeb 时，该参数的值会被强制设置为 decimal。""",
    "describe_vpc_access_config": """Args:params: A JSON structure
     ServiceId (String): 是  待查询配置的服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "apply_vpc_upload_info": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 StoreKey (String): 否  上传文件的存储 Key。默认使用随机生成的字符串作为存储 Key。 
       存储 Key 详细命名规范请参看 veImageX 存储 Key 通用字符规则。 
 Prefix (String): 否  指定的上传文件路径。指定 Prefix 时，下发的存储 Key 为：Prefix/{随机Key}.{FileExtension}，拼接形成的存储 Key 需满足 veImageX 存储 Key 通用字符规则。 
       仅当未指定 StoreKeys 时生效。 
 FileExtension (String): 否  文件扩展名，最大长度限制为 8 个字节。 
       仅当未指定 StoreKeys 时生效。 
 ContentType (String): 否  上传文件的 Content-Type 值。 
       需确保指定值在服务维度的白名单内，否则无法成功上传，参看上传 Content-Type 限制。 
 StorageClass (String): 否  存储类型。 
       - STANDARD：标准存储 
       - IA：低频存储 
       - ARCHIVE_FR：归档闪回存储 
       - ARCHIVE：归档存储 
       - COLD_ARCHIVE：冷归档存储 
 FileSize (Long): 否  文件大小。 
 PartSize (Long): 否  分片大小，单位为字节，默认值为 200 MB。 
       当 FileSize 大于 PartSize 时，下发分片上传的 URL。 
 Overwrite (Boolean): 否  是否开启重名文件覆盖上传，取值如下所示： 
       - true：开启 
       - false：（默认）关闭 
       在指定 Overwrite 为 true 前，请确保您指定的 ServiceId 对应服务已开启了覆盖上传能力。""",
    "ai_process": """Args:body: A JSON structure
     ServiceId (String): 是  服务 ID。 
       * 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       * 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 WorkflowTemplateId (String): 是  AI 图像处理模板 ID。根据您需要的图像处理功能，参看 AI 图像处理模板页面获取模板 ID 和参数信息。 
 WorkflowParameter (String): 是  AI 图像处理模板参数，需要将 JSON 压缩并转义为字符串。根据您需要的图像处理功能，参看 AI 图像处理模板页面获取模板 ID 和参数信息。""",
    "get_image_ai_details": """Args:params: A JSON structure
     QueueId (String): 是  队列 ID，通过 CreateImageAITask 接口返回。 
 TaskId (String): 是  任务 ID，通过 CreateImageAITask 接口返回，缺省时查询指定队列下全部的任务。 
 StartTime (Long): 是  查询的起始 Unix 时间戳，StartTime 与 EndTime 时间间隔最大不超过 7 天。 
 EndTime (Long): 是  查询的结束 Unix 时间戳，StartTime 与 EndTime 时间间隔最大不超过 7 天。 
 Status (String): 否  执行状态，填入多个时使用英文逗号分隔。取值如下所示： 
       - Pending：排队中 
       - Running：执行中 
       - Success：执行成功 
       - Fail：执行失败 
 SearchPtn (String): 否  返回图片 URL 或 URI 中包含该值的任务。默认为空，不传则返回所有任务。 
 Limit (Long): 是  分页条数，取值范围为 (0, 100]。 
 Offset (Long): 否  分页偏移量，默认为 0。取值为 1 时，表示跳过第一条数据，从第二条数据取值。 
 ServiceId (String): 是  服务 ID。若 DataType 取值 uri，则提交的图片 URI 列表需在该服务内。 
       - 您可以在 veImageX 控制台服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。""",
    "get_image_ai_tasks": """Args:params: A JSON structure
     ServiceId (String): 是  服务 ID。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 QueueId (String): 是  队列 ID，通过 CreateImageAITask 接口返回。 
 TaskId (String): 否  任务 ID，通过 CreateImageAITask 接口返回，缺省时查询指定队列下全部的任务。 
 Marker (String): 否  上一次查询返回的位置标记，作为本次查询的起点信息，默认值为空。 
 Limit (Long): 否  单次查询列出的任务的个数，取值范围为 (0,1000]，默认值为 1000。 
 Status (String): 否  指定查询的任务状态，缺省时将查询全部状态的任务。取值如下所示： 
       - Running：任务运行中 
       - Suspend：任务中断 
       - Done：任务已完成 
       - Cancel：任务取消 
       - Failed：任务失败 
 StartTime (Long): 是  查询的起始 Unix 时间戳，StartTime 与 EndTime 时间间隔最大不超过 7 天。 
 EndTime (Long): 是  查询的结束 Unix 时间戳，StartTime 与 EndTime 时间间隔最大不超过 7 天。""",
    "create_image_ai_task": """Args:body: A JSON structure
     ServiceId (String): 是  服务 ID。若 DataType 取值 uri，则提交的图片 URI 列表需在该服务内。 
       - 您可以在 veImageX 控制台 服务管理页面，在创建好的图片服务中获取服务 ID。 
       - 您也可以通过 OpenAPI 的方式获取服务 ID，具体请参考获取所有服务信息。 
 WorkflowTemplateId (String): 是  AI 图像处理模板 ID。根据您需要的图像处理功能，参看 AI 图像处理模板页面获取模板 ID 和参数信息。 
 WorkflowParameter (String): 是  AI 图像处理模板参数，需要将 JSON 压缩并转义为字符串。根据您需要的图像处理功能，参看 AI 图像处理模板页面获取模板 ID 和参数信息。 
 DataType (String): 是  需要提交的图片数据类型，取值如下所示： 
       - uri：指定 ServiceId 下存储 URI。 
       - url：公网可访问的 URL。 
 DataList (Array of String): 是  待进行 AI 处理的图片 URI 或 URL 列表，其中 URI 不需要带 tos-cn-i-* 前缀。传入图片的短边不小于 256 px，长边不大于 2048 px，大小不超过 10 MB。 
       若 DataType 取值 uri，则待转码图片 URI 必须为指定服务 ID 下的存储 URI。您可通过调用 GetImageUploadFiles 获取指定服务下全部的上传文件存储 URI。 
 CallbackConf (Object of CallbackConf): 否  任务回调配置。 

字段： CallbackConf
 Method (String): 是  回调方式，仅支持取值 HTTP。 
 Endpoint (String): 是  回调 HTTP 请求地址，用于接收转码结果详情。支持使用 https 和 http 协议。 
 DataFormat (String): 否  回调数据格式，仅支持取值 JSON。 
 Args (String): 否  业务自定义回调参数，将在回调消息的 callback_args 中透传。具体回调参数请参考 AI 图像处理回调。 
 Type (String): 否  回调的维度类型，缺省情况下按照条目级别进行回调。取值如下所示： 
       - task：将按照任务级别进行回调。可分批回调，一个批次内最多一次性可回调 5000 条图片转码条目执行信息。 
       - entry：将按照条目级别进行回调。当该条目执行完毕，将立即产生回调。""",
}
