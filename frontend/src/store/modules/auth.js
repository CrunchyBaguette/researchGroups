import { api } from "@/services/api";
import authService from "@/services/authService";
import jwt_decode from "jwt-decode"

const state = {
    accessToken: localStorage.getItem("accessToken") || "",
    refreshToken: localStorage.getItem("refreshToken") || "",
};

const getters = {
    accessToken: (state) => state.accessToken,
    accessTokenDecoded: (state) => jwt_decode(state.accessToken),
    refreshToken: (state) => state.refreshToken,
    isAuthenticated: (state) => !!state.accessToken,
    authUser: (state, getters) => getters.accessTokenDecoded.user
};

const actions = {
    getTokenPairs({ dispatch }, credentials) {
        return new Promise((resolve, reject) => {
            authService.fetchTokens(credentials).then((data) => {
                dispatch("setTokens", data);
                resolve();
            }).catch((err) => {
                reject(err);
            })
        })
    },
    setTokens({ commit, dispatch }, data) {
        commit("setAccessToken", data.access);
        commit("setRefreshToken", data.refresh);
        dispatch("setAxiosHeaders", data.access);
    },
    setAxiosHeaders({ getters }) {
        api.defaults.headers.common["Authorization"] = "Bearer " + getters.accessToken;
    },
    removeAxiosHeaders() {
        delete api.defaults.headers.common["Authorization"];
    },
    logOut({ commit, getters, dispatch }) {
        authService.logOutUser(getters.refreshToken);
        commit("removeTokens");
        dispatch("removeAxiosHeaders");
    }
};

const mutations = {
    setAccessToken(state, token) {
        state.accessToken = token;
        localStorage.setItem("accessToken", token);
    },
    setRefreshToken(state, token) {
        state.refreshToken = token;
        localStorage.setItem("refreshToken", token);
    },
    removeTokens(state) {
        state.accessToken = "";
        state.refreshToken = "";
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refreshToken");
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}