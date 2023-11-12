from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status
from models.skill import select_skill, insert_skill
from pydantic import BaseModel
from models.user import read_user
from app.utils import verify_jwt
from app.database import PRIVATE_KEY

router_skill = APIRouter()

@router_skill.get('/skill')
async def get_skill():
    try:
        data = select_skill()
        return data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")

class Skill(BaseModel):
    skill_id: int
    dept: str
    tools_name: str
    language: str

@router_skill.post('/skill')
async def create_skill(user_data: Skill):
    try:
        token_data = verify_jwt(user_data.token, PRIVATE_KEY)
        if read_user(token_data['username']):
            insert_skill(user_data.skill_id, user_data.dept, user_data.tools_name, user_data.language)          
            return { 'message': "success" }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")

