<template>
    <div
      v-on:click="$layout.closeSidebar()"
      v-show="$layout.sidebar.isOpen"
      class="fixed inset-0 z-30 bg-gray-950/50 transition duration-500 dark:bg-gray-950/75 lg:hidden"
    ></div>
</template>
<script>
export default {
  name: 'back-drop',
  data() {
    return {}
  }
}
</script>