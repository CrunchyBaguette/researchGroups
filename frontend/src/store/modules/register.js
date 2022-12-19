import registerService from "@/services/registerService";

const state = {
    user: {},
    message: "",
};

const getters = {
    user: (state) => state.user,
    message: (state) => state.message,
};

const actions = {
    registerUser({ commit }, params) {
        return new Promise((resolve, reject) => {
            registerService.register(params).then((response) => {
                commit("setUser", params)
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    finishRegisterUser({ commit }, token) {
        return new Promise((resolve, reject) => {
            registerService.finishRegister(token).then((response) => {
                commit("setUser", response.user)
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    sendResetEmail({ commit }, params) {
        return new Promise((resolve, reject) => {
            registerService.resetPasswordEmail(params).then((response) => {
                commit("setMessage", response.message)
                resolve(response);
            }).catch((err) => reject(err));
        });
    },
    resetUserPassword({ commit }, params) {
        return new Promise((resolve, reject) => {
            registerService.resetPassword(params).then((response) => {
                commit("setMessage", response.message)
                commit("setUser", response.user)
                resolve(response);
            }).catch((err) => reject(err));
        });
    }
};

const mutations = {
    setUser(state, params) {
        state.user = params;
    },
    setMessage(state, message) {
        state.message = message;
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};