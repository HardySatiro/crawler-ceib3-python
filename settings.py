import yaml
from easydict import EasyDict

from singleton import Singleton


class Settings(metaclass=Singleton):
    def __init__(self):
        pass

    def set_env(self, env):
        with open("./config/environment.yaml") as f:
            config = yaml.safe_load(f)
        if not self.__dict__.get("env"):
            self.__dict__[env].update(EasyDict(config[env]))
            self.__dict__ = self.__dict__[env]
            self.env = env
