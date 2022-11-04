import Vue from 'vue'
import router from "@/router"
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import App from './App.vue'

Vue.config.productionTip = false

Vue.use(Buefy)
new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
