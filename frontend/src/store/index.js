import Vue from "vue";
import Vuex from "vuex";

import researchGroup from "./modules/researchGroup";
import groupForumPost from "./modules/groupForumPost";
import auth from "./modules/auth";

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        groupForumPost,
        researchGroup,
        auth,
    },
});