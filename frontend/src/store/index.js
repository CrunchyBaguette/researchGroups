import Vue from "vue";
import Vuex from "vuex";
import VueFilterDateFormat from '@vuejs-community/vue-filter-date-format';

import researchGroup from "./modules/researchGroup";
import researchGroupMember from "./modules/researchGroupMember";
import researchGroupPost from "./modules/researchGroupPost";
import researchGroupLink from "./modules/researchGroupLink";
import researchGroupDisk from "./modules/researchGroupDisk";
import project from "./modules/project";
import projectMember from "./modules/projectMember";
import projectPost from "./modules/projectPost";
import projectLink from "./modules/projectLink";
import projectDisk from "./modules/projectDisk";
import tutorial from "./modules/tutorial";
import announcement from "./modules/announcement";
import auth from "./modules/auth";
import user from "./modules/user";

Vue.use(Vuex);
Vue.use(VueFilterDateFormat);

export default new Vuex.Store({
    modules: {
        researchGroupPost,
        researchGroupMember,
        researchGroupLink,
        researchGroupDisk,
        researchGroup,
        project,
        projectMember,
        projectLink,
        projectDisk,
        projectPost,
        tutorial,
        announcement,
        user,
        auth,
    },
});
