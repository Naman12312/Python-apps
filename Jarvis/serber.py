from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
templates = Jinja2Templates(directory="templates")
server = FastAPI()
# server.mount("/static", StaticFiles(directory="static"), name="static")
@server.get("/", response_class=HTMLResponse)
async def main(request:Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})