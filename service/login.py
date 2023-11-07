from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status
from models.user import read_user, add_user
from pydantic import BaseModel
from app.utils import verify_jwt , encrypt_jwt , create_jwt_token
# from main import PRIVATE_KEY, EXPIRE

from pathlib import Path
import dotenv
import os

# load environment variables.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(BASE_DIR / ".env")

PRIVATE_KEY = os.getenv("SECRET_KEY")
EXPIRE = int(os.getenv("EXPIRATION_TIME_MINUTES"))

router_login = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router_login.post('/login')
async def login(user_data: User):
    try:
        user = read_user(user_data.username)
        err = "username or password invalid" 
        result = {}
        if user:
            current_password = verify_jwt(user["password"], PRIVATE_KEY)
            if user_data.password == current_password["password"]: 
                result["message"] = "login success" 
                payload = {"id": user['id'] ,"username": user['username']}
                result["token"] = create_jwt_token(payload, PRIVATE_KEY, EXPIRE)
            else:
                result["message"] = err
        else:
            result["message"] = err
        return result
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")

@router_login.post('/register')
async def register(user_data: User):
    try:
        payload = { "password" : user_data.password }
        pwd = encrypt_jwt(payload, PRIVATE_KEY)
        id = add_user(user_data.username, pwd)
        return { 'id': id }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")