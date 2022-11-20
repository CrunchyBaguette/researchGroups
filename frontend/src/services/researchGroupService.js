import { api } from "@/services/api";

export default {
    fetchGroups() {
        return api.get("research-group/").then((response) => response.data);
    },
    postGroup(data) {
        return api.post("research-group/", data).then((response) => response.data);
    }
};