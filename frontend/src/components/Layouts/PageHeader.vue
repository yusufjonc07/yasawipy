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
      <YButton :isLoading="false" v-if="simpleResouce==1" :tooltip="`Yangi ${label} qo'shish`" color="primary" icon="plus">
        <span class="fi-btn-label"> Yangi {{ label }} </span>
      </YButton>
      <YButton v-if="simpleResouce==0" tag="a" urlTo="/create" :tooltip="`Yangi ${label} qo'shish`" color="danger" icon="plus">
        <span class="fi-btn-label"> Yangi {{ label }} </span>
      </YButton>
    </div>
  </header>
</template>
<script>
import { YBreadcumb, YButton } from '../Common/Components.vue'
export default {
  name: 'page-header',
  props: {
    title: String,
    label: String,
    simpleResouce: Number,
    breadcumbs: Array
  },
  methods: {
    somefunc() {
      console.log('saom')
    }
  },
  mounted(){
    console.log(this.simpleResouce);
  },
  components: { YBreadcumb, YButton }
}
</script>