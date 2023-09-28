<template>
  <div
    class="fi-page" :class="$router.name+'-page'"
  >
    <section class="grid auto-cols-fr gap-y-8 py-8">
        <PageHeader />
        <div>
          <div class="grid auto-cols-fr gap-y-8">

            <div class="flex flex-col gap-y-6">
              <DataTable />
            </div>

          </div>
        </div>
    </section>
  </div>
</template>
<script>
import PageHeader from "../components/Layouts/PageHeader.vue"
import DataTable from "../components/DataTable/DataTable.vue"

export default {
    name: "ProductView",
    components: {
      PageHeader, DataTable
    }

}
</script>