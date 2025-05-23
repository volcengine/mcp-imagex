 # Copyright 2025 Beijing Volcano Engine Technology Ltd.
 # SPDX-License-Identifier: Apache-2.0
 
import os
from volcengine.imagex.v2.imagex_service import ImagexService
from .config import *
import json

class ImagexAPI(ImagexService):
    def __init__(self):
        super().__init__(
            ak=os.getenv("VOLCENGINE_ACCESS_KEY"),
            sk=os.getenv("VOLCENGINE_SECRET_KEY"),
        )
        self.api_info = {**self.api_info, **api_info}
        self.service_info.header["x-tt-mcp"] = 'volc'
        self.service_id = os.getenv("SERVICE_ID")
        self.domain = os.getenv("DOMAIN")
        self.set_connection_timeout(100)
        self.set_socket_timeout(100)


    def mcp_get(self, action, params={}, doseq=0):
        res = self.get(action, params, doseq)
        if res == "":
            raise Exception("%s: empty response" % action)
        res_json = json.loads(json.dumps(res))
        return res_json

    def mcp_post(self, action, params={}, body={}):
        res = self.json(action, params, body)
        if res == "":
            raise Exception("%s: empty response" % action)
        res_json = json.loads(json.dumps(res))
        return res_json

            