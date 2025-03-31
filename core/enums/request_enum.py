from enum import Enum


class HeaderKeys(Enum):
    CONTENT_TYPE: str = "Content-type"
    X_LANG: str = "X-lang"


class HeaderValues(Enum):
    APP_JSON: str = "application/json"
    APP_FORM: str = "application/x-www-form-urlencoded"
