from enum import Enum


class Links(Enum):
    BASE_URL: str = "https://box.qlab.site"
    AUTH_ENDPOINT: str = "/api/v1/auth/login"