import Vue from 'vue'
import Router from 'vue-router'

import announcements from "@/components/announcements/announcements"
import groupCatalog from "@/components/groupCatalog/groupCatalog"
import projectCatalog from "@/components/projectCatalog/projectCatalog"
import tutorialCatalog from "@/components/tutorialCatalog/tutorialCatalog"
import loginPage from "@/components/user/loginPage"
import registerPage from "@/components/user/registerPage"
import passwordReminder from "@/components/user/passwordReminder"
import group from "@/components/groupCatalog/group"

Vue.use(Router);

const router = new Router({
    routes: [
        {
            path: "/",
            name: "announcements",
            component: announcements,
        },
        {
            path: "/group-catalog",
            name: "groupCatalog",
            component: groupCatalog,
        },
        {
            path: "/project-catalog",
            name: "projectCatalog",
            component: projectCatalog,
        },
        {
            path: "/tutorial-catalog",
            name: "tutorialCatalog",
            component: tutorialCatalog,
        },
        {
            path: "/register",
            name: "register",
            component: registerPage,
        },
        {
            path: "/login",
            name: "login",
            component: loginPage,
        },
        {
            path: "/login/password-reminder",
            name: "passwordReminder",
            component: passwordReminder,
        },
        {
            path: "/group",
            name: "group",
            component: group,
        },
    ],
});
export default router;