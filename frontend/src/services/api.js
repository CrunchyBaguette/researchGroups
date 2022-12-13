import axios from "axios";
import auth from "@/store/modules/auth";

const api = axios.create({
    baseURL: "http://localhost:8000/api", //tu najlepiej żeby to dało się zmienić w jednym miejscu najlepiej żeby można to było ustawić w czasie buildu
    timeout: 5000,
    headers: auth.isAuthenticated ? {
        "Content-Type": "application/json",
        "Authorization": auth.state.accessToken === undefined ? "" : "Bearer " + auth.state.accessToken,
    } : {
        "Content-Type": "application/json"
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

api.interceptors.response.use(
    function (response) {
        pendingRequests--;
        return response;
    },
    function (error) {
        pendingRequests--;
        return Promise.reject(error);
    }
);

export { api, pendingRequests };