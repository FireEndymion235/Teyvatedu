<template>
  <div>
    <v-navigation-drawer
        v-model="isGlobalDrawerSwitchOn"
        absolute
        bottom
        temporary
        floating
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
        <div class="pa-2">
          <v-btn block @click="switchTheme">
            Dark
          </v-btn>
        </div>
      </template>
      </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  data: () => ({
    group: null,
  }),
  methods:{
    switchTheme(){
      this.$attrs.theme = !this.$attrs.theme
    },
    drawerback(){
      this.$store.dispatch('toggleglobalDrawerSwitch');
    }
  },
  created:{
    
  },
  computed: {
    // 使用计算属性来获取全局开关状态
    isGlobalDrawerSwitchOn(){
        return this.$store.state.globalDrawerSwitch;
    }
    
  },
}
</script>