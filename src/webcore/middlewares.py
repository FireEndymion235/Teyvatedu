
"""
中间件模块
"""
from starlette.datastructures import Headers
from starlette.types import ASGIApp, Message, Receive, Scope, Send

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
        if message["type"] != "http.response.start":
            # 从ASGI的标准来看，如果不在此判断，那么lifespan就无法使用
            await send(message)
            return
        await send(message)
    