import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import SurveyView from "../views/SurveyView.vue";
import ResultsView from "../views/ResultsView.vue";
import ProfileView from "../views/ProfileView.vue";
import RegisterView from "../views/RegisterView.vue";
import LoginView from "../views/LoginView.vue";

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
            path: "/results",
            name: "results",
            component: ResultsView,
        },
        {
            path: "/profile",
            name: "profile",
            component: ProfileView,
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