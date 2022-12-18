import axios from "axios";
import auth from "@/store/modules/auth";
import store from "@/store"
import Cookies from "js-cookie"

const api = axios.create({
    baseURL: "http://localhost:8000/api", //tu najlepiej żeby to dało się zmienić w jednym miejscu najlepiej żeby można to było ustawić w czasie buildu
    timeout: 5000,
    headers: auth.isAuthenticated ? {
        "Content-Type": "application/json",
        "X-CSRFToken": Cookies.get("csrftoken"),
        "Authorization": auth.state.accessToken === undefined ? "" : "Bearer " + auth.state.accessToken,
    } : {
        "Content-Type": "application/json",
        "X-CSRFToken": Cookies.get("csrftoken"),
    },
});

const api_auth = axios.create({
    baseURL: "http://localhost:8000/api-auth", //tu najlepiej żeby to dało się zmienić w jednym miejscu najlepiej żeby można to było ustawić w czasie buildu
    timeout: 5000,
    headers: {
        "Content-Type": "application/json",
    },
});

let pendingRequests = 0;

api.interceptors.request.use(
    function (config) {
        pendingRequests++;
        return config;
    },
    function (error) {
        return Promise.reject(error);
    }
);

api_auth.interceptors.request.use(
    function (config) {
        pendingRequests++;
        return config;
    },
    function (error) {
        return Promise.reject(error);
    }
);

api.interceptors.response.use(
    function (response) {
        pendingRequests--;
        return response;
    },
    function (error) {
        pendingRequests--;
        store.dispatch["auth/logOut"];
        return Promise.reject(error);
    }
);

api_auth.interceptors.response.use(
    function (response) {
        pendingRequests--;
        return response;
    },
    function (error) {
        pendingRequests--;
        return Promise.reject(error);
    }
);

export { api, api_auth, pendingRequests };