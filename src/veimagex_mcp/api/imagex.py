import os
from volcengine.imagex.v2.imagex_service import ImagexService


class ImagexAPI(ImagexService):
    def __init__(self):
        super().__init__(
            ak=os.getenv("VOLCENGINE_ACCESS_KEY"),
            sk=os.getenv("VOLCENGINE_SECRET_KEY"),
        )
        self.set_connection_timeout(30)
