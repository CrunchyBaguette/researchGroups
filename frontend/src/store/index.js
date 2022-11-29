import Vue from "vue";
import Vuex from "vuex";
import VueFilterDateFormat from '@vuejs-community/vue-filter-date-format';

import researchGroup from "./modules/researchGroup";
import researchGroupPost from "./modules/researchGroupPost";
import project from "./modules/project";
import projectPost from "./modules/projectPost";
import announcement from "./modules/announcement";
import auth from "./modules/auth";

Vue.use(Vuex);
Vue.use(VueFilterDateFormat);

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
