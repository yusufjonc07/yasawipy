<template>
  <header class="fi-header flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
    <div>
      <!-- __BLOCK__ -->
      <YBreadcumb v-bind:items="breadcumbs" />
      <!-- __ENDBLOCK__ -->

      <h1
        class="fi-header-heading text-2xl font-bold tracking-tight text-gray-950 dark:text-white sm:text-3xl"
      >
        {{ title }}
      </h1>
    </div>

    <div class="fi-ac gap-3 flex flex-wrap items-center justify-start shrink-0 sm:mt-7">
      <YButton tooltip="Kallenga" color="danger" icon="user" class="bg-danger-600">
        <span class="fi-btn-label"> Yangi qo'shish </span>
      </YButton>
    </div>
  </header>
</template>
<script>
import { YBreadcumb, YButton } from '../Common/Components.vue'
export default {
  name: 'page-header',
  data() {
    return {
      title: 'Mahsulotlar',
      breadcumbs: [
        {
          label: 'Mahsulotlar',
          to: '/products'
        },
        {
          label: 'Braklar',
          to: '/products/broken'
        },
        {
          label: "Ro'yxat",
          to: '#'
        }
      ]
    }
  },
  methods: {
    somefunc() {
      console.log('saom')
    }
  },
  components: { YBreadcumb, YButton }
}
</script>