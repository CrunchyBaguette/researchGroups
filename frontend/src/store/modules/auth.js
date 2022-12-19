import router from "@/router";
import { api } from "@/services/api";
import authService from "@/services/authService";
import jwt_decode from "jwt-decode"

const state = {
    accessToken: localStorage.getItem("accessToken") || "",
    refreshToken: localStorage.getItem("refreshToken") || "",
    refreshTokenCountdownID: "",
};

const getters = {
    accessToken: (state) => state.accessToken,
    accessTokenDecoded: (state) => jwt_decode(state.accessToken),
    refreshToken: (state) => state.refreshToken,
    refreshTokenCountdownID: (state) => state.refreshTokenCountdownID,
    isAuthenticated: (state) => !!state.accessToken,
    isAccessTokenExpired: (state, getters) => {
        const expire = getters.accessTokenDecoded.exp;
        if (new Date(expire * 1000) < new Date()) {
            return true;
        } else {
            return false;
        }
    },
    authUser: (state, getters) => getters.accessTokenDecoded.user
};

const actions = {
    getTokenPairs({ dispatch }, credentials) {
        return new Promise((resolve, reject) => {
            authService.fetchTokens(credentials).then((data) => {
                dispatch("setTokens", data);
                dispatch("beginTokenRefreshCountdown")
                resolve();
            }).catch((err) => {
                reject(err);
            })
        })
    },
    refreshAccessToken({ commit, getters, dispatch }) {
        return new Promise((resolve, reject) => {
            authService.fetchNewAccessToken(getters.refreshToken).then((data) => {
                commit("setAccessToken", data.access);
                dispatch("setAxiosHeaders", data.access);
                resolve();
            }).catch((err) => { reject(err); });
        })
    },
    beginTokenRefreshCountdown({ dispatch, commit }) {
        const ID = setInterval(() => {
            dispatch("refreshAccessToken").catch(() => {
                dispatch("logOut");
                router.push("/login");
            });
        }, 60000); // minuta
        commit("setTokenRefreshCountdownID", ID);
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

        const ID = getters.refreshTokenCountdownID;
        if (ID != "") {
            clearInterval(ID);
        }
    }
};

const mutations = {
    setAccessToken(state, token) {
        state.accessToken = token;
        localStorage.setItem("accessToken", token);
    },
    setTokenRefreshCountdownID(state, ID) {
        state.refreshTokenCountdownID = ID;
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