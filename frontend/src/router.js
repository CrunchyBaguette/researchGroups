import Vue from 'vue'
import Router from 'vue-router'

import announcements from "@/components/announcements/announcements"
import groupCatalog from "@/components/groupCatalog/groupCatalog"
import addGroup from "@/components/groupCatalog/addGroup"
import projectCatalog from "@/components/projectCatalog/projectCatalog"
import addProject from "@/components/projectCatalog/addProject"
import projectPanel from "@/components/projectPanel/projectPanel"
import tutorialCatalog from "@/components/tutorialCatalog/tutorialCatalog"
import loginPage from "@/components/user/loginPage"
import registerPage from "@/components/user/registerPage"
import passwordReminder from "@/components/user/passwordReminder"
import groupPanel from "@/components/groupPanel/groupPanel"
import groupTutorials from "@/components/tutorialCatalog/groupTutorials"
import projectForum from "@/components/forum/projectForum";
import groupForum from "@/components/forum/groupForum";
import groupPost from "@/components/forum/groupPost";
import projectPost from "@/components/forum/projectPost";

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
            path: "/group/:groupId/forum",
            name: "groupForum",
            component: groupForum,
        },
        {
            path: "/group/:groupId/post/:postId",
            name: "groupPost",
            component: groupPost,
        },
        {
            path: "/project/:projectId/forum",
            name: "projectForum",
            component: projectForum,
        },
        {
            path: "/project/:projectId/post/:postId",
            name: "projectPost",
            component: projectPost,
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

        // { strona dla error 404 - router do dowolnego url
        //     path: '/:pathMatch(.*)*',
        //     name: 'NotFound',
        //     component: NotFound
        // },

    ],
});
export default router;