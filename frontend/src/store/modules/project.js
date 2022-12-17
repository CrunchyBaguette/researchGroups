import projectService from "@/services/projectService";

const state = {
    project: {},
    projects: [],
    groupProjects: [],
};

const getters = {
    projects: (state) => {
        return state.projects;
    },
    project: (state) => {
        return state.project;
    },
    groupProjects: (state) => {
        return state.groupProjects
    }
};

const actions = {
    addProject({ commit }, project) {
        return new Promise((resolve, reject) => {
            projectService.postProject(project).then((response) => {
                commit("addProject", project);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    getProject({ commit }, params) {
        return new Promise((resolve, reject) => {
            projectService.fetchProject(params).then((response) => {
                commit("setProject", response);
                resolve(response);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    updateProject({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectService.patchProject(params).then((response) => {
                dispatch("getProjects");
                resolve(response);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    removeProject({ dispatch }, projectId) {
        return new Promise((resolve, reject) => {
            projectService.deleteProject(projectId).then(() => {
                dispatch("getProjects");
                dispatch("getGroupProjects");
                resolve();
            }).catch((err) => {
                reject(err);
            });
        });
    },
    getProjects({ commit }) {
        return new Promise((resolve, reject) => {
            projectService.fetchProjects().then((response) => {
                commit("setProjects", response);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    getGroupProjects({ commit }, group) {
        return new Promise((resolve, reject) => {
            projectService.fetchGroupProjects(group).then((response) => {
                commit("setGroupProjects", response);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    sendProjectEmailMessage({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectService.sendEmail(params).then((response) => {
                dispatch("getProjects");
                resolve(response);
            }).catch((err) => reject(err));
        });
    }
};

const mutations = {
    setProjects(state, data) {
        state.projects = data;
    },
    addProject(state, group) {
        state.projects.push(group)
    },
    setProject(state, data) {
        state.project = data;
    },
    setGroupProjects(state, data) {
        state.groupProjects = data
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};