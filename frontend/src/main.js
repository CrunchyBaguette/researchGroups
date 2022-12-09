import Vue from 'vue'
import router from "@/router"
import store from "@/store"
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import App from './App.vue'
<<<<<<< HEAD
//import { marked } from 'marked'

// const markedMixin = {
//   methods: {
//     marked: function (input) {
//       return marked(input);
//     }
//   }
// };
=======
import mdiVue from 'mdi-vue/v2'
import * as mdijs from '@mdi/js'
>>>>>>> main

Vue.config.productionTip = false

Vue.use(Buefy)
Vue.use(mdiVue, {
  icons: mdijs
})
new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

// Vue.use(Buefy)
// new Vue({
//   router,
//   store,
//   render: h => h(App),
// }).$mixin(markedMixin).$mount('#app')

