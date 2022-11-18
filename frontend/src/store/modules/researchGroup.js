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
};

const mutations = {
    setResearchGroups(state, data) {
        state.researchGroups = data;
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};