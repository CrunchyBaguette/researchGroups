import Vue from "vue";
import Vuex from "vuex";

import researchGroup from "./modules/researchGroup";
import researchGroupPost from "./modules/researchGroupPost";
import project from "./modules/project";
import projectPost from "./modules/projectPost";
import announcement from "./modules/announcement";
import auth from "./modules/auth";
import JwPagination from 'jw-vue-pagination';

Vue.component('jw-pagination', JwPagination);

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        researchGroupPost,
        researchGroup,
        project,
        projectPost,
        announcement,
        auth,
    },
});