def make_sidebar(resources):

    groups = []
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

    return {
        "groups": nGroups
    }

