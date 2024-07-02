from fastapi import APIRouter,Security

from webcore.authorize import check_permissions
secure_router = APIRouter(prefix="/api/v1")

@secure_router.get("/authencation",dependencies=[Security(check_permissions,scopes=["admin"])])
async def verify_token():
    return {"message": "Hello World"}