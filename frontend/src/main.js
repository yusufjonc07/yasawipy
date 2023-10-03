import './assets/css/yasawi/forms/forms.css'
import './assets/css/yasawi/support/support.css'
import './assets/style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useLayoutStore } from '@/stores/layout'
import * as SolidIcons from '@heroicons/vue/20/solid'
import * as OutlineIcons from '@heroicons/vue/24/outline'
import {getIcon as myIcon} from "./utils/helpers"


import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

const layoutStore = useLayoutStore()
app.config.globalProperties.$layout = layoutStore

app.config.globalProperties.$icon =  {
    solid: SolidIcons,
    outline: OutlineIcons
}

app.config.globalProperties.$getIcon = (name) => {
    return myIcon(name)
}


app.mount('#app')
