import os
import traceback
from fastapi import FastAPI, APIRouter, HTTPException

from retry import retry

from settings import Settings

router = APIRouter()
from pydantic import BaseModel
from v1.routines.routine import Routine

from pydantic import BaseModel, Field
from typing import Optional, List


class Registry(BaseModel):
    company: str
    type: str
    value: str
    code: str
    qtde: str
    totalValue: str


@router.get('/wallet-portfolio', response_model=List[Registry])
async def teste(user: str, password: str):
    try:

        return Routine().run(user, password)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
