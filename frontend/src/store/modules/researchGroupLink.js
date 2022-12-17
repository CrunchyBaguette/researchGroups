import researchGroupLinkService from "@/services/researchGroupLinkService";

const state = {
    researchGroupLinks: []
};

const getters = {
    researchGroupLinks: (state) => {
        return state.researchGroupLinks;
    },
};

const actions = {
    getResearchGroupLinks({ commit }, params) {
        return new Promise((resolve, reject) => {
            researchGroupLinkService.fetchGroupLinks(params).then((response) => {
                commit("setResearchGroupLinks", response.links);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    addResearchGroupLink({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            researchGroupLinkService.postGroupLink(params).then((response) => {
                dispatch("getResearchGroupLinks", { researchGroupId: params.researchGroupId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    deleteResearchGroupLink({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            researchGroupLinkService.deleteGroupLink(params).then((response) => {
                dispatch("getResearchGroupLinks", { researchGroupId: params.researchGroupId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    updateResearchGroupLink({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            researchGroupLinkService.updateGroupLink(params).then((response) => {
                dispatch("getResearchGroupLinks", { researchGroupId: params.researchGroupId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    updateResearchGroupLinks({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            researchGroupLinkService.updateGroupLinks(params).then((response) => {
                dispatch("getResearchGroupLinks", params.researchGroupId);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
};

const mutations = {
    setResearchGroupLinks(state, data) {
        state.researchGroupLinks = data
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};