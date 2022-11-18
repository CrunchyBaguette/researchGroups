import { api } from "@/services/api";

export default {
    fetchGroups() {
        return api.get("research-group/").then((response) => response.data);
    },
};