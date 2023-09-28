<template>
  <div
    class="fi-input-wrp flex rounded-lg shadow-sm ring-1 transition duration-75 bg-white focus-within:ring-2 dark:bg-white/5 ring-gray-950/10 focus-within:ring-primary-600 dark:ring-white/20 dark:focus-within:ring-primary-500"
  >
    <!-- __BLOCK__ -->
    <div class="items-center gap-x-3 ps-3 flex pe-2">
      <MagnifyingGlassIcon class="fi-input-wrp-icon h-5 w-5 text-gray-400 dark:text-gray-500" />
      <img
        v-show="isLoading"
        src="../../assets/images/loading.svg"
        class="animate-spin fi-input-wrp-icon h-5 w-5"
      />
    </div>
    <!-- __ENDBLOCK__ -->

    <div class="min-w-0 flex-1">
      <input
        class="fi-input block w-full border-none bg-transparent py-1.5 text-base text-gray-950 outline-none transition duration-75 placeholder:text-gray-400 focus:ring-0 disabled:text-gray-500 disabled:[-webkit-text-fill-color:theme(colors.gray.500)] disabled:placeholder:[-webkit-text-fill-color:theme(colors.gray.400)] dark:text-white dark:placeholder:text-gray-500 dark:disabled:text-gray-400 dark:disabled:[-webkit-text-fill-color:theme(colors.gray.400)] dark:disabled:placeholder:[-webkit-text-fill-color:theme(colors.gray.500)] sm:text-sm sm:leading-6 ps-0 pe-3"
        autocomplete="off"
        :placeholder="placeholder"
        type="search"
        id="input-1"
      />
    </div>

    <!-- __BLOCK__ -->
    <!-- __ENDBLOCK__ -->
  </div>
</template>
<script>
import { MagnifyingGlassIcon } from '@heroicons/vue/20/solid'

export default {
  name: 'yw-button',
  props: {
    placeholder: String,
    isLoading: Boolean
  },
  components: { MagnifyingGlassIcon }
}
</script>