import os

lb = "{"
rb = "}"

def make_view_files(resources: list):
    
   

    try:
        for res in resources:
            capName = res.name.capitalize()
            simpleRes = 1 if res.simple == True else 0
            content = f'''<template>
  <div
    class="fi-page" :class="$router.name+'-page'"
  >
    <section class="grid auto-cols-fr gap-y-8 py-8">
        <PageHeader title="{res.pluralLabel}" label="{res.label}" :breadcumbs="breadcumbs" :simpleResouce="{simpleRes}" />
        <div>
          <div class="grid auto-cols-fr gap-y-8">
            <div class="flex flex-col gap-y-6">
              <ListRecords />
            </div>

          </div>
        </div>
    </section>
  </div>
</template>
<script>
import PageHeader from "../../components/Layouts/PageHeader.vue"
import ListRecords from "../../components/Layouts/ListRecords.vue";

export default {lb}
    name: "{capName}View",
    data(){lb}
      return {lb}
        breadcumbs: [
          {lb}
            label: '{res.pluralLabel}',
            to: '/{res.name}'
          {rb},
          {lb}
            label: 'Ro`yxat',
            to: ''
          {rb},
        ]
      {rb}
    {rb},
    components: {lb}
      PageHeader, ListRecords
    {rb}
{rb}
</script>
'''            
            filename = f"./frontend/src/views/{capName}View/List{capName}.vue"
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(filename, "w") as f:
                f.write(content)

        return True
    except Exception as e:
        print(e.args)
        return False