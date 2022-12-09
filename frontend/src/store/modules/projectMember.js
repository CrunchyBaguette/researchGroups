import projectMemberService from "@/services/projectMemberService";

const state = {
    projectMembers: []
};

const getters = {
    projectMembers: (state) => {
        return state.projectMembers;
    },
};

const actions = {
    getProjectMembers({ commit }, projectId) {
        return new Promise((resolve, reject) => {
            projectMemberService.fetchProjectMembers(projectId).then((response) => {
                commit("setProjectMembers", response.members);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    updateProjectMembers({ dispatch }, data) {
        return new Promise((resolve, reject) => {
            projectMemberService.updateProjectMembers(data).then((response) => {
                dispatch("getProjectMembers", data.projectId);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
};

const mutations = {
    setProjectMembers(state, data) {
        state.projectMembers = data
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};