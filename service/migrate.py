from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status
from models.migrate import create_user, create_tables_portfolio, create_tables_skill, create_tables_experince, create_tables_knowledge
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

router_migrate = APIRouter()

class Token(BaseModel):
    token: str

@router_migrate.post('/initdb')
async def initdb(user_data: Token):
    try:
        token_data = verify_jwt(user_data.token, PRIVATE_KEY)
        if read_user(token_data['username']):
            create_user()
            create_tables_portfolio()
            create_tables_skill()
            create_tables_experince()
            create_tables_knowledge()
        return {"message": "Tables created!"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_BAD_REQUEST,detail=f"Error {e}")