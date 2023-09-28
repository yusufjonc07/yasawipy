<template>
  <div class="fi-topbar sticky top-0 z-20 overflow-x-clip">
    <nav
      class="flex h-16 items-center gap-x-4 bg-white px-4 shadow-sm ring-1 ring-gray-950/5 dark:bg-gray-900 dark:ring-white/10 md:px-6 lg:px-8"
    >
      <!-- __BLOCK__ -->
      <button
        style="
          --c-300: var(--gray-300);
          --c-400: var(--gray-400);
          --c-500: var(--gray-500);
          --c-600: var(--gray-600);
        "
        class="fi-icon-btn relative flex items-center justify-center rounded-lg outline-none transition duration-75 focus:ring-2 disabled:pointer-events-none disabled:opacity-70 h-9 w-9 text-gray-400 hover:text-gray-500 focus:ring-primary-600 dark:text-gray-500 dark:hover:text-gray-400 dark:focus:ring-primary-500 -ms-1.5 lg:hidden"
        title="Expand sidebar"
        type="button"
        v-on:click="$layout.openSidebar()"
        v-if="!$layout.sidebar.isOpen"
      >
        <!-- __BLOCK__ -->
        <span class="sr-only"> Expand sidebar </span>
        <!-- __ENDBLOCK__ -->
        <Bars3Icon class="w-5" />
      </button>

      <!-- __BLOCK__ -->
      <button
        style="
          --c-300: var(--gray-300);
          --c-400: var(--gray-400);
          --c-500: var(--gray-500);
          --c-600: var(--gray-600);
        "
        class="fi-icon-btn relative flex items-center justify-center rounded-lg outline-none transition duration-75 focus:ring-2 disabled:pointer-events-none disabled:opacity-70 h-9 w-9 text-gray-400 hover:text-gray-500 focus:ring-primary-600 dark:text-gray-500 dark:hover:text-gray-400 dark:focus:ring-primary-500 -ms-1.5 lg:hidden"
        title="Collapse sidebar"
        type="button"
        v-on:click="$layout.closeSidebar()"
        v-show="$layout.sidebar.isOpen"
      >
        <!-- __BLOCK__ -->
        <!-- __ENDBLOCK__ -->
      </button>
      <!-- __ENDBLOCK__ -->

      <div class="flex ms-auto items-center gap-x-4 ">
        
          <div class="fi-global-search flex items-center">
            <div class="sm:relative">
                <YSearchInput  placeholder="global qidiruv" />
            </div>
          </div>

        <YDropdown />
      </div>
    </nav>
  </div>
</template>
<script>
import { Bars3Icon } from '@heroicons/vue/20/solid'
import {YDropdown, YSearchInput} from '../Common/Components.vue'

export default {
  name: 'nav-bar',
  components: { Bars3Icon, YDropdown, YSearchInput }
}
</script>