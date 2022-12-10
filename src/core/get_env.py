import  pathlib
from dotenv import load_dotenv
from pathlib import Path
DEBUG = True

class GetEnvOrDefault:
    def __init__(self, os):
        if DEBUG:
            path_envs =  f"{Path().absolute()}/.dev-env"
            load_dotenv(dotenv_path=path_envs)
            self.environ = os.environ
    def get_env(self, name: str, default_value = ""):
        try:
            return self.environ[name]
        except KeyError:
            return default_value

