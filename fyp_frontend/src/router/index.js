import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import SurveyView from "../views/SurveyView.vue";
import ReplyView from "../views/ReplyView.vue";
import MessagesView from "../views/MessagesView.vue";
import AccountView from "../views/AccountView.vue";
import RegisterView from "../views/RegisterView.vue";
import LoginView from "../views/LoginView.vue";
import SurveyDetail from "../components/SurveyDetail.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: HomeView,
        },
        {
            path: '/home',
            redirect: '/'
        },
        {
            path: "/about",
            name: "about",
            component: AboutView,
        },
        {
            path: "/surveys",
            name: "surveys",
            component: SurveyView,
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
            component: MessagesView,
        },
        {
            path: "/reply/:id",
            name: "reply",
            component: ReplyView,
        },
        {
            path: "/account/:id",
            name: "account",
            component: AccountView,
        },
        {
            path: "/register",
            name: "register",
            component: RegisterView,
        },
        {
            path: "/login",
            name: "login",
            component: LoginView,
        },
    ],
});

export default router;