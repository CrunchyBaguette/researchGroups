import { api } from "@/services/api";

export default {
    fetchProject(projectId) {
        return api.get(`project/${projectId}/`).then((response) => response.data);
    },
    postProject(data) {
        return api.post("project/", data).then((response) => response.data);
    },
    patchProject(update) {
        return api.patch(`project/${update.id}/`, update.payload).then((response) => response.data);
    },
    deleteProject(projectId) {
        return api.delete(`project/${projectId}/`).then((response) => response.data);
    },
    fetchProjects() {
        return api.get("project/").then((response) => response.data);
    },
    fetchGroupProjects(params) {
        return api.get("project/grouped/", { params }).then((response) => response.data);
    }
};