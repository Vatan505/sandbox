from dataclasses import dataclass

from core.helper.helper_settings import settings


@dataclass
class AuthorizationData:
    username: str = settings.auth.username
    password: str = settings.auth.password