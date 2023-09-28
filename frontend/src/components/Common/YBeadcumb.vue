<template>
  <nav class="fi-breadcrumbs mb-2 hidden sm:block">
    <ol class="flex flex-wrap items-center gap-x-2">
      <li class="flex gap-x-2" v-for="(item, i) in items" :key="item">
        <ChevronRightIcon
          class="h-5 w-5 text-gray-400 dark:text-gray-500 rtl:hidden"
          v-if="i !== 0"
        />
        <ChevronLeftIcon
          class="h-5 w-5 text-gray-400 dark:text-gray-500 ltr:hidden"
          v-if="i !== 0"
        />
        <router-link
          class="text-sm font-medium text-gray-500 outline-none transition duration-75 hover:text-gray-700 focus:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 dark:focus:text-gray-200"
          :to="item.to"
        >
          {{ item.label }}
        </router-link>
      </li>

      <!-- __ENDBLOCK__ -->
    </ol>
  </nav>
</template>
<script>
import { ChevronRightIcon, ChevronLeftIcon } from '@heroicons/vue/20/solid'

export default {
  name: 'bead-cumb',
  components: { ChevronRightIcon, ChevronLeftIcon },
  props: {
    items: Array
  }
}
</script>