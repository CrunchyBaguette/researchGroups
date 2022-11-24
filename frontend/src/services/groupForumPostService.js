import { api } from "@/services/api";

export default {
    fetchFroumPost(params) {
        return api.get("group-forum-post/", { params }).then((response) => response.data);
    },
    postForumPost(data) {
        return api.post("group-forum-post/", data).then((response) => response.data);
    },
    patchForumPost(update) {
        return api.patch(`group-forum-post/${update.id}/`, update.payload).then((response) => response.data);
    },
    fetchGroupForumPosts(params) {
        return api.get("group-forum-post/grouped/", { params }).then((response) => response.data);
    }
};