import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify'


new Vue({
  router,
  el: '#app',
  vuetify,
  render: h => h(App)
});
