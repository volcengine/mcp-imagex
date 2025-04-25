 # Copyright 2025 Beijing Volcano Engine Technology Ltd.
 # SPDX-License-Identifier: Apache-2.0
 
from volcengine.ApiInfo import ApiInfo

api_info = {
    "McpGetDomainConfig": ApiInfo(
        "GET", "/", {"Action": "GetDomainConfig", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetImageStyleResult": ApiInfo(
        "POST", "/", {"Action": "GetImageStyleResult", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetAllCerts": ApiInfo(
        "GET", "/", {"Action": "GetAllCerts", "Version": "2018-08-01"}, {}, {}
    ),
    "McpAddCert": ApiInfo(
        "POST", "/", {"Action": "AddCert", "Version": "2018-08-01"}, {}, {}
    ),
    "McpDelCert": ApiInfo(
        "POST", "/", {"Action": "DelCert", "Version": "2018-08-01"}, {}, {}
    ),
    "McpDownloadCert": ApiInfo(
        "GET", "/", {"Action": "DownloadCert", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetCertInfo": ApiInfo(
        "GET", "/", {"Action": "GetCertInfo", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetImageAllDomainCert": ApiInfo(
        "GET", "/", {"Action": "GetImageAllDomainCert", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateImageBatchDomainCert": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageBatchDomainCert", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpCreateImageTemplate": ApiInfo(
        "POST", "/", {"Action": "CreateImageTemplate", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateHttps": ApiInfo(
        "POST", "/", {"Action": "UpdateHttps", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateImageDomainUaAccess": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageDomainUaAccess", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpUpdateImageDomainAreaAccess": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageDomainAreaAccess", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpGetServiceDomains": ApiInfo(
        "GET", "/", {"Action": "GetServiceDomains", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateRefer": ApiInfo(
        "POST", "/", {"Action": "UpdateRefer", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateImageDomainIPAuth": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageDomainIPAuth", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpUpdateResponseHeader": ApiInfo(
        "POST", "/", {"Action": "UpdateResponseHeader", "Version": "2018-08-01"}, {}, {}
    ),
    "McpDescribeImageVolcCdnAccessLog": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageVolcCdnAccessLog", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpUpdateImageFileKey": ApiInfo(
        "POST", "/", {"Action": "UpdateImageFileKey", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateImageDomainConfig": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageDomainConfig", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpUpdateAdvance": ApiInfo(
        "POST", "/", {"Action": "UpdateAdvance", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetImageOCRV2": ApiInfo(
        "POST", "/", {"Action": "GetImageOCRV2", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetUrlFetchTask": ApiInfo(
        "GET", "/", {"Action": "GetUrlFetchTask", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetImageQuality": ApiInfo(
        "POST", "/", {"Action": "GetImageQuality", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetImageEnhanceResult": ApiInfo(
        "POST",
        "/",
        {"Action": "GetImageEnhanceResult", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpGetPrivateImageType": ApiInfo(
        "POST", "/", {"Action": "GetPrivateImageType", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateImageDomainBandwidthLimit": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageDomainBandwidthLimit", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpUpdateImageDomainDownloadSpeedLimit": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageDomainDownloadSpeedLimit", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpUpdateImageMirrorConf": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageMirrorConf", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpGetImageDuplicateDetection": ApiInfo(
        "POST",
        "/",
        {"Action": "GetImageDuplicateDetection", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpGetDedupTaskStatus": ApiInfo(
        "GET", "/", {"Action": "GetDedupTaskStatus", "Version": "2018-08-01"}, {}, {}
    ),
    "McpApplyImageUpload": ApiInfo(
        "GET", "/", {"Action": "ApplyImageUpload", "Version": "2018-08-01"}, {}, {}
    ),
    "McpCommitImageUpload": ApiInfo(
        "POST", "/", {"Action": "CommitImageUpload", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetImageUploadFiles": ApiInfo(
        "GET", "/", {"Action": "GetImageUploadFiles", "Version": "2018-08-01"}, {}, {}
    ),
    "McpDeleteImageUploadFiles": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteImageUploadFiles", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpGetImageAlertRecords": ApiInfo(
        "POST", "/", {"Action": "GetImageAlertRecords", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetImageService": ApiInfo(
        "GET", "/", {"Action": "GetImageService", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetImageStyleDetail": ApiInfo(
        "GET", "/", {"Action": "GetImageStyleDetail", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateImageStyle": ApiInfo(
        "POST", "/", {"Action": "UpdateImageStyle", "Version": "2018-08-01"}, {}, {}
    ),
    "McpAddDomainV1": ApiInfo(
        "POST", "/", {"Action": "AddDomainV1", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetTemplatesFromBin": ApiInfo(
        "GET", "/", {"Action": "GetTemplatesFromBin", "Version": "2018-08-01"}, {}, {}
    ),
    "McpCreateImageCompressTask": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageCompressTask", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpGetCompressTaskInfo": ApiInfo(
        "GET", "/", {"Action": "GetCompressTaskInfo", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetResourceURL": ApiInfo(
        "GET", "/", {"Action": "GetResourceURL", "Version": "2023-05-01"}, {}, {}
    ),
    "McpCreateImageTranscodeQueue": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageTranscodeQueue", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateImageMonitorRule": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageMonitorRule", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpGetImageMonitorRules": ApiInfo(
        "GET", "/", {"Action": "GetImageMonitorRules", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateImageMonitorRule": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageMonitorRule", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpUpdateImageMonitorRuleStatus": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageMonitorRuleStatus", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpDeleteImageMonitorRules": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteImageMonitorRules", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpDeleteImageMonitorRecords": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteImageMonitorRecords", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpGetImageTemplate": ApiInfo(
        "GET", "/", {"Action": "GetImageTemplate", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetAllImageTemplates": ApiInfo(
        "GET", "/", {"Action": "GetAllImageTemplates", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateResEventRule": ApiInfo(
        "POST", "/", {"Action": "UpdateResEventRule", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateImageUploadOverwrite": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageUploadOverwrite", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpGetImageStorageFiles": ApiInfo(
        "GET", "/", {"Action": "GetImageStorageFiles", "Version": "2018-08-01"}, {}, {}
    ),
    "McpGetSyncAuditResult": ApiInfo(
        "POST", "/", {"Action": "GetSyncAuditResult", "Version": "2018-08-01"}, {}, {}
    ),
    "McpUpdateImageFileCT": ApiInfo(
        "POST", "/", {"Action": "UpdateImageFileCT", "Version": "2018-08-01"}, {}, {}
    ),
    "McpCreateImageAnalyzeTask": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageAnalyzeTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpUpdateImageAnalyzeTask": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageAnalyzeTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDeleteImageAnalyzeTask": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteImageAnalyzeTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageAnalyzeTasks": ApiInfo(
        "GET", "/", {"Action": "GetImageAnalyzeTasks", "Version": "2023-05-01"}, {}, {}
    ),
    "McpDeleteImageAnalyzeTaskRun": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteImageAnalyzeTaskRun", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageAnalyzeResult": ApiInfo(
        "GET", "/", {"Action": "GetImageAnalyzeResult", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateImageAnalyzeTaskStatus": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageAnalyzeTaskStatus", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageAuditResult": ApiInfo(
        "GET", "/", {"Action": "GetImageAuditResult", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageAuditTasks": ApiInfo(
        "GET", "/", {"Action": "GetImageAuditTasks", "Version": "2023-05-01"}, {}, {}
    ),
    "McpCreateImageTranscodeTask": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageTranscodeTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpUpdateImageTranscodeQueue": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageTranscodeQueue", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpUpdateImageTranscodeQueueStatus": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageTranscodeQueueStatus", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDeleteImageTranscodeQueue": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteImageTranscodeQueue", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageTranscodeQueues": ApiInfo(
        "GET",
        "/",
        {"Action": "GetImageTranscodeQueues", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageTranscodeDetails": ApiInfo(
        "GET",
        "/",
        {"Action": "GetImageTranscodeDetails", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateImageTranscodeCallback": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageTranscodeCallback", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDeleteImageTranscodeDetail": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteImageTranscodeDetail", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageSettings": ApiInfo(
        "GET", "/", {"Action": "GetImageSettings", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageSettingRules": ApiInfo(
        "GET", "/", {"Action": "GetImageSettingRules", "Version": "2023-05-01"}, {}, {}
    ),
    "McpCreateImageSettingRule": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageSettingRule", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpUpdateImageSettingRule": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageSettingRule", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDeleteImageSettingRule": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteImageSettingRule", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpUpdateImageSettingRulePriority": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageSettingRulePriority", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageSettingRuleHistory": ApiInfo(
        "GET",
        "/",
        {"Action": "GetImageSettingRuleHistory", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageAddOnTag": ApiInfo(
        "GET", "/", {"Action": "GetImageAddOnTag", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateImageObjectAccess": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageObjectAccess", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageServiceSubscription": ApiInfo(
        "GET",
        "/",
        {"Action": "GetImageServiceSubscription", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateImageService": ApiInfo(
        "POST", "/", {"Action": "CreateImageService", "Version": "2023-05-01"}, {}, {}
    ),
    "McpDeleteImageService": ApiInfo(
        "POST", "/", {"Action": "DeleteImageService", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateImageAuthKey": ApiInfo(
        "POST", "/", {"Action": "UpdateImageAuthKey", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageAuthKey": ApiInfo(
        "GET", "/", {"Action": "GetImageAuthKey", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateServiceName": ApiInfo(
        "POST", "/", {"Action": "UpdateServiceName", "Version": "2023-05-01"}, {}, {}
    ),
    "McpDeleteImageTemplate": ApiInfo(
        "POST", "/", {"Action": "DeleteImageTemplate", "Version": "2023-05-01"}, {}, {}
    ),
    "McpCreateImageTemplatesByImport": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageTemplatesByImport", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateTemplatesFromBin": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateTemplatesFromBin", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDeleteTemplatesFromBin": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteTemplatesFromBin", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateImageContentTask": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageContentTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageContentTaskDetail": ApiInfo(
        "POST",
        "/",
        {"Action": "GetImageContentTaskDetail", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageContentBlockList": ApiInfo(
        "POST",
        "/",
        {"Action": "GetImageContentBlockList", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateImageAuditTask": ApiInfo(
        "POST", "/", {"Action": "CreateImageAuditTask", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateImageAuditTask": ApiInfo(
        "POST", "/", {"Action": "UpdateImageAuditTask", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageStyles": ApiInfo(
        "GET", "/", {"Action": "GetImageStyles", "Version": "2023-05-01"}, {}, {}
    ),
    "McpCreateImageStyle": ApiInfo(
        "POST", "/", {"Action": "CreateImageStyle", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateImageStyleMeta": ApiInfo(
        "POST", "/", {"Action": "UpdateImageStyleMeta", "Version": "2023-05-01"}, {}, {}
    ),
    "McpDeleteImageStyle": ApiInfo(
        "POST", "/", {"Action": "DeleteImageStyle", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageFonts": ApiInfo(
        "GET", "/", {"Action": "GetImageFonts", "Version": "2023-05-01"}, {}, {}
    ),
    "McpAddImageElements": ApiInfo(
        "POST", "/", {"Action": "AddImageElements", "Version": "2023-05-01"}, {}, {}
    ),
    "McpDeleteImageElements": ApiInfo(
        "POST", "/", {"Action": "DeleteImageElements", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageElements": ApiInfo(
        "GET", "/", {"Action": "GetImageElements", "Version": "2023-05-01"}, {}, {}
    ),
    "McpAddImageBackgroundColors": ApiInfo(
        "POST",
        "/",
        {"Action": "AddImageBackgroundColors", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDeleteImageBackgroundColors": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteImageBackgroundColors", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageBackgroundColors": ApiInfo(
        "GET",
        "/",
        {"Action": "GetImageBackgroundColors", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateImageHmExtract": ApiInfo(
        "POST", "/", {"Action": "CreateImageHmExtract", "Version": "2023-05-01"}, {}, {}
    ),
    "McpCreateImageHmEmbed": ApiInfo(
        "POST", "/", {"Action": "CreateImageHmEmbed", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageEraseResult": ApiInfo(
        "POST", "/", {"Action": "GetImageEraseResult", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetComprehensiveEnhanceImage": ApiInfo(
        "POST",
        "/",
        {"Action": "GetComprehensiveEnhanceImage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageBgFillResult": ApiInfo(
        "POST", "/", {"Action": "GetImageBgFillResult", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageComicResult": ApiInfo(
        "POST", "/", {"Action": "GetImageComicResult", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetSegmentImage": ApiInfo(
        "POST", "/", {"Action": "GetSegmentImage", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageSuperResolutionResult": ApiInfo(
        "POST",
        "/",
        {"Action": "GetImageSuperResolutionResult", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageSmartCropResult": ApiInfo(
        "POST",
        "/",
        {"Action": "GetImageSmartCropResult", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImagePSDetection": ApiInfo(
        "POST", "/", {"Action": "GetImagePSDetection", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetAiGenerateImage": ApiInfo(
        "POST", "/", {"Action": "GetAiGenerateImage", "Version": "2023-05-01"}, {}, {}
    ),
    "McpDescribeImageXSummary": ApiInfo(
        "GET", "/", {"Action": "DescribeImageXSummary", "Version": "2023-05-01"}, {}, {}
    ),
    "McpDescribeImageXDomainTrafficData": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXDomainTrafficData", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXDomainBandwidthData": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXDomainBandwidthData", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXBillingRequestCntUsage": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXBillingRequestCntUsage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXRequestCntUsage": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXRequestCntUsage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXBaseOpUsage": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXBaseOpUsage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCompressUsage": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXCompressUsage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXScreenshotUsage": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXScreenshotUsage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXVideoClipDurationUsage": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXVideoClipDurationUsage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXMultiCompressUsage": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXMultiCompressUsage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXEdgeRequest": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXEdgeRequest", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXEdgeRequestBandwidth": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXEdgeRequestBandwidth", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXEdgeRequestTraffic": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXEdgeRequestTraffic", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXEdgeRequestRegions": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXEdgeRequestRegions", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXMirrorRequestHttpCodeByTime": ApiInfo(
        "POST",
        "/",
        {
            "Action": "DescribeImageXMirrorRequestHttpCodeByTime",
            "Version": "2023-05-01",
        },
        {},
        {},
    ),
    "McpDescribeImageXMirrorRequestHttpCodeOverview": ApiInfo(
        "POST",
        "/",
        {
            "Action": "DescribeImageXMirrorRequestHttpCodeOverview",
            "Version": "2023-05-01",
        },
        {},
        {},
    ),
    "McpDescribeImageXMirrorRequestTraffic": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXMirrorRequestTraffic", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXMirrorRequestBandwidth": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXMirrorRequestBandwidth", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXServerQPSUsage": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXServerQPSUsage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXHitRateTrafficData": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXHitRateTrafficData", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXHitRateRequestData": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXHitRateRequestData", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCDNTopRequestData": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXCDNTopRequestData", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageXQueryApps": ApiInfo(
        "GET", "/", {"Action": "GetImageXQueryApps", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageXQueryRegions": ApiInfo(
        "GET", "/", {"Action": "GetImageXQueryRegions", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageXQueryDims": ApiInfo(
        "GET", "/", {"Action": "GetImageXQueryDims", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageXQueryVals": ApiInfo(
        "GET", "/", {"Action": "GetImageXQueryVals", "Version": "2023-05-01"}, {}, {}
    ),
    "McpDescribeImageXUploadCountByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXUploadCountByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXUploadDuration": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXUploadDuration", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXUploadSuccessRateByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXUploadSuccessRateByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXUploadFileSize": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXUploadFileSize", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXUploadErrorCodeByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXUploadErrorCodeByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXUploadErrorCodeAll": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXUploadErrorCodeAll", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXUploadSpeed": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXUploadSpeed", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXUploadSegmentSpeedByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXUploadSegmentSpeedByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCdnSuccessRateByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXCdnSuccessRateByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCdnSuccessRateAll": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXCdnSuccessRateAll", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCdnErrorCodeByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXCdnErrorCodeByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCdnErrorCodeAll": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXCdnErrorCodeAll", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCdnDurationDetailByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXCdnDurationDetailByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCdnDurationAll": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXCdnDurationAll", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCdnReuseRateByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXCdnReuseRateByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCdnReuseRateAll": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXCdnReuseRateAll", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXCdnProtocolRateByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXCdnProtocolRateByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientFailureRate": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientFailureRate", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientDecodeSuccessRateByTime": ApiInfo(
        "POST",
        "/",
        {
            "Action": "DescribeImageXClientDecodeSuccessRateByTime",
            "Version": "2023-05-01",
        },
        {},
        {},
    ),
    "McpDescribeImageXClientDecodeDurationByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientDecodeDurationByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientQueueDurationByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientQueueDurationByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientErrorCodeByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientErrorCodeByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientErrorCodeAll": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientErrorCodeAll", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientLoadDuration": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientLoadDuration", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientLoadDurationAll": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientLoadDurationAll", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientSdkVerByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientSdkVerByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientFileSize": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientFileSize", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientTopFileSize": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientTopFileSize", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientCountByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientCountByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientQualityRateByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientQualityRateByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientTopQualityURL": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientTopQualityURL", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientDemotionRateByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientDemotionRateByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientTopDemotionURL": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientTopDemotionURL", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXClientScoreByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXClientScoreByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXSensibleCountByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXSensibleCountByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXSensibleCacheHitRateByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXSensibleCacheHitRateByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXSensibleTopSizeURL": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXSensibleTopSizeURL", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXSensibleTopResolutionURL": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXSensibleTopResolutionURL", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXSensibleTopRamURL": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXSensibleTopRamURL", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXSensibleTopUnknownURL": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXSensibleTopUnknownURL", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageUploadFile": ApiInfo(
        "GET", "/", {"Action": "GetImageUploadFile", "Version": "2023-05-01"}, {}, {}
    ),
    "McpPreviewImageUploadFile": ApiInfo(
        "GET",
        "/",
        {"Action": "PreviewImageUploadFile", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageEraseModels": ApiInfo(
        "GET", "/", {"Action": "GetImageEraseModels", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateSlimConfig": ApiInfo(
        "POST", "/", {"Action": "UpdateSlimConfig", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateDomainAdaptiveFmt": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateDomainAdaptiveFmt", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetResponseHeaderValidateKeys": ApiInfo(
        "GET",
        "/",
        {"Action": "GetResponseHeaderValidateKeys", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDelDomain": ApiInfo(
        "POST", "/", {"Action": "DelDomain", "Version": "2023-05-01"}, {}, {}
    ),
    "McpSetDefaultDomain": ApiInfo(
        "POST", "/", {"Action": "SetDefaultDomain", "Version": "2023-05-01"}, {}, {}
    ),
    "McpFetchImageUrl": ApiInfo(
        "POST", "/", {"Action": "FetchImageUrl", "Version": "2023-05-01"}, {}, {}
    ),
    "McpCreateHiddenWatermarkImage": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateHiddenWatermarkImage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXDomainBandwidthNinetyFiveData": ApiInfo(
        "GET",
        "/",
        {
            "Action": "DescribeImageXDomainBandwidthNinetyFiveData",
            "Version": "2023-05-01",
        },
        {},
        {},
    ),
    "McpGetBatchProcessResult": ApiInfo(
        "POST",
        "/",
        {"Action": "GetBatchProcessResult", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateBatchProcessTask": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateBatchProcessTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetBatchTaskInfo": ApiInfo(
        "GET", "/", {"Action": "GetBatchTaskInfo", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateFileStorageClass": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateFileStorageClass", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateFileRestore": ApiInfo(
        "POST", "/", {"Action": "CreateFileRestore", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateStorageRules": ApiInfo(
        "POST", "/", {"Action": "UpdateStorageRules", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetAllImageServices": ApiInfo(
        "GET", "/", {"Action": "GetAllImageServices", "Version": "2018-08-01"}, {}, {}
    ),
    "McpDescribeImageXBucketRetrievalUsage": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXBucketRetrievalUsage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageDetectResult": ApiInfo(
        "POST", "/", {"Action": "GetImageDetectResult", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateImageResourceStatus": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageResourceStatus", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXExceedCountByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXExceedCountByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXExceedFileSize": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXExceedFileSize", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXExceedResolutionRatioAll": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXExceedResolutionRatioAll", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageMigrateTasks": ApiInfo(
        "GET", "/", {"Action": "GetImageMigrateTasks", "Version": "2023-05-01"}, {}, {}
    ),
    "McpRerunImageMigrateTask": ApiInfo(
        "POST",
        "/",
        {"Action": "RerunImageMigrateTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpTerminateImageMigrateTask": ApiInfo(
        "POST",
        "/",
        {"Action": "TerminateImageMigrateTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDeleteImageMigrateTask": ApiInfo(
        "POST",
        "/",
        {"Action": "DeleteImageMigrateTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateImageMigrateTask": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageMigrateTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpUpdateImageTaskStrategy": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateImageTaskStrategy", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetVendorBuckets": ApiInfo(
        "POST", "/", {"Action": "GetVendorBuckets", "Version": "2023-05-01"}, {}, {}
    ),
    "McpExportFailedMigrateTask": ApiInfo(
        "GET",
        "/",
        {"Action": "ExportFailedMigrateTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXSourceRequest": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXSourceRequest", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXSourceRequestBandwidth": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXSourceRequestBandwidth", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXSourceRequestTraffic": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeImageXSourceRequestTraffic", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateImageFromUri": ApiInfo(
        "POST", "/", {"Action": "CreateImageFromUri", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageEnhanceResultWithData": ApiInfo(
        "POST",
        "/",
        {"Action": "GetImageEnhanceResultWithData", "Version": "2018-08-01"},
        {},
        {},
    ),
    "McpGetProductAIGCResult": ApiInfo(
        "POST", "/", {"Action": "GetProductAIGCResult", "Version": "2023-05-01"}, {}, {}
    ),
    "McpUpdateImageExifData": ApiInfo(
        "POST", "/", {"Action": "UpdateImageExifData", "Version": "2023-05-01"}, {}, {}
    ),
    "McpCreateCVImageGenerateTask": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateCVImageGenerateTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetCVImageGenerateTask": ApiInfo(
        "POST",
        "/",
        {"Action": "GetCVImageGenerateTask", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetCVTextGenerateImage": ApiInfo(
        "POST",
        "/",
        {"Action": "GetCVTextGenerateImage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetCVAnimeGenerateImage": ApiInfo(
        "POST",
        "/",
        {"Action": "GetCVAnimeGenerateImage", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetCVImageGenerateResult": ApiInfo(
        "POST",
        "/",
        {"Action": "GetCVImageGenerateResult", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXHeifEncodeDurationByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXHeifEncodeDurationByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXHeifEncodeSuccessCountByTime": ApiInfo(
        "POST",
        "/",
        {
            "Action": "DescribeImageXHeifEncodeSuccessCountByTime",
            "Version": "2023-05-01",
        },
        {},
        {},
    ),
    "McpDescribeImageXHeifEncodeSuccessRateByTime": ApiInfo(
        "POST",
        "/",
        {
            "Action": "DescribeImageXHeifEncodeSuccessRateByTime",
            "Version": "2023-05-01",
        },
        {},
        {},
    ),
    "McpDescribeImageXHeifEncodeErrorCodeByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXHeifEncodeErrorCodeByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXHeifEncodeFileInSizeByTime": ApiInfo(
        "POST",
        "/",
        {"Action": "DescribeImageXHeifEncodeFileInSizeByTime", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeImageXHeifEncodeFileOutSizeByTime": ApiInfo(
        "POST",
        "/",
        {
            "Action": "DescribeImageXHeifEncodeFileOutSizeByTime",
            "Version": "2023-05-01",
        },
        {},
        {},
    ),
    "McpUpdateStorageVersioning": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateStorageVersioning", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageStorageVersionFiles": ApiInfo(
        "GET",
        "/",
        {"Action": "GetImageStorageVersionFiles", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpUpdateHistoryVersionFile": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateHistoryVersionFile", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpGetImageTranscodeTasks": ApiInfo(
        "GET",
        "/",
        {"Action": "GetImageTranscodeTasks", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpCreateImageTranscodeTaskCallback": ApiInfo(
        "POST",
        "/",
        {"Action": "CreateImageTranscodeTaskCallback", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpUpdateVpcAccessConfig": ApiInfo(
        "POST",
        "/",
        {"Action": "UpdateVpcAccessConfig", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpDescribeVpcAccessConfig": ApiInfo(
        "GET",
        "/",
        {"Action": "DescribeVpcAccessConfig", "Version": "2023-05-01"},
        {},
        {},
    ),
    "McpApplyVpcUploadInfo": ApiInfo(
        "GET", "/", {"Action": "ApplyVpcUploadInfo", "Version": "2023-05-01"}, {}, {}
    ),
    "McpAIProcess": ApiInfo(
        "POST", "/", {"Action": "AIProcess", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageAIDetails": ApiInfo(
        "GET", "/", {"Action": "GetImageAIDetails", "Version": "2023-05-01"}, {}, {}
    ),
    "McpGetImageAITasks": ApiInfo(
        "GET", "/", {"Action": "GetImageAITasks", "Version": "2023-05-01"}, {}, {}
    ),
    "McpCreateImageAITask": ApiInfo(
        "POST", "/", {"Action": "CreateImageAITask", "Version": "2023-05-01"}, {}, {}
    ),
}
