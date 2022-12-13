import { api_auth } from "@/services/api";

export default {
    register(params) {
        return api_auth.post("register/", params).then((response) => response.data);
    },
    finishRegister(token) {
        return api_auth.get(`register/?token=${token}`).then((response) => response.data);
    },
    resetPasswordEmail(params) {
        return api_auth.post("reset-pass/", params).then((response) => response.data);
    },
    resetPassword(params) {
        return api_auth.put("reset-pass/", params).then((response) => response.data);
    }
};