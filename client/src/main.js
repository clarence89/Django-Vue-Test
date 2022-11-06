import Vue from 'vue'
import VueSweetalert2 from 'vue-sweetalert2';
import App from './App.vue'
import 'sweetalert2/dist/sweetalert2.min.css';
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
Vue.use(VueSweetalert2);
Vue.config.productionTip = false
new Vue({
  render: h => h(App),
}).$mount('#app')
