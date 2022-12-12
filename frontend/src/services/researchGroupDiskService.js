import { api } from "@/services/api"

export default {
    fetchGroupDisks(params) {
        return api.post("research-group-disk/groupDisks/", params).then((response) => response.data)
    },
    postGroupDisk(params) {
        return api.post("research-group-disk/", params.disk).then((response) => response.data)
    },
    deleteGroupDisk(params) {
        return api.delete(`research-group-disk/${params.diskId}`).then((response) => response.data)
    },
    updateGroupDisk(params) {
        return api.patch(`research-group-disk/${params.diskId}/`, params.disk).then((response) => response.data)
    },
    updateGroupDisks(params) {
        return api.post(`research-group-disk/updateDisks/`, params).then((response) => response.data);
    },
}