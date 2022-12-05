import { api } from "@/services/api";

export default {
    fetchFroumPost(params) {
        return api.get("research-group-post/", { params }).then((response) => response.data);
    },
    postForumPost(data) {
        return api.post("research-group-post/", data).then((response) => response.data);
    },
    patchForumPost(update) {
        return api.patch(`research-group-post/${update.id}/`, update.payload).then((response) => response.data);
    },
    fetchGroupForumPosts(params) {
        return api.get("research-group-post/grouped/", { params }).then((response) => response.data);
    }
};