import argparse
import os
import os
import uvicorn
from fastapi import FastAPI
from importlib import import_module

from settings import Settings
from v1.app import api_router

app = FastAPI()

cfg = Settings()
cfg.set_secret()
cfg.load_models()

app.include_router(api_router)

if __name__ == "__main__":
    # Run app with uvicorn with port and host specified. Host needed for docker port mapping
    uvicorn.run(app, port=8000, host="0.0.0.0", debug=True)
