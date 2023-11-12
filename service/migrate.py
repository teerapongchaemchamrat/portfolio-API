from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status
from models.migrate import create_users, create_tables_portfolio, create_tables_skill, create_tables_experince, create_tables_knowledge
from pydantic import BaseModel
from models.user import read_user
from app.utils import verify_jwt
from app.database import PRIVATE_KEY

router_migrate = APIRouter()

class Token(BaseModel):
    token: str

@router_migrate.post('/initdb')
async def initdb(data:Token):
    try:
        token_data = verify_jwt(data.token, PRIVATE_KEY)
        if read_user(token_data['username']):
            create_tables_portfolio()
            create_tables_skill()
            create_tables_experince()
            create_tables_knowledge()
        return {"message": "Tables created!"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_BAD_REQUEST,detail=f"Error {e}")
    
class KeyPrivate(BaseModel):
    private_key: str 

@router_migrate.post('/init_system')
async def initdb_system(user_data: KeyPrivate):
    try:
        if user_data.private_key == PRIVATE_KEY:
            create_users()
            return {"message": "Tables systems created!"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_BAD_REQUEST,detail=f"Error {e}")
    
