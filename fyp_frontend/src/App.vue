<script>
import NavBar from "./components/NavBar.vue";
import ToastNotification from "./components/ToastNotification.vue";
import axios from "axios";
import { useAuthUserStore } from "./stores/AuthUser";

export default {
    setup() {
        const AuthUserStore = useAuthUserStore(); // Initialize the AuthUserStore to handle the user's authentication status and profile

        return {
            AuthUserStore, // Make AuthUserStore available to the template
        };
    },

    name: "App",

    beforeCreate() {
        // Initialize the AuthUserStore to handle the user's authentication status and profile before the app is created before they log in
        this.AuthUserStore.setupStore();

        // Set the default Authorization header to the user's token
        const tokenForAuth = this.AuthUserStore.AuthUser.accessToken;

        // If the user is logged in, set the Authorization header to the user's token
        if (tokenForAuth) {
            axios.defaults.headers.common["Authorization"] = "Bearer " + tokenForAuth;
        } else {
            axios.defaults.headers.common["Authorization"] = null; // Delete the token from the header if the user is not logged in to prevent errors
        }
    },

    components: {
        NavBar, // Import the NavBar component to display the navigation bar
        ToastNotification, // Import the ToastNotification component to display pop-up notifications
    },
};
</script>

<template>
    <NavBar />
    <ToastNotification />
</template>
