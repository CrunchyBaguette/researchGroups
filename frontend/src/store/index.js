import Vue from "vue";
import Vuex from "vuex";
import VueFilterDateFormat from '@vuejs-community/vue-filter-date-format';

import researchGroup from "./modules/researchGroup";
import researchGroupMember from "./modules/researchGroupMember";
import researchGroupPost from "./modules/researchGroupPost";
import project from "./modules/project";
import projectMember from "./modules/projectMember";
import projectPost from "./modules/projectPost";
import announcement from "./modules/announcement";
import auth from "./modules/auth";
import user from "./modules/user"

Vue.use(Vuex);
Vue.use(VueFilterDateFormat);

export default new Vuex.Store({
    modules: {
        researchGroupPost,
        researchGroupMember,
        researchGroup,
        project,
        projectMember,
        projectPost,
        announcement,
        user,
        auth,
    },
});
