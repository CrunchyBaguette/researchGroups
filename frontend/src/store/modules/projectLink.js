import projectLinkService from "@/services/projectLinkService";

const state = {
    projectLinks: []
};

const getters = {
    projectLinks: (state) => {
        return state.projectLinks;
    },
};

const actions = {
    getProjectLinks({ commit }, params) {
        return new Promise((resolve, reject) => {
            projectLinkService.fetchProjectLinks(params).then((response) => {
                commit("setProjectLinks", response.links);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    addProjectLink({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectLinkService.postProjectLink(params).then((response) => {
                dispatch("getProjectLinks", { projectId: params.projectId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    deleteProjectLink({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectLinkService.deleteProjectLink(params).then((response) => {
                dispatch("getProjectLinks", { projectId: params.projectId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    updateProjectLink({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectLinkService.updateProjectLink(params).then((response) => {
                dispatch("getProjectLinks", { projectId: params.projectId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    updateProjectLinks({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectLinkService.updateProjectLinks(params).then((response) => {
                dispatch("getProjectLinks", params.projectId);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
};

const mutations = {
    setProjectLinks(state, data) {
        state.projectLinks = data
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};