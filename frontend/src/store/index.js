import Vue from "vue";
import Vuex from "vuex";

import researchGroup from "./modules/researchGroup";

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        researchGroup,
    },
});