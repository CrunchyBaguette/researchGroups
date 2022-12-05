import { api } from "@/services/api"

export default {
    fetchGroupLinks(params) {
        return api.post("research-group-link/groupLinks/", params).then((response) => response.data)
    },
    updateGroupLinks(params) {
        return api.post(`research-group-link/updateLinks/`, params).then((response) => response.data);
    },
}