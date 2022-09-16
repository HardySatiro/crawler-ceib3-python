from fastapi import APIRouter

from v1.services import all_technical
from v1.services import predict
from v1.services import predict_technical

api_router = APIRouter()

api_router.include_router(predict.router, prefix='/v1')
