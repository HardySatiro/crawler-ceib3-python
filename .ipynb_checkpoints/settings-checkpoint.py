import gcsfs
import h5py
import json
import pandas as pd
import pkgutil
import yaml
from binance.client import Client
from easydict import EasyDict
from google.cloud import storage
from keras.models import load_model
from utils import access_secret_version

from singleton import Singleton


class Settings(metaclass=Singleton):
    def __init__(self):
        self.models = {}

    def set_env(self, env):
        with open("./config/environment.yaml") as f:
            config = yaml.safe_load(f)
        if not self.__dict__.get("env"):
            self.__dict__[env].update(EasyDict(config[env]))
            self.__dict__ = self.__dict__[env]
            self.env = env
