import researchGroupService from "@/services/researchGroupService";

const state = {
    researchGroups: [],
};

const getters = {
    researchGroups: (state) => {
        return state.researchGroups;
    },
};

const actions = {
    getResearchGroups({ commit }) {
        return new Promise((resolve, reject) => {
            researchGroupService.fetchGroups().then((data) => {
                commit("setResearchGroups", data);
                resolve();
            }).catch((err) => reject(err));
        });
    },
    addResearchGroup({ commit }, group) {
        return new Promise((resolve, reject) => {
            researchGroupService.postGroup(group).then((response) => {
                commit("addResearchGroup", group);
                resolve(response);
            }).catch((err) => reject(err));
        });
    }
};

const mutations = {
    setResearchGroups(state, data) {
        state.researchGroups = data;
    },
    addResearchGroup(state, group) {
        state.researchGroups.push(group)
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};