

from fastapi import FastAPI,Request
from webcore.lifespan import app_lifespan
from fastapi.middleware.cors import CORSMiddleware
from webcore.endpoints import all_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from webcore.middlewares import BaseMiddleware, bind_context_request
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from api.exceptions import not_found_html
from conf import config


app = FastAPI(lifespan=app_lifespan, title=config.APP_TITLE, version=config.APP_VERSION)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return RedirectResponse("/index.html")


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ALLOW_ORIGINS,
    allow_credentials=config.CORS_ALLOW_CREDENTIALS,
    allow_methods=config.CORS_ALLOW_METHODS,
    allow_headers=config.CORS_ALLOW_HEADERS,
)
app.add_middleware(BaseMiddleware)
app.middleware("http")(bind_context_request)
app.include_router(all_router)


# 自定义异常处理器
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        # 判断请求路径是否以 /api/v1 开头
        if not request.url.path.startswith("/api/v1"):
            return HTMLResponse(content=not_found_html, status_code=404)
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return await http_exception_handler(request, exc)