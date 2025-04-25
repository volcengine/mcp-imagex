 # Copyright 2025 Beijing Volcano Engine Technology Ltd.
 # SPDX-License-Identifier: Apache-2.0
 
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
