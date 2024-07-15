import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // 定义全局开关Drawer状态
    globalDrawerSwitch: false,
    // 定义全局文本字典
    globalTextDict: {
      'title':"",
      "routers":[],
    }
  },
  mutations: {
    INIT_GLOBAL_TEXT_DICT(state, dict) {
      state.globalTextDict = dict;
    },
    // 更改开关状态的 mutation
    TOGGLE_GLOBAL_DRAWER_SWITCH(state) {
      state.globalDrawerSwitch = !state.globalDrawerSwitch;
    }
  },
  actions: {
    // 触发 mutation 的 action
    initGlobalTextDict({commit}, dict) {
      commit('INIT_GLOBAL_TEXT_DICT', dict);
    },
    toggleglobalDrawerSwitch({ commit }) {
      commit('TOGGLE_GLOBAL_DRAWER_SWITCH');
    }
  }
});