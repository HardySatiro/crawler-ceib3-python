import base64
import datetime
import gcsfs
import h5py
import itertools
import json
import numpy as np
import numpy as np
import os
import pandas as pd
import pytz
import requests
import ta
import talib
import time
import traceback
from fastapi import FastAPI, APIRouter
from keras.models import load_model
from retry import retry
from utils import round_step_size, get_call

from settings import Settings

router = APIRouter()

from pydantic import BaseModel


class Features(BaseModel):
    ticker: str
    interval: str
    window_size: int
    investiment: int


from fastapi import FastAPI, Request


@router.post('/predict-technical')
async def predict(request: Request):
    try:

        cfg = Settings()
        ## LOCAL

        request_json = await request.json()
        if request_json.get("message", {}).get("data"):  # If by validation request on PUBSUB Trigger
            request_json = json.loads(base64.b64decode(request_json["message"]["data"]).decode("utf-8"))

    except Exception as e:
        print(traceback.format_exc())
        return "success"
    return "success"
