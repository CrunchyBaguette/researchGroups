import axios from "axios"

const api = axios.create({
    baseURL: "/api",
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
        return Promise.reject(error);
    }
);

export { api, pendingRequests };