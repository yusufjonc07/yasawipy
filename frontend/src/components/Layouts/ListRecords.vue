<template>
  <div class="flex flex-col gap-y-6">
    <nav v-if="tabs"
      class="fi-tabs flex max-w-full gap-x-1 overflow-x-auto mx-auto rounded-xl bg-white p-2 shadow-sm ring-1 ring-gray-950/5 dark:bg-gray-900 dark:ring-white/10"
      role="tablist"
    >

      <!-- __BLOCK__ -->
      <button v-for="tab in tabs" :key="tab"
        type="button"
        class="fi-tabs-item flex items-center gap-x-2 rounded-lg px-3 py-2 text-sm font-medium outline-none transition duration-75 hover:bg-gray-50 focus:bg-gray-50 dark:hover:bg-white/5 dark:focus:bg-white/5 text-gray-500 hover:text-gray-700 focus:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 dark:focus:text-gray-200"
        role="tab"
        @click="set('activeTab', 'all')"
      >
        <!-- __BLOCK__ -->
        <component v-if="tab.icon" :is="this.$getIcon[tab.icon]" class="fi-tabs-item-icon h-5 w-5 text-gray-400 dark:text-gray-500"></component>
        <!-- __ENDBLOCK__ -->

        <!-- __BLOCK__ -->
        <span> {{ tab.name }} </span>
        <!-- __ENDBLOCK__ -->

        <!-- __BLOCK__ -->
        <div
        
            v-if="tab.badge"
          style="
            --c-50: var(--primary-50);
            --c-300: var(--primary-300);
            --c-400: var(--primary-400);
            --c-600: var(--primary-600);
          "
          class="fi-badge flex items-center justify-center gap-x-1 rounded-md text-xs font-medium ring-1 ring-inset px-1.5 min-w-[theme(spacing.5)] py-0.5 tracking-tight bg-custom-50 text-custom-600 ring-custom-600/10 dark:bg-custom-400/10 dark:text-custom-400 dark:ring-custom-400/30"
        >
          <!-- __BLOCK__ -->
          <span class="grid">
              <span class="truncate"> {{ tab.badge.text }} </span>
            </span>
        <!-- __ENDBLOCK__ -->

          <!-- __BLOCK__ -->
          <!-- __ENDBLOCK__ -->
        </div>
        <!-- __ENDBLOCK__ -->
      </button>

      <!-- __ENDBLOCK__ -->
    </nav>
    <DataTable />
  </div>
</template>
<script>

import DataTable from '../DataTable/DataTable.vue';

export default {
    name: 'list-records',
    props: {
        tabs: Array,
    },
    components: {
        DataTable
    }
}
</script>