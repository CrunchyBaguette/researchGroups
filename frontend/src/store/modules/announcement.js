import announcementService from "@/services/announcementService";

const state = {
    announcement: {},
    announcements: [],
};

const getters = {
    announcements: (state) => {
        return state.announcements;
    },
    announcement: (state) => {
        return state.announcement;
    }
};

const actions = {
    addAnnouncement({ commit }, announcement) {
        return new Promise((resolve, reject) => {
            announcementService.postAnnouncement(announcement).then((response) => {
                commit("addAnnouncement", announcement);
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    getAnnouncement({ commit }, params) {
        return new Promise((resolve, reject) => {
            announcementService.fetchAnnouncement(params).then((data) => {
                commit("setAnnouncement", data);
                resolve();
            }).catch((err) => {
                reject(err);
            });
        });
    },
    updateAnnouncement({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            announcementService.patchAnnouncement(params).then(() => {
                dispatch("getAnnouncements");
                resolve();
            }).catch((err) => {
                reject(err);
            });
        });
    },
    removeAnnouncement({ dispatch }, announcementId) {
        return new Promise((resolve, reject) => {
            announcementService.deleteAnnouncement(announcementId).then(() => {
                dispatch("getAnnouncements");
                resolve();
            }).catch((err) => {
                reject(err);
            });
        });
    },
    getAnnouncements({ commit }) {
        return new Promise((resolve, reject) => {
            announcementService.fetchAnnouncements().then((data) => {
                commit("setAnnouncements", data);
                resolve();
            }).catch((err) => reject(err));
        });
    },
    sendEmailMessage({ dispatch }, params) {
        return new Promise((resolve, reject) => {
            announcementService.sendEmail(params).then((response) => {
                dispatch("getAnnouncements");
                resolve(response);
            }).catch((err) => reject(err));
        });
    }
};

const mutations = {
    setAnnouncements(state, data) {
        state.announcements = data;
    },
    addAnnouncement(state, group) {
        state.announcements.push(group)
    },
    setAnnouncement(state, data) {
        state.announcement = data;
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};