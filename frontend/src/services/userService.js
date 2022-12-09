import { api } from "@/services/api";

export default {
    fetchUserResearchGroups(userId) {
        return api.get(`user/${userId}/researchGroups/`).then((response) => response.data);
    },
    fetchUserProjects(userId) {
        return api.get(`user/${userId}/projects/`).then((response) => response.data);
    },
    fetchUserAdminResearchGroups(userId) {
        return api.get(`user/${userId}/adminResearchGroups/`).then((response) => response.data);
    },
};