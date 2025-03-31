import os

from core.helper.helper_config_env import HelperConfigEnv

HelperConfigEnv.set_load_dotenv()

class Auth:
    username: str = os.getenv("AUTH_USERNAME")
    password: str = os.getenv("AUTH_PASSWORD")

class Settings:
    auth: Auth = Auth()


settings = Settings()