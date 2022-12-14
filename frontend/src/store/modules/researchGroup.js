import researchGroupService from "@/services/researchGroupService";

const state = {
    researchGroup: {},
    researchGroups: [],
};

const getters = {
    researchGroups: (state) => {
        return state.researchGroups;
    },
    researchGroup: (state) => {
        return state.researchGroup;
    }
};

const actions = {
    addResearchGroup({ commit }, group) {
        return new Promise((resolve, reject) => {
            researchGroupService.postGroup(group).then((response) => {
                commit("addResearchGroup", group);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    getResearchGroup({ commit }, params) {
        return new Promise((resolve, reject) => {
            researchGroupService.fetchGroup(params).then((response) => {
                commit("setGroup", response);
                resolve(response);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    updateResearchGroup({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            researchGroupService.patchGroup(params).then((response) => {
                dispatch("getResearchGroups");
                resolve(response);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    removeResearchGroup({ dispatch }, researchGroupId) {
        return new Promise((resolve, reject) => {
            researchGroupService.deleteGroup(researchGroupId).then(() => {
                dispatch("getResearchGroups");
                resolve();
            }).catch((err) => {
                reject(err);
            });
        });
    },
    getResearchGroups({ commit }) {
        return new Promise((resolve, reject) => {
            researchGroupService.fetchGroups().then((response) => {
                commit("setResearchGroups", response);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
};

const mutations = {
    setResearchGroups(state, data) {
        state.researchGroups = data;
    },
    addResearchGroup(state, group) {
        state.researchGroups.push(group)
    },
    setGroup(state, data) {
        state.researchGroup = data;
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};