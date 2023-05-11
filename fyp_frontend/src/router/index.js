import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Survey from "../views/Survey.vue";
import Reply from "../views/Reply.vue";
import Messages from "../views/Messages.vue";
import Account from "../views/Account.vue";
import Register from "../views/Register.vue";
import Login from "../views/Login.vue";
import SurveyDetail from "../components/SurveyDetail.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: Home,
        },
        {
            path: '/home',
            redirect: '/'
        },
        {
            path: "/about",
            name: "about",
            component: About,
        },
        {
            path: "/surveys",
            name: "surveys",
            component: Survey,
        },
        {
            path: "/survey/:slug",
            name: "survey",
            component: SurveyDetail,
            props: true
        },
        {
            path: "/messages",
            name: "messages",
            component: Messages,
        },
        {
            path: "/:id",
            name: "reply",
            component: Reply,
        },
        {
            path: "/account/:id",
            name: "account",
            component: Account,
        },
        {
            path: "/register",
            name: "register",
            component: Register,
        },
        {
            path: "/login",
            name: "login",
            component: Login,
        },
    ],
});

export default router;