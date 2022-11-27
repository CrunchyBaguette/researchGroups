import Vue from "vue";
import Vuex from "vuex";

import researchGroup from "./modules/researchGroup";
import auth from "./modules/auth";
import JwPagination from 'jw-vue-pagination';

Vue.component('jw-pagination', JwPagination);

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        researchGroup,
        auth,
    },
});