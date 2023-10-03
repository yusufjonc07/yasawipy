import os

lb = "{"
rb = "}"

def make_router_index(resources: list):

    try:
        routes = "["
        view_imports  = ""

        for res in resources:

            capName = res.name.capitalize()


            routes = routes + f'''
    {lb}
      path: '/{res.name}:',
      component: List{capName},
    {rb},'''

            view_imports = view_imports + f"import List{capName} from \"../views/{capName}View/List{capName}.vue\"\n"
        

        content = f'''import {lb} createRouter, createWebHistory {rb} from 'vue-router'
{view_imports}

const router = createRouter({lb}
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: {routes}\n  ]
{rb})

export default router
        '''

       
        with open("./frontend/src/router/index.js", "w") as f:
            f.write(content)

        return True

    except Exception as e:
        return False
        print(e.args)