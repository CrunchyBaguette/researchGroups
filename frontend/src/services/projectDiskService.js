import { api } from "@/services/api"

export default {
    fetchProjectDisks(params) {
        return api.post("project-disk/projectDisks/", params).then((response) => response.data)
    },
    postProjectDisk(params) {
        return api.post("project-disk/", params.disk).then((response) => response.data)
    },
    deleteProjectDisk(params) {
        return api.delete(`project-disk/${params.diskId}`).then((response) => response.data)
    },
    updateProjectDisk(params) {
        return api.post(`project-link/${params.DiskId}/`, params.disk).then((response) => response.data)
    },
    updateProjectDisks(params) {
        return api.post(`project-disk/updateDisks/`, params).then((response) => response.data);
    },
}