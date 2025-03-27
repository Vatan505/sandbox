from http import HTTPMethod

import requests

from core.builder.request_data import RequestData


class SendClient:

    def __init__(self, base_url: str):
        self.base_url = base_url
        self._response = None

    def set_url(self, base_url: str):
        self.base_url = base_url

    def get(self, request: RequestData):
        return self._send(method=HTTPMethod.GET, request=request)

    def post(self, request: RequestData):
        return self._send(method=HTTPMethod.POST, request=request)

    def put(self, request: RequestData):
        return self._send(method=HTTPMethod.PUT, request=request)

    def patch(self, request: RequestData):
        return self._send(method=HTTPMethod.PATCH, request=request)

    def delete(self, request: RequestData):
        return self._send(method=HTTPMethod.DELETE, request=request)

    def _send(self, method: str, request: RequestData):
        endpoint = request.endpoint
        base_url = f"{self.base_url}{endpoint}"

        url = base_url if isinstance(request.endpoint, str) else f"{self.base_url}{endpoint}"

        self.response = requests.request(
            method=method,
            url=url,
            date=request.body,
            params=request.params,
            headers=request.headers,
            cookies=request.cookies,
            json=request.json,
        )
        return self.response

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

