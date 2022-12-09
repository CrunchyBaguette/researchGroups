import { api } from "@/services/api";

export default {
    fetchProjectMembers(projectId) {
        return api.get(`project-user/projectMembers/?projectId=${projectId}`).then((response) => response.data);
    },
    updateProjectMembers(data) {
        return api.post("project-user/updateMembers/", data).then((response) => response.data);
    },
};