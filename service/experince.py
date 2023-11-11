from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status
from models.experince import select_experince, insert_experince
from pydantic import BaseModel
from models.user import read_user
from app.utils import verify_jwt
from app.database import PRIVATE_KEY

router_experince = APIRouter()

class experince(BaseModel):
    skill_id: str
    title: str
    description: str
    company: str
    token: str

@router_experince.get('/experince')
async def get_experince():
    try:
        data = select_experince()
        return data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")
    
@router_experince.post('/experince')
async def create_experince(user_data = experince):
    try:
        # token_data = verify_jwt(user_data.token, PRIVATE_KEY)
        # if read_user(token_data['username']):
        result = insert_experince(user_data.skill_id, user_data.title, user_data.description, user_data.company)
        return { 'message': result }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")