import projectPostService from "@/services/projectPostService";

const state = {
    forumPost: {},
    forumPosts: [],
};

const getters = {
    forumPosts: (state) => {
        return state.forumPosts;
    },
    forumPost: (state) => {
        return state.forumPost;
    }
};

const actions = {
    addForumPost({ commit }, post) {
        return new Promise((resolve, reject) => {
            projectPostService.postForumPost(post).then((response) => {
                commit("addForumPost", post);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    getForumPost({ commit }, params) {
        return new Promise((resolve, reject) => {
            projectPostService.fetchForumPost(params).then((data) => {
                commit("setForumPost", data);
                resolve(data);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    updateForumPost({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectPostService.patchForumPost(params).then((data) => {
                dispatch("getForumPosts", {project: data.project});
                resolve(data);
            }).catch((err) => {
                reject(err);
            });
        });
    },
    deleteForumPost({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectPostService.deleteProjectForumPosts(params).then(() => {
                dispatch("getForumPosts", {project: params.projectId});
                resolve();
            }).catch((err) => {
                reject(err);
            });
        });
    },
    getForumPosts({ commit }, group) {
        return new Promise((resolve, reject) => {
            projectPostService.fetchProjectForumPosts(group).then((data) => {
                commit("setForumPosts", data);
                resolve(data);
            }).catch((err) => reject(err));
        });
    },
};

const mutations = {
    setForumPosts(state, data) {
        state.forumPosts = data.posts;
    },
    addForumPost(state, post) {
        state.forumPosts.push(post)
    },
    setForumPost(state, data) {
        state.forumPost = data;
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};