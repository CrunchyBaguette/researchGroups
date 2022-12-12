import { api } from "@/services/api"

export default {
    fetchGroupLinks(params) {
        return api.post("research-group-link/groupLinks/", params).then((response) => response.data)
    },
    postGroupLink(params) {
        return api.post("research-group-link/", params.link).then((response) => response.data)
    },
    deleteGroupLink(params) {
        return api.delete(`research-group-link/${params.linkId}`).then((response) => response.data)
    },
    updateGroupLink(params) {
        return api.patch(`research-group-link/${params.linkId}/`, params.link).then((response) => response.data)
    },
    updateGroupLinks(params) {
        return api.post(`research-group-link/updateLinks/`, params).then((response) => response.data);
    },
}