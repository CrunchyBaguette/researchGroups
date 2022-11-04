import Vue from 'vue'
import Router from 'vue-router'

import GroupCatalog from "@/components/groupCatalog/groupCatalog"

Vue.use(Router);

const router = new Router({
    routes: [
        {
            path: "/group-catalog",
            name: "GroupCatalog",
            component: GroupCatalog,
        },
    ],
});
export default router;