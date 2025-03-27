import configparser
import os

from dotenv import load_dotenv

from core.helper.helper_for_path import PathProvider


class HelperConfigEnv:
    @classmethod
    def set_load_dotenv(cls):
        root_dir = PathProvider().root_dir
        stand = cls.read_pytest_ini(os.path.join(root_dir, "pytest.ini"))
        dotenv_path = os.path.join(root_dir, ".env", f".env.{stand}")
        load_dotenv(dotenv_path)

    @staticmethod
    def read_pytest_ini(file_path):
        config = configparser.ConfigParser()
        config.read(file_path)
        return config['pytest'].get('stand', 'stage')
