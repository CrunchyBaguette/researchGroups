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
                resolve();
            }).catch((err) => {
                reject(err);
            });
        });
    },
    updateForumPost({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            projectPostService.patchForumPost(params).then(() => {
                dispatch("getForumPosts");
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
                resolve();
            }).catch((err) => reject(err));
        });
    },
};

const mutations = {
    setForumPosts(state, data) {
        state.forumPosts = data;
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