from core.builder.request_data import RequestData


class RequestBuilder:
    def __init__(self):
        self.request = RequestData()

    def set_body(self, body: dict):
        self.request.body = body
        return self
    def set_headers(self, headers: dict):
        self.request.headers.update(headers)
        return self
    def set_endpoint(self, endpoint: dict):
        self.request.endpoint = endpoint
        return self
    def set_cookies(self, cookies: dict):
        self.request.cookies = cookies
        return self
    def set_params(self, params: dict):
        self.request.params = params
        return self
    def set_json(self, json: dict):
        self.request.json = json
        return self
    def build(self) -> RequestData:
        return self.request
