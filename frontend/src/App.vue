<script setup>
import { RouterView } from 'vue-router'
import Sidebar from './components/Layouts/Sidebar.vue'
import Backdrop from './components/Layouts/Backdrop.vue'
import Navbar from './components/Layouts/Navbar.vue'

</script>

<template>
  <div :class="$layout.getTheme()">
    <div
      class="min-h-screen bg-gray-50 font-normal text-gray-950 antialiased dark:bg-gray-950 dark:text-white"
    >
      <div class="fi-layout flex min-h-screen w-full overflow-x-clip">
        <Backdrop />
        <Sidebar />
        <div class="fi-main-ctn w-screen flex flex-1 flex-col">
          <Navbar />
          <main class="fi-main w-full px-4 md:px-6 lg:px-7 max-w-7xl">
              <RouterView />
          </main>
        </div>
      </div>
    </div>
  </div>
</template>
