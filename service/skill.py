from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status
from models.skill import select_skill
from pydantic import BaseModel
from models.user import read_user
from app.utils import verify_jwt
from app.database import PRIVATE_KEY
from app.database import PgDatabase
router_skil = APIRouter()

class skill(BaseModel):
    skill_id : int
    dept: str
    tools_name: str
    language: str

@router_skil.get('/skill')
async def get_skill():
    try:
        data = select_skill()
        return data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")



def insert_skill(skill_id, dept, tools_name, language):
    with PgDatabase() as db:
            sql = f"""INSERT INTO skill(skill_id, department, tools_name, programming_language)
	                        VALUES ('{skill_id}','{dept}', '{tools_name}', '{language}');
                   """          
            db.cursor.execute(sql)
            db.connection.commit()
            msg = "insert skill success..."
            print(msg)
 
# @router_skil.post('/skill')
# async def create_skill(user_data = skill):
#     insert_skill(user_data.dept, user_data.tools_name, user_data.language) 
    # try:
    #     # token_data = verify_jwt(user_data.token, PRIVATE_KEY)
    #     # if read_user(token_data['username']):
    #     # insert_skill(user_data.skill_id, user_data.dept, user_data.tools_name, user_data.language)                 
    #     return { 'message': "success" }
    # except Exception as e:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error {e}")

@router_skil.post('/skill')
async def create_skill(skill: dict):
    insert_skill(skill.get('skill_id'),skill.get('dept'), skill.get('tools_name'), skill.get('language'))