from fastapi import APIRouter
import glob

routes = APIRouter(prefix='/api')
routers = glob.glob("app/resources/*.py")

for router_file in routers:
    router_name = router_file.split(".py")[0].split("app/resources/")[1]
    router = __import__(f"app.resources.{router_name}", globals(), locals(), [f"{router_name}_router"], 0)
    routes.include_router(getattr(router, f"{router_name}_router"))
