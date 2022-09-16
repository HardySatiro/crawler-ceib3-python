import os

print(os.listdir())
from fastapi import APIRouter
from v1.services import process

api_router = APIRouter()

api_router.include_router(process.router, prefix='/v1')
