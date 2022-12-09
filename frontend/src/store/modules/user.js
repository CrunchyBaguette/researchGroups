import userService from "@/services/userService";

const state = {
    userResearchGroups: [],
    userAdminResearchGroups: [],
    userProjects: [],
};

const getters = {
    userResearchGroups: (state) => {
        return state.userResearchGroups;
    },
    userAdminResearchGroups: (state) => {
        return state.userAdminResearchGroups;
    },
    userProjects: (state) => {
        return state.userProjects;
    }
};

const actions = {
    getUserResearchGroups({ commit }, userId) {
        return new Promise((resolve, reject) => {
            userService.fetchUserResearchGroups(userId).then((response) => {
                commit("setUserResearchGroups", response);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    getUserAdminResearchGroups({ commit }, userId) {
        return new Promise((resolve, reject) => {
            userService.fetchUserAdminResearchGroups(userId).then((response) => {
                commit("setUserAdminResearchGroups", response);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    getUserProjects({ commit }, userId) {
        return new Promise((resolve, reject) => {
            userService.fetchUserProjects(userId).then((response) => {
                commit("setUserProjects", response);
                resolve(response);
            }).catch((err) => reject(err));
        });
    }
};

const mutations = {
    setUserResearchGroups(state, data) {
        state.userResearchGroups = data
    },
    setUserAdminResearchGroups(state, data) {
        state.userAdminResearchGroups = data
    },
    setUserProjects(state, data) {
        state.userProjects = data
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};