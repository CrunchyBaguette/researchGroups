import Vue from 'vue'
import Router from 'vue-router'

import announcementsCatalog from "@/components/announcementCatalog/announcementCatalog"
import addAnnouncement from "@/components/announcementCatalog/addAnnouncement"
import announcementPanel from "@/components/announcementPanel/announcementPanel"
import groupCatalog from "@/components/groupCatalog/groupCatalog"
import addGroup from "@/components/groupCatalog/addGroup"
import projectCatalog from "@/components/projectCatalog/projectCatalog"
import addProject from "@/components/projectCatalog/addProject"
import projectPanel from "@/components/projectPanel/projectPanel"
import tutorialPanel from "@/components/tutorialPanel/tutorialPanel"
import addTutorial from "@/components/tutorialCatalog/addTutorial"
import tutorialCatalog from "@/components/tutorialCatalog/tutorialCatalog"
import loginPage from "@/components/user/loginPage"
import registerPage from "@/components/user/registerPage"
import passwordReminder from "@/components/user/passwordReminder"
import passwordReset from "@/components/user/passwordReset"
import groupPanel from "@/components/groupPanel/groupPanel"
import groupTutorials from "@/components/tutorialCatalog/groupTutorials"
import forum from "@/components/forum/forum"

Vue.use(Router);

const router = new Router({
    routes: [
        {
            path: "/",
            name: "announcements",
            component: announcementsCatalog,
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
            path: "/add-project",
            name: "addProject",
            component: addProject,
        },
        {
            path: "/project/:id",
            name: "project",
            component: projectPanel,
        },
        {
            path: "/tutorial/:id",
            name: "tutorial",
            component: tutorialPanel,
        },
        {
            path: "/add-tutorial",
            name: "addTutorial",
            component: addTutorial,
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
        {
            path: "/login/password-reset",
            name: "passwordReset",
            component: passwordReset,
        },

    ],
});
export default router;