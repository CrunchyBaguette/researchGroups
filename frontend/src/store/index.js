import Vue from "vue";
import Vuex from "vuex";

import researchGroup from "./modules/researchGroup";
import researchGroupMember from "./modules/researchGroupMember";
import researchGroupPost from "./modules/researchGroupPost";
import project from "./modules/project";
import projectMember from "./modules/projectMember";
import projectPost from "./modules/projectPost";
import announcement from "./modules/announcement";
import auth from "./modules/auth";
import user from "./modules/user";
import register from "./modules/register";

Vue.use(Vuex);

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
        register,
    },
});