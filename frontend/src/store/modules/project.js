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
            projectService.fetchProject(params).then((data) => {
                commit("setProject", data);
                resolve();
            }).catch((err) => {
                reject(err);
            });
        });
    },
    updateProject({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectService.patchProject(params).then(() => {
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
            projectService.fetchProjects().then((data) => {
                commit("setProjects", data);
                resolve();
            }).catch((err) => reject(err));
        });
    },
    getGroupProjects({ commit }, group) {
        return new Promise((resolve, reject) => {
            projectService.fetchGroupProjects(group).then((data) => {
                commit("setGroupProjects", data);
                resolve();
            }).catch((err) => reject(err));
        });
    },
};

const mutations = {
    setProjects(state, data) {
        state.Projects = data;
    },
    addProject(state, group) {
        state.Projects.push(group)
    },
    setProject(state, data) {
        state.Project = data;
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