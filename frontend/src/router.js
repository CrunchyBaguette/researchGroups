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
import projectForum from "@/components/forum/projectForum";
import groupForum from "@/components/forum/groupForum";
import groupPost from "@/components/forum/groupPost";
import projectPost from "@/components/forum/projectPost";
import store from './store'

Vue.use(Router);

const router = new Router({
    routes: [
        {
            path: "/",
            name: "announcements",
            component: announcementsCatalog,
            meta: {
                requiresAuth: false,
                requiresNoAuth: false,
            }
        },
        {
            path: "/announcement/:id",
            name: "announcement",
            component: announcementPanel,
            meta: {
                requiresAuth: false,
                requiresNoAuth: false,
            }
        },
        {
            path: "/add-announcement",
            name: "addAnnouncement",
            component: addAnnouncement,
            meta: {
                requiresAuth: true,
                requiresNoAuth: false,
            }
        },
        {
            path: "/group-catalog",
            name: "groupCatalog",
            component: groupCatalog,
            meta: {
                requiresAuth: false,
                requiresNoAuth: false,
            }
        },
        {
            path: "/add-group",
            name: "addGroup",
            component: addGroup,
            meta: {
                requiresAuth: true,
                requiresNoAuth: false,
            }
        },
        {
            path: "/group/:id",
            name: "group",
            component: groupPanel,
            meta: {
                requiresAuth: false,
                requiresNoAuth: false,
            }
        },
        {
            path: "/project-catalog",
            name: "projectCatalog",
            component: projectCatalog,
            meta: {
                requiresAuth: false,
                requiresNoAuth: false,
            }
        },
        {
            path: "/add-project",
            name: "addProject",
            component: addProject,
            meta: {
                requiresAuth: true,
                requiresNoAuth: false,
            }
        },
        {
            path: "/project/:id",
            name: "project",
            component: projectPanel,
            meta: {
                requiresAuth: false,
                requiresNoAuth: false,
            }
        },
        {
            path: "/tutorial/:id",
            name: "tutorial",
            component: tutorialPanel,
            meta: {
                requiresAuth: false,
                requiresNoAuth: false,
            }
        },
        {
            path: "/add-tutorial",
            name: "addTutorial",
            component: addTutorial,
            meta: {
                requiresAuth: true,
                requiresNoAuth: false,
            }
        },
        {
            path: "/tutorial-catalog",
            name: "tutorialCatalog",
            component: tutorialCatalog,
            meta: {
                requiresAuth: false,
                requiresNoAuth: false,
            }
        },
        {
            path: "/group-tutorials",
            name: "groupTutorials",
            component: groupTutorials,
            meta: {
                requiresAuth: false,
                requiresNoAuth: false,
            }
        },
        {
            path: "/group/:groupId/forum",
            name: "groupForum",
            component: groupForum,
            meta: {
                requiresAuth: true,
                requiresNoAuth: false,
            }
        },
        {
            path: "/group/:groupId/post/:postId",
            name: "groupPost",
            component: groupPost,
            meta: {
                requiresAuth: true,
                requiresNoAuth: false,
            }
        },
        {
            path: "/project/:projectId/forum",
            name: "projectForum",
            component: projectForum,
            meta: {
                requiresAuth: true,
                requiresNoAuth: false,
            }
        },
        {
            path: "/project/:projectId/post/:postId",
            name: "projectPost",
            component: projectPost,
            meta: {
                requiresAuth: true,
                requiresNoAuth: false,
            }
        },
        {
            path: "/register",
            name: "register",
            component: registerPage,
            meta: {
                requiresAuth: false,
                requiresNoAuth: true,
            }
        },
        {
            path: "/login",
            name: "login",
            component: loginPage,
            meta: {
                requiresAuth: false,
                requiresNoAuth: true,
            }
        },
        {
            path: "/login/password-reminder",
            name: "passwordReminder",
            component: passwordReminder,
            meta: {
                requiresAuth: false,
                requiresNoAuth: false,
            }
        },
        {
            path: "/login/password-reset",
            name: "passwordReset",
            component: passwordReset,
        },

    ],
    scrollBehavior() {
        return { x: 0, y: 0 };
    }
});
export default router;

router.beforeEach((to, from, next) => {
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (store.getters["auth/isAuthenticated"] && !store.getters["auth/isAccessTokenExpired"]) {
            next();
        } else {
            next({ name: "Login", query: { redirect: to.path } });
        }
    } else if (to.matched.some((record) => record.meta.requiresNoAuth)) {
        if (!store.getters["auth/isAuthenticated"]) {
            next();
        } else {
            next("/");
        }
    } else {
        next();
    }
})