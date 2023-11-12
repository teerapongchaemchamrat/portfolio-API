from fastapi import FastAPI
from service.index import router_index
from service.migrate import router_migrate
from service.login import router_login
from service.experince import router_experince
from service.portfolio import router_portfolio
from service.skill import router_skill
from service.test import router_test

# define fastapi.
app = FastAPI()

# register routes.
app.include_router(router_index)
app.include_router(router_login)
app.include_router(router_migrate)
app.include_router(router_test)
# app.include_router(router_experince)
# app.include_router(router_portfolio)
# app.include_router(router_skil)
