<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      absolute
      dark
      :collapse="!collapseOnScroll"
      :collapse-on-scroll="collapseOnScroll"
      @click="drawer = true"
    >
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
    

      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />
    
    </div>
    <v-toolbar-title>Collapsing Bar</v-toolbar-title>

      
      <v-spacer></v-spacer>

    </v-app-bar>
    
    <v-navigation-drawer
        v-model="drawer"
        absolute
        fouc
      >
    <div class="pa-2">
          <v-btn
            class="mx-2"
            fab
            dark
            small
            @click="drawerback"
            color="primary"
          >
            <v-icon dark>
              mdi-menu-left
            </v-icon>
          </v-btn>
        </div>
        <v-list
          nav
          dense
        >
          <v-list-item-group
            v-model="group"
            active-class="deep-purple--text text--accent-4"
          >

            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-home</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item>
  
            <v-list-item to="/login">
              <v-list-item-icon>
                <v-icon>mdi-account</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Account</v-list-item-title>
            </v-list-item>

          </v-list-item-group>
        </v-list>

         <v-list-item to="/login">
              <v-list-item-icon>
                <v-icon>mdi-account</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Account</v-list-item-title>
            </v-list-item>

  

        <template v-slot:append>
        <div class="pa-2">
          <v-btn block @click="drawerback">
            收起菜单
          </v-btn>
        </div>
      </template>

      </v-navigation-drawer>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',


  data: () => ({
    collapseOnScroll: true,
    drawer: false,
    group: null,
  }),
  methods: {
    drawerback() {
      this.drawer = false;
    }
  }

};
</script>
