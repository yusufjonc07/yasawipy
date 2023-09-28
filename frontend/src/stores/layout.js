// stores/index.js
import { defineStore } from 'pinia'

export const useLayoutStore = defineStore('layout', {
  state: () => {
    return {
      theme: localStorage.getItem('theme'),
      sidebar: {
        isOpen: window.innerWidth > 1024 ? true : false,
        collapsedGroups: []
      }
    }
  },

  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    closeSidebar() {
      this.sidebar.isOpen = false
    },
    openSidebar() {
      this.sidebar.isOpen = true
    },
    groupIsCollapsed(label) {
      return this.sidebar.collapsedGroups.includes(label)
    },
    toggleCollapsedGroup(label) {
      if (this.groupIsCollapsed(label)) {
        this.sidebar.collapsedGroups = this.sidebar.collapsedGroups.filter(function (_l) {
          return _l !== label;
        });
      } else {
        this.sidebar.collapsedGroups.push(label)
      }
    },

    getTheme() {
      if (this.theme == 'time') {
        let hour = (new Date()).getHours()
        if (hour > 7 && hour < 18) {
          return 'light'
        } else {
          return 'dark'
        }
      }
      return this.theme
    },

    changeTheme(theme) {

      this.theme = theme
      localStorage.setItem('theme', this.theme)

      return 1
    }

  },
})