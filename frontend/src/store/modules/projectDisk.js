import projectDiskService from "@/services/projectDiskService";

const state = {
    projectDisks: []
};

const getters = {
    projectDisks: (state) => {
        return state.projectDisks;
    },
};

const actions = {
    getProjectDisks({ commit }, params) {
        return new Promise((resolve, reject) => {
            projectDiskService.fetchProjectDisks(params).then((response) => {
                commit("setProjectDisks", response.disks);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    addProjectDisk({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectDiskService.postProjectDisk(params).then((response) => {
                dispatch("getProjectDisks", { projectId: params.projectId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    deleteProjectDisk({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectDiskService.deleteProjectDisk(params).then((response) => {
                dispatch("getProjectLinks", { projectId: params.projectId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    updateProjectDisk({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectDiskService.updateProjectDisk(params).then((response) => {
                dispatch("getProjectDisks", { projectId: params.projectId });
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    updateProjectDisks({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectDiskService.updateProjectDisks(params).then((response) => {
                dispatch("getProjectDisks", params.projectId);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
};

const mutations = {
    setProjectDisks(state, data) {
        state.projectDisks = data
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};