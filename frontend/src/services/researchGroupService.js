import { api } from "@/services/api";

export default {
    fetchGroup(researchGroupId) {
        return api.get(`research-group/${researchGroupId}/`).then((response) => response.data);
    },
    postGroup(data) {
        return api.post("research-group/", data).then((response) => response.data);
    },
    patchGroup(update) {
        return api.patch(`research-group/${update.id}/`, update.payload).then((response) => response.data);
    },
    deleteGroup(researchGroupId) {
        return api.delete(`research-group/${researchGroupId}/`).then((response) => response.data);
    },
    fetchGroups() {
        return api.get("research-group/").then((response) => response.data);
    },
    sendEmail(params) {
        return api.post("research-group/email/", params).then((response) => response.data);
    }
};