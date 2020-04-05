import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

let store = new Vuex.Store({
  state: {
    count: 0,
  },
  mutations: {
    increment(state, payload) {
      state.count += payload;
    },
  },
  actions: {
    incrementBtnClicked(context) {
      context.commit("increment", 1);
    },
  },
});

export default store;
