import { api } from "@/services/api";

export default {
    fetchProjectMembers(params) {
        return api.get("project-user/projectMembers/", { params }).then((response) => response.data);
    },
    updateProjectMembers(data) {
        return api.post("project-user/updateMembers/", data).then((response) => response.data);
    },
};