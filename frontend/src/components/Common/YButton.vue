<template>
  <button
    v-if="tag == 'button'"
    :title="tooltip"
    v-bind:class="buttonClasses"
    :disabled="disabled"
    :type="type"
  >
    <img
      v-if="isLoading"
      src="../../assets/images/loading.svg"
      class="animate-spin fi-input-wrp-icon h-5 w-5"
    />
    <component v-else :is="this.$icon[iconType][this.iconComonent]" :class="iconClasses"></component>
    <slot></slot>
  </button>
</template>
<script>
import { get_color_css_variables } from '../../utils/helpers'

export default {
  name: 'yw-button',
  props: {
    badge: String,
    badgeColor: {
      type: String,
      default: 'primary'
    },
    color: {
      type: String,
      default: 'primary'
    },
    urlTo: {
      type: String,
      default: '--'
    },
    disabled: {
      type: Boolean,
      default: false
    },
    form: String,
    grouped: {
      type: Boolean,
      default: false
    },
    icon: String,
    iconAlias: String,
    iconPosition: String,
    iconSize: String,
    labeledFrom: String,
    labelSrOnly: {
      type: Boolean,
      default: false
    },
    outlined: {
      type: Boolean,
      default: false
    },
    size: {
      type: String,
      default: 'md'
    },
    type: {
      type: String,
      default: 'button'
    },
    iconType: {
      type: String,
      default: 'outline'
    },
    tag: {
      type: String,
      default: 'button'
    },
    isLoading: Boolean,
    tooltip: String
  },
  data() {
    return {
      buttonStyles: null,
      buttonClasses: null,
      iconClasses: null,
      labelClasses: null,
      iconComonent: null,
      badgeContainerClasses:
        'fi-button-badge-ctn absolute -top-1 start-full z-[1] -ms-1 -translate-x-1/2 rounded-md bg-white rtl:translate-x-1/2 dark:bg-gray-900'
    }
  },
  mounted() {
    let cons = []

    this.icon.split('-').forEach((element) => {
      cons.push(this.capitalized(element))
    })

    this.iconComonent = cons.join('') + 'Icon'

    this.buttonStyles = get_color_css_variables(this.color, [400, 500, 600])

    this.buttonClasses = [
      `fi-btn fi-btn-size-${this.size} relative grid-flow-col items-center justify-center font-semibold outline-none transition duration-75 focus:ring-2 fi-btn-color-${this.color}`,
      this.disabled ? 'pointer-events-none opacity-70' : '',
      this.grouped ? 'flex-1' : 'rounded-lg',
      this.labeledFrom ? 'hidden' : '',
      this.size == 'xs'
        ? 'gap-1 px-2 py-1.5 text-xs'
        : this.size == 'sm'
        ? 'gap-1 px-2.5 py-1.5 text-sm'
        : this.size == 'md'
        ? 'gap-1.5 px-3 py-2 text-sm'
        : this.size == 'lg'
        ? 'gap-1.5 px-3.5 py-2.5 text-sm'
        : this.size == 'xs'
        ? 'gap-1.5 px-4 py-3 text-sm'
        : this.size,
      ['sm', 'md', 'lg', 'xl', '2xl'].includes(this.labeledFrom)
        ? `${this.labeledFrom}:inline-grid`
        : 'inline-grid',
      this.outlined
        ? [
            'fi-btn-outlined ring-1',
            this.color == 'gray'
              ? 'text-gray-950 ring-gray-300 hover:bg-gray-400/10 focus:ring-gray-400/40 dark:text-white dark:ring-gray-700'
              : `text-custom-600 ring-${this.color}-600 hover:bg-${this.color}-400/10 dark:text-custom-400 dark:ring-${this.color}-500`
          ].join(' ')
        : [
            !this.grouped ? 'shadow-sm' : '',
            this.color == 'gray'
              ? [
                  'bg-white text-gray-950 hover:bg-gray-50 dark:bg-white/5 dark:text-white dark:hover:bg-white/10',
                  !this.grouped ? 'ring-1 ring-gray-950/10 dark:ring-white/20' : ''
                ].join(' ')
              : [
                  `bg-${this.color}-600 text-white hover:bg-${this.color}-500 dark:bg-${this.color}-500 dark:hover:bg-${this.color}-400`,
                  !this.grouped
                    ? `focus:ring-${this.color}-500/50 dark:focus:ring-${this.color}-400/50`
                    : ''
                ].join(' ')
          ].join(' ')
    ].join(' ')

    let iconSize = ['xs', 'sm'].includes(this.size) ? 'sm' : 'md'

    this.iconClasses = [
      'fi-btn-icon',
      iconSize == 'sm'
        ? 'h-4 w-4'
        : iconSize == 'md'
        ? 'h-5 w-5'
        : iconSize == 'lg'
        ? 'h-6 w-6'
        : iconSize,
      this.color == 'gray' ? 'text-gray-400 dark:text-gray-500' : ''
    ].join(' ')

    this.labelClasses = ['fi-btn-label', this.labelSrOnly ? 'sr-only' : ''].join(' ')

    // let hasFileUploadLoadingIndicator = false;

    // if(this.type === 'submit' && this.form){
    //   hasFileUploadLoadingIndicator = true
    // }

    // if(this.$attrs.onClick || this.$attrs.target || hasFileUploadLoadingIndicator){

    // }

    // let wireTarget = this.$attrs =  $attributes->whereStartsWith(['wire:target', 'wire:click'])->filter(fn ($value): bool => filled($value))->first();

    // $hasLoadingIndicator = filled($wireTarget) || $hasFileUploadLoadingIndicator;

    // if ($hasLoadingIndicator) {
    //     $loadingIndicatorTarget = html_entity_decode($wireTarget ?: $form, ENT_QUOTES);
    // }
  },
  methods: {
    capitalized(name) {
      const capitalizedFirst = name[0].toUpperCase()
      const rest = name.slice(1)

      return capitalizedFirst + rest
    }
  }
}
</script>