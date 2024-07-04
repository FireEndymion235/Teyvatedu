
"""
中间件模块
"""
from fastapi import Request
from starlette.types import ASGIApp, Scope, Receive, Send, Message
from starlette.datastructures import Headers
from .logcontroller import log as logger
from .proxy import request_var
class BaseMiddleware:
    def __init__(
            self,
            app: ASGIApp,
    ) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        async def send_wrapper(message: Message) -> None:
            await send(message)

        await self.app(scope, receive, send_wrapper)
    async def send(
        self, message: Message, send: Send, request_headers: Headers
    ) -> None:
        logger.info(f"Request Headers: {request_headers}")
        if message["type"] != "http.response.start":
            await send(message)
            return
        await send(message)


async def bind_context_request(request: Request, call_next):
    """
    middleware for request
    bind the current request to context var
    """
    token = request_var.set(request)
    logger.debug(f"[REQ] {request.client.host}/{request.client.port} [ACCESSED] {request.url}" )
    try:
        response = await call_next(request)
        return response
    finally:
        request_var.reset(token)