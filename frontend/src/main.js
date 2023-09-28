import './assets/css/yasawi/forms/forms.css'
import './assets/css/yasawi/support/support.css'
import './assets/style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useLayoutStore } from '@/stores/layout'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

const layoutStore = useLayoutStore()
app.config.globalProperties.$layout = layoutStore

app.mount('#app')
