import researchGroupDiskService from "@/services/researchGroupDiskService";

const state = {
    researchGroupDisks: []
};

const getters = {
    researchGroupDisks: (state) => {
        return state.researchGroupDisks;
    },
};

const actions = {
    getResearchGroupDisks({ commit }, params) {
        return new Promise((resolve, reject) => {
            researchGroupDiskService.fetchGroupDisks(params).then((response) => {
                commit("setResearchGroupDisks", response.disks);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    addResearchGroupDisk({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            researchGroupDiskService.postGroupDisk(params).then((response) => {
                dispatch("getResearchGroupDisks", { researchGroupId: params.researchGroupId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    deleteResearchGroupDisk({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            researchGroupDiskService.deleteGroupDisk(params).then((response) => {
                dispatch("getResearchGroupDisks", { researchGroupId: params.researchGroupId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    updateResearchGroupDisk({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            researchGroupDiskService.updateGroupDisk(params).then((response) => {
                dispatch("getResearchGroupDisks", { researchGroupId: params.researchGroupId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    updateResearchGroupDisks({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            researchGroupDiskService.updateGroupDisks(params).then((response) => {
                dispatch("getResearchGroupDisks", params.researchGroupId);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
};

const mutations = {
    setResearchGroupDisks(state, data) {
        state.researchGroupDisks = data
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};