import json

import pytest

from API.services.authentication.authorization_data import AuthorizationData
from core.builder.request_builder import RequestBuilder
from core.enums.links_enum import Links
from core.enums.request_enum import HeaderValues, HeaderKeys
from core.send_client import SendClient


@pytest.fixture()
def auth_user_fixture() -> dict:
    data = AuthorizationData()
    req =(
        RequestBuilder()
        .set_endpoint({Links.AUTH_ENDPOINT})
        .set_headers({HeaderKeys.CONTENT_TYPE.value: HeaderValues.APP_FORM.value})
        .set_body(data.__dict__)
        .build()
    )
    client = SendClient(Links.BASE_URL)
    response = client.post(req)
    auth = json.loads(response.content.decode('utf-8'))
    auth_token = {"Authorization": f"{auth.get("token_type")} {auth.get("access_token")}"}
    return auth_token