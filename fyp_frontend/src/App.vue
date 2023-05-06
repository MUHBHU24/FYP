<script>
import NavBar from "./components/NavBar.vue";
import ToastNotification from "./components/ToastNotification.vue";

export default {
    name: "App",
    components: {
        NavBar,
        ToastNotification,
    },
};
</script>

<template>
    <NavBar />
    <ToastNotification />
</template>
