import { api } from "@/services/api";

export default {
    fetchForumPost(params) {
        return api.get("project-post/", { params }).then((response) => response.data);
    },
    postForumPost(data) {
        return api.post("project-post/", data).then((response) => response.data);
    },
    patchForumPost(update) {
        return api.patch(`project-post/${update.id}/`, update.payload).then((response) => response.data);
    },
    fetchProjectForumPosts(params) {
        return api.get("project-post/grouped/", { params }).then((response) => response.data);
    }
};