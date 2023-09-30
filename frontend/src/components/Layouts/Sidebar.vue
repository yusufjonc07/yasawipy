<template>
  <aside
    :class="
      $layout.sidebar.isOpen
        ? 'fi-sidebar-open translate-x-0 shadow-xl ring-1 ring-gray-950\/5 rtl:-translate-x-0 dark:ring-white\/10'
        : '-translate-x-full rtl:translate-x-full'
    "
    class="fi-sidebar w-[--sidebar-width] lg:sticky fixed inset-y-0 start-0 z-30 grid h-screen content-start bg-white transition-all dark:bg-gray-900 lg:z-0 lg:bg-transparent lg:shadow-none lg:ring-0 lg:transition-none dark:lg:bg-transparent lg:translate-x-0 rtl:lg:-translate-x-0"
  >
    <header
      class="fi-sidebar-header flex h-16 items-center bg-white px-6 ring-1 ring-gray-950/5 dark:bg-gray-900 dark:ring-white/10 lg:shadow-sm"
    >
      <div>
        <a href="#">
          <!-- __BLOCK__ -->
          <div
            class="fi-logo text-xl font-bold leading-5 tracking-tight text-gray-950 dark:text-white"
          >
            Yasawi Demo
          </div>
          <!-- __ENDBLOCK__ -->
        </a>
      </div>
    </header>
    <nav
      class="fi-sidebar-nav flex flex-col gap-y-7 overflow-y-auto overflow-x-hidden px-6 py-8"
      style="scrollbar-gutter: stable"
    >
      <ul class="-mx-2 flex flex-col gap-y-7">
        <li class="fi-sidebar-group flex flex-col gap-y-1" v-for="group in groups" :key="group">
          <div
            v-if="group.label"
            v-on:click="$layout.toggleCollapsedGroup(group.label)"
            class="flex items-center gap-x-3 px-2 py-2 cursor-pointer"
          >
            <span
              class="fi-sidebar-group-label flex-1 text-sm font-semibold text-gray-700 dark:text-gray-200 select-none"
            >
              {{ group.label }}
            </span>
            <button
              style="
                --c-300: var(--gray-300);
                --c-400: var(--gray-400);
                --c-500: var(--gray-500);
                --c-600: var(--gray-600);
              "
              class="fi-icon-btn relative flex items-center justify-center rounded-lg outline-none transition duration-75 focus:ring-2 disabled:pointer-events-none disabled:opacity-70 h-6 w-6 text-gray-400 hover:text-gray-500 focus:ring-primary-600 dark:text-gray-500 dark:hover:text-gray-400 dark:focus:ring-primary-500 fi-sidebar-group-collapse-button -my-2 -me-2"
              type="button"
              :class="$layout.groupIsCollapsed(group.label) ? '' : 'rotate-180'"
            >
              <ChevronDownIcon />
            </button>
          </div>
          <Transition name="bounce">
            <ul
              v-if="!($layout.groupIsCollapsed(group.label) && ($layout.sidebar.isOpen || true))"
              class="fi-sidebar-group-items duration-200 flex flex-col gap-y-1 overflow-hidden"
            >
              <li class="fi-sidebar-item" v-for="item in group.items" :key="item">
                <router-link
                  :to="item.to"
                  class="fi-sidebar-item-button relative flex items-center justify-center gap-x-3 rounded-lg px-2 py-2 text-sm outline-none transition duration-75 hover:bg-gray-100 focus:bg-gray-100 dark:hover:bg-white/5 dark:focus:bg-white/5"
                >
                  <component
                    class="w-5"
                    :is="this.$icon['outline'][getIcon(item.icon)]"
                  ></component>
                  <span
                    class="fi-sidebar-item-label flex-1 truncate text-gray-700 dark:text-gray-200 font-medium"
                  >
                    {{ item.label }}
                  </span>

                  <span>
                    <div
                      v-if="item.nCount > 0"
                      style="
                        --c-50: var(--primary-50);
                        --c-400: var(--primary-400);
                        --c-600: var(--primary-600);
                      "
                      class="fi-badge flex items-center justify-center gap-x-1 rounded-md text-xs font-medium ring-1 ring-inset px-2 min-w-[theme(spacing.6)] py-1 bg-custom-50 text-custom-600 ring-custom-600/10 dark:bg-custom-400/10 dark:text-custom-400 dark:ring-custom-400/30"
                    >
                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <span class="grid">
                        <span class="truncate"> {{ item.nCount }} </span>
                      </span>

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                    </div>
                  </span>
                </router-link>
              </li>
            </ul>
          </Transition>
        </li>
      </ul>
    </nav>
  </aside>
</template>
<script>
import { ChevronDownIcon } from '@heroicons/vue/20/solid'
import Navigations from '../data/navigation.json'

export default {
  name: 'side-bar',
  components: {
    ChevronDownIcon
  },
  data() {
    return {
      groups: Navigations.sidebar.groups
    }
  },

  methods: {
    capitalized(name) {
      const capitalizedFirst = name[0].toUpperCase()
      const rest = name.slice(1)

      return capitalizedFirst + rest
    },
    getIcon(name) {
      let cons = []

      name.split('-').forEach((element) => {
        cons.push(this.capitalized(element))
      })
      return cons.join('') + 'Icon'
    }
  }
}
</script>