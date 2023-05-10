<script>
import { useAuthUserStore } from "../stores/AuthUser";
import { useRouter } from "vue-router";
import axios from "axios";

export default {
    setup() {
        const AuthUserStore = useAuthUserStore(); // Initialize the AuthUserStore to handle the user's authentication status and profile
        console.log(AuthUserStore);
        const router = useRouter(); // Initialize the router to handle navigation

        const logout = () => {
            AuthUserStore.deleteToken(); // Log the user out by deleting their token

            axios.defaults.headers.common["Authorization"] = null; // Delete the token from the header

            router.push("/login"); // Redirect the user to the login page
        };

        return {
            AuthUserStore, // Make AuthUserStore available to the template
            logout, // Make logout() available to the template
        };
    },
};
</script>

<template>
    <header>
        <nav
            class="navbar navbar-expand-lg navbar-dark"
            :style="{
                background:
                    'linear-gradient(90deg, rgba(63,94,251,1) 0%, rgba(252,70,107,1) 100%)',
            }"
        >
            <div class="container">
                <a class="navbar-brand d-flex align-items-center" href="#">
                    <img
                        src="../assets/fyp_logo.png"
                        alt="logo"
                        width="80"
                        height="80"
                        class="me-2"
                    />
                    <h2 class="m-0 me-2 fs-1" :style="{ color: 'white' }">
                        Vocabularious
                    </h2>
                </a>
                <button
                    class="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarNav"
                    aria-controls="navbarNav"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div
                    class="collapse navbar-collapse justify-content-center"
                    id="navbarNav"
                >
                    <ul class="navbar-nav fs-4">
                        <li class="nav-item">
                            <RouterLink
                                to="/home"
                                class="nav-link custom-nav-link"
                                href="#"
                                ><svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="16"
                                    height="16"
                                    fill="currentColor"
                                    class="bi bi-house-fill"
                                    viewBox="0 0 16 16"
                                >
                                    <path
                                        d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z"
                                    />
                                    <path
                                        d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z"
                                    />
                                </svg>
                                Home</RouterLink
                            >
                        </li>
                        <li class="nav-item">
                            <RouterLink
                                to="/about"
                                class="nav-link custom-nav-link"
                                href="#"
                                ><svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="16"
                                    height="16"
                                    fill="currentColor"
                                    class="bi bi-info-circle-fill"
                                    viewBox="0 0 16 16"
                                >
                                    <path
                                        d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"
                                    />
                                </svg>
                                About</RouterLink
                            >
                        </li>
                        <li
                            class="nav-item"
                            v-if="AuthUserStore.AuthUser.isAuthenticated"
                        >
                            <RouterLink
                                to="/surveys"
                                class="nav-link custom-nav-link"
                                href="#"
                                ><svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="16"
                                    height="16"
                                    fill="currentColor"
                                    class="bi bi-clipboard-fill"
                                    viewBox="0 0 16 16"
                                >
                                    <path
                                        fill-rule="evenodd"
                                        d="M10 1.5a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-1Zm-5 0A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5v1A1.5 1.5 0 0 1 9.5 4h-3A1.5 1.5 0 0 1 5 2.5v-1Zm-2 0h1v1A2.5 2.5 0 0 0 6.5 5h3A2.5 2.5 0 0 0 12 2.5v-1h1a2 2 0 0 1 2 2V14a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V3.5a2 2 0 0 1 2-2Z"
                                    />
                                </svg>
                                Take Our Surveys!</RouterLink
                            >
                        </li>
                        <li
                            class="nav-item"
                            v-if="AuthUserStore.AuthUser.isAuthenticated"
                        >
                            <RouterLink
                                to="/messages"
                                class="nav-link custom-nav-link"
                                href="#"
                                ><svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="16"
                                    height="16"
                                    fill="currentColor"
                                    class="bi bi-pin-map-fill"
                                    viewBox="0 0 16 16"
                                >
                                    <path
                                        fill-rule="evenodd"
                                        d="M3.1 11.2a.5.5 0 0 1 .4-.2H6a.5.5 0 0 1 0 1H3.75L1.5 15h13l-2.25-3H10a.5.5 0 0 1 0-1h2.5a.5.5 0 0 1 .4.2l3 4a.5.5 0 0 1-.4.8H.5a.5.5 0 0 1-.4-.8l3-4z"
                                    />
                                    <path
                                        fill-rule="evenodd"
                                        d="M4 4a4 4 0 1 1 4.5 3.969V13.5a.5.5 0 0 1-1 0V7.97A4 4 0 0 1 4 3.999z"
                                    />
                                </svg>
                                Messages</RouterLink
                            >
                        </li>
                        <li
                            class="nav-item"
                            v-if="AuthUserStore.AuthUser.isAuthenticated"
                        >
                            <RouterLink
                                :to="{
                                    uname: 'account',
                                    params:{'id': AuthUserStore.AuthUser.id},
                                }"
                                class="nav-link custom-nav-link"
                                ><svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="16"
                                    height="16"
                                    fill="currentColor"
                                    class="bi bi-person-lines-fill"
                                    viewBox="0 0 16 16"
                                >
                                    <path
                                        d="M6 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-5 6s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zM11 3.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5zm.5 2.5a.5.5 0 0 0 0 1h4a.5.5 0 0 0 0-1h-4zm2 3a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1h-2zm0 3a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1h-2z"
                                    />
                                </svg>
                                Account</RouterLink
                            >
                        </li>
                    </ul>
                </div>
                <ul
                    class="navbar-nav fs-4"
                    v-if="!AuthUserStore.AuthUser.isAuthenticated"
                >
                    <li class="nav-item">
                        <RouterLink
                            to="/login"
                            class="nav-link custom-nav-link btn custom-login-btn"
                            href="#"
                            ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                fill="currentColor"
                                class="bi bi-door-open-fill"
                                viewBox="0 0 16 16"
                            >
                                <path
                                    d="M1.5 15a.5.5 0 0 0 0 1h13a.5.5 0 0 0 0-1H13V2.5A1.5 1.5 0 0 0 11.5 1H11V.5a.5.5 0 0 0-.57-.495l-7 1A.5.5 0 0 0 3 1.5V15H1.5zM11 2h.5a.5.5 0 0 1 .5.5V15h-1V2zm-2.5 8c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z"
                                />
                            </svg>
                            Login</RouterLink
                        >
                    </li>
                    <li
                        class="nav-item"
                        v-if="!AuthUserStore.AuthUser.isAuthenticated"
                    >
                        <RouterLink
                            to="/register"
                            class="nav-link custom-nav-link btn custom-register-btn"
                            href="#"
                            ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                fill="currentColor"
                                class="bi bi-door-open"
                                viewBox="0 0 16 16"
                            >
                                <path
                                    d="M8.5 10c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z"
                                />
                                <path
                                    d="M10.828.122A.5.5 0 0 1 11 .5V1h.5A1.5 1.5 0 0 1 13 2.5V15h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V1.5a.5.5 0 0 1 .43-.495l7-1a.5.5 0 0 1 .398.117zM11.5 2H11v13h1V2.5a.5.5 0 0 0-.5-.5zM4 1.934V15h6V1.077l-6 .857z"
                                />
                            </svg>
                            Register</RouterLink
                        >
                    </li>
                </ul>
                <ul
                    class="navbar-nav fs-4"
                    v-if="AuthUserStore.AuthUser.isAuthenticated"
                >
                    <!-- logout appears when user is authenticated, in place of where login/register would be -->
                    <li class="nav-item">
                        <RouterLink
                            to="/login"
                            class="nav-link custom-nav-link btn custom-logout-btn"
                            href="#"
                            @click="logout"
                            ><svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                fill="currentColor"
                                class="bi bi-box-arrow-left"
                                viewBox="0 0 16 16"
                            >
                                <path
                                    fill-rule="evenodd"
                                    d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"
                                />
                                <path
                                    fill-rule="evenodd"
                                    d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"
                                />
                                width="16" height="16" fill="currentColor"
                                class="bi bi-door-closed-fill" viewBox="0 0 16
                                16" >
                            </svg>
                            Logout</RouterLink
                        >
                    </li>
                </ul>
            </div>
        </nav>
    </header>
    <main class="p-3 bg-light">
        <RouterView />
    </main>
</template>

<style scoped>
.custom-login-btn {
    color: #fff;
    background-color: #1b5211;
    border-color: #0c3106;
    transition: background-color 0.3s, border-color 0.3s;
}

.custom-login-btn:hover {
    background-color: #34a921;
    border-color: #1b5211;
}

.custom-register-btn {
    color: #4e73df;
    background-color: #34a921;
    border-color: #1b5211;
    transition: color 0.3s, background-color 0.3s, border-color 0.3s;
}

.custom-register-btn:hover {
    color: #fff;
    background-color: #249510;
    border-color: #10340a;
}
.custom-logout-btn {
    color: #fff;
    background-color: #b22222;
    border-color: #6b1515;
    transition: background-color 0.3s, border-color 0.3s;
}

.custom-logout-btn:hover {
    background-color: #dc3232;
    border-color: #b22222;
}
</style>
