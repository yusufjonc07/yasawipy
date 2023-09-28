<template>
  <button
    class="fi-btn fi-btn-size-md relative grid-flow-col items-center justify-center font-semibold outline-none transition duration-75 focus:ring-2 rounded-lg fi-btn-color-primary gap-1.5 px-3 py-2 text-sm inline-grid   text-white hover:bg-custom-500 dark:bg-custom-500 dark:hover:bg-custom-400 focus:ring-custom-500/50 dark:focus:ring-custom-400/50 fi-ac-btn-action"
  >
    <slot></slot>
  </button>
</template>
  <script>
export default {
  name: 'yw-button'
}
</script>