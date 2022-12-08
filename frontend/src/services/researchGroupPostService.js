import {api} from "@/services/api";

export default {
    fetchForumPost(params) {
        return api.get("research-group-post/" + (params.id !== undefined ? params.id : ""), {params}).then((response) => response.data);
    },
    postForumPost(data) {
        return api.post("research-group-post/", data).then((response) => response.data);
    },
    patchForumPost(update) {
        return api.patch(`research-group-post/${update.id}/`, update.payload).then((response) => response.data);
    },
    fetchGroupForumPosts(params) {
        return api.get("research-group-post/grouped/", {params}).then((response) => response.data);
    },
    deleteGroupForumPosts(params) {
        return api.delete(`research-group-post/${params.id}`,).then((response) => response.data);
    }
};