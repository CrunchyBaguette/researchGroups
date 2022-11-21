import Vue from 'vue'
import Router from 'vue-router'

import announcements from "@/components/announcements/announcements"
import groupCatalog from "@/components/groupCatalog/groupCatalog"
import addGroup from "@/components/groupCatalog/addGroup"
import projectCatalog from "@/components/projectCatalog/projectCatalog"
import tutorialCatalog from "@/components/tutorialCatalog/tutorialCatalog"
import loginPage from "@/components/user/loginPage"
import registerPage from "@/components/user/registerPage"
import passwordReminder from "@/components/user/passwordReminder"
import groupPanel from "@/components/groupPanel/groupPanel"
import editGroup from "@/components/groupPanel/editGroup"
import groupTutorials from "@/components/tutorialCatalog/groupTutorials"
import forum from "@/components/forum/forum"

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
            path: "/add-group",
            name: "addGroup",
            component: addGroup,
        },
        {
            path: "/edit-group",
            name: "editGroup",
            component: editGroup,
        },
        {
            path: "/group-panel",
            name: "groupPanel",
            component: groupPanel,
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
            path: "/group-tutorials",
            name: "groupTutorials",
            component: groupTutorials,
        },
        {
            path: "/forum",
            name: "forum",
            component: forum,
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

    ],
});
export default router;