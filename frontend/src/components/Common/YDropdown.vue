<template>
  <div class="fi-dropdown fi-user-menu relative">
    <div v-on:click="toggle" class="fi-dropdown-trigger flex cursor-pointer select-none">
      <button aria-label="User menu" type="button">
        <div
          style="
            background-image: url(https://yt3.googleusercontent.com/cqhdvuYeeUKutpUJZJcN2Plzuu5E8UlRMpK-BLeciHaX-s-83LBhAZ33YQWjxlVu3IoHsmYf=s900-c-k-c0x00ffffff-no-rj);
          "
          class="fi-avatar bg-cover bg-center h-9 w-9 fi-user-avatar rounded-full"
        ></div>
      </button>
    </div>

    <div
      v-show="isOpen"
      class="fi-dropdown-panel absolute z-10 mt-1 w-screen right-0 divide-gray-100 rounded-lg bg-white shadow-lg ring-1 ring-gray-950/5 transition dark:divide-white/5 dark:bg-gray-900 dark:ring-white/10 max-w-[14rem]"
    >
      <div
        class="fi-dropdown-header flex w-full gap-2 p-3 text-sm fi-dropdown-header-color-gray"
        icon-alias="panels::user-menu.profile-item"
      >
        <!-- __BLOCK__ -->
        <UserCircleIcon class="w-5" />
        <!-- __ENDBLOCK__ -->

        <span
          class="fi-dropdown-header-label flex-1 truncate text-start text-gray-700 dark:text-gray-200"
        >
          Demo User
        </span>
      </div>

      <div class="fi-dropdown-list p-1">
        <div
          x-data="{
        theme: null,

        init: function () {
            this.theme = localStorage.getItem('theme') || 'system'

            $dispatch('theme-changed', theme)

            $watch('theme', (theme) => {
                $dispatch('theme-changed', theme)
            })
        },
    }"
          class="fi-theme-switcher grid grid-flow-col gap-x-1"
        >
          <button
            aria-label="Enable light theme"
            type="button"
            :class="
              $layout.theme === 'light'
                ? 'bg-gray-50 text-primary-500 dark:bg-white/5 dark:text-primary-400'
                : 'text-gray-400 hover:text-gray-500 focus:text-gray-500 dark:text-gray-500 dark:hover:text-gray-400 dark:focus:text-gray-400'
            "
            v-on:click="$layout.changeTheme('light') && close()"
            class="flex justify-center rounded-lg p-2 outline-none transition duration-75 hover:bg-gray-50 focus:bg-gray-50 dark:hover:bg-white/5 dark:focus:bg-white/5"
          >
            <!-- __BLOCK__ -->
            <SunIcon class="w-6 text-yellow-500" />
            <!-- __ENDBLOCK__ -->
          </button>

          <button
            :class="
              $layout.theme === 'dark'
                ? 'bg-gray-50 text-primary-500 dark:bg-white/5 dark:text-primary-400'
                : 'text-gray-400 hover:text-gray-500 focus:text-gray-500 dark:text-gray-500 dark:hover:text-gray-400 dark:focus:text-gray-400'
            "
            v-on:click="$layout.changeTheme('dark') && close()"
            class="flex justify-center rounded-lg p-2 outline-none transition duration-75 hover:bg-gray-50 focus:bg-gray-50 dark:hover:bg-white/5 dark:focus:bg-white/5"
          >
            <!-- __BLOCK__ -->
            <MoonIcon class="w-6 text-blue-400" />
            <!-- __ENDBLOCK__ -->
          </button>

          <button
            :class="
              $layout.theme === 'time'
                ? 'bg-gray-50 text-primary-500 dark:bg-white/5 dark:text-primary-400'
                : 'text-gray-400 hover:text-gray-500 focus:text-gray-500 dark:text-gray-500 dark:hover:text-gray-400 dark:focus:text-gray-400'
            "
            v-on:click="$layout.changeTheme('time') && close()"
            class="flex justify-center rounded-lg p-2 outline-none transition duration-75 hover:bg-gray-50 focus:bg-gray-50 dark:hover:bg-white/5 dark:focus:bg-white/5"
          >
            <!-- __BLOCK__ -->
            <ClockIcon class="w-6" />
            <!-- __ENDBLOCK__ -->
          </button>
        </div>
      </div>

      <div class="fi-dropdown-list p-1">
        <button
          type="submit"
          style=""
          class="fi-dropdown-list-item flex w-full items-center gap-2 whitespace-nowrap rounded-md p-2 text-sm transition-colors duration-75 outline-none disabled:pointer-events-none disabled:opacity-70 fi-dropdown-list-item-color-gray hover:bg-gray-50 focus:bg-gray-50 dark:hover:bg-white/5 dark:focus:bg-white/5"
        >
          <!-- __BLOCK__ -->
          <ArrowLeftOnRectangleIcon class="w-5" />
          <!-- __ENDBLOCK__ -->

          <span
            class="fi-dropdown-list-item-label flex-1 truncate text-start text-gray-700 dark:text-gray-200"
          >
            Sign out
          </span>
        </button>
      </div>
    </div>
  </div>
</template>
<script scoped>
import { SunIcon, MoonIcon, UserCircleIcon } from '@heroicons/vue/20/solid'
import { ClockIcon, ArrowLeftOnRectangleIcon } from '@heroicons/vue/24/outline'

export default {
  name: 'drop-down',
  data() {
    return {
      isOpen: false
    }
  },
  methods: {
    toggle: function () {
      this.isOpen = !this.isOpen
    },
    open: function () {
      this.isOpen = true
    },
    close: function () {
      this.isOpen = false
    }
  },

  components: { SunIcon, MoonIcon, ClockIcon, ArrowLeftOnRectangleIcon, UserCircleIcon },
  mounted() {
    document.addEventListener('click', (e) => {
      if (!document.querySelector('.fi-dropdown').contains(e.target)) {
        this.close()
      }
    })
  }
}
</script>