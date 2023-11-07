from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status
from models.knowledge import select_knowledge, insert_knowledge
from pydantic import BaseModel
from models.user import read_user
from app.utils import verify_jwt
# from main import PRIVATE_KEY

from pathlib import Path
import dotenv
import os

# load environment variables.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(BASE_DIR / ".env")

PRIVATE_KEY = os.getenv("SECRET_KEY")
EXPIRE = int(os.getenv("EXPIRATION_TIME_MINUTES"))

router_experince = APIRouter()

class knowledge(BaseModel):
    skill_id: str
    title: str
    description: str
    company: str
    token: str

@router_experince.get('/experince')
async def get_experince():
    try:
        data = select_knowledge()
        return data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")
    
@router_experince.post('/experince')
async def create_experince(user_data = knowledge):
    try:
        token_data = verify_jwt(user_data.token, PRIVATE_KEY)
        if read_user(token_data['username']):
            result = insert_knowledge(user_data.skill_id, user_data.title, user_data.description, user_data.company)
            return { 'message': result }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")