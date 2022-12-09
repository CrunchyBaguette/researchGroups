import { api } from "@/services/api";

export default {
    fetchGroupMembers(researchGroupId) {
        return api.get(`research-group-user/groupMembers/?researchGroupId=${researchGroupId}`).then((response) => response.data);
    },
    updateGroupMembers(data) {
        return api.post(`research-group-user/updateMembers/`, data).then((response) => response.data);
    },
};