import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000/api", //tu najlepiej żeby to dało się zmienić w jednym miejscu najlepiej żeby można to było ustawić w czasie buildu
    timeout: 5000,
    headers: {
        "Content-Type": "application/json",
    },
});

const api_auth = axios.create({
    baseURL: "http://localhost:8000/api-auth", //tu najlepiej żeby to dało się zmienić w jednym miejscu najlepiej żeby można to było ustawić w czasie buildu
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