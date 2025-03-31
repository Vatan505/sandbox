from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from core.enums.request_enum import HeaderKeys, HeaderValues



def default_headers_factory():
    return {HeaderKeys.CONTENT_TYPE.value: HeaderValues.APP_JSON.value}

@dataclass
class RequestData:
    body: Any = None
    json: Any = None
    Headers: Dict[str, str] = field(default_factory=default_headers_factory())
    endpoint: Optional[str] = None
    cookies: Any = None
    params: Dict[str, str] = field(default_factory=dict)


    def add_headers(self, new_headers: Dict[str, str]):
        self.headers.update(new_headers)