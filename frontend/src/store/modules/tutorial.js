import tutorialService from "@/services/tutorialService";

const state = {
    tutorial: {},
    tutorials: [],
    researchGroupTutorials: [],
    projectTutorials: [],
};

const getters = {
    tutorial: (state) => {
        return state.tutorial;
    },
    tutorials: (state) => {
        return state.tutorials;
    },
    researchGroupTutorials: (state) => {
        return state.researchGroupTutorials;
    },
    projectTutorials: (state) => {
        return state.projectTutorials;
    },
};

const actions = {
    addTutorial({ commit }, tutorial) {
        return new Promise((resolve, reject) => {
            tutorialService.postTutorial(tutorial).then((response) => {
                commit("addTutorial", tutorial);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    getTutorial({ commit }, tutorialId) {
        return new Promise((resolve, reject) => {
            tutorialService.fetchTutorial(tutorialId).then((response) => {
                commit("setTutorial", response);
                resolve(response);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    getTutorials({ commit }) {
        return new Promise((resolve, reject) => {
            tutorialService.fetchTutorials().then((response) => {
                commit("setTutorials", response);
                resolve(response);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    getResearchGroupTutorials({ commit }, researchGroupId) {
        return new Promise((resolve, reject) => {
            tutorialService.fetchResearchGroupTutorials(researchGroupId).then((response) => {
                commit("setResearchGroupTutorials", response);
                resolve(response);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    getProjectTutorials({ commit }, projectId) {
        return new Promise((resolve, reject) => {
            tutorialService.fetchProjectTutorials(projectId).then((response) => {
                commit("setProjectTutorials", response);
                resolve(response);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    updateTutorial({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            tutorialService.patchTutorial(params).then((response) => {
                dispatch("getTutorial", params.tutorialId);
                dispatch("getTutorials");
                dispatch("getResearchGroupTutorials");
                dispatch("getProjectTutorials");
                resolve(response);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    removeTutorial({ dispatch }, tutorialId) {
        return new Promise((resolve, reject) => {
            tutorialService.deleteTutorial(tutorialId).then(() => {
                dispatch("getTutorials");
                dispatch("getResearchGroupTutorials");
                dispatch("getProjectTutorials");
                resolve();
            }).catch((err) => {
                reject(err);
            });
        });
    },
};

const mutations = {
    setTutorial(state, tutorial) {
        state.tutorial = tutorial;
    },
    addTutorial(state, tutorial) {
        state.tutorials.push(tutorial);
    },
    setTutorials(state, tutorials) {
        state.tutorials = tutorials;
    },
    setResearchGroupTutorials(state, tutorials) {
        state.researchGroupTutorials = tutorials;
    },
    setProjectTutorials(state, tutorials) {
        state.projectTutorials = tutorials;
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};