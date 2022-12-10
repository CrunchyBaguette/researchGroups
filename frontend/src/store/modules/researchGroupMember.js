import researchGroupMemberService from "@/services/researchGroupMemberService";

const state = {
    researchGroupMembers: []
};

const getters = {
    researchGroupMembers: (state) => {
        return state.researchGroupMembers;
    },
};

const actions = {
    getResearchGroupMembers({ commit }, researchGroupId) {
        return new Promise((resolve, reject) => {
            researchGroupMemberService.fetchGroupMembers(researchGroupId).then((response) => {
                commit("setResearchGroupMembers", response.members);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    updateResearchGroupMembers({ dispatch }, data) {
        return new Promise((resolve, reject) => {
            researchGroupMemberService.updateGroupMembers(data).then((response) => {
                dispatch("getResearchGroupMembers", data.researchGroupId);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
};

const mutations = {
    setResearchGroupMembers(state, data) {
        state.researchGroupMembers = data
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};