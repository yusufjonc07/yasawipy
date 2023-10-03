<template>
  <div
    class="fi-page" :class="$router.name+'-page'"
  >
    <section class="grid auto-cols-fr gap-y-8 py-8">
        <PageHeader title="Mahsulotlar" label="Mahsulot" :breadcumbs="breadcumbs" :simpleResouce="0" />
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
    name: "ProductView",
    data(){
      return {
        breadcumbs: [
          {
            label: 'Mahsulotlar',
            to: '/product'
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
