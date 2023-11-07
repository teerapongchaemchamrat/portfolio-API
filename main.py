from fastapi import FastAPI
from service.index import router_index
from service.migrate import router_migrate
from service.login import router_login
from service.experince import router_experince

from pathlib import Path
import dotenv
import os

# load environment variables.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(BASE_DIR / ".env")

PRIVATE_KEY = os.getenv("SECRET_KEY")
EXPIRE = int(os.getenv("EXPIRATION_TIME_MINUTES"))

# define fastapi.
app = FastAPI()

# register routes.
app.include_router(router_index)
app.include_router(router_login)
app.include_router(router_migrate)
app.include_router(router_experince)
