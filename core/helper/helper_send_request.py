from ctypes import GetLastError
from typing import Any

from requests import Response
from requests.auth import HTTPBasicAuth

from core.builder.request_builder import RequestBuilder
from core.enums.links_enum import Links
from core.send_client import SendClient


class HelperSendRequest:

    @staticmethod
    def send_request(
            method: str,
            url: str | None = None,
            endpoint: str | None =None,
            headers: dict | None = None,
            params: dict | None =None,
            cookies: dict | None = None,
            body: Any | None = None,
            json: Any | None = None,
    )-> Response:
        request = (
            RequestBuilder()
            .set_endpoint(endpoint)
            .set_headers(headers)
            .set_params(params)
            .set_cookies(cookies)
            .set_json(body)
            .set_json(json)
            .build()
        )

        base_url = Links.BASE_URL if url is None else url