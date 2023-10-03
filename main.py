from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import routes
from app.generate.main import generate_frontend
import subprocess
from app.utils.helpers import delete_files

templates = Jinja2Templates(directory="public")

app = FastAPI(
    title="TELEGRAM PLUS",
)



@app.middleware("http")
async def my_middleware(request: Request, call_next) -> Response:

    routes = str(request.url).replace(str(request.base_url), '').split("/")

    if routes[0] in ['assets', 'api', 'docs', 'openapi.json']:
        return await call_next(request)
    else:
        return templates.TemplateResponse("index.html", {"request": request})
    

@app.on_event("startup")
async def generate_app():
    generate_frontend(app)
    res = subprocess.run("cd frontend && npm run build", shell=True, capture_output=True)
    print(res.stdout.decode())

    app.mount("/assets", StaticFiles(directory="./public/assets"), name="assets")

# @app.on_event("shutdown")
# async def drop_all():
#     delete_files("./public/assets", ['js', 'css'])
#     delete_files("./frontend/src/router", ['js'])
#     print("Fayllar o'chirildi!")
        
    
@app.get("/api/sayhi")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}

app.include_router(routes)


