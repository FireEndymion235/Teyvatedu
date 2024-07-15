<template>
  <v-app>
    <Index />
  </v-app>
</template>

<script>
import Index from './views/IndexView.vue';
export default {
  name: 'App',
  components:{
    Index,
  },
  created() {

    this.$store.dispatch('initGlobalTextDict',{
      "title":"TEP",
      "routers":{
        "Home":"home",
        "Publications":"publications",
        "Notifications": "notifications",
        "Productions": "productions",
        "About us": "aboutus",
      }
    })
  }
};
</script>
