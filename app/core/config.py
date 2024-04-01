from functools import lru_cache
from typing import Any
from typing import Dict
from typing import List


class Settings():
    API_V1_STR: str = "/v1"
    PROJECT_NAME: str = "capstone"
    ALLOW_ORIGINS: List[str] = [
        "*",  # TODO 나중에 쓰는 서버 ip로 바꿀 것
        # 'http://127.0.0.1:3000',
        # 'http://localhost',
        # 'https://spoon8.com/',
        # 'https://spoon8.com/*',
        # 'https://www.spoon8.com',
    ]
    ROOT_PATH = "/dev"
    ROOT_PRODUCT_PATH = "/product"


@lru_cache()
def get_settings() -> Settings:
    return Settings()