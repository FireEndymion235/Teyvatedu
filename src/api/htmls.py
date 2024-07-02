from fastapi import  Request,Depends,APIRouter

from webcore.dependencies import GlobalState,get_global_state
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")
html_router = APIRouter()

@html_router.get("/index.html", response_class=HTMLResponse)
async def read_index(request: Request,state:GlobalState=Depends(get_global_state)):
    webres_dict = state.runtime.get("webres")
    context = {}
    context.update(webres_dict)
    context.update({"request": request})
    return templates.TemplateResponse("index.html", context)

@html_router.get("/publications.html", response_class=HTMLResponse)
async def read_generic(request: Request,state:GlobalState=Depends(get_global_state)):
    webres_dict = state.runtime.get("webres")
    context = {}
    context.update(webres_dict)
    context.update({"request": request})
    return templates.TemplateResponse("publications.html", context)

@html_router.get("/notifications.html", response_class=HTMLResponse)
async def read_notifications(request: Request,state:GlobalState=Depends(get_global_state)):
    webres_dict = state.runtime.get("webres")
    context = {}
    context.update(webres_dict)
    context.update({"request": request})
    return templates.TemplateResponse("notifications.html", context)

@html_router.get("/aboutus.html", response_class=HTMLResponse)
async def read_aboutus(request: Request,state:GlobalState=Depends(get_global_state)):
    webres_dict = state.runtime.get("webres")
    context = {}
    context.update(webres_dict)
    context.update({"request": request})
    return templates.TemplateResponse("aboutus.html", context)


@html_router.get("/contact.html", response_class=HTMLResponse)
async def read_contact(request: Request,state:GlobalState=Depends(get_global_state)):
    webres_dict = state.runtime.get("webres")
    context = {}
    context.update(webres_dict)
    context.update({"request": request})
    return templates.TemplateResponse("contact.html", context)
