from fastapi import APIRouter,Security
from conf import config
from webcore.authorize import check_permissions
secure_router = APIRouter(prefix="/api/v1",tags=["secure"])

@secure_router.get("/authencation",dependencies=[Security(check_permissions,scopes=["admin"])])
async def verify_token():
    return {"message": "Hello World"}

@secure_router.get("/env",dependencies=[Security(check_permissions,scopes=["admin"])])
async def get_env():
    return {"ES":config.ES}