<template>
  <div
    ax-load=""
    ax-load-src="https://demo.filamentphp.com/js/filament/tables/components/table.js?v=3.0.60.0"
    x-data="table"
    class="fi-ta"
  >
    <div
      class="fi-ta-ctn divide-y divide-gray-200 overflow-hidden rounded-xl bg-white shadow-sm ring-1 ring-gray-950/5 dark:divide-white/10 dark:bg-gray-900 dark:ring-white/10"
    >
      <div
        x-bind:hidden="! (true || (selectedRecords.length &amp;&amp; 1))"
        x-show="true || (selectedRecords.length &amp;&amp; 1)"
        class="fi-ta-header-ctn divide-y divide-gray-200 dark:divide-white/10"
      >
        <!-- __BLOCK__ -->
        <!-- __ENDBLOCK__ -->

        <!-- __BLOCK__ -->
        <!-- __ENDBLOCK__ -->

        <div
          x-show="true || (selectedRecords.length &amp;&amp; 1)"
          class="fi-ta-header-toolbar flex items-center justify-between gap-3 px-4 py-3 sm:px-6"
        >
          <div class="flex shrink-0 items-center gap-x-3">
            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->

            <!-- __BLOCK__ -->
            <div
              class="fi-ta-actions flex shrink-0 items-center gap-3 justify-end"
              x-show="selectedRecords.length"
              style="display: none"
            >
              <!-- __BLOCK__ -->
              <span class="inline-flex -mx-2 sm:mx-0">
                <!-- __BLOCK__ -->
                <div
                  x-data="{
        toggle: function (event) {
            $refs.panel.toggle(event)
        },

        open: function (event) {
            $refs.panel.open(event)
        },

        close: function (event) {
            $refs.panel.close(event)
        },
    }"
                  class="fi-dropdown"
                >
                  <div x-on:click="toggle" class="fi-dropdown-trigger flex cursor-pointer">
                    <!-- __BLOCK__ -->
                    <!-- __BLOCK__ -->
                    <button
                      style="
                        --c-300: var(--gray-300);
                        --c-400: var(--gray-400);
                        --c-500: var(--gray-500);
                        --c-600: var(--gray-600);
                      "
                      class="fi-icon-btn relative flex items-center justify-center rounded-lg outline-none transition duration-75 focus:ring-2 disabled:pointer-events-none disabled:opacity-70 h-9 w-9 text-gray-400 hover:text-gray-500 focus:ring-primary-600 dark:text-gray-500 dark:hover:text-gray-400 dark:focus:ring-primary-500 sm:hidden fi-ac-btn-group"
                      title="Bulk actions"
                      type="button"
                    >
                      <!-- __BLOCK__ -->
                      <span class="sr-only"> Bulk actions </span>
                      <!-- __ENDBLOCK__ -->

                      <!-- __BLOCK__ -->
                      <svg
                        class="fi-icon-btn-icon h-5 w-5"
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                        aria-hidden="true"
                      >
                        <path
                          d="M10 3a1.5 1.5 0 110 3 1.5 1.5 0 010-3zM10 8.5a1.5 1.5 0 110 3 1.5 1.5 0 010-3zM11.5 15.5a1.5 1.5 0 10-3 0 1.5 1.5 0 003 0z"
                        ></path>
                      </svg>
                      <!-- __ENDBLOCK__ -->

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                    </button>
                    <!-- __ENDBLOCK__ -->
                    <!-- __ENDBLOCK__ -->

                    <!-- __BLOCK__ -->
                    <button
                      style=""
                      class="fi-btn fi-btn-size-md relative grid-flow-col items-center justify-center font-semibold outline-none transition duration-75 focus:ring-2 rounded-lg fi-btn-color-gray gap-1.5 px-3 py-2 text-sm hidden sm:inline-grid shadow-sm bg-white text-gray-950 hover:bg-gray-50 dark:bg-white/5 dark:text-white dark:hover:bg-white/10 ring-1 ring-gray-950/10 dark:ring-white/20 fi-ac-btn-group"
                      type="button"
                      wire:loading.attr="disabled"
                    >
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <svg
                        class="fi-btn-icon h-5 w-5 text-gray-400 dark:text-gray-500"
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                        aria-hidden="true"
                      >
                        <path
                          d="M10 3a1.5 1.5 0 110 3 1.5 1.5 0 010-3zM10 8.5a1.5 1.5 0 110 3 1.5 1.5 0 010-3zM11.5 15.5a1.5 1.5 0 10-3 0 1.5 1.5 0 003 0z"
                        ></path>
                      </svg>
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <span class="fi-btn-label"> Bulk actions </span>

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                    </button>
                    <!-- __ENDBLOCK__ -->
                  </div>

                  <div
                    x-float.placement.bottom-start.flip.teleport.offset="{ offset: 8 }"
                    x-ref="panel"
                    x-transition:enter-start="opacity-0"
                    x-transition:leave-end="opacity-0"
                    class="fi-dropdown-panel absolute z-10 w-screen divide-y divide-gray-100 rounded-lg bg-white shadow-lg ring-1 ring-gray-950/5 transition dark:divide-white/5 dark:bg-gray-900 dark:ring-white/10 max-w-[14rem]"
                    style="position: fixed; display: none"
                  >
                    <!-- __BLOCK__ -->
                    <div class="fi-dropdown-list p-1">
                      <!-- __BLOCK__ -->
                      <button
                        style="
                          --c-50: var(--danger-50);
                          --c-400: var(--danger-400);
                          --c-500: var(--danger-500);
                          --c-600: var(--danger-600);
                        "
                        class="fi-dropdown-list-item flex w-full items-center gap-2 whitespace-nowrap rounded-md p-2 text-sm transition-colors duration-75 outline-none disabled:pointer-events-none disabled:opacity-70 fi-dropdown-list-item-color-danger hover:bg-custom-50 focus:bg-custom-50 dark:hover:bg-custom-400/10 dark:focus:bg-custom-400/10 fi-ac-grouped-action"
                        type="button"
                        wire:loading.attr="disabled"
                        wire:target="mountTableBulkAction('delete')"
                        x-on:click="mountBulkAction('delete')"
                        x-bind:disabled="! selectedRecords.length"
                        disabled="disabled"
                      >
                        <!-- __BLOCK__ -->
                        <svg
                          wire:loading.remove.delay="1"
                          wire:target="mountTableBulkAction('delete')"
                          class="fi-dropdown-list-item-icon h-5 w-5 text-custom-500 dark:text-custom-400"
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            fill-rule="evenodd"
                            d="M8.75 1A2.75 2.75 0 006 3.75v.443c-.795.077-1.584.176-2.365.298a.75.75 0 10.23 1.482l.149-.022.841 10.518A2.75 2.75 0 007.596 19h4.807a2.75 2.75 0 002.742-2.53l.841-10.52.149.023a.75.75 0 00.23-1.482A41.03 41.03 0 0014 4.193V3.75A2.75 2.75 0 0011.25 1h-2.5zM10 4c.84 0 1.673.025 2.5.075V3.75c0-.69-.56-1.25-1.25-1.25h-2.5c-.69 0-1.25.56-1.25 1.25v.325C8.327 4.025 9.16 4 10 4zM8.58 7.72a.75.75 0 00-1.5.06l.3 7.5a.75.75 0 101.5-.06l-.3-7.5zm4.34.06a.75.75 0 10-1.5-.06l-.3 7.5a.75.75 0 101.5.06l.3-7.5z"
                            clip-rule="evenodd"
                          ></path>
                        </svg>
                        <!-- __ENDBLOCK__ -->

                        <svg
                          fill="none"
                          viewBox="0 0 24 24"
                          xmlns="http://www.w3.org/2000/svg"
                          class="animate-spin fi-dropdown-list-item-icon h-5 w-5 text-custom-500 dark:text-custom-400"
                          wire:loading.delay=""
                          wire:target="mountTableBulkAction('delete')"
                        >
                          <path
                            clip-rule="evenodd"
                            d="M12 19C15.866 19 19 15.866 19 12C19 8.13401 15.866 5 12 5C8.13401 5 5 8.13401 5 12C5 15.866 8.13401 19 12 19ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
                            fill-rule="evenodd"
                            fill="currentColor"
                            opacity="0.2"
                          ></path>
                          <path
                            d="M2 12C2 6.47715 6.47715 2 12 2V5C8.13401 5 5 8.13401 5 12H2Z"
                            fill="currentColor"
                          ></path>
                        </svg>

                        <span
                          class="fi-dropdown-list-item-label flex-1 truncate text-start text-custom-600 dark:text-custom-400"
                        >
                          Delete selected
                        </span>
                      </button>

                      <!-- __ENDBLOCK__ -->
                    </div>
                    <!-- __ENDBLOCK__ -->
                  </div>
                </div>
                <!-- __ENDBLOCK__ -->
              </span>
              <!-- __ENDBLOCK__ -->
            </div>
            <!-- __ENDBLOCK__ -->

            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->
          </div>

          <!-- __BLOCK__ -->
          <div class="ms-auto flex items-center gap-x-4">
            <!-- __BLOCK__ -->
            <div x-id="['input']" class="fi-ta-search-field">
              <label x-bind:for="$id('input')" class="sr-only" for="input-1"> Search </label>
              <YSearchInput placeholder="Qidirish" v-model="search" />
            </div>
            <!-- __ENDBLOCK__ -->

            <!-- __BLOCK__ -->
            <!-- __BLOCK__ -->
            <div
              x-data="{
        toggle: function (event) {
            $refs.panel.toggle(event)
        },

        open: function (event) {
            $refs.panel.open(event)
        },

        close: function (event) {
            $refs.panel.close(event)
        },
    }"
              class="fi-dropdown fi-ta-filters-dropdown"
              wire:key="YDjdrqMZkmrJTuGzMaXn.table.filters"
            >
              <div x-on:click="toggle" class="fi-dropdown-trigger flex cursor-pointer">
                <span class="inline-flex -mx-2">
                  <!-- __BLOCK__ -->
                  <button
                    style="
                      --c-300: var(--gray-300);
                      --c-400: var(--gray-400);
                      --c-500: var(--gray-500);
                      --c-600: var(--gray-600);
                    "
                    class="fi-icon-btn relative flex items-center justify-center rounded-lg outline-none transition duration-75 focus:ring-2 disabled:pointer-events-none disabled:opacity-70 h-9 w-9 text-gray-400 hover:text-gray-500 focus:ring-primary-600 dark:text-gray-500 dark:hover:text-gray-400 dark:focus:ring-primary-500 fi-ac-icon-btn-action"
                    title="Filter"
                    type="button"
                  >
                    <!-- __BLOCK__ -->
                    <span class="sr-only"> Filter </span>
                    <!-- __ENDBLOCK__ -->

                    <!-- __BLOCK__ -->
                    <svg
                      class="fi-icon-btn-icon h-5 w-5"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      aria-hidden="true"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M2.628 1.601C5.028 1.206 7.49 1 10 1s4.973.206 7.372.601a.75.75 0 01.628.74v2.288a2.25 2.25 0 01-.659 1.59l-4.682 4.683a2.25 2.25 0 00-.659 1.59v3.037c0 .684-.31 1.33-.844 1.757l-1.937 1.55A.75.75 0 018 18.25v-5.757a2.25 2.25 0 00-.659-1.591L2.659 6.22A2.25 2.25 0 012 4.629V2.34a.75.75 0 01.628-.74z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                    <!-- __ENDBLOCK__ -->

                    <!-- __BLOCK__ -->
                    <!-- __ENDBLOCK__ -->

                    <!-- __BLOCK__ -->
                    <div
                      class="fi-icon-btn-badge-ctn absolute start-full top-0 z-[1] -ms-1 w-max -translate-x-1/2 rounded-md bg-white rtl:translate-x-1/2 dark:bg-gray-900"
                    >
                      <div
                        style="
                          --c-50: var(--primary-50);
                          --c-400: var(--primary-400);
                          --c-600: var(--primary-600);
                        "
                        class="fi-badge flex items-center justify-center gap-x-1 rounded-md text-xs font-medium ring-1 ring-inset px-0.5 min-w-[theme(spacing.4)] tracking-tighter bg-custom-50 text-custom-600 ring-custom-600/10 dark:bg-custom-400/10 dark:text-custom-400 dark:ring-custom-400/30"
                      >
                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <span class="grid">
                          <span class="truncate"> 0 </span>
                        </span>

                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->
                      </div>
                    </div>
                    <!-- __ENDBLOCK__ -->
                  </button>
                  <!-- __ENDBLOCK__ -->
                </span>
              </div>

              <div
                x-float.placement.bottom-end.flip.shift.offset="{ offset: 8 }"
                x-ref="panel"
                x-transition:enter-start="opacity-0"
                x-transition:leave-end="opacity-0"
                wire:ignore.self=""
                wire:key="YDjdrqMZkmrJTuGzMaXn.table.filters.panel"
                class="fi-dropdown-panel absolute z-10 w-screen divide-y divide-gray-100 rounded-lg bg-white shadow-lg ring-1 ring-gray-950/5 transition dark:divide-white/5 dark:bg-gray-900 dark:ring-white/10 max-w-xs"
                style="display: none"
              >
                <div class="fi-ta-filters grid gap-y-4 p-6">
                  <div class="flex items-center justify-between">
                    <h4 class="text-base font-semibold leading-6 text-gray-950 dark:text-white">
                      Filters
                    </h4>

                    <!-- __BLOCK__ -->
                    <button
                      style="
                        --c-300: var(--danger-300);
                        --c-400: var(--danger-400);
                        --c-500: var(--danger-500);
                        --c-600: var(--danger-600);
                      "
                      class="fi-link fi-link-size-md relative inline-flex items-center justify-center font-semibold outline-none transition duration-75 hover:underline focus:underline gap-1.5 text-sm text-custom-600 dark:text-custom-400"
                      type="button"
                      wire:loading.attr="disabled"
                      wire:target="tableFilters,resetTableFiltersForm"
                      wire:click="resetTableFiltersForm"
                      wire:loading.remove.delay=""
                    >
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <!-- __BLOCK__ -->
                      <svg
                        fill="none"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                        class="animate-spin fi-link-icon h-5 w-5 text-custom-600 dark:text-custom-400"
                        wire:loading.delay=""
                        wire:target="resetTableFiltersForm"
                      >
                        <path
                          clip-rule="evenodd"
                          d="M12 19C15.866 19 19 15.866 19 12C19 8.13401 15.866 5 12 5C8.13401 5 5 8.13401 5 12C5 15.866 8.13401 19 12 19ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
                          fill-rule="evenodd"
                          fill="currentColor"
                          opacity="0.2"
                        ></path>
                        <path
                          d="M2 12C2 6.47715 6.47715 2 12 2V5C8.13401 5 5 8.13401 5 12H2Z"
                          fill="currentColor"
                        ></path>
                      </svg>
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      Reset

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                    </button>
                    <!-- __ENDBLOCK__ -->

                    <svg
                      fill="none"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                      class="animate-spin h-5 w-5 text-gray-400 dark:text-gray-500"
                      wire:loading.delay=""
                      wire:target="tableFilters,resetTableFiltersForm"
                    >
                      <path
                        clip-rule="evenodd"
                        d="M12 19C15.866 19 19 15.866 19 12C19 8.13401 15.866 5 12 5C8.13401 5 5 8.13401 5 12C5 15.866 8.13401 19 12 19ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
                        fill-rule="evenodd"
                        fill="currentColor"
                        opacity="0.2"
                      ></path>
                      <path
                        d="M2 12C2 6.47715 6.47715 2 12 2V5C8.13401 5 5 8.13401 5 12H2Z"
                        fill="currentColor"
                      ></path>
                    </svg>
                  </div>

                  <div
                    style="
                      --cols-default: repeat(1, minmax(0, 1fr));
                      --cols-lg: repeat(1, minmax(0, 1fr));
                    "
                    class="grid grid-cols-[--cols-default] lg:grid-cols-[--cols-lg] fi-fo-component-ctn gap-6"
                  >
                    <!-- __BLOCK__ -->
                    <div
                      style="--col-span-default: span 1 / span 1"
                      class="col-[--col-span-default]"
                    >
                      <!-- __BLOCK__ -->
                      <div>
                        <div
                          style="--cols-default: repeat(1, minmax(0, 1fr))"
                          class="grid grid-cols-[--cols-default] fi-fo-component-ctn gap-6"
                        >
                          <!-- __BLOCK__ -->
                          <div
                            style="--col-span-default: span 1 / span 1"
                            class="col-[--col-span-default]"
                            wire:key="YDjdrqMZkmrJTuGzMaXn.tableFilters.brand.values.Filament\Forms\Components\Select"
                          >
                            <!-- __BLOCK__ -->
                            <div class="fi-fo-field-wrp">
                              <!-- __BLOCK__ -->
                              <!-- __ENDBLOCK__ -->

                              <div class="grid gap-y-2">
                                <!-- __BLOCK__ -->
                                <div class="flex items-center justify-between gap-x-3">
                                  <!-- __BLOCK__ -->
                                  <label
                                    class="fi-fo-field-wrp-label inline-flex items-center gap-x-3"
                                    for="tableFilters.brand.values"
                                  >
                                    <span
                                      class="text-sm font-medium leading-6 text-gray-950 dark:text-white"
                                    >
                                      Brand<!-- __BLOCK__ -->
                                      <!-- __ENDBLOCK__ -->
                                    </span>
                                  </label>
                                  <!-- __ENDBLOCK__ -->

                                  <!-- __BLOCK__ -->
                                  <!-- __ENDBLOCK__ -->
                                </div>
                                <!-- __ENDBLOCK__ -->

                                <!-- __BLOCK__ -->
                                <div class="grid gap-y-2">
                                  <div
                                    class="fi-input-wrp flex rounded-lg shadow-sm ring-1 transition duration-75 bg-white focus-within:ring-2 dark:bg-white/5 ring-gray-950/10 focus-within:ring-primary-600 dark:ring-white/20 dark:focus-within:ring-primary-500 fi-fo-select"
                                  >
                                    <!-- __BLOCK__ -->
                                    <!-- __ENDBLOCK__ -->

                                    <div class="min-w-0 flex-1">
                                      <!-- __BLOCK__ -->
                                      <div
                                        ax-load=""
                                        ax-load-src="https://demo.filamentphp.com/js/filament/forms/components/select.js?v=3.0.60.0"
                                        x-data="selectFormComponent({
                            canSelectPlaceholder: true,
                            isHtmlAllowed: false,
                            getOptionLabelUsing: async () => {
                                return await $wire.getFormSelectOptionLabel('tableFilters.brand.values')
                            },
                            getOptionLabelsUsing: async () => {
                                return await $wire.getFormSelectOptionLabels('tableFilters.brand.values')
                            },
                            getOptionsUsing: async () => {
                                return await $wire.getFormSelectOptions('tableFilters.brand.values')
                            },
                            getSearchResultsUsing: async (search) => {
                                return await $wire.getFormSelectSearchResults('tableFilters.brand.values', search)
                            },
                            isAutofocused: false,
                            isMultiple: true,
                            isSearchable: true,
                            livewireId: 'YDjdrqMZkmrJTuGzMaXn',
                            hasDynamicOptions: true,
                            hasDynamicSearchResults: false,
                            loadingMessage: 'Loading...',
                            maxItems: null,
                            maxItemsMessage: 'Only  can be selected.',
                            noSearchResultsMessage: 'No options match your search.',
                            options: JSON.parse('[{\u0022label\u0022:\u0022Abshire-Hahn\u0022,\u0022value\u0022:\u0022308\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Ankunding-Daniel\u0022,\u0022value\u0022:\u0022236\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Auer LLC\u0022,\u0022value\u0022:\u002228\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bailey-Wyman\u0022,\u0022value\u0022:\u0022370\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Balistreri, Lind and Bosco\u0022,\u0022value\u0022:\u002298\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Barrows and Sons\u0022,\u0022value\u0022:\u0022309\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Barrows, Waelchi and Bartell\u0022,\u0022value\u0022:\u0022155\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bartoletti-Rutherford\u0022,\u0022value\u0022:\u002245\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bartoletti, Cummerata and Prosacco\u0022,\u0022value\u0022:\u0022376\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Batz, Lang and Grady\u0022,\u0022value\u0022:\u0022156\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Batz, Mosciski and Mann\u0022,\u0022value\u0022:\u0022396\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bauch-Hickle\u0022,\u0022value\u0022:\u002239\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Beahan PLC\u0022,\u0022value\u0022:\u0022256\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Beahan-Luettgen\u0022,\u0022value\u0022:\u0022296\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Beatty-Bauch\u0022,\u0022value\u0022:\u0022351\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Becker-Koch\u0022,\u0022value\u0022:\u0022180\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bednar, Kuphal and Little\u0022,\u0022value\u0022:\u00226\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bednar, Streich and Keebler\u0022,\u0022value\u0022:\u0022306\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Beer Group\u0022,\u0022value\u0022:\u0022108\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Beier-Kertzmann\u0022,\u0022value\u0022:\u0022119\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bergnaum PLC\u0022,\u0022value\u0022:\u0022100\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bergnaum-Breitenberg\u0022,\u0022value\u0022:\u002287\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bernhard-Leffler\u0022,\u0022value\u0022:\u002299\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bernhard, Rohan and Jakubowski\u0022,\u0022value\u0022:\u0022331\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bernier-Kemmer\u0022,\u0022value\u0022:\u0022379\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bernier-Mraz\u0022,\u0022value\u0022:\u0022362\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bins, Langworth and Schneider\u0022,\u0022value\u0022:\u0022275\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bins, Zulauf and Rowe\u0022,\u0022value\u0022:\u002213\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Block-Kutch\u0022,\u0022value\u0022:\u0022299\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bode-Kilback\u0022,\u0022value\u0022:\u002257\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bode-Lehner\u0022,\u0022value\u0022:\u002294\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bode-Sanford\u0022,\u0022value\u0022:\u0022163\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bogan Group\u0022,\u0022value\u0022:\u0022196\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bosco, Grady and Jast\u0022,\u0022value\u0022:\u002290\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Boyer and Sons\u0022,\u0022value\u0022:\u0022255\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Bradtke-Miller\u0022,\u0022value\u0022:\u002279\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Braun Inc\u0022,\u0022value\u0022:\u0022158\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Braun, Buckridge and Tremblay\u0022,\u0022value\u0022:\u002223\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Breitenberg-Nolan\u0022,\u0022value\u0022:\u0022312\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Brekke-Howe\u0022,\u0022value\u0022:\u0022127\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cassin, Hintz and Carroll\u0022,\u0022value\u0022:\u0022283\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cassin, Prosacco and Predovic\u0022,\u0022value\u0022:\u0022215\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Champlin Inc\u0022,\u0022value\u0022:\u0022239\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Champlin-Harvey\u0022,\u0022value\u0022:\u0022186\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cole and Sons\u0022,\u0022value\u0022:\u0022207\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Collier Inc\u0022,\u0022value\u0022:\u0022336\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Collins Ltd\u0022,\u0022value\u0022:\u002212\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Collins-Balistreri\u0022,\u0022value\u0022:\u0022252\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Collins, Bauch and Treutel\u0022,\u0022value\u0022:\u0022197\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Conn LLC\u0022,\u0022value\u0022:\u0022314\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Conroy, Okuneva and Bins\u0022,\u0022value\u0022:\u00228\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Corkery and Sons\u0022,\u0022value\u0022:\u0022167\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Corkery Group\u0022,\u0022value\u0022:\u0022381\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Corkery LLC\u0022,\u0022value\u0022:\u0022300\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Corkery PLC\u0022,\u0022value\u0022:\u0022295\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cormier-Macejkovic\u0022,\u0022value\u0022:\u0022304\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Corwin, Gerlach and Kuphal\u0022,\u0022value\u0022:\u002289\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cremin Inc\u0022,\u0022value\u0022:\u0022129\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Crona-Klein\u0022,\u0022value\u0022:\u0022221\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cronin and Sons\u0022,\u0022value\u0022:\u0022124\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cronin Inc\u0022,\u0022value\u0022:\u0022378\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cronin-Daniel\u0022,\u0022value\u0022:\u0022357\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Crooks, Aufderhar and Conroy\u0022,\u0022value\u0022:\u0022338\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cruickshank-Klocko\u0022,\u0022value\u0022:\u0022263\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cummerata-Hermann\u0022,\u0022value\u0022:\u0022211\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cummings-Nikolaus\u0022,\u0022value\u0022:\u0022133\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Cummings-Sauer\u0022,\u0022value\u0022:\u0022324\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022D\\u0027Amore, Stracke and Ward\u0022,\u0022value\u0022:\u002284\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Dach, Kertzmann and Swaniawski\u0022,\u0022value\u0022:\u0022243\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Dare PLC\u0022,\u0022value\u0022:\u0022173\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Dare-Rowe\u0022,\u0022value\u0022:\u002210\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Dare, Boehm and Reichel\u0022,\u0022value\u0022:\u0022231\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Dare, Heaney and Bergstrom\u0022,\u0022value\u0022:\u0022177\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Davis, Bartell and Gusikowski\u0022,\u0022value\u0022:\u0022238\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Denesik, Cummerata and Bosco\u0022,\u0022value\u0022:\u0022355\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Dicki and Sons\u0022,\u0022value\u0022:\u0022384\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Dietrich-Ritchie\u0022,\u0022value\u0022:\u0022254\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Donnelly LLC\u0022,\u0022value\u0022:\u002233\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Donnelly-Padberg\u0022,\u0022value\u0022:\u002260\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Dooley, Beier and Wisozk\u0022,\u0022value\u0022:\u0022171\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Dooley, Smith and Runolfsson\u0022,\u0022value\u0022:\u002283\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Doyle LLC\u0022,\u0022value\u0022:\u0022320\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Doyle Ltd\u0022,\u0022value\u0022:\u0022200\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Doyle, Bogan and Ritchie\u0022,\u0022value\u0022:\u0022392\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022DuBuque LLC\u0022,\u0022value\u0022:\u0022115\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Durgan Group\u0022,\u0022value\u0022:\u0022223\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Durgan, Jakubowski and Beahan\u0022,\u0022value\u0022:\u0022199\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Effertz-Altenwerth\u0022,\u0022value\u0022:\u0022386\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Eichmann PLC\u0022,\u0022value\u0022:\u0022168\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Fadel, Sanford and Bauch\u0022,\u0022value\u0022:\u0022122\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Fahey-Lockman\u0022,\u0022value\u0022:\u0022363\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Fahey, Funk and Pacocha\u0022,\u0022value\u0022:\u0022175\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Farrell Ltd\u0022,\u0022value\u0022:\u0022371\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Farrell-Jones\u0022,\u0022value\u0022:\u0022342\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Feeney and Sons\u0022,\u0022value\u0022:\u002267\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Feeney Ltd\u0022,\u0022value\u0022:\u0022210\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Feeney-Mann\u0022,\u0022value\u0022:\u0022387\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Feeney, Wisozk and Powlowski\u0022,\u0022value\u0022:\u002266\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Flatley and Sons\u0022,\u0022value\u0022:\u0022154\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Flatley, Windler and Morissette\u0022,\u0022value\u0022:\u0022266\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Franecki Inc\u0022,\u0022value\u0022:\u002218\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Franecki, Kohler and Ebert\u0022,\u0022value\u0022:\u0022248\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Friesen Group\u0022,\u0022value\u0022:\u0022104\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Funk-Daniel\u0022,\u0022value\u0022:\u0022172\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Funk-Krajcik\u0022,\u0022value\u0022:\u0022343\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Funk-Spinka\u0022,\u0022value\u0022:\u0022134\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Gerhold LLC\u0022,\u0022value\u0022:\u0022262\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Gislason Group\u0022,\u0022value\u0022:\u0022284\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Gislason-Herzog\u0022,\u0022value\u0022:\u002227\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Gleichner, Gibson and Marvin\u0022,\u0022value\u0022:\u002221\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Glover, O\\u0027Hara and Fisher\u0022,\u0022value\u0022:\u0022391\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Gorczany-Gusikowski\u0022,\u0022value\u0022:\u002217\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Goyette, Gaylord and Ferry\u0022,\u0022value\u0022:\u0022249\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Grady and Sons\u0022,\u0022value\u0022:\u0022271\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Green Group\u0022,\u0022value\u0022:\u0022125\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Green-Russel\u0022,\u0022value\u0022:\u002226\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Grimes, Hayes and Schmidt\u0022,\u0022value\u0022:\u0022321\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Grimes, Rogahn and Quitzon\u0022,\u0022value\u0022:\u002249\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Gulgowski Ltd\u0022,\u0022value\u0022:\u002256\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Gulgowski PLC\u0022,\u0022value\u0022:\u0022114\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Gusikowski and Sons\u0022,\u0022value\u0022:\u0022354\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Gusikowski-Steuber\u0022,\u0022value\u0022:\u0022347\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Gusikowski, Carroll and Ritchie\u0022,\u0022value\u0022:\u0022267\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hackett PLC\u0022,\u0022value\u0022:\u002264\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hackett, Yundt and Bruen\u0022,\u0022value\u0022:\u002211\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hagenes and Sons\u0022,\u0022value\u0022:\u002238\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hahn-Weissnat\u0022,\u0022value\u0022:\u0022182\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Haley Group\u0022,\u0022value\u0022:\u0022185\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hammes-Raynor\u0022,\u0022value\u0022:\u0022140\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hammes, Conn and Reilly\u0022,\u0022value\u0022:\u0022184\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hane-Rutherford\u0022,\u0022value\u0022:\u0022176\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hansen LLC\u0022,\u0022value\u0022:\u0022216\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hansen PLC\u0022,\u0022value\u0022:\u00221\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Harber-Hermiston\u0022,\u0022value\u0022:\u0022335\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hauck LLC\u0022,\u0022value\u0022:\u0022310\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Heaney Group\u0022,\u0022value\u0022:\u0022139\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Heathcote, Balistreri and Lang\u0022,\u0022value\u0022:\u0022187\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hegmann, Mann and Lehner\u0022,\u0022value\u0022:\u0022307\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Heller Ltd\u0022,\u0022value\u0022:\u0022198\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hermann-Rempel\u0022,\u0022value\u0022:\u0022128\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Herzog, Littel and Huel\u0022,\u0022value\u0022:\u0022279\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hessel-Kassulke\u0022,\u0022value\u0022:\u002248\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hettinger-Kuhlman\u0022,\u0022value\u0022:\u0022245\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hettinger, Braun and Kshlerin\u0022,\u0022value\u0022:\u0022222\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hill, Jaskolski and Adams\u0022,\u0022value\u0022:\u002273\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hirthe PLC\u0022,\u0022value\u0022:\u0022257\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hodkiewicz PLC\u0022,\u0022value\u0022:\u002215\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hoeger-Armstrong\u0022,\u0022value\u0022:\u0022348\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Homenick, Breitenberg and Hudson\u0022,\u0022value\u0022:\u002280\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hoppe-Haag\u0022,\u0022value\u0022:\u002278\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Howe and Sons\u0022,\u0022value\u0022:\u0022339\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Howe-Conn\u0022,\u0022value\u0022:\u0022202\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Howe-Crist\u0022,\u0022value\u0022:\u0022116\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Howe, Marks and Kunze\u0022,\u0022value\u0022:\u002261\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hudson, Rogahn and Ziemann\u0022,\u0022value\u0022:\u0022383\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Huel-Sanford\u0022,\u0022value\u0022:\u002214\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hyatt Group\u0022,\u0022value\u0022:\u0022147\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Hyatt-Rempel\u0022,\u0022value\u0022:\u0022106\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Jacobs PLC\u0022,\u0022value\u0022:\u0022152\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Jacobs-Auer\u0022,\u0022value\u0022:\u0022208\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Jacobs, Turner and Abbott\u0022,\u0022value\u0022:\u0022278\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Jenkins-Bartell\u0022,\u0022value\u0022:\u0022272\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Johns-Pouros\u0022,\u0022value\u0022:\u0022109\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Johnson-Adams\u0022,\u0022value\u0022:\u0022369\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Jones PLC\u0022,\u0022value\u0022:\u0022399\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Jones-Langworth\u0022,\u0022value\u0022:\u0022146\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kassulke-Von\u0022,\u0022value\u0022:\u0022288\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kautzer, Carroll and Heathcote\u0022,\u0022value\u0022:\u002247\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kautzer, Langworth and Parisian\u0022,\u0022value\u0022:\u0022102\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Keebler, Schmeler and Kassulke\u0022,\u0022value\u0022:\u0022277\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kerluke PLC\u0022,\u0022value\u0022:\u002285\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kerluke, Rippin and Greenholt\u0022,\u0022value\u0022:\u002263\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kertzmann, Kertzmann and Hand\u0022,\u0022value\u0022:\u0022141\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kilback-Beer\u0022,\u0022value\u0022:\u0022334\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Klein, Ankunding and Morar\u0022,\u0022value\u0022:\u0022400\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Klein, Bergstrom and Morissette\u0022,\u0022value\u0022:\u0022349\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Klein, Jacobson and Ledner\u0022,\u0022value\u0022:\u002254\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Klein, King and Parisian\u0022,\u0022value\u0022:\u0022328\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kling Group\u0022,\u0022value\u0022:\u0022361\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Klocko and Sons\u0022,\u0022value\u0022:\u002236\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Konopelski and Sons\u0022,\u0022value\u0022:\u0022315\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Koss, Kirlin and Koss\u0022,\u0022value\u0022:\u0022390\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kovacek Inc\u0022,\u0022value\u0022:\u002224\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kozey, Williamson and McDermott\u0022,\u0022value\u0022:\u0022164\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Krajcik, Ankunding and Rohan\u0022,\u0022value\u0022:\u0022120\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kreiger LLC\u0022,\u0022value\u0022:\u002262\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kreiger-Hahn\u0022,\u0022value\u0022:\u0022110\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kub Ltd\u0022,\u0022value\u0022:\u0022130\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kub, Bode and Price\u0022,\u0022value\u0022:\u0022111\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kub, Kozey and Brown\u0022,\u0022value\u0022:\u0022398\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kuhic PLC\u0022,\u0022value\u0022:\u0022112\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kuhic, Abernathy and Armstrong\u0022,\u0022value\u0022:\u0022360\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kuhn, O\\u0027Kon and Ruecker\u0022,\u0022value\u0022:\u0022228\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kunde LLC\u0022,\u0022value\u0022:\u0022190\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kunze-Rippin\u0022,\u0022value\u0022:\u002235\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kuphal-Dickens\u0022,\u0022value\u0022:\u0022394\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kutch LLC\u0022,\u0022value\u0022:\u002288\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kutch-Turcotte\u0022,\u0022value\u0022:\u0022317\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kutch, Yost and Gaylord\u0022,\u0022value\u0022:\u0022313\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Kuvalis-Schulist\u0022,\u0022value\u0022:\u0022121\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lakin-Windler\u0022,\u0022value\u0022:\u0022319\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Langosh-Boehm\u0022,\u0022value\u0022:\u002296\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Langosh, Dach and Dibbert\u0022,\u0022value\u0022:\u0022397\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Langworth-Dicki\u0022,\u0022value\u0022:\u0022294\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Larkin-Jerde\u0022,\u0022value\u0022:\u0022126\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Larkin-Skiles\u0022,\u0022value\u0022:\u0022282\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Larkin, Fisher and Smitham\u0022,\u0022value\u0022:\u0022142\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Ledner-Hand\u0022,\u0022value\u0022:\u0022132\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Leffler, Robel and Kreiger\u0022,\u0022value\u0022:\u002258\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Leffler, Stroman and Volkman\u0022,\u0022value\u0022:\u002269\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Legros-Fadel\u0022,\u0022value\u0022:\u0022227\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lehner-Bahringer\u0022,\u0022value\u0022:\u0022136\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lehner, Gaylord and Hill\u0022,\u0022value\u0022:\u0022143\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lehner, O\\u0027Keefe and Bradtke\u0022,\u0022value\u0022:\u002282\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lemke-Parisian\u0022,\u0022value\u0022:\u0022201\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lesch, Schultz and Auer\u0022,\u0022value\u0022:\u0022330\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Leuschke LLC\u0022,\u0022value\u0022:\u0022123\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lind-Wintheiser\u0022,\u0022value\u0022:\u0022382\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lind, Adams and Marquardt\u0022,\u0022value\u0022:\u0022137\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lindgren, Terry and Grant\u0022,\u0022value\u0022:\u0022323\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Littel Inc\u0022,\u0022value\u0022:\u0022183\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Littel-Goodwin\u0022,\u0022value\u0022:\u0022345\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lowe, Carroll and Collins\u0022,\u0022value\u0022:\u0022332\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lueilwitz and Sons\u0022,\u0022value\u0022:\u00224\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lueilwitz-Rutherford\u0022,\u0022value\u0022:\u002222\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Luettgen Ltd\u0022,\u0022value\u0022:\u0022258\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Lynch-Sauer\u0022,\u0022value\u0022:\u0022101\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Macejkovic-Rutherford\u0022,\u0022value\u0022:\u0022395\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Marks, Halvorson and Aufderhar\u0022,\u0022value\u0022:\u0022131\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Marks, Orn and Howell\u0022,\u0022value\u0022:\u0022298\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Marquardt Group\u0022,\u0022value\u0022:\u0022157\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Marquardt-Hoppe\u0022,\u0022value\u0022:\u0022229\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Marvin PLC\u0022,\u0022value\u0022:\u0022393\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Marvin-Yost\u0022,\u0022value\u0022:\u0022353\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Mayer, Witting and Quigley\u0022,\u0022value\u0022:\u0022206\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022McLaughlin-Funk\u0022,\u0022value\u0022:\u0022289\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022McLaughlin-Gulgowski\u0022,\u0022value\u0022:\u0022188\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022McLaughlin-Klein\u0022,\u0022value\u0022:\u0022301\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022McLaughlin-O\\u0027Keefe\u0022,\u0022value\u0022:\u0022135\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022McLaughlin-Tremblay\u0022,\u0022value\u0022:\u002225\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Medhurst, Hermiston and Larson\u0022,\u0022value\u0022:\u0022322\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Metz Ltd\u0022,\u0022value\u0022:\u002237\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Metz, Langworth and Reilly\u0022,\u0022value\u0022:\u0022162\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Mills, Ankunding and Olson\u0022,\u0022value\u0022:\u0022326\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Mohr, Parker and Schumm\u0022,\u0022value\u0022:\u00223\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Moore-Jakubowski\u0022,\u0022value\u0022:\u0022374\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Moore, Beatty and Spencer\u0022,\u0022value\u0022:\u0022302\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Morar LLC\u0022,\u0022value\u0022:\u002242\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Mosciski and Sons\u0022,\u0022value\u0022:\u0022333\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Muller Group\u0022,\u0022value\u0022:\u0022388\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Muller, Haag and Breitenberg\u0022,\u0022value\u0022:\u0022316\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Murazik-Marquardt\u0022,\u0022value\u0022:\u002281\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Murazik, Abernathy and Hill\u0022,\u0022value\u0022:\u002293\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Murazik, Ward and Marvin\u0022,\u0022value\u0022:\u0022166\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Murray, DuBuque and Gorczany\u0022,\u0022value\u0022:\u002270\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Nader, Fisher and Rau\u0022,\u0022value\u0022:\u002253\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Nienow LLC\u0022,\u0022value\u0022:\u0022148\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Nienow-Wolf\u0022,\u0022value\u0022:\u0022247\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Nikolaus, Larson and Jenkins\u0022,\u0022value\u0022:\u0022280\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Nitzsche-Conn\u0022,\u0022value\u0022:\u00222\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Nolan and Sons\u0022,\u0022value\u0022:\u0022389\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Nolan Inc\u0022,\u0022value\u0022:\u0022286\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022O\\u0027Connell and Sons\u0022,\u0022value\u0022:\u0022105\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022O\\u0027Conner Group\u0022,\u0022value\u0022:\u0022235\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022O\\u0027Conner LLC\u0022,\u0022value\u0022:\u0022265\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022O\\u0027Hara-Conn\u0022,\u0022value\u0022:\u0022219\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022O\\u0027Hara, Marvin and Brakus\u0022,\u0022value\u0022:\u0022268\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022O\\u0027Keefe, Schiller and Ebert\u0022,\u0022value\u0022:\u0022297\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022O\\u0027Reilly LLC\u0022,\u0022value\u0022:\u0022174\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022O\\u0027Reilly PLC\u0022,\u0022value\u0022:\u002275\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Oberbrunner-Kerluke\u0022,\u0022value\u0022:\u0022311\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Oberbrunner, Jaskolski and Erdman\u0022,\u0022value\u0022:\u002291\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Olson Group\u0022,\u0022value\u0022:\u0022218\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Ondricka Inc\u0022,\u0022value\u0022:\u002271\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Ondricka-Schulist\u0022,\u0022value\u0022:\u002272\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Orn, Bogisich and Turcotte\u0022,\u0022value\u0022:\u0022220\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Osinski-Daniel\u0022,\u0022value\u0022:\u0022118\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Pacocha Group\u0022,\u0022value\u0022:\u002259\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Pacocha, Nikolaus and Mitchell\u0022,\u0022value\u0022:\u0022377\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Pagac-Okuneva\u0022,\u0022value\u0022:\u0022213\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Pagac, Green and Ratke\u0022,\u0022value\u0022:\u0022346\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Pfeffer PLC\u0022,\u0022value\u0022:\u0022233\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Pouros and Sons\u0022,\u0022value\u0022:\u0022273\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Pouros, Sanford and Hand\u0022,\u0022value\u0022:\u002286\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Powlowski-Fadel\u0022,\u0022value\u0022:\u0022325\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Predovic Inc\u0022,\u0022value\u0022:\u002240\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Price, Bergnaum and Jenkins\u0022,\u0022value\u0022:\u0022264\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Prosacco and Sons\u0022,\u0022value\u0022:\u002241\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Purdy-Lakin\u0022,\u0022value\u0022:\u0022358\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Quitzon, Johns and Abshire\u0022,\u0022value\u0022:\u0022261\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Ratke-Auer\u0022,\u0022value\u0022:\u0022352\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Ratke-Goyette\u0022,\u0022value\u0022:\u0022165\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Rau-Dooley\u0022,\u0022value\u0022:\u0022253\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Rau, Baumbach and Upton\u0022,\u0022value\u0022:\u002234\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Reichert-O\\u0027Keefe\u0022,\u0022value\u0022:\u0022214\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Reichert-Walker\u0022,\u0022value\u0022:\u0022385\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Reichert, Romaguera and Kulas\u0022,\u0022value\u0022:\u0022209\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Reilly PLC\u0022,\u0022value\u0022:\u0022251\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Rempel Ltd\u0022,\u0022value\u0022:\u0022113\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Rempel-Prohaska\u0022,\u0022value\u0022:\u0022305\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Renner Ltd\u0022,\u0022value\u0022:\u0022217\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Rice, Willms and Bradtke\u0022,\u0022value\u0022:\u0022194\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Roberts Inc\u0022,\u0022value\u0022:\u0022193\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Rolfson-Langworth\u0022,\u0022value\u0022:\u0022181\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Romaguera-Jast\u0022,\u0022value\u0022:\u0022107\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Runolfsdottir-O\\u0027Conner\u0022,\u0022value\u0022:\u002246\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Runolfsdottir-Wilkinson\u0022,\u0022value\u0022:\u0022341\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Ryan PLC\u0022,\u0022value\u0022:\u002244\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Satterfield Ltd\u0022,\u0022value\u0022:\u0022373\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Sauer-Rath\u0022,\u0022value\u0022:\u0022226\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Sawayn LLC\u0022,\u0022value\u0022:\u002232\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Sawayn-Jacobson\u0022,\u0022value\u0022:\u0022291\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Sawayn-Medhurst\u0022,\u0022value\u0022:\u0022230\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Sawayn, Anderson and Hackett\u0022,\u0022value\u0022:\u0022237\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schaden-Kautzer\u0022,\u0022value\u0022:\u0022274\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schamberger Inc\u0022,\u0022value\u0022:\u0022103\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schamberger LLC\u0022,\u0022value\u0022:\u0022192\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schamberger, Zulauf and Corwin\u0022,\u0022value\u0022:\u0022250\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schiller, Kessler and Walker\u0022,\u0022value\u0022:\u0022329\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schimmel PLC\u0022,\u0022value\u0022:\u002231\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schmidt-Christiansen\u0022,\u0022value\u0022:\u002229\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schmidt-Schulist\u0022,\u0022value\u0022:\u0022365\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schmidt, Ullrich and Torphy\u0022,\u0022value\u0022:\u0022144\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schmitt-Kreiger\u0022,\u0022value\u0022:\u002216\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schroeder Ltd\u0022,\u0022value\u0022:\u0022153\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schroeder, Parisian and Batz\u0022,\u0022value\u0022:\u0022203\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schulist-Schumm\u0022,\u0022value\u0022:\u0022160\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schultz, Gleason and Doyle\u0022,\u0022value\u0022:\u0022287\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Schumm LLC\u0022,\u0022value\u0022:\u0022225\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Senger Inc\u0022,\u0022value\u0022:\u0022270\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Shanahan, Bechtelar and Rogahn\u0022,\u0022value\u0022:\u0022161\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Simonis, Raynor and Kuvalis\u0022,\u0022value\u0022:\u0022375\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Skiles-Pfannerstill\u0022,\u0022value\u0022:\u002295\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Smitham, Schaefer and Lindgren\u0022,\u0022value\u0022:\u0022205\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Spencer-Nicolas\u0022,\u0022value\u0022:\u0022276\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Spinka LLC\u0022,\u0022value\u0022:\u0022242\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Spinka-O\\u0027Keefe\u0022,\u0022value\u0022:\u0022244\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Sporer-Sauer\u0022,\u0022value\u0022:\u0022293\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Sporer, Keeling and Carter\u0022,\u0022value\u0022:\u0022337\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Stanton-Considine\u0022,\u0022value\u0022:\u0022145\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Stehr and Sons\u0022,\u0022value\u0022:\u00229\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Stiedemann, Feest and Kunde\u0022,\u0022value\u0022:\u002292\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Stokes and Sons\u0022,\u0022value\u0022:\u002252\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Stoltenberg, Kassulke and DuBuque\u0022,\u0022value\u0022:\u0022259\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Streich, Jenkins and Cormier\u0022,\u0022value\u0022:\u0022359\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Stroman PLC\u0022,\u0022value\u0022:\u0022169\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Strosin-Lindgren\u0022,\u0022value\u0022:\u0022179\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Swift Inc\u0022,\u0022value\u0022:\u0022368\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Swift PLC\u0022,\u0022value\u0022:\u0022212\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Swift-Von\u0022,\u0022value\u0022:\u0022269\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Swift, Dickinson and Kovacek\u0022,\u0022value\u0022:\u0022290\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Terry, Feest and Trantow\u0022,\u0022value\u0022:\u0022344\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Thiel, Quigley and Emmerich\u0022,\u0022value\u0022:\u0022356\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Thompson-Bechtelar\u0022,\u0022value\u0022:\u002251\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Tillman, Hessel and Zulauf\u0022,\u0022value\u0022:\u0022189\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Torp, Schmitt and Wilderman\u0022,\u0022value\u0022:\u0022195\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Toy Ltd\u0022,\u0022value\u0022:\u0022246\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Toy-Fritsch\u0022,\u0022value\u0022:\u0022281\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Trantow, Carter and Grimes\u0022,\u0022value\u0022:\u0022303\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Treutel-Miller\u0022,\u0022value\u0022:\u0022159\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Tromp, Schumm and Welch\u0022,\u0022value\u0022:\u002220\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Turcotte Inc\u0022,\u0022value\u0022:\u002250\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Turner Inc\u0022,\u0022value\u0022:\u0022191\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Ullrich Inc\u0022,\u0022value\u0022:\u0022240\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Ullrich, Mante and Hill\u0022,\u0022value\u0022:\u002276\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Volkman-Hand\u0022,\u0022value\u0022:\u0022232\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Volkman, Bogan and Robel\u0022,\u0022value\u0022:\u0022318\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Von, Terry and Goldner\u0022,\u0022value\u0022:\u00225\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022VonRueden Inc\u0022,\u0022value\u0022:\u002274\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022VonRueden, Beer and Hahn\u0022,\u0022value\u0022:\u0022178\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Waelchi Inc\u0022,\u0022value\u0022:\u0022204\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Walsh-Dickens\u0022,\u0022value\u0022:\u002265\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Walsh-Hammes\u0022,\u0022value\u0022:\u0022138\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Walter PLC\u0022,\u0022value\u0022:\u0022372\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Waters PLC\u0022,\u0022value\u0022:\u002243\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Waters-Jacobson\u0022,\u0022value\u0022:\u0022224\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wehner-Lowe\u0022,\u0022value\u0022:\u0022366\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wehner, Hill and Hermann\u0022,\u0022value\u0022:\u0022350\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Weimann, Bode and Larson\u0022,\u0022value\u0022:\u0022364\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Weimann, Pouros and Dibbert\u0022,\u0022value\u0022:\u0022149\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Weissnat and Sons\u0022,\u0022value\u0022:\u0022260\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Welch, Stokes and Sauer\u0022,\u0022value\u0022:\u0022170\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022West-Turner\u0022,\u0022value\u0022:\u0022151\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022West-Wehner\u0022,\u0022value\u0022:\u002268\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wilkinson Group\u0022,\u0022value\u0022:\u00227\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wilkinson-Kuvalis\u0022,\u0022value\u0022:\u0022292\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Will, Weimann and Ziemann\u0022,\u0022value\u0022:\u0022150\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Willms-Stiedemann\u0022,\u0022value\u0022:\u002255\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wisoky Inc\u0022,\u0022value\u0022:\u002219\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wisozk, Koss and Nikolaus\u0022,\u0022value\u0022:\u0022234\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wisozk, Russel and Daugherty\u0022,\u0022value\u0022:\u0022380\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Witting, Kris and Rice\u0022,\u0022value\u0022:\u0022367\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wolf, Gusikowski and McCullough\u0022,\u0022value\u0022:\u0022340\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wunsch, Hagenes and Moen\u0022,\u0022value\u0022:\u0022241\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wyman and Sons\u0022,\u0022value\u0022:\u002230\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Wyman-O\\u0027Keefe\u0022,\u0022value\u0022:\u002297\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Yost PLC\u0022,\u0022value\u0022:\u0022327\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Zboncak LLC\u0022,\u0022value\u0022:\u0022117\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Zemlak Inc\u0022,\u0022value\u0022:\u0022285\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Zemlak, Wolf and Witting\u0022,\u0022value\u0022:\u002277\u0022,\u0022disabled\u0022:false}]'),
                            optionsLimit: 50,
                            placeholder: 'All',
                            position: null,
                            searchDebounce: 1000,
                            searchingMessage: 'Searching...',
                            searchPrompt: 'Start typing to search...',
                            searchableOptionFields: JSON.parse('[\u0022label\u0022]'),
                            state: $wire.$entangle('tableFilters.brand.values', true),
                            statePath: 'tableFilters.brand.values',
                        })"
                                        wire:ignore=""
                                        x-on:keydown.esc="select.dropdown.isActive &amp;&amp; $event.stopPropagation()"
                                      >
                                        <div
                                          class="choices"
                                          data-type="select-multiple"
                                          role="combobox"
                                          aria-autocomplete="list"
                                          aria-haspopup="true"
                                          aria-expanded="false"
                                        >
                                          <div class="choices__inner">
                                            <select
                                              x-ref="input"
                                              id="tableFilters.brand.values"
                                              multiple="multiple"
                                              class="choices__input"
                                              hidden=""
                                              tabindex="-1"
                                              data-choice="active"
                                            ></select>
                                            <div
                                              class="choices__list choices__list--multiple"
                                            ></div>
                                            <input
                                              type="search"
                                              name="search_terms"
                                              class="choices__input choices__input--cloned"
                                              autocomplete="off"
                                              autocapitalize="off"
                                              spellcheck="false"
                                              role="textbox"
                                              aria-autocomplete="list"
                                              aria-label="All"
                                              placeholder="All"
                                              style="min-width: 4ch; width: 1ch"
                                            />
                                          </div>
                                          <div
                                            class="choices__list choices__list--dropdown"
                                            aria-expanded="false"
                                          >
                                            <div
                                              class="choices__list"
                                              aria-multiselectable="true"
                                              role="listbox"
                                            >
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-1"
                                                class="choices__item choices__item--choice choices__item--selectable is-highlighted"
                                                role="option"
                                                data-choice=""
                                                data-id="1"
                                                data-value="308"
                                                data-select-text=""
                                                data-choice-selectable=""
                                                aria-selected="true"
                                              >
                                                Abshire-Hahn
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-2"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="2"
                                                data-value="236"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Ankunding-Daniel
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-3"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="3"
                                                data-value="28"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Auer LLC
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-4"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="4"
                                                data-value="370"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bailey-Wyman
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-5"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="5"
                                                data-value="98"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Balistreri, Lind and Bosco
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-6"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="6"
                                                data-value="309"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Barrows and Sons
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-7"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="7"
                                                data-value="155"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Barrows, Waelchi and Bartell
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-8"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="8"
                                                data-value="45"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bartoletti-Rutherford
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-9"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="9"
                                                data-value="376"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bartoletti, Cummerata and Prosacco
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-10"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="10"
                                                data-value="156"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Batz, Lang and Grady
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-11"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="11"
                                                data-value="396"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Batz, Mosciski and Mann
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-12"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="12"
                                                data-value="39"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bauch-Hickle
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-13"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="13"
                                                data-value="256"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Beahan PLC
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-14"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="14"
                                                data-value="296"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Beahan-Luettgen
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-15"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="15"
                                                data-value="351"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Beatty-Bauch
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-16"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="16"
                                                data-value="180"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Becker-Koch
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-17"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="17"
                                                data-value="6"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bednar, Kuphal and Little
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-18"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="18"
                                                data-value="306"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bednar, Streich and Keebler
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-19"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="19"
                                                data-value="108"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Beer Group
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-20"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="20"
                                                data-value="119"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Beier-Kertzmann
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-21"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="21"
                                                data-value="100"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bergnaum PLC
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-22"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="22"
                                                data-value="87"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bergnaum-Breitenberg
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-23"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="23"
                                                data-value="99"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bernhard-Leffler
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-24"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="24"
                                                data-value="331"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bernhard, Rohan and Jakubowski
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-25"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="25"
                                                data-value="379"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bernier-Kemmer
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-26"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="26"
                                                data-value="362"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bernier-Mraz
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-27"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="27"
                                                data-value="275"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bins, Langworth and Schneider
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-28"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="28"
                                                data-value="13"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bins, Zulauf and Rowe
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-29"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="29"
                                                data-value="299"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Block-Kutch
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-30"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="30"
                                                data-value="57"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bode-Kilback
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-31"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="31"
                                                data-value="94"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bode-Lehner
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-32"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="32"
                                                data-value="163"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bode-Sanford
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-33"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="33"
                                                data-value="196"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bogan Group
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-34"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="34"
                                                data-value="90"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bosco, Grady and Jast
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-35"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="35"
                                                data-value="255"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Boyer and Sons
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-36"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="36"
                                                data-value="79"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Bradtke-Miller
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-37"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="37"
                                                data-value="158"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Braun Inc
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-38"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="38"
                                                data-value="23"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Braun, Buckridge and Tremblay
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-39"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="39"
                                                data-value="312"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Breitenberg-Nolan
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-40"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="40"
                                                data-value="127"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Brekke-Howe
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-41"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="41"
                                                data-value="283"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Cassin, Hintz and Carroll
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-42"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="42"
                                                data-value="215"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Cassin, Prosacco and Predovic
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-43"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="43"
                                                data-value="239"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Champlin Inc
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-44"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="44"
                                                data-value="186"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Champlin-Harvey
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-45"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="45"
                                                data-value="207"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Cole and Sons
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-46"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="46"
                                                data-value="336"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Collier Inc
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-47"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="47"
                                                data-value="12"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Collins Ltd
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-48"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="48"
                                                data-value="252"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Collins-Balistreri
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-49"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="49"
                                                data-value="197"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Collins, Bauch and Treutel
                                              </div>
                                              <div
                                                id="choices--tableFiltersbrandvalues-item-choice-50"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="50"
                                                data-value="314"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Conn LLC
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </div>
                                      <!-- __ENDBLOCK__ -->
                                    </div>

                                    <!-- __BLOCK__ -->
                                    <!-- __ENDBLOCK__ -->
                                  </div>

                                  <!-- __BLOCK__ -->
                                  <!-- __ENDBLOCK__ -->

                                  <!-- __BLOCK__ -->
                                  <!-- __ENDBLOCK__ -->
                                </div>
                                <!-- __ENDBLOCK__ -->
                              </div>
                            </div>

                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->
                        </div>
                      </div>

                      <!-- __ENDBLOCK__ -->
                    </div>

                    <div
                      style="--col-span-default: span 1 / span 1"
                      class="col-[--col-span-default]"
                    >
                      <!-- __BLOCK__ -->
                      <div>
                        <div
                          style="--cols-default: repeat(1, minmax(0, 1fr))"
                          class="grid grid-cols-[--cols-default] fi-fo-component-ctn gap-6"
                        >
                          <!-- __BLOCK__ -->
                          <div
                            style="--col-span-default: span 1 / span 1"
                            class="col-[--col-span-default]"
                            wire:key="YDjdrqMZkmrJTuGzMaXn.tableFilters.is_visible.value.Filament\Forms\Components\Select"
                          >
                            <!-- __BLOCK__ -->
                            <div class="fi-fo-field-wrp">
                              <!-- __BLOCK__ -->
                              <!-- __ENDBLOCK__ -->

                              <div class="grid gap-y-2">
                                <!-- __BLOCK__ -->
                                <div class="flex items-center justify-between gap-x-3">
                                  <!-- __BLOCK__ -->
                                  <label
                                    class="fi-fo-field-wrp-label inline-flex items-center gap-x-3"
                                    for="tableFilters.is_visible.value"
                                  >
                                    <span
                                      class="text-sm font-medium leading-6 text-gray-950 dark:text-white"
                                    >
                                      Visibility<!-- __BLOCK__ -->
                                      <!-- __ENDBLOCK__ -->
                                    </span>
                                  </label>
                                  <!-- __ENDBLOCK__ -->

                                  <!-- __BLOCK__ -->
                                  <!-- __ENDBLOCK__ -->
                                </div>
                                <!-- __ENDBLOCK__ -->

                                <!-- __BLOCK__ -->
                                <div class="grid gap-y-2">
                                  <div
                                    class="fi-input-wrp flex rounded-lg shadow-sm ring-1 transition duration-75 bg-white focus-within:ring-2 dark:bg-white/5 ring-gray-950/10 focus-within:ring-primary-600 dark:ring-white/20 dark:focus-within:ring-primary-500 fi-fo-select"
                                  >
                                    <!-- __BLOCK__ -->
                                    <!-- __ENDBLOCK__ -->

                                    <div class="min-w-0 flex-1">
                                      <!-- __BLOCK__ -->
                                      <div
                                        ax-load=""
                                        ax-load-src="https://demo.filamentphp.com/js/filament/forms/components/select.js?v=3.0.60.0"
                                        x-data="selectFormComponent({
                            canSelectPlaceholder: true,
                            isHtmlAllowed: false,
                            getOptionLabelUsing: async () => {
                                return await $wire.getFormSelectOptionLabel('tableFilters.is_visible.value')
                            },
                            getOptionLabelsUsing: async () => {
                                return await $wire.getFormSelectOptionLabels('tableFilters.is_visible.value')
                            },
                            getOptionsUsing: async () => {
                                return await $wire.getFormSelectOptions('tableFilters.is_visible.value')
                            },
                            getSearchResultsUsing: async (search) => {
                                return await $wire.getFormSelectSearchResults('tableFilters.is_visible.value', search)
                            },
                            isAutofocused: false,
                            isMultiple: false,
                            isSearchable: false,
                            livewireId: 'YDjdrqMZkmrJTuGzMaXn',
                            hasDynamicOptions: false,
                            hasDynamicSearchResults: false,
                            loadingMessage: 'Loading...',
                            maxItems: null,
                            maxItemsMessage: 'Only  can be selected.',
                            noSearchResultsMessage: 'No options match your search.',
                            options: JSON.parse('[{\u0022label\u0022:\u0022Only visible\u0022,\u0022value\u0022:\u00221\u0022,\u0022disabled\u0022:false},{\u0022label\u0022:\u0022Only hidden\u0022,\u0022value\u0022:\u00220\u0022,\u0022disabled\u0022:false}]'),
                            optionsLimit: 50,
                            placeholder: '-',
                            position: null,
                            searchDebounce: 1000,
                            searchingMessage: 'Searching...',
                            searchPrompt: 'Start typing to search...',
                            searchableOptionFields: JSON.parse('[\u0022label\u0022]'),
                            state: $wire.$entangle('tableFilters.is_visible.value', true),
                            statePath: 'tableFilters.is_visible.value',
                        })"
                                        wire:ignore=""
                                        x-on:keydown.esc="select.dropdown.isActive &amp;&amp; $event.stopPropagation()"
                                      >
                                        <div
                                          class="choices"
                                          data-type="select-one"
                                          tabindex="0"
                                          role="listbox"
                                          aria-haspopup="true"
                                          aria-expanded="false"
                                        >
                                          <div class="choices__inner">
                                            <select
                                              x-ref="input"
                                              id="tableFilters.is_visible.value"
                                              class="choices__input"
                                              hidden=""
                                              tabindex="-1"
                                              data-choice="active"
                                            ></select>
                                            <div class="choices__list choices__list--single">
                                              <div class="choices__placeholder choices__item">
                                                -
                                              </div>
                                            </div>
                                          </div>
                                          <div
                                            class="choices__list choices__list--dropdown"
                                            aria-expanded="false"
                                          >
                                            <div class="choices__list" role="listbox">
                                              <div
                                                id="choices--tableFiltersis_visiblevalue-item-choice-1"
                                                class="choices__item choices__item--choice choices__item--selectable is-highlighted"
                                                role="option"
                                                data-choice=""
                                                data-id="1"
                                                data-value="1"
                                                data-select-text=""
                                                data-choice-selectable=""
                                                aria-selected="true"
                                              >
                                                Only visible
                                              </div>
                                              <div
                                                id="choices--tableFiltersis_visiblevalue-item-choice-2"
                                                class="choices__item choices__item--choice choices__item--selectable"
                                                role="option"
                                                data-choice=""
                                                data-id="2"
                                                data-value="0"
                                                data-select-text=""
                                                data-choice-selectable=""
                                              >
                                                Only hidden
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </div>
                                      <!-- __ENDBLOCK__ -->
                                    </div>

                                    <!-- __BLOCK__ -->
                                    <!-- __ENDBLOCK__ -->
                                  </div>

                                  <!-- __BLOCK__ -->
                                  <!-- __ENDBLOCK__ -->

                                  <!-- __BLOCK__ -->
                                  <!-- __ENDBLOCK__ -->
                                </div>
                                <!-- __ENDBLOCK__ -->
                              </div>
                            </div>

                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->
                        </div>
                      </div>

                      <!-- __ENDBLOCK__ -->
                    </div>
                    <!-- __ENDBLOCK__ -->
                  </div>
                </div>
              </div>
            </div>
            <!-- __ENDBLOCK__ -->

            <!-- __BLOCK__ -->
            <div
              x-data="{
        toggle: function (event) {
            $refs.panel.toggle(event)
        },

        open: function (event) {
            $refs.panel.open(event)
        },

        close: function (event) {
            $refs.panel.close(event)
        },
    }"
              class="fi-dropdown fi-ta-col-toggle"
              wire:key="YDjdrqMZkmrJTuGzMaXn.table.column-toggle"
            >
              <div x-on:click="toggle" class="fi-dropdown-trigger flex cursor-pointer">
                <span class="inline-flex -mx-2">
                  <!-- __BLOCK__ -->
                  <button
                    style="
                      --c-300: var(--gray-300);
                      --c-400: var(--gray-400);
                      --c-500: var(--gray-500);
                      --c-600: var(--gray-600);
                    "
                    class="fi-icon-btn relative flex items-center justify-center rounded-lg outline-none transition duration-75 focus:ring-2 disabled:pointer-events-none disabled:opacity-70 h-9 w-9 text-gray-400 hover:text-gray-500 focus:ring-primary-600 dark:text-gray-500 dark:hover:text-gray-400 dark:focus:ring-primary-500 fi-ac-icon-btn-action"
                    title="Toggle columns"
                    type="button"
                  >
                    <!-- __BLOCK__ -->
                    <span class="sr-only"> Toggle columns </span>
                    <!-- __ENDBLOCK__ -->

                    <!-- __BLOCK__ -->
                    <svg
                      class="fi-icon-btn-icon h-5 w-5"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      aria-hidden="true"
                    >
                      <path
                        d="M14 17h2.75A2.25 2.25 0 0019 14.75v-9.5A2.25 2.25 0 0016.75 3H14v14zM12.5 3h-5v14h5V3zM3.25 3H6v14H3.25A2.25 2.25 0 011 14.75v-9.5A2.25 2.25 0 013.25 3z"
                      ></path>
                    </svg>
                    <!-- __ENDBLOCK__ -->

                    <!-- __BLOCK__ -->
                    <!-- __ENDBLOCK__ -->

                    <!-- __BLOCK__ -->
                    <!-- __ENDBLOCK__ -->
                  </button>
                  <!-- __ENDBLOCK__ -->
                </span>
              </div>

              <div
                x-float.placement.bottom-end.flip.shift.offset="{ offset: 8 }"
                x-ref="panel"
                x-transition:enter-start="opacity-0"
                x-transition:leave-end="opacity-0"
                wire:ignore.self=""
                wire:key="YDjdrqMZkmrJTuGzMaXn.table.column-toggle.panel"
                class="fi-dropdown-panel absolute z-10 w-screen divide-y divide-gray-100 rounded-lg bg-white shadow-lg ring-1 ring-gray-950/5 transition dark:divide-white/5 dark:bg-gray-900 dark:ring-white/10 max-w-xs"
                style="display: none"
              >
                <div class="grid gap-y-4 p-6">
                  <h4 class="text-base font-semibold leading-6 text-gray-950 dark:text-white">
                    Columns
                  </h4>

                  <div
                    style="
                      --cols-default: repeat(1, minmax(0, 1fr));
                      --cols-lg: repeat(1, minmax(0, 1fr));
                    "
                    class="grid grid-cols-[--cols-default] lg:grid-cols-[--cols-lg] fi-fo-component-ctn gap-6"
                  >
                    <!-- __BLOCK__ -->
                    <div
                      style="--col-span-default: span 1 / span 1"
                      class="col-[--col-span-default]"
                      wire:key="YDjdrqMZkmrJTuGzMaXn.toggledTableColumns.brand.name.Filament\Forms\Components\Checkbox"
                    >
                      <!-- __BLOCK__ -->
                      <div class="fi-fo-field-wrp">
                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <div class="grid gap-y-2">
                          <!-- __BLOCK__ -->
                          <div class="flex items-center justify-between gap-x-3">
                            <!-- __BLOCK__ -->
                            <label
                              class="fi-fo-field-wrp-label inline-flex items-center gap-x-3"
                              for="toggledTableColumns.brand.name"
                            >
                              <input
                                type="checkbox"
                                class="fi-checkbox-input rounded border-none bg-white shadow-sm ring-1 transition duration-75 checked:ring-0 focus:ring-2 focus:ring-offset-0 disabled:pointer-events-none disabled:bg-gray-50 disabled:text-gray-50 disabled:checked:bg-current disabled:checked:text-gray-400 dark:bg-white/5 dark:disabled:bg-transparent dark:disabled:checked:bg-gray-600 text-primary-600 ring-gray-950/10 focus:ring-primary-600 checked:focus:ring-primary-500/50 dark:ring-white/20 dark:checked:bg-primary-500 dark:focus:ring-primary-500 dark:checked:focus:ring-primary-400/50 dark:disabled:ring-white/10"
                                id="toggledTableColumns.brand.name"
                                wire:loading.attr="disabled"
                                wire:model.live="toggledTableColumns.brand.name"
                              />

                              <span
                                class="text-sm font-medium leading-6 text-gray-950 dark:text-white"
                              >
                                Brand<!-- __BLOCK__ -->
                                <!-- __ENDBLOCK__ -->
                              </span>
                            </label>
                            <!-- __ENDBLOCK__ -->

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->

                          <!-- __BLOCK__ -->
                          <!-- __ENDBLOCK__ -->
                        </div>
                      </div>

                      <!-- __ENDBLOCK__ -->
                    </div>

                    <div
                      style="--col-span-default: span 1 / span 1"
                      class="col-[--col-span-default]"
                      wire:key="YDjdrqMZkmrJTuGzMaXn.toggledTableColumns.is_visible.Filament\Forms\Components\Checkbox"
                    >
                      <!-- __BLOCK__ -->
                      <div class="fi-fo-field-wrp">
                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <div class="grid gap-y-2">
                          <!-- __BLOCK__ -->
                          <div class="flex items-center justify-between gap-x-3">
                            <!-- __BLOCK__ -->
                            <label
                              class="fi-fo-field-wrp-label inline-flex items-center gap-x-3"
                              for="toggledTableColumns.is_visible"
                            >
                              <input
                                type="checkbox"
                                class="fi-checkbox-input rounded border-none bg-white shadow-sm ring-1 transition duration-75 checked:ring-0 focus:ring-2 focus:ring-offset-0 disabled:pointer-events-none disabled:bg-gray-50 disabled:text-gray-50 disabled:checked:bg-current disabled:checked:text-gray-400 dark:bg-white/5 dark:disabled:bg-transparent dark:disabled:checked:bg-gray-600 text-primary-600 ring-gray-950/10 focus:ring-primary-600 checked:focus:ring-primary-500/50 dark:ring-white/20 dark:checked:bg-primary-500 dark:focus:ring-primary-500 dark:checked:focus:ring-primary-400/50 dark:disabled:ring-white/10"
                                id="toggledTableColumns.is_visible"
                                wire:loading.attr="disabled"
                                wire:model.live="toggledTableColumns.is_visible"
                              />

                              <span
                                class="text-sm font-medium leading-6 text-gray-950 dark:text-white"
                              >
                                Visibility<!-- __BLOCK__ -->
                                <!-- __ENDBLOCK__ -->
                              </span>
                            </label>
                            <!-- __ENDBLOCK__ -->

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->

                          <!-- __BLOCK__ -->
                          <!-- __ENDBLOCK__ -->
                        </div>
                      </div>

                      <!-- __ENDBLOCK__ -->
                    </div>

                    <div
                      style="--col-span-default: span 1 / span 1"
                      class="col-[--col-span-default]"
                      wire:key="YDjdrqMZkmrJTuGzMaXn.toggledTableColumns.sku.Filament\Forms\Components\Checkbox"
                    >
                      <!-- __BLOCK__ -->
                      <div class="fi-fo-field-wrp">
                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <div class="grid gap-y-2">
                          <!-- __BLOCK__ -->
                          <div class="flex items-center justify-between gap-x-3">
                            <!-- __BLOCK__ -->
                            <label
                              class="fi-fo-field-wrp-label inline-flex items-center gap-x-3"
                              for="toggledTableColumns.sku"
                            >
                              <input
                                type="checkbox"
                                class="fi-checkbox-input rounded border-none bg-white shadow-sm ring-1 transition duration-75 checked:ring-0 focus:ring-2 focus:ring-offset-0 disabled:pointer-events-none disabled:bg-gray-50 disabled:text-gray-50 disabled:checked:bg-current disabled:checked:text-gray-400 dark:bg-white/5 dark:disabled:bg-transparent dark:disabled:checked:bg-gray-600 text-primary-600 ring-gray-950/10 focus:ring-primary-600 checked:focus:ring-primary-500/50 dark:ring-white/20 dark:checked:bg-primary-500 dark:focus:ring-primary-500 dark:checked:focus:ring-primary-400/50 dark:disabled:ring-white/10"
                                id="toggledTableColumns.sku"
                                wire:loading.attr="disabled"
                                wire:model.live="toggledTableColumns.sku"
                              />

                              <span
                                class="text-sm font-medium leading-6 text-gray-950 dark:text-white"
                              >
                                SKU<!-- __BLOCK__ -->
                                <!-- __ENDBLOCK__ -->
                              </span>
                            </label>
                            <!-- __ENDBLOCK__ -->

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->

                          <!-- __BLOCK__ -->
                          <!-- __ENDBLOCK__ -->
                        </div>
                      </div>
                    </div>

                    <div
                      style="--col-span-default: span 1 / span 1"
                      class="col-[--col-span-default]"
                      wire:key="YDjdrqMZkmrJTuGzMaXn.toggledTableColumns.qty.Filament\Forms\Components\Checkbox"
                    >
                      <!-- __BLOCK__ -->
                      <div class="fi-fo-field-wrp">
                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <div class="grid gap-y-2">
                          <!-- __BLOCK__ -->
                          <div class="flex items-center justify-between gap-x-3">
                            <!-- __BLOCK__ -->
                            <label
                              class="fi-fo-field-wrp-label inline-flex items-center gap-x-3"
                              for="toggledTableColumns.qty"
                            >
                              <input
                                type="checkbox"
                                class="fi-checkbox-input rounded border-none bg-white shadow-sm ring-1 transition duration-75 checked:ring-0 focus:ring-2 focus:ring-offset-0 disabled:pointer-events-none disabled:bg-gray-50 disabled:text-gray-50 disabled:checked:bg-current disabled:checked:text-gray-400 dark:bg-white/5 dark:disabled:bg-transparent dark:disabled:checked:bg-gray-600 text-primary-600 ring-gray-950/10 focus:ring-primary-600 checked:focus:ring-primary-500/50 dark:ring-white/20 dark:checked:bg-primary-500 dark:focus:ring-primary-500 dark:checked:focus:ring-primary-400/50 dark:disabled:ring-white/10"
                                id="toggledTableColumns.qty"
                                wire:loading.attr="disabled"
                                wire:model.live="toggledTableColumns.qty"
                              />

                              <span
                                class="text-sm font-medium leading-6 text-gray-950 dark:text-white"
                              >
                                Quantity<!-- __BLOCK__ -->
                                <!-- __ENDBLOCK__ -->
                              </span>
                            </label>
                            <!-- __ENDBLOCK__ -->

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->

                          <!-- __BLOCK__ -->
                          <!-- __ENDBLOCK__ -->
                        </div>
                      </div>

                      <!-- __ENDBLOCK__ -->
                    </div>

                    <div
                      style="--col-span-default: span 1 / span 1"
                      class="col-[--col-span-default]"
                      wire:key="YDjdrqMZkmrJTuGzMaXn.toggledTableColumns.security_stock.Filament\Forms\Components\Checkbox"
                    >
                      <!-- __BLOCK__ -->
                      <div class="fi-fo-field-wrp">
                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <div class="grid gap-y-2">
                          <!-- __BLOCK__ -->
                          <div class="flex items-center justify-between gap-x-3">
                            <!-- __BLOCK__ -->
                            <label
                              class="fi-fo-field-wrp-label inline-flex items-center gap-x-3"
                              for="toggledTableColumns.security_stock"
                            >
                              <input
                                type="checkbox"
                                class="fi-checkbox-input rounded border-none bg-white shadow-sm ring-1 transition duration-75 checked:ring-0 focus:ring-2 focus:ring-offset-0 disabled:pointer-events-none disabled:bg-gray-50 disabled:text-gray-50 disabled:checked:bg-current disabled:checked:text-gray-400 dark:bg-white/5 dark:disabled:bg-transparent dark:disabled:checked:bg-gray-600 text-primary-600 ring-gray-950/10 focus:ring-primary-600 checked:focus:ring-primary-500/50 dark:ring-white/20 dark:checked:bg-primary-500 dark:focus:ring-primary-500 dark:checked:focus:ring-primary-400/50 dark:disabled:ring-white/10"
                                id="toggledTableColumns.security_stock"
                                wire:loading.attr="disabled"
                                wire:model.live="toggledTableColumns.security_stock"
                              />

                              <span
                                class="text-sm font-medium leading-6 text-gray-950 dark:text-white"
                              >
                                Security stock<!-- __BLOCK__ -->
                                <!-- __ENDBLOCK__ -->
                              </span>
                            </label>
                            <!-- __ENDBLOCK__ -->

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->

                          <!-- __BLOCK__ -->
                          <!-- __ENDBLOCK__ -->
                        </div>
                      </div>

                      <!-- __ENDBLOCK__ -->
                    </div>

                    <div
                      style="--col-span-default: span 1 / span 1"
                      class="col-[--col-span-default]"
                      wire:key="YDjdrqMZkmrJTuGzMaXn.toggledTableColumns.published_at.Filament\Forms\Components\Checkbox"
                    >
                      <!-- __BLOCK__ -->
                      <div class="fi-fo-field-wrp">
                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <div class="grid gap-y-2">
                          <!-- __BLOCK__ -->
                          <div class="flex items-center justify-between gap-x-3">
                            <!-- __BLOCK__ -->
                            <label
                              class="fi-fo-field-wrp-label inline-flex items-center gap-x-3"
                              for="toggledTableColumns.published_at"
                            >
                              <input
                                type="checkbox"
                                class="fi-checkbox-input rounded border-none bg-white shadow-sm ring-1 transition duration-75 checked:ring-0 focus:ring-2 focus:ring-offset-0 disabled:pointer-events-none disabled:bg-gray-50 disabled:text-gray-50 disabled:checked:bg-current disabled:checked:text-gray-400 dark:bg-white/5 dark:disabled:bg-transparent dark:disabled:checked:bg-gray-600 text-primary-600 ring-gray-950/10 focus:ring-primary-600 checked:focus:ring-primary-500/50 dark:ring-white/20 dark:checked:bg-primary-500 dark:focus:ring-primary-500 dark:checked:focus:ring-primary-400/50 dark:disabled:ring-white/10"
                                id="toggledTableColumns.published_at"
                                wire:loading.attr="disabled"
                                wire:model.live="toggledTableColumns.published_at"
                              />

                              <span
                                class="text-sm font-medium leading-6 text-gray-950 dark:text-white"
                              >
                                Publish Date<!-- __BLOCK__ -->
                                <!-- __ENDBLOCK__ -->
                              </span>
                            </label>
                            <!-- __ENDBLOCK__ -->

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->

                          <!-- __BLOCK__ -->
                          <!-- __ENDBLOCK__ -->
                        </div>
                      </div>

                      <!-- __ENDBLOCK__ -->
                    </div>
                    <!-- __ENDBLOCK__ -->
                  </div>
                </div>
              </div>
            </div>
            <!-- __ENDBLOCK__ -->

            <!-- __ENDBLOCK__ -->
          </div>
          <!-- __ENDBLOCK__ -->
        </div>
      </div>

      <!-- __BLOCK__ -->
      <div
        class="fi-ta-selection-indicator flex flex-col justify-between gap-y-1 bg-gray-50 px-3 py-2 dark:bg-white/5 sm:flex-row sm:items-center sm:px-6 sm:py-1.5"
        wire:key="YDjdrqMZkmrJTuGzMaXn.table.selection.indicator"
        colspan="9"
        x-bind:hidden="! selectedRecords.length"
        x-show="selectedRecords.length"
        hidden="hidden"
        style="display: none"
      >
        <div class="flex gap-x-3">
          <svg
            fill="none"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            class="animate-spin h-5 w-5 text-gray-400 dark:text-gray-500"
            x-show="isLoading"
            style="display: none"
          >
            <path
              clip-rule="evenodd"
              d="M12 19C15.866 19 19 15.866 19 12C19 8.13401 15.866 5 12 5C8.13401 5 5 8.13401 5 12C5 15.866 8.13401 19 12 19ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
              fill-rule="evenodd"
              fill="currentColor"
              opacity="0.2"
            ></path>
            <path
              d="M2 12C2 6.47715 6.47715 2 12 2V5C8.13401 5 5 8.13401 5 12H2Z"
              fill="currentColor"
            ></path>
          </svg>

          <span
            x-text="
                window.pluralize('1 record selected|:count records selected', selectedRecords.length, {
                    count: selectedRecords.length,
                })
            "
            class="text-sm font-medium leading-6 text-gray-700 dark:text-gray-200"
            >1 record selected</span
          >
        </div>

        <div class="flex gap-x-3">
          <!-- __BLOCK__ -->
          <button
            style="
              --c-300: var(--primary-300);
              --c-400: var(--primary-400);
              --c-500: var(--primary-500);
              --c-600: var(--primary-600);
            "
            class="fi-link fi-link-size-md relative inline-flex items-center justify-center font-semibold outline-none transition duration-75 hover:underline focus:underline gap-1.5 text-sm text-custom-600 dark:text-custom-400"
            type="button"
            wire:loading.attr="disabled"
            id="YDjdrqMZkmrJTuGzMaXn.table.selection.indicator.record-count.50"
            x-on:click="selectAllRecords"
            x-show="50 !== selectedRecords.length"
          >
            <!-- __BLOCK__ -->
            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->

            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->
            <!-- __ENDBLOCK__ -->

            Select all 50

            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->

            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->
          </button>
          <!-- __ENDBLOCK__ -->

          <!-- __BLOCK__ -->
          <button
            style="
              --c-300: var(--danger-300);
              --c-400: var(--danger-400);
              --c-500: var(--danger-500);
              --c-600: var(--danger-600);
            "
            class="fi-link fi-link-size-md relative inline-flex items-center justify-center font-semibold outline-none transition duration-75 hover:underline focus:underline gap-1.5 text-sm text-custom-600 dark:text-custom-400"
            type="button"
            wire:loading.attr="disabled"
            x-on:click="deselectAllRecords"
          >
            <!-- __BLOCK__ -->
            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->

            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->
            <!-- __ENDBLOCK__ -->

            Deselect all

            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->

            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->
          </button>
          <!-- __ENDBLOCK__ -->
        </div>
      </div>
      <!-- __ENDBLOCK__ -->

      <!-- __BLOCK__ -->
      <!-- __ENDBLOCK__ -->

      <div
        class="fi-ta-content relative divide-y divide-gray-200 overflow-x-auto dark:divide-white/10 dark:border-t-white/10"
      >
        <!-- __BLOCK__ -->
        <table
          class="fi-ta-table w-full table-auto divide-y divide-gray-200 text-start dark:divide-white/5"
        >
          <!-- __BLOCK__ -->
          <thead class="bg-gray-50 dark:bg-white/5">
            <tr>
              <!-- __BLOCK__ -->
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <th
                class="fi-ta-cell p-0 first-of-type:ps-1 last-of-type:pe-1 sm:first-of-type:ps-3 sm:last-of-type:pe-3 w-1"
              >
                <div class="px-3 py-4">
                  <label class="flex">
                    <input
                      type="checkbox"
                      class="fi-checkbox-input rounded border-none bg-white shadow-sm ring-1 transition duration-75 checked:ring-0 focus:ring-2 focus:ring-offset-0 disabled:pointer-events-none disabled:bg-gray-50 disabled:text-gray-50 disabled:checked:bg-current disabled:checked:text-gray-400 dark:bg-white/5 dark:disabled:bg-transparent dark:disabled:checked:bg-gray-600 text-primary-600 ring-gray-950/10 focus:ring-primary-600 checked:focus:ring-primary-500/50 dark:ring-white/20 dark:checked:bg-primary-500 dark:focus:ring-primary-500 dark:checked:focus:ring-primary-400/50 dark:disabled:ring-white/10"
                      wire:loading.attr="disabled"
                      wire:target="gotoPage,nextPage,previousPage,removeTableFilter,removeTableFilters,reorderTable,resetTableFiltersForm,sortTable,tableColumnSearches,tableFilters,tableRecordsPerPage,tableSearch"
                      x-bind:checked="const recordsOnPage = getRecordsOnPage()

                                            if (recordsOnPage.length &amp;&amp; areRecordsSelected(recordsOnPage)) {
                                                $el.checked = true

                                                return 'checked'
                                            }

                                            $el.checked = false

                                            return null"
                      x-on:click="toggleSelectRecordsOnPage"
                    />

                    <!-- __BLOCK__ -->
                    <span class="sr-only"> Select/deselect all items for bulk actions. </span>
                    <!-- __ENDBLOCK__ -->
                  </label>
                </div>
              </th>
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <th
                class="fi-ta-header-cell px-3 py-3.5 sm:first-of-type:ps-6 sm:last-of-type:pe-6 fi-table-header-cell-product-image"
              >
                <span class="group flex w-full items-center gap-x-1 whitespace-nowrap">
                  <!-- __BLOCK__ -->
                  <!-- __ENDBLOCK__ -->

                  <span class="text-sm font-semibold text-gray-950 dark:text-white"> Image </span>

                  <!-- __BLOCK__ -->
                  <!-- __ENDBLOCK__ -->
                </span>
              </th>
              <th
                class="fi-ta-header-cell px-3 py-3.5 sm:first-of-type:ps-6 sm:last-of-type:pe-6 fi-table-header-cell-name"
              >
                <button
                  type="button"
                  wire:click="sortTable('name')"
                  class="group flex w-full items-center gap-x-1 whitespace-nowrap"
                >
                  <!-- __BLOCK__ -->
                  <span class="sr-only"> Sort by </span>
                  <!-- __ENDBLOCK__ -->

                  <span class="text-sm font-semibold text-gray-950 dark:text-white"> Name </span>

                  <!-- __BLOCK__ -->
                  <!-- __BLOCK__ -->
                  <svg
                    class="fi-ta-header-cell-sort-icon h-5 w-5 transition duration-75 text-gray-400 dark:text-gray-500 group-hover:text-gray-500 group-focus:text-gray-500 dark:group-hover:text-gray-400 dark:group-focus:text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  <!-- __ENDBLOCK__ -->

                  <span class="sr-only"> Ascending </span>
                  <!-- __ENDBLOCK__ -->
                </button>
              </th>
              <th
                class="fi-ta-header-cell px-3 py-3.5 sm:first-of-type:ps-6 sm:last-of-type:pe-6 fi-table-header-cell-brand.name"
              >
                <button
                  type="button"
                  wire:click="sortTable('brand.name')"
                  class="group flex w-full items-center gap-x-1 whitespace-nowrap"
                >
                  <!-- __BLOCK__ -->
                  <span class="sr-only"> Sort by </span>
                  <!-- __ENDBLOCK__ -->

                  <span class="text-sm font-semibold text-gray-950 dark:text-white"> Brand </span>

                  <!-- __BLOCK__ -->
                  <!-- __BLOCK__ -->
                  <svg
                    class="fi-ta-header-cell-sort-icon h-5 w-5 transition duration-75 text-gray-400 dark:text-gray-500 group-hover:text-gray-500 group-focus:text-gray-500 dark:group-hover:text-gray-400 dark:group-focus:text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  <!-- __ENDBLOCK__ -->

                  <span class="sr-only"> Ascending </span>
                  <!-- __ENDBLOCK__ -->
                </button>
              </th>
              <th
                class="fi-ta-header-cell px-3 py-3.5 sm:first-of-type:ps-6 sm:last-of-type:pe-6 fi-table-header-cell-is-visible"
              >
                <button
                  type="button"
                  wire:click="sortTable('is_visible')"
                  class="group flex w-full items-center gap-x-1 whitespace-nowrap"
                >
                  <!-- __BLOCK__ -->
                  <span class="sr-only"> Sort by </span>
                  <!-- __ENDBLOCK__ -->

                  <span class="text-sm font-semibold text-gray-950 dark:text-white">
                    Visibility
                  </span>

                  <!-- __BLOCK__ -->
                  <!-- __BLOCK__ -->
                  <svg
                    class="fi-ta-header-cell-sort-icon h-5 w-5 transition duration-75 text-gray-400 dark:text-gray-500 group-hover:text-gray-500 group-focus:text-gray-500 dark:group-hover:text-gray-400 dark:group-focus:text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  <!-- __ENDBLOCK__ -->

                  <span class="sr-only"> Ascending </span>
                  <!-- __ENDBLOCK__ -->
                </button>
              </th>
              <th
                class="fi-ta-header-cell px-3 py-3.5 sm:first-of-type:ps-6 sm:last-of-type:pe-6 fi-table-header-cell-price"
              >
                <button
                  type="button"
                  wire:click="sortTable('price')"
                  class="group flex w-full items-center gap-x-1 whitespace-nowrap"
                >
                  <!-- __BLOCK__ -->
                  <span class="sr-only"> Sort by </span>
                  <!-- __ENDBLOCK__ -->

                  <span class="text-sm font-semibold text-gray-950 dark:text-white"> Price </span>

                  <!-- __BLOCK__ -->
                  <!-- __BLOCK__ -->
                  <svg
                    class="fi-ta-header-cell-sort-icon h-5 w-5 transition duration-75 text-gray-400 dark:text-gray-500 group-hover:text-gray-500 group-focus:text-gray-500 dark:group-hover:text-gray-400 dark:group-focus:text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  <!-- __ENDBLOCK__ -->

                  <span class="sr-only"> Ascending </span>
                  <!-- __ENDBLOCK__ -->
                </button>
              </th>
              <th
                class="fi-ta-header-cell px-3 py-3.5 sm:first-of-type:ps-6 sm:last-of-type:pe-6 fi-table-header-cell-sku"
              >
                <button
                  type="button"
                  wire:click="sortTable('sku')"
                  class="group flex w-full items-center gap-x-1 whitespace-nowrap"
                >
                  <!-- __BLOCK__ -->
                  <span class="sr-only"> Sort by </span>
                  <!-- __ENDBLOCK__ -->

                  <span class="text-sm font-semibold text-gray-950 dark:text-white"> SKU </span>

                  <!-- __BLOCK__ -->
                  <!-- __BLOCK__ -->
                  <svg
                    class="fi-ta-header-cell-sort-icon h-5 w-5 transition duration-75 text-gray-400 dark:text-gray-500 group-hover:text-gray-500 group-focus:text-gray-500 dark:group-hover:text-gray-400 dark:group-focus:text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  <!-- __ENDBLOCK__ -->

                  <span class="sr-only"> Ascending </span>
                  <!-- __ENDBLOCK__ -->
                </button>
              </th>
              <th
                class="fi-ta-header-cell px-3 py-3.5 sm:first-of-type:ps-6 sm:last-of-type:pe-6 fi-table-header-cell-qty"
              >
                <button
                  type="button"
                  wire:click="sortTable('qty')"
                  class="group flex w-full items-center gap-x-1 whitespace-nowrap"
                >
                  <!-- __BLOCK__ -->
                  <span class="sr-only"> Sort by </span>
                  <!-- __ENDBLOCK__ -->

                  <span class="text-sm font-semibold text-gray-950 dark:text-white">
                    Quantity
                  </span>

                  <!-- __BLOCK__ -->
                  <!-- __BLOCK__ -->
                  <svg
                    class="fi-ta-header-cell-sort-icon h-5 w-5 transition duration-75 text-gray-400 dark:text-gray-500 group-hover:text-gray-500 group-focus:text-gray-500 dark:group-hover:text-gray-400 dark:group-focus:text-gray-400"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  <!-- __ENDBLOCK__ -->

                  <span class="sr-only"> Ascending </span>
                  <!-- __ENDBLOCK__ -->
                </button>
              </th>
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __BLOCK__ -->
              <!-- __BLOCK__ -->
              <th class="w-1"></th>
              <!-- __ENDBLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
              <!-- __ENDBLOCK__ -->
            </tr>
          </thead>
          <!-- __ENDBLOCK__ -->

          <tbody class="divide-y divide-gray-200 whitespace-nowrap dark:divide-white/5">
            <!-- __BLOCK__ -->
            <!-- __ENDBLOCK__ -->

            <tr
              x-bind:class="{
            'hidden': false &amp;&amp; isGroupCollapsed(''),
            'bg-gray-50 dark:bg-white/5': isRecordSelected('1'),
            '[&amp;>*:first-child]:relative [&amp;>*:first-child]:before:absolute [&amp;>*:first-child]:before:start-0 [&amp;>*:first-child]:before:inset-y-0 [&amp;>*:first-child]:before:w-0.5 [&amp;>*:first-child]:before:bg-primary-600 [&amp;>*:first-child]:dark:before:bg-primary-500': isRecordSelected('1'),
        }"
              class="fi-ta-row [@media(hover:hover)]:transition [@media(hover:hover)]:duration-75 hover:bg-gray-50 dark:hover:bg-white/5"
              wire:key="YDjdrqMZkmrJTuGzMaXn.table.records.1"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <td
                class="fi-ta-cell p-0 first-of-type:ps-1 last-of-type:pe-1 sm:first-of-type:ps-3 sm:last-of-type:pe-3 w-1"
              >
                <div class="px-3 py-4">
                  <!-- __BLOCK__ -->
                  <label class="flex">
                    <input
                      type="checkbox"
                      class="fi-checkbox-input rounded border-none bg-white shadow-sm ring-1 transition duration-75 checked:ring-0 focus:ring-2 focus:ring-offset-0 disabled:pointer-events-none disabled:bg-gray-50 disabled:text-gray-50 disabled:checked:bg-current disabled:checked:text-gray-400 dark:bg-white/5 dark:disabled:bg-transparent dark:disabled:checked:bg-gray-600 text-primary-600 ring-gray-950/10 focus:ring-primary-600 checked:focus:ring-primary-500/50 dark:ring-white/20 dark:checked:bg-primary-500 dark:focus:ring-primary-500 dark:checked:focus:ring-primary-400/50 dark:disabled:ring-white/10 fi-ta-record-checkbox"
                      wire:loading.attr="disabled"
                      wire:target="gotoPage,nextPage,previousPage,removeTableFilter,removeTableFilters,reorderTable,resetTableFiltersForm,sortTable,tableColumnSearches,tableFilters,tableRecordsPerPage,tableSearch"
                      value="1"
                      x-model="selectedRecords"
                    />

                    <!-- __BLOCK__ -->
                    <span class="sr-only"> Select/deselect item 1 for bulk actions. </span>
                    <!-- __ENDBLOCK__ -->
                  </label>
                  <!-- __ENDBLOCK__ -->
                </div>
              </td>
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <td
                class="fi-ta-cell p-0 first-of-type:ps-1 last-of-type:pe-1 sm:first-of-type:ps-3 sm:last-of-type:pe-3 fi-table-cell-product-image"
                wire:key="YDjdrqMZkmrJTuGzMaXn.table.record.1.column.product-image"
              >
                <div class="fi-ta-col-wrp">
                  <!-- __BLOCK__ -->
                  <a
                    href="https://demo.filamentphp.com/shop/products/1/edit"
                    class="flex w-full disabled:pointer-events-none justify-start text-start"
                  >
                    <div class="fi-ta-image px-3 py-4">
                      <!-- __BLOCK__ -->
                      <div class="flex items-center gap-x-2.5">
                        <div class="flex gap-x-1.5">
                          <!-- __BLOCK__ -->
                          <img
                            src="https://demo.filamentphp.com/storage/1/200x200.jpeg"
                            style="height: 2.5rem"
                            class="max-w-none object-cover object-center ring-white dark:ring-gray-900"
                          />
                          <!-- __ENDBLOCK__ -->

                          <!-- __BLOCK__ -->
                          <!-- __ENDBLOCK__ -->
                        </div>

                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->
                      </div>
                      <!-- __ENDBLOCK__ -->
                    </div>
                  </a>
                  <!-- __ENDBLOCK__ -->
                </div>
              </td>

              <td
                class="fi-ta-cell p-0 first-of-type:ps-1 last-of-type:pe-1 sm:first-of-type:ps-3 sm:last-of-type:pe-3 fi-table-cell-name"
                wire:key="YDjdrqMZkmrJTuGzMaXn.table.record.1.column.name"
              >
                <div class="fi-ta-col-wrp">
                  <!-- __BLOCK__ -->
                  <a
                    href="https://demo.filamentphp.com/shop/products/1/edit"
                    class="flex w-full disabled:pointer-events-none justify-start text-start"
                  >
                    <div class="fi-ta-text grid gap-y-1 px-3 py-4">
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <div class="">
                        <!-- __BLOCK__ -->
                        <!-- __BLOCK__ -->
                        <div class="flex max-w-max">
                          <!-- __BLOCK__ -->
                          <div
                            class="fi-ta-text-item inline-flex items-center gap-1.5 text-sm text-gray-950 dark:text-white"
                            style=""
                          >
                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->

                            <div>Enhanced heuristic migration</div>

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->
                        </div>
                        <!-- __ENDBLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->
                      </div>

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                    </div>
                  </a>
                  <!-- __ENDBLOCK__ -->
                </div>
              </td>

              <td
                class="fi-ta-cell p-0 first-of-type:ps-1 last-of-type:pe-1 sm:first-of-type:ps-3 sm:last-of-type:pe-3 fi-table-cell-brand.name"
                wire:key="YDjdrqMZkmrJTuGzMaXn.table.record.1.column.brand.name"
              >
                <div class="fi-ta-col-wrp">
                  <!-- __BLOCK__ -->
                  <a
                    href="https://demo.filamentphp.com/shop/products/1/edit"
                    class="flex w-full disabled:pointer-events-none justify-start text-start"
                  >
                    <div class="fi-ta-text grid gap-y-1 px-3 py-4">
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <div class="">
                        <!-- __BLOCK__ -->
                        <!-- __BLOCK__ -->
                        <div class="flex max-w-max">
                          <!-- __BLOCK__ -->
                          <div
                            class="fi-ta-text-item inline-flex items-center gap-1.5 text-sm text-gray-950 dark:text-white"
                            style=""
                          >
                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->

                            <div>Mayer, Witting and Quigley</div>

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->
                        </div>
                        <!-- __ENDBLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->
                      </div>

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                    </div>
                  </a>
                  <!-- __ENDBLOCK__ -->
                </div>
              </td>

              <td
                class="fi-ta-cell p-0 first-of-type:ps-1 last-of-type:pe-1 sm:first-of-type:ps-3 sm:last-of-type:pe-3 fi-table-cell-is-visible"
                wire:key="YDjdrqMZkmrJTuGzMaXn.table.record.1.column.is_visible"
              >
                <div class="fi-ta-col-wrp">
                  <!-- __BLOCK__ -->
                  <a
                    href="https://demo.filamentphp.com/shop/products/1/edit"
                    class="flex w-full disabled:pointer-events-none justify-start text-start"
                  >
                    <div class="fi-ta-icon flex flex-wrap gap-1.5 px-3 py-4">
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <svg
                        style="--c-400: var(--success-400); --c-500: var(--success-500)"
                        class="fi-ta-icon-item fi-ta-icon-item-size-lg h-6 w-6 text-custom-500 dark:text-custom-400"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="currentColor"
                        aria-hidden="true"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                        ></path>
                      </svg>
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                    </div>
                  </a>
                  <!-- __ENDBLOCK__ -->
                </div>
              </td>

              <td
                class="fi-ta-cell p-0 first-of-type:ps-1 last-of-type:pe-1 sm:first-of-type:ps-3 sm:last-of-type:pe-3 fi-table-cell-price"
                wire:key="YDjdrqMZkmrJTuGzMaXn.table.record.1.column.price"
              >
                <div class="fi-ta-col-wrp">
                  <!-- __BLOCK__ -->
                  <a
                    href="https://demo.filamentphp.com/shop/products/1/edit"
                    class="flex w-full disabled:pointer-events-none justify-start text-start"
                  >
                    <div class="fi-ta-text grid gap-y-1 px-3 py-4">
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <div class="">
                        <!-- __BLOCK__ -->
                        <!-- __BLOCK__ -->
                        <div class="flex max-w-max">
                          <!-- __BLOCK__ -->
                          <div
                            class="fi-ta-text-item inline-flex items-center gap-1.5 text-sm text-gray-950 dark:text-white"
                            style=""
                          >
                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->

                            <div>121.34</div>

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->
                        </div>
                        <!-- __ENDBLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->
                      </div>

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                    </div>
                  </a>
                  <!-- __ENDBLOCK__ -->
                </div>
              </td>

              <td
                class="fi-ta-cell p-0 first-of-type:ps-1 last-of-type:pe-1 sm:first-of-type:ps-3 sm:last-of-type:pe-3 fi-table-cell-sku"
                wire:key="YDjdrqMZkmrJTuGzMaXn.table.record.1.column.sku"
              >
                <div class="fi-ta-col-wrp">
                  <!-- __BLOCK__ -->
                  <a
                    href="https://demo.filamentphp.com/shop/products/1/edit"
                    class="flex w-full disabled:pointer-events-none justify-start text-start"
                  >
                    <div class="fi-ta-text grid gap-y-1 px-3 py-4">
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <div class="">
                        <!-- __BLOCK__ -->
                        <!-- __BLOCK__ -->
                        <div class="flex max-w-max">
                          <!-- __BLOCK__ -->
                          <div
                            class="fi-ta-text-item inline-flex items-center gap-1.5 text-sm text-gray-950 dark:text-white"
                            style=""
                          >
                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->

                            <div>06175412</div>

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->
                        </div>
                        <!-- __ENDBLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->
                      </div>

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                    </div>
                  </a>
                  <!-- __ENDBLOCK__ -->
                </div>
              </td>

              <td
                class="fi-ta-cell p-0 first-of-type:ps-1 last-of-type:pe-1 sm:first-of-type:ps-3 sm:last-of-type:pe-3 fi-table-cell-qty"
                wire:key="YDjdrqMZkmrJTuGzMaXn.table.record.1.column.qty"
              >
                <div class="fi-ta-col-wrp">
                  <!-- __BLOCK__ -->
                  <a
                    href="https://demo.filamentphp.com/shop/products/1/edit"
                    class="flex w-full disabled:pointer-events-none justify-start text-start"
                  >
                    <div class="fi-ta-text grid gap-y-1 px-3 py-4">
                      <!-- __BLOCK__ -->
                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->

                      <div class="">
                        <!-- __BLOCK__ -->
                        <!-- __BLOCK__ -->
                        <div class="flex max-w-max">
                          <!-- __BLOCK__ -->
                          <div
                            class="fi-ta-text-item inline-flex items-center gap-1.5 text-sm text-gray-950 dark:text-white"
                            style=""
                          >
                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->

                            <div>5</div>

                            <!-- __BLOCK__ -->
                            <!-- __ENDBLOCK__ -->
                          </div>
                          <!-- __ENDBLOCK__ -->
                        </div>
                        <!-- __ENDBLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->
                      </div>

                      <!-- __BLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                      <!-- __ENDBLOCK__ -->
                    </div>
                  </a>
                  <!-- __ENDBLOCK__ -->
                </div>
              </td>
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <td
                class="fi-ta-cell p-0 first-of-type:ps-1 last-of-type:pe-1 sm:first-of-type:ps-3 sm:last-of-type:pe-3"
              >
                <div class="whitespace-nowrap px-3 py-4">
                  <div class="fi-ta-actions flex shrink-0 items-center gap-3 justify-end">
                    <!-- __BLOCK__ -->
                    <span class="inline-flex">
                      <!-- __BLOCK__ -->
                      <a
                        href="https://demo.filamentphp.com/shop/products/1/edit"
                        style="
                          --c-300: var(--primary-300);
                          --c-400: var(--primary-400);
                          --c-500: var(--primary-500);
                          --c-600: var(--primary-600);
                        "
                        class="fi-link fi-link-size-sm relative inline-flex items-center justify-center font-semibold outline-none transition duration-75 hover:underline focus:underline gap-1 text-sm text-custom-600 dark:text-custom-400 fi-ac-link-action"
                      >
                        <!-- __BLOCK__ -->
                        <!-- __BLOCK__ -->
                        <svg
                          style="--c-500: var(--primary-500)"
                          class="fi-link-icon h-4 w-4 text-custom-600 dark:text-custom-400"
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            d="M5.433 13.917l1.262-3.155A4 4 0 017.58 9.42l6.92-6.918a2.121 2.121 0 013 3l-6.92 6.918c-.383.383-.84.685-1.343.886l-3.154 1.262a.5.5 0 01-.65-.65z"
                          ></path>
                          <path
                            d="M3.5 5.75c0-.69.56-1.25 1.25-1.25H10A.75.75 0 0010 3H4.75A2.75 2.75 0 002 5.75v9.5A2.75 2.75 0 004.75 18h9.5A2.75 2.75 0 0017 15.25V10a.75.75 0 00-1.5 0v5.25c0 .69-.56 1.25-1.25 1.25h-9.5c-.69 0-1.25-.56-1.25-1.25v-9.5z"
                          ></path>
                        </svg>
                        <!-- __ENDBLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        Edit

                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->

                        <!-- __BLOCK__ -->
                        <!-- __ENDBLOCK__ -->
                      </a>
                      <!-- __ENDBLOCK__ -->
                    </span>
                    <!-- __ENDBLOCK__ -->
                  </div>
                </div>
              </td>
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
            </tr>
            <!-- __ENDBLOCK__ -->
          </tbody>

          <!-- __BLOCK__ -->
          <!-- __ENDBLOCK__ -->
        </table>
        <!-- __ENDBLOCK__ -->
      </div>

      <!-- __BLOCK__ -->
      <nav
        aria-label="Pagination navigation"
        role="navigation"
        class="fi-pagination grid grid-cols-3 items-center px-3 py-3 sm:px-6"
      >
        <!-- __BLOCK__ -->
        <!-- __ENDBLOCK__ -->

        <!-- __BLOCK__ -->
        <span class="hidden text-sm font-medium text-gray-700 dark:text-gray-200 md:inline">
          Showing 1 to 10 of 50 results
        </span>

        <div class="col-start-2 justify-self-center">
          <label class="sm:hidden">
            <div
              class="fi-input-wrp flex rounded-lg shadow-sm ring-1 transition duration-75 bg-white focus-within:ring-2 dark:bg-white/5 ring-gray-950/10 focus-within:ring-primary-600 dark:ring-white/20 dark:focus-within:ring-primary-500"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <div class="min-w-0 flex-1">
                <select
                  class="fi-select-input block w-full border-none bg-transparent py-1.5 pe-8 text-base text-gray-950 transition duration-75 focus:ring-0 disabled:text-gray-500 disabled:[-webkit-text-fill-color:theme(colors.gray.500)] dark:text-white dark:disabled:text-gray-400 dark:disabled:[-webkit-text-fill-color:theme(colors.gray.400)] sm:text-sm sm:leading-6 [&amp;_optgroup]:bg-white [&amp;_optgroup]:dark:bg-gray-900 [&amp;_option]:bg-white [&amp;_option]:dark:bg-gray-900 ps-3"
                  wire:model.live="tableRecordsPerPage"
                >
                  <!-- __BLOCK__ -->
                  <option value="5">5</option>
                  <option value="10">10</option>
                  <option value="25">25</option>
                  <option value="50">50</option>
                  <option value="all">All</option>
                  <!-- __ENDBLOCK__ -->
                </select>
              </div>

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
            </div>

            <span class="sr-only"> Per page </span>
          </label>

          <label class="hidden sm:inline">
            <div
              class="fi-input-wrp flex rounded-lg shadow-sm ring-1 transition duration-75 bg-white focus-within:ring-2 dark:bg-white/5 ring-gray-950/10 focus-within:ring-primary-600 dark:ring-white/20 dark:focus-within:ring-primary-500"
            >
              <!-- __BLOCK__ -->
              <div
                class="items-center gap-x-3 ps-3 flex border-e border-gray-200 pe-3 ps-3 dark:border-white/10"
              >
                <!-- __BLOCK__ -->
                <!-- __ENDBLOCK__ -->

                <!-- __BLOCK__ -->
                <!-- __ENDBLOCK__ -->

                <!-- __BLOCK__ -->
                <!-- __ENDBLOCK__ -->

                <!-- __BLOCK__ -->
                <span
                  class="fi-input-wrp-label whitespace-nowrap text-sm text-gray-500 dark:text-gray-400"
                >
                  Per page
                </span>
                <!-- __ENDBLOCK__ -->
              </div>
              <!-- __ENDBLOCK__ -->

              <div class="min-w-0 flex-1">
                <select
                  class="fi-select-input block w-full border-none bg-transparent py-1.5 pe-8 text-base text-gray-950 transition duration-75 focus:ring-0 disabled:text-gray-500 disabled:[-webkit-text-fill-color:theme(colors.gray.500)] dark:text-white dark:disabled:text-gray-400 dark:disabled:[-webkit-text-fill-color:theme(colors.gray.400)] sm:text-sm sm:leading-6 [&amp;_optgroup]:bg-white [&amp;_optgroup]:dark:bg-gray-900 [&amp;_option]:bg-white [&amp;_option]:dark:bg-gray-900 ps-3"
                  wire:model.live="tableRecordsPerPage"
                >
                  <!-- __BLOCK__ -->
                  <option value="5">5</option>
                  <option value="10">10</option>
                  <option value="25">25</option>
                  <option value="50">50</option>
                  <option value="all">All</option>
                  <!-- __ENDBLOCK__ -->
                </select>
              </div>

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
            </div>
          </label>
        </div>
        <!-- __ENDBLOCK__ -->

        <!-- __BLOCK__ -->
        <!-- __BLOCK__ -->
        <!-- __ENDBLOCK__ -->

        <!-- __BLOCK__ -->
        <button
          style=""
          class="fi-btn fi-btn-size-md relative grid-flow-col items-center justify-center font-semibold outline-none transition duration-75 focus:ring-2 rounded-lg fi-btn-color-gray gap-1.5 px-3 py-2 text-sm inline-grid shadow-sm bg-white text-gray-950 hover:bg-gray-50 dark:bg-white/5 dark:text-white dark:hover:bg-white/10 ring-1 ring-gray-950/10 dark:ring-white/20 col-start-3 justify-self-end inline-grid md:hidden"
          type="button"
          wire:loading.attr="disabled"
          wire:target="nextPage('page')"
          rel="next"
          wire:click="nextPage('page')"
          wire:key="YDjdrqMZkmrJTuGzMaXn.pagination.next"
        >
          <!-- __BLOCK__ -->
          <!-- __BLOCK__ -->
          <!-- __ENDBLOCK__ -->

          <!-- __BLOCK__ -->
          <svg
            fill="none"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            class="animate-spin fi-btn-icon h-5 w-5 text-gray-400 dark:text-gray-500"
            wire:loading.delay=""
            wire:target="nextPage('page')"
          >
            <path
              clip-rule="evenodd"
              d="M12 19C15.866 19 19 15.866 19 12C19 8.13401 15.866 5 12 5C8.13401 5 5 8.13401 5 12C5 15.866 8.13401 19 12 19ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
              fill-rule="evenodd"
              fill="currentColor"
              opacity="0.2"
            ></path>
            <path
              d="M2 12C2 6.47715 6.47715 2 12 2V5C8.13401 5 5 8.13401 5 12H2Z"
              fill="currentColor"
            ></path>
          </svg>
          <!-- __ENDBLOCK__ -->

          <!-- __BLOCK__ -->
          <!-- __ENDBLOCK__ -->
          <!-- __ENDBLOCK__ -->

          <span class="fi-btn-label"> Next </span>

          <!-- __BLOCK__ -->
          <!-- __ENDBLOCK__ -->

          <!-- __BLOCK__ -->
          <!-- __ENDBLOCK__ -->

          <!-- __BLOCK__ -->
          <!-- __ENDBLOCK__ -->
        </button>
        <!-- __ENDBLOCK__ -->
        <!-- __ENDBLOCK__ -->

        <!-- __BLOCK__ -->
        <ol
          class="fi-pagination-items hidden justify-self-end rounded-lg bg-white shadow-sm ring-1 ring-gray-950/10 dark:bg-white/5 dark:ring-white/20 md:flex"
        >
          <!-- __BLOCK__ -->
          <!-- __ENDBLOCK__ -->

          <!-- __BLOCK__ -->
          <!-- __BLOCK__ -->
          <!-- __ENDBLOCK__ -->

          <!-- __BLOCK__ -->
          <!-- __BLOCK__ -->
          <li
            class="fi-pagination-item overflow-hidden border-x-[0.5px] border-gray-200 first:rounded-s-lg first:border-s-0 last:rounded-e-lg last:border-e-0 dark:border-white/10 focus-within:z-10 focus-within:ring-2 focus-within:ring-primary-600 dark:focus-within:ring-primary-500"
            aria-label="Go to page 1"
            wire:click="gotoPage(1, 'page')"
            wire:key="YDjdrqMZkmrJTuGzMaXn.pagination.page.1"
          >
            <button
              type="button"
              class="relative overflow-hidden p-2 text-sm font-semibold outline-none transition duration-75 hover:bg-gray-50 dark:hover:bg-white/5 bg-gray-50 text-primary-600 dark:bg-white/5 dark:text-primary-400"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <span class="px-1.5"> 1 </span>
              <!-- __ENDBLOCK__ -->
            </button>
          </li>
          <li
            class="fi-pagination-item overflow-hidden border-x-[0.5px] border-gray-200 first:rounded-s-lg first:border-s-0 last:rounded-e-lg last:border-e-0 dark:border-white/10 focus-within:z-10 focus-within:ring-2 focus-within:ring-primary-600 dark:focus-within:ring-primary-500"
            aria-label="Go to page 2"
            wire:click="gotoPage(2, 'page')"
            wire:key="YDjdrqMZkmrJTuGzMaXn.pagination.page.2"
          >
            <button
              type="button"
              class="relative overflow-hidden p-2 text-sm font-semibold outline-none transition duration-75 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-white/5"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <span class="px-1.5"> 2 </span>
              <!-- __ENDBLOCK__ -->
            </button>
          </li>
          <li
            class="fi-pagination-item overflow-hidden border-x-[0.5px] border-gray-200 first:rounded-s-lg first:border-s-0 last:rounded-e-lg last:border-e-0 dark:border-white/10 focus-within:z-10 focus-within:ring-2 focus-within:ring-primary-600 dark:focus-within:ring-primary-500"
            aria-label="Go to page 3"
            wire:click="gotoPage(3, 'page')"
            wire:key="YDjdrqMZkmrJTuGzMaXn.pagination.page.3"
          >
            <button
              type="button"
              class="relative overflow-hidden p-2 text-sm font-semibold outline-none transition duration-75 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-white/5"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <span class="px-1.5"> 3 </span>
              <!-- __ENDBLOCK__ -->
            </button>
          </li>
          <li
            class="fi-pagination-item overflow-hidden border-x-[0.5px] border-gray-200 first:rounded-s-lg first:border-s-0 last:rounded-e-lg last:border-e-0 dark:border-white/10 focus-within:z-10 focus-within:ring-2 focus-within:ring-primary-600 dark:focus-within:ring-primary-500"
            aria-label="Go to page 4"
            wire:click="gotoPage(4, 'page')"
            wire:key="YDjdrqMZkmrJTuGzMaXn.pagination.page.4"
          >
            <button
              type="button"
              class="relative overflow-hidden p-2 text-sm font-semibold outline-none transition duration-75 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-white/5"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <span class="px-1.5"> 4 </span>
              <!-- __ENDBLOCK__ -->
            </button>
          </li>
          <li
            class="fi-pagination-item overflow-hidden border-x-[0.5px] border-gray-200 first:rounded-s-lg first:border-s-0 last:rounded-e-lg last:border-e-0 dark:border-white/10 focus-within:z-10 focus-within:ring-2 focus-within:ring-primary-600 dark:focus-within:ring-primary-500"
            aria-label="Go to page 5"
            wire:click="gotoPage(5, 'page')"
            wire:key="YDjdrqMZkmrJTuGzMaXn.pagination.page.5"
          >
            <button
              type="button"
              class="relative overflow-hidden p-2 text-sm font-semibold outline-none transition duration-75 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-white/5"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <span class="px-1.5"> 5 </span>
              <!-- __ENDBLOCK__ -->
            </button>
          </li>
          <!-- __ENDBLOCK__ -->
          <!-- __ENDBLOCK__ -->
          <!-- __ENDBLOCK__ -->

          <!-- __BLOCK__ -->
          <li
            class="fi-pagination-item overflow-hidden border-x-[0.5px] border-gray-200 first:rounded-s-lg first:border-s-0 last:rounded-e-lg last:border-e-0 dark:border-white/10 focus-within:z-10 focus-within:ring-2 focus-within:ring-primary-600 dark:focus-within:ring-primary-500"
            aria-label="Next"
            rel="next"
            wire:click="nextPage('page')"
            wire:key="YDjdrqMZkmrJTuGzMaXn.pagination.next"
          >
            <button
              type="button"
              class="relative overflow-hidden p-2 text-sm font-semibold outline-none transition duration-75 text-gray-400 hover:text-gray-500 dark:text-gray-500 dark:hover:text-gray-400 hover:bg-gray-50 dark:hover:bg-white/5"
            >
              <!-- __BLOCK__ -->
              <!-- __BLOCK__ -->
              <svg
                class="fi-pagination-item-icon h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.5 4.25a.75.75 0 010 1.08l-4.5 4.25a.75.75 0 01-1.06-.02z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <!-- __ENDBLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
            </button>
          </li>
          <!-- __ENDBLOCK__ -->
        </ol>
        <!-- __ENDBLOCK__ -->
      </nav>
      <!-- __ENDBLOCK__ -->

      <!-- __BLOCK__ -->
      <!-- __ENDBLOCK__ -->
    </div>

    <!-- __BLOCK__ -->
    <form wire:submit.prevent="callMountedAction">
      <div
        aria-modal="true"
        role="dialog"
        x-data="{
        isOpen: false,

        livewire: null,

        close: function () {
            this.isOpen = false

            this.$refs.modalContainer.dispatchEvent(
                new CustomEvent('modal-closed', { id: 'YDjdrqMZkmrJTuGzMaXn-action' }),
            )
        },

        open: function () {
            this.isOpen = true

            this.$refs.modalContainer.dispatchEvent(
                new CustomEvent('modal-opened', { id: 'YDjdrqMZkmrJTuGzMaXn-action' }),
            )
        },
    }"
        x-on:close-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn-action') close()"
        x-on:open-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn-action') open()"
        x-trap.noscroll="isOpen"
        wire:ignore.self=""
        class="fi-modal block"
      >
        <!-- __BLOCK__ -->
        <!-- __ENDBLOCK__ -->

        <div
          x-show="isOpen"
          x-transition.duration.300ms.opacity=""
          class="fixed inset-0 z-40 min-h-full overflow-y-auto overflow-x-hidden transition flex items-center"
          style="display: none"
        >
          <div
            aria-hidden="true"
            x-on:click="$dispatch('close-modal', { id: 'YDjdrqMZkmrJTuGzMaXn-action' })"
            class="fi-modal-close-overlay fixed inset-0 bg-gray-950/50 dark:bg-gray-950/75 cursor-pointer"
            style="will-change: transform"
          ></div>

          <div
            x-ref="modalContainer"
            class="pointer-events-none relative w-full transition my-auto p-4"
            x-on:closed-form-component-action-modal.window="if (($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn') &amp;&amp; $wire.mountedActions.length) open()"
            x-on:modal-closed.stop="const mountedActionShouldOpenModal = false


                if (! mountedActionShouldOpenModal) {
                    return
                }

                if ($wire.mountedFormComponentActions.length) {
                    return
                }

                $wire.unmountAction(false)"
            x-on:opened-form-component-action-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn') close()"
          >
            <div
              x-data="{ isShown: false }"
              x-init="
                    $nextTick(() => {
                        isShown = isOpen
                        $watch('isOpen', () => (isShown = isOpen))
                    })
                "
              x-on:keydown.window.escape="$dispatch('close-modal', { id: 'YDjdrqMZkmrJTuGzMaXn-action' })"
              x-show="isShown"
              x-transition:enter="duration-300"
              x-transition:leave="duration-300"
              x-transition:enter-start="scale-95"
              x-transition:enter-end="scale-100"
              x-transition:leave-start="scale-95"
              x-transition:leave-end="scale-100"
              class="fi-modal-window pointer-events-auto relative flex w-full cursor-default flex-col bg-white shadow-xl ring-1 ring-gray-950/5 dark:bg-gray-900 dark:ring-white/10 mx-auto rounded-xl hidden max-w-sm"
              style="display: none"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
            </div>
          </div>
        </div>
      </div>
    </form>

    <!-- __ENDBLOCK__ -->

    <!-- __BLOCK__ -->
    <form wire:submit.prevent="callMountedTableAction">
      <div
        aria-modal="true"
        role="dialog"
        x-data="{
        isOpen: false,

        livewire: null,

        close: function () {
            this.isOpen = false

            this.$refs.modalContainer.dispatchEvent(
                new CustomEvent('modal-closed', { id: 'YDjdrqMZkmrJTuGzMaXn-table-action' }),
            )
        },

        open: function () {
            this.isOpen = true

            this.$refs.modalContainer.dispatchEvent(
                new CustomEvent('modal-opened', { id: 'YDjdrqMZkmrJTuGzMaXn-table-action' }),
            )
        },
    }"
        x-on:close-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn-table-action') close()"
        x-on:open-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn-table-action') open()"
        x-trap.noscroll="isOpen"
        wire:ignore.self=""
        class="fi-modal block"
      >
        <!-- __BLOCK__ -->
        <!-- __ENDBLOCK__ -->

        <div
          x-show="isOpen"
          x-transition.duration.300ms.opacity=""
          class="fixed inset-0 z-40 min-h-full overflow-y-auto overflow-x-hidden transition flex items-center"
          style="display: none"
        >
          <div
            aria-hidden="true"
            x-on:click="$dispatch('close-modal', { id: 'YDjdrqMZkmrJTuGzMaXn-table-action' })"
            class="fi-modal-close-overlay fixed inset-0 bg-gray-950/50 dark:bg-gray-950/75 cursor-pointer"
            style="will-change: transform"
          ></div>

          <div
            x-ref="modalContainer"
            class="pointer-events-none relative w-full transition my-auto p-4"
            x-on:closed-form-component-action-modal.window="if (($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn') &amp;&amp; $wire.mountedTableActions.length) open()"
            x-on:modal-closed.stop="const mountedTableActionShouldOpenModal = false


                if (! mountedTableActionShouldOpenModal) {
                    return
                }

                if ($wire.mountedFormComponentActions.length) {
                    return
                }

                $wire.unmountTableAction(false)"
            x-on:opened-form-component-action-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn') close()"
          >
            <div
              x-data="{ isShown: false }"
              x-init="
                    $nextTick(() => {
                        isShown = isOpen
                        $watch('isOpen', () => (isShown = isOpen))
                    })
                "
              x-on:keydown.window.escape="$dispatch('close-modal', { id: 'YDjdrqMZkmrJTuGzMaXn-table-action' })"
              x-show="isShown"
              x-transition:enter="duration-300"
              x-transition:leave="duration-300"
              x-transition:enter-start="scale-95"
              x-transition:enter-end="scale-100"
              x-transition:leave-start="scale-95"
              x-transition:leave-end="scale-100"
              class="fi-modal-window pointer-events-auto relative flex w-full cursor-default flex-col bg-white shadow-xl ring-1 ring-gray-950/5 dark:bg-gray-900 dark:ring-white/10 mx-auto rounded-xl hidden max-w-sm"
              style="display: none"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
            </div>
          </div>
        </div>
      </div>
    </form>

    <form wire:submit.prevent="callMountedTableBulkAction">
      <div
        aria-modal="true"
        role="dialog"
        x-data="{
        isOpen: false,

        livewire: null,

        close: function () {
            this.isOpen = false

            this.$refs.modalContainer.dispatchEvent(
                new CustomEvent('modal-closed', { id: 'YDjdrqMZkmrJTuGzMaXn-table-bulk-action' }),
            )
        },

        open: function () {
            this.isOpen = true

            this.$refs.modalContainer.dispatchEvent(
                new CustomEvent('modal-opened', { id: 'YDjdrqMZkmrJTuGzMaXn-table-bulk-action' }),
            )
        },
    }"
        x-on:close-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn-table-bulk-action') close()"
        x-on:open-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn-table-bulk-action') open()"
        x-trap.noscroll="isOpen"
        wire:ignore.self=""
        class="fi-modal block"
      >
        <!-- __BLOCK__ -->
        <!-- __ENDBLOCK__ -->

        <div
          x-show="isOpen"
          x-transition.duration.300ms.opacity=""
          class="fixed inset-0 z-40 min-h-full overflow-y-auto overflow-x-hidden transition flex items-center"
          style="display: none"
        >
          <div
            aria-hidden="true"
            x-on:click="$dispatch('close-modal', { id: 'YDjdrqMZkmrJTuGzMaXn-table-bulk-action' })"
            class="fi-modal-close-overlay fixed inset-0 bg-gray-950/50 dark:bg-gray-950/75 cursor-pointer"
            style="will-change: transform"
          ></div>

          <div
            x-ref="modalContainer"
            class="pointer-events-none relative w-full transition my-auto p-4"
            x-on:closed-form-component-action-modal.window="if (($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn') &amp;&amp; $wire.mountedTableBulkAction) open()"
            x-on:modal-closed.stop="const mountedTableBulkActionShouldOpenModal = false


                if (! mountedTableBulkActionShouldOpenModal) {
                    return
                }

                if ($wire.mountedFormComponentActions.length) {
                    return
                }

                $wire.mountedTableBulkAction = null"
            x-on:opened-form-component-action-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn') close()"
          >
            <div
              x-data="{ isShown: false }"
              x-init="
                    $nextTick(() => {
                        isShown = isOpen
                        $watch('isOpen', () => (isShown = isOpen))
                    })
                "
              x-on:keydown.window.escape="$dispatch('close-modal', { id: 'YDjdrqMZkmrJTuGzMaXn-table-bulk-action' })"
              x-show="isShown"
              x-transition:enter="duration-300"
              x-transition:leave="duration-300"
              x-transition:enter-start="scale-95"
              x-transition:enter-end="scale-100"
              x-transition:leave-start="scale-95"
              x-transition:leave-end="scale-100"
              class="fi-modal-window pointer-events-auto relative flex w-full cursor-default flex-col bg-white shadow-xl ring-1 ring-gray-950/5 dark:bg-gray-900 dark:ring-white/10 mx-auto rounded-xl hidden max-w-sm"
              style="display: none"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
            </div>
          </div>
        </div>
      </div>
    </form>

    <!-- __ENDBLOCK__ -->

    <!-- __BLOCK__ -->
    <form wire:submit.prevent="callMountedInfolistAction">
      <div
        aria-modal="true"
        role="dialog"
        x-data="{
        isOpen: false,

        livewire: null,

        close: function () {
            this.isOpen = false

            this.$refs.modalContainer.dispatchEvent(
                new CustomEvent('modal-closed', { id: 'YDjdrqMZkmrJTuGzMaXn-infolist-action' }),
            )
        },

        open: function () {
            this.isOpen = true

            this.$refs.modalContainer.dispatchEvent(
                new CustomEvent('modal-opened', { id: 'YDjdrqMZkmrJTuGzMaXn-infolist-action' }),
            )
        },
    }"
        x-on:close-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn-infolist-action') close()"
        x-on:open-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn-infolist-action') open()"
        x-trap.noscroll="isOpen"
        wire:ignore.self=""
        class="fi-modal block"
      >
        <!-- __BLOCK__ -->
        <!-- __ENDBLOCK__ -->

        <div
          x-show="isOpen"
          x-transition.duration.300ms.opacity=""
          class="fixed inset-0 z-40 min-h-full overflow-y-auto overflow-x-hidden transition flex items-center"
          style="display: none"
        >
          <div
            aria-hidden="true"
            x-on:click="$dispatch('close-modal', { id: 'YDjdrqMZkmrJTuGzMaXn-infolist-action' })"
            class="fi-modal-close-overlay fixed inset-0 bg-gray-950/50 dark:bg-gray-950/75 cursor-pointer"
            style="will-change: transform"
          ></div>

          <div
            x-ref="modalContainer"
            class="pointer-events-none relative w-full transition my-auto p-4"
            x-on:closed-form-component-action-modal.window="if (($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn') &amp;&amp; $wire.mountedInfolistActions.length) open()"
            x-on:modal-closed.stop="const mountedInfolistActionShouldOpenModal = false


                if (! mountedInfolistActionShouldOpenModal) {
                    return
                }

                if ($wire.mountedFormComponentActions.length) {
                    return
                }

                $wire.unmountInfolistAction(false)"
            x-on:opened-form-component-action-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn') close()"
          >
            <div
              x-data="{ isShown: false }"
              x-init="
                    $nextTick(() => {
                        isShown = isOpen
                        $watch('isOpen', () => (isShown = isOpen))
                    })
                "
              x-on:keydown.window.escape="$dispatch('close-modal', { id: 'YDjdrqMZkmrJTuGzMaXn-infolist-action' })"
              x-show="isShown"
              x-transition:enter="duration-300"
              x-transition:leave="duration-300"
              x-transition:enter-start="scale-95"
              x-transition:enter-end="scale-100"
              x-transition:leave-start="scale-95"
              x-transition:leave-end="scale-100"
              class="fi-modal-window pointer-events-auto relative flex w-full cursor-default flex-col bg-white shadow-xl ring-1 ring-gray-950/5 dark:bg-gray-900 dark:ring-white/10 mx-auto rounded-xl hidden max-w-sm"
              style="display: none"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
            </div>
          </div>
        </div>
      </div>
    </form>

    <!-- __ENDBLOCK__ -->

    <!-- __BLOCK__ -->
    <form wire:submit.prevent="callMountedFormComponentAction">
      <div
        aria-modal="true"
        role="dialog"
        x-data="{
        isOpen: false,

        livewire: null,

        close: function () {
            this.isOpen = false

            this.$refs.modalContainer.dispatchEvent(
                new CustomEvent('modal-closed', { id: 'YDjdrqMZkmrJTuGzMaXn-form-component-action' }),
            )
        },

        open: function () {
            this.isOpen = true

            this.$refs.modalContainer.dispatchEvent(
                new CustomEvent('modal-opened', { id: 'YDjdrqMZkmrJTuGzMaXn-form-component-action' }),
            )
        },
    }"
        x-on:close-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn-form-component-action') close()"
        x-on:open-modal.window="if ($event.detail.id === 'YDjdrqMZkmrJTuGzMaXn-form-component-action') open()"
        x-trap.noscroll="isOpen"
        wire:ignore.self=""
        class="fi-modal block"
      >
        <!-- __BLOCK__ -->
        <!-- __ENDBLOCK__ -->

        <div
          x-show="isOpen"
          x-transition.duration.300ms.opacity=""
          class="fixed inset-0 z-40 min-h-full overflow-y-auto overflow-x-hidden transition flex items-center"
          style="display: none"
        >
          <div
            aria-hidden="true"
            x-on:click="$dispatch('close-modal', { id: 'YDjdrqMZkmrJTuGzMaXn-form-component-action' })"
            class="fi-modal-close-overlay fixed inset-0 bg-gray-950/50 dark:bg-gray-950/75 cursor-pointer"
            style="will-change: transform"
          ></div>

          <div
            x-ref="modalContainer"
            class="pointer-events-none relative w-full transition my-auto p-4"
            x-on:modal-closed.stop="const mountedFormComponentActionShouldOpenModal = false


                if (mountedFormComponentActionShouldOpenModal) {
                    $wire.unmountFormComponentAction(false)
                }"
          >
            <div
              x-data="{ isShown: false }"
              x-init="
                    $nextTick(() => {
                        isShown = isOpen
                        $watch('isOpen', () => (isShown = isOpen))
                    })
                "
              x-on:keydown.window.escape="$dispatch('close-modal', { id: 'YDjdrqMZkmrJTuGzMaXn-form-component-action' })"
              x-show="isShown"
              x-transition:enter="duration-300"
              x-transition:leave="duration-300"
              x-transition:enter-start="scale-95"
              x-transition:enter-end="scale-100"
              x-transition:leave-start="scale-95"
              x-transition:leave-end="scale-100"
              class="fi-modal-window pointer-events-auto relative flex w-full cursor-default flex-col bg-white shadow-xl ring-1 ring-gray-950/5 dark:bg-gray-900 dark:ring-white/10 mx-auto rounded-xl hidden max-w-sm"
              style="display: none"
            >
              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->

              <!-- __BLOCK__ -->
              <!-- __ENDBLOCK__ -->
            </div>
          </div>
        </div>
      </div>
    </form>

    <!-- __ENDBLOCK__ -->
  </div>
</template>
<script>
import { YSearchInput } from '../Common/Components.vue'

export default {
  name: 'data-table',
  data() {
    return {
      search: '',
      columns: [
        {
          name: 'image',
          type: 'image',
          circular: false,
          label: 'Avatar',
          searchable: false,
          sortable: false,
          copyable: false,
          disabled: false,
          hidden: false,
          inline: false,
          summarized: false,
          toggled: false
        }
      ],
      table_data: []
    }
  },
  created() {
    this.table_data = [
      {
        image:
          'https://yt3.googleusercontent.com/cqhdvuYeeUKutpUJZJcN2Plzuu5E8UlRMpK-BLeciHaX-s-83LBhAZ33YQWjxlVu3IoHsmYf=s900-c-k-c0x00ffffff-no-rj'
      }
    ]
  },
  watch(){
    if(this.search.length > 0){
        alert('salom')
    }
  },
  components: { YSearchInput }
}
</script>