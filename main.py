from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import routes

templates = Jinja2Templates(directory="public")

app = FastAPI()

app.mount("/assets", StaticFiles(directory="./public/assets"), name="assets")

@app.middleware("http")
async def my_middleware(request: Request, call_next) -> Response:

    routes = str(request.url).replace(str(request.base_url), '').split("/")

    if routes[0] in ['assets', 'api', 'docs', 'openapi.json']:
        return await call_next(request)
    else:
        return templates.TemplateResponse("index.html", {"request": request})
    
@app.get("/api/sayhi")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}

app.include_router(routes)
