from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2
from app.utils import JWTBearer

router_test = APIRouter()

@router_test.post("/items",dependencies=[Depends(JWTBearer())], tags=["private"])
async def read_items() -> dict:
    return {"token": "aAAAA"}