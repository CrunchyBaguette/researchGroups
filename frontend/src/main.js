import Vue from 'vue'
import router from "@/router"
import store from "@/store"
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import App from './App.vue'
import mdiVue from 'mdi-vue/v2'
import * as mdijs from '@mdi/js'

Vue.config.productionTip = false

if (store.getters["auth/isAuthenticated"]) {
  store.dispatch("auth/setAxiosHeaders");
  if (store.getters["auth/isAccessTokenExpired"]) {
    store.dispatch("auth/logOut");
    router.push("/login");
  } else {
    store.dispatch("auth/refreshAccessToken").then(() => {
      store.dispatch("auth/beginTokenRefreshCountdown");
    })
  }
}

Vue.use(Buefy)
Vue.use(mdiVue, {
  icons: mdijs
})
new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
