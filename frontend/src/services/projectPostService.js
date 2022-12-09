import { api } from "@/services/api";

export default {
    fetchForumPost(params) {
        return api.get("project-post/" + (params.id !== undefined ? params.id : ""), { params }).then((response) => response.data);
    },
    postForumPost(data) {
        return api.post("project-post/", data).then((response) => response.data);
    },
    patchForumPost(update) {
        return api.patch(`project-post/${update.id}/`, update).then((response) => response.data);
    },
    fetchProjectForumPosts(params) {
        return api.get("project-post/grouped/", { params }).then((response) => response.data);
    },
    deleteProjectForumPosts(params) {
        return api.delete(`project-post/${params.id}`,).then((response) => response.data);
    }
};