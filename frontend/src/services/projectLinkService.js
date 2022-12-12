import { api } from "@/services/api"

export default {
    fetchProjectLinks(params) {
        return api.post("project-link/projectLinks/", params).then((response) => response.data)
    },
    postProjectLink(params) {
        return api.post("project-link/", params.link).then((response) => response.data)
    },
    deleteProjectLink(params) {
        return api.delete(`project-link/${params.linkId}`).then((response) => response.data)
    },
    updateProjectLink(params) {
        return api.post(`project-link/${params.linkId}/`, params.link).then((response) => response.data)
    },
    updateProjectLinks(params) {
        return api.post(`project-link/updateLinks/`, params).then((response) => response.data);
    },
}