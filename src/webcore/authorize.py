

from fastapi import Request, Depends
from fastapi.security import SecurityScopes
from pydantic import ValidationError

from fastapi import HTTPException, status
from typing import Optional, Any

import jwt
from webcore.logcontroller import log
from webcore.dependencies import get_global_state

def HTTP_E401(details: Optional[Any] = None, headers: Optional[dict[str, Any]] = None) -> None:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=details,
        headers=headers
    )


def scope_contains(access_required_scope:list, user_has_scope:list) -> bool:
    """
    检查权限是否包含
    用于检查用户的权限是否包含所需的权限
    :param access_required_scope: 需要的权限
    :param user_has_scope: 用户的权限
    :return: 是否包含
    """
    return set(access_required_scope).issubset(set(user_has_scope))


async def check_permissions(
        req: Request,
        required_scope: SecurityScopes, 
        state = Depends(get_global_state)) -> None:
    
    """
    检查权限
    检查权限一般和fastapi的security的Depends一起使用，用于检查用户的权限是否满足要求
    :param req: 请求
    :param required_scope: 需要的权限
    :param state: 全局状态
    """
    header = req.headers.get("Authorization")
    if not header:
        HTTP_E401("Not Authenticate, use access token please")
    token = header.split(" ")[1]
    payload = None
    try:
        log.debug(f"jwt is {token} \n decode by secret key {state.runtime.get('JWT_KEY')} and algoritem is {state.runtime.get('JWT_DECRYPT')} ")
        payload = jwt.decode(token, state.runtime.get("JWT_KEY"), algorithms=[state.runtime.get("JWT_DECRYPT")])
        log.debug(f"Payload: {payload}")
        if not payload:
            HTTP_E401("Invalid certification", {"WWW-Authenticate": f"Bearer {token}"})
    except jwt.ExpiredSignatureError:
        HTTP_E401("Certification has expired", {"WWW-Authenticate": f"Bearer {token}"})
    except jwt.InvalidTokenError:
        HTTP_E401("Certification parse error", {"WWW-Authenticate": f"Bearer {token}"})
    except (jwt.PyJWTError, ValidationError):
        HTTP_E401("Certification parse failed", {"WWW-Authenticate": f"Bearer {token}"})
    user_requested_scope = payload.get("per")
    log.debug(f"User requested scope: {user_requested_scope}")
    if scope_contains(required_scope.scopes, user_requested_scope) is False:
        HTTP_E401("Not enough scope for authorization", {"WWW-Authenticate": f"Bearer {token}"})
    state.user = payload
