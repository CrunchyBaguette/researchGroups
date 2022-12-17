import { api } from "@/services/api";

export default {
    fetchAnnouncement(announcementId) {
        return api.get(`announcement/${announcementId}/`).then((response) => response.data);
    },
    postAnnouncement(data) {
        return api.post("announcement/", data).then((response) => response.data);
    },
    patchAnnouncement(update) {
        return api.patch(`announcement/${update.id}/`, update.payload).then((response) => response.data);
    },
    deleteAnnouncement(announcementId) {
        return api.delete(`announcement/${announcementId}/`).then((response) => response.data);
    },
    fetchAnnouncements() {
        return api.get("announcement/").then((response) => response.data);
    },
    sendEmail(params) {
        return api.post("announcement/email/", params).then((response) => response.data);
    }
};