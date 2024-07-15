<template>
    <div>
        <v-container class="pa-10">
            <h1 class="text-center">Latest Books</h1>
        <v-row>
            <v-col>
                <BookCard />
            </v-col>
            <v-col>
                <BookCard />
            </v-col>
            <v-col>
                <BookCard />
            </v-col>
        </v-row>
        </v-container>

       
    </div>
</template>
<script>
import BookCard from './BookCard.vue';
  export default {
    components:{
        BookCard,
    },
    data: () => ({

    }),

    methods: {

    },
  }
</script>