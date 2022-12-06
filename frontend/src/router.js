import Vue from 'vue'
import Router from 'vue-router'

import announcementCatalog from "@/components/announcementCatalog/announcementCatalog"
import addAnnouncement from "@/components/announcementCatalog/addAnnouncement"
import announcementPanel from "@/components/announcementPanel/announcementPanel"
import groupCatalog from "@/components/groupCatalog/groupCatalog"
import addGroup from "@/components/groupCatalog/addGroup"
import projectCatalog from "@/components/projectCatalog/projectCatalog"
import tutorialCatalog from "@/components/tutorialCatalog/tutorialCatalog"
import loginPage from "@/components/user/loginPage"
import registerPage from "@/components/user/registerPage"
import passwordReminder from "@/components/user/passwordReminder"
import groupPanel from "@/components/groupPanel/groupPanel"
import groupTutorials from "@/components/tutorialCatalog/groupTutorials"
import forum from "@/components/forum/forum"

Vue.use(Router);

const router = new Router({
    routes: [
        {
            path: "/",
            name: "announcementCatalog",
            component: announcementCatalog,
        },
        {
            path: "/announcement/:id",
            name: "announcement",
            component: announcementPanel,
        },
        {
            path: "/add-announcement",
            name: "addAnnouncement",
            component: addAnnouncement,
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
            path: "/group/:id",
            name: "group",
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