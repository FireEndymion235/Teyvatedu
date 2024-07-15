<template>
  <div class="prog-translate">
   
    <Carousel />
    <div class=""></div>
      <v-row class="text-center">
        
        <v-col class="mb-4">

        <div class="display-2 font-weight-bold mb-3">
        </div>

        <h1 class="display-2 font-weight-bold mb-3">
          {{ this.$store.state.globalTextDict.title }}
        </h1>
        <p class="subheading font-weight-regular">
          For help and collaboration with other Vuetify developers,
          <br>please join our online
          <a
            href="https://community.vuetifyjs.com"
            target="_blank"
          >Discord Community</a>
        </p>
      </v-col>
      </v-row>

      <v-divider />
      <LatestNotification />
      <LatestBook />


  </div>

</template>

<script>
import LatestNotification from '@/components/Home/LatestNotification.vue'
import LatestBook from '@/components/Home/LatestBook.vue'
import Carousel from '@/components/Home/CarouselPage.vue'
  export default {
    name: 'HomeView',

    components: {
      Carousel,
      LatestBook,
      LatestNotification,
    },
  }
</script>
