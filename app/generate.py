from fastapi import APIRouter
import glob
from app.resource import Resource
import json

def make_sidebar():

    routers = glob.glob("app/resources/*.py")

    resources = []
    groups = []

    for router_file in routers:
        router_name = router_file.split(".py")[0].split("app/resources/")[1]
        router = __import__(f"app.resources.{router_name}", globals(), locals(), [
                            f"{router_name}_router"], 0)
        recource: Resource = getattr(router, f"{router_name}_router")
        resources.append(recource)

    for res in resources:
        groups.append(res.navigationGroup)

    groups = list(set(groups))

    nGroups = []

    for group in groups:

        nGroupItems = []

        for res in resources:

            if res.navigationGroup == group:
                nGroupItems.append({
                    "label": res.pluralLabel,
                    "to": f"/{res.name}",
                    "icon": res.navigationIcon,
                    "nCount": 0
                })

        nGroups.append({
            "label": group,
            "items": nGroupItems
        })

    context = {
        "groups": nGroups
    }

    with open("./frontend/src/components/data/navigation.json", "w") as f:
        f.write(json.dumps(context))

    print(nGroups)