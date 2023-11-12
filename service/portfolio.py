from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status
from models.portfolio import select_portfolio, insert_portfolio
from pydantic import BaseModel
from models.user import read_user
from app.utils import verify_jwt
from app.database import PRIVATE_KEY

router_portfolio = APIRouter()

class portfolio(BaseModel):
    f_name: str
    l_name: str
    age: int
    email: str
    phone: int
    line: str
    address: str
    education: str

@router_portfolio.get('/portfolio')
async def get_portfolio():
    try:
        data = select_portfolio()
        return data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")
    
@router_portfolio.post('/portfolio')
async def create_portfolio(data: portfolio):
    try:
        # token_data = verify_jwt(user_data.token, PRIVATE_KEY)
        # if read_user(token_data['username']):
        result = insert_portfolio(data.f_name, data.l_name, data.age, data.email, data.phone, data.line, data.address, data.education)
        return { 'message': result }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")