from fastapi import  Request,Depends,APIRouter
from api.render import render_books, render_notifications
from webcore.dependencies import GlobalState,get_global_state
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models.Book import Book
templates = Jinja2Templates(directory="templates")
html_router = APIRouter(tags=["Htmls"])

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
    books = await render_books()
    context.update({"request": request})
    context.update({"books": books})
    return templates.TemplateResponse("publications.html", context)

@html_router.get("/notifications.html", response_class=HTMLResponse)
async def read_notifications(request: Request,state:GlobalState=Depends(get_global_state)):
    webres_dict = state.runtime.get("webres")
    context = {}
    context.update(webres_dict)
    notification_text = await render_notifications()
    context.update({"request": request})
    context.update({"notifications":notification_text})
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

@html_router.get("/singlebook", response_class=HTMLResponse)
async def read_singalbook(request: Request, id:int, state:GlobalState=Depends(get_global_state)):
    webres_dict = state.runtime.get("webres")
    context = {}
    book = await Book.filter(id=id).first()
    context.update(webres_dict)
    context.update(**book.__dict__)
    context.update({"request": request})
    return templates.TemplateResponse("singlebook.html", context)