<template>
  <div
    class="fi-page" :class="$router.name+'-page'"
  >
    <section class="grid auto-cols-fr gap-y-8 py-8">
        <PageHeader title="Mijozlar" label="Mijoz" :breadcumbs="breadcumbs" :simpleResouce="1" />
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

export default {
    name: "CustomerView",
    data(){
      return {
        breadcumbs: [
          {
            label: 'Mijozlar',
            to: '/customer'
          },
          {
            label: 'Ro`yxat',
            to: ''
          },
        ]
      }
    },
    components: {
      PageHeader, ListRecords
    }
}
</script>
