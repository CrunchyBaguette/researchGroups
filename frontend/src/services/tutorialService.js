import { api } from "@/services/api"

export default {
    fetchTutorial(tutorialId) {
        return api.get(`tutorial/${tutorialId}/`).then((response) => response.data);
    },
    fetchTutorials() {
        return api.get("tutorial/").then((response) => response.data)
    },
    fetchResearchGroupTutorials(researchGroupId) {
        return api.get(`tutorial/?researchGroupId=${researchGroupId}/`).then((response) => response.data)
    },
    fetchProjectTutorials(projectId) {
        return api.get(`tutorial/?projectId=${projectId}/`).then((response) => response.data)
    },
    postTutorial(params) {
        return api.post("tutorial/", params).then((response) => response.data)
    },
    patchTutorial(params) {
        return api.patch(`tutorial/${params.tutorialId}/`, params.tutorial).then((response) => response.data)
    },
    deleteTutorial(tutorialId) {
        return api.delete(`tutorial/${tutorialId}/`).then((response) => response.data)
    },
}