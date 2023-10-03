from fastapi import FastAPI
import glob
from app.resource import Resource
import json

from app.generate.layouts.routes import make_router_index
from app.generate.layouts.sidebar import make_sidebar
from app.generate.views.main import make_view_files


def generate_frontend(app: FastAPI):

    routers = glob.glob("app/resources/*.py")
    resources = []
    for router_file in routers:
        router_name = router_file.split(".py")[0].split("app/resources/")[1]
        router = __import__(f"app.resources.{router_name}", globals(), locals(), [
                            f"{router_name}_router"], 0)
        recource: Resource = getattr(router, f"{router_name}_router")
        resources.append(recource)

    sidebar = make_sidebar(resources)


    if make_view_files(resources):
        print("✅ View files have been generated!")
    else:
        print("❌ View files have not been generated!")

    if make_router_index(resources):
        print("✅ routes/index.js has been generated!")
    else:
        print("❌ routes/index.js has not been generated!")

    


    content = {
        "sidebar": sidebar,
        "app_name": app.title
    }

    with open("./frontend/src/components/data/navigation.json", "w") as f:
        f.write(json.dumps(content))
