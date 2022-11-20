import Vue from "vue";
import Vuex from "vuex";

import researchGroup from "./modules/researchGroup";
import auth from "./modules/auth";

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        researchGroup,
        auth,
    },
});