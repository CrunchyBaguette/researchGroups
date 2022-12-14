import axios from "axios";
import store from "@/store"

const api = axios.create({
    baseURL: "http://localhost:8000/api", //tu najlepiej żeby to dało się zmienić w jednym miejscu najlepiej żeby można to było ustawić w czasie buildu
    timeout: 5000,
    headers: {
        "Content-Type": "application/json",
    },
});

var pendingRequests = 0;

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
        store.dispatch["auth/logOut"];
        return Promise.reject(error);
    }
);

export { api, pendingRequests };