from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status

router_index = APIRouter()

@router_index.get('/')
async def index():
    return {'message': 'Welcome to news app!'}