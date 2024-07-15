<template>
  <div>
  <v-app-bar
      app
      color="primary"
      dark
      clipped-left
      @click="changeDrawerStatus"
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
    <template>
  <div>
    <v-navigation-drawer
        v-model="isGlobalDrawerSwitchOn"
        app
        temporary
        clipped
        height="100rm"
      >
    <div class="pa-2">
          <v-btn
            class="mx-2"
            fab
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
        <div class="pa-2">
          <v-btn block @click="switchTheme">
            Dark
          </v-btn>
        </div>
      </template>
      </v-navigation-drawer>
  </div>
</template>
    <v-main>
      <router-view/>
      <Footer />
    </v-main>
  </div>
</template>

<script>
//import Navbar from "@/components/NavbarPage.vue"
import Footer from "@/views/FooterView.vue"
export default {
  components:{
    
    Footer
  },
  data: () => ({
    //properties for       :collapse="!collapseOnScroll"      :collapse-on-scroll="collapseOnScroll"
    collapseOnScroll: true,
  }),
  methods:{
    changeDrawerStatus(){
      this.$store.dispatch('toggleglobalDrawerSwitch');
    },
    switchTheme(){
      this.$attrs.theme = !this.$attrs.theme
    },
    drawerback(){
      this.$store.dispatch('toggleglobalDrawerSwitch');
    }
  },
  computed: {
    // 使用计算属性来获取全局开关状态
    isGlobalDrawerSwitchOn(){
        return this.$store.state.globalDrawerSwitch;
    }
    
  },
}
</script>