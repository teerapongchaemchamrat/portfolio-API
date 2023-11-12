from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status
from models.user import read_user, add_user ,read_all_user
from pydantic import BaseModel
from app.utils import verify_jwt , encrypt_jwt , create_jwt_token
from app.database import PRIVATE_KEY, EXPIRE

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
        if len(read_all_user()) >= 1 :
            return { 'message' : 'Can not create user any more.' }
        else:
            payload = { "password" : user_data.password }
            pwd = encrypt_jwt(payload, PRIVATE_KEY)
            id = add_user(user_data.username, pwd)
            return { 'id': id }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")

class Token(BaseModel):
    access_token : str

@router_login.post('/decode')
async def decode(user_data: Token):
    try:
        result = verify_jwt(user_data.access_token, PRIVATE_KEY)
        return { 'result': result }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")