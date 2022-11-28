import { api } from "@/services/api";

export default {
    fetchAnnouncement(params) {
        return api.get("announcement/", { params }).then((response) => response.data);
    },
    postAnnouncement(data) {
        return api.post("announcement/", data).then((response) => response.data);
    },
    patchAnnouncement(update) {
        return api.patch(`announcement/${update.id}`, update.payload).then((response) => response.data);
    },
    fetchAnnouncements() {
        return api.get("announcement/").then((response) => response.data);
    }
};