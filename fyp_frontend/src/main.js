import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

//import './style.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)

app.use(createPinia())
app.use(router, axios)

app.mount('#app')
