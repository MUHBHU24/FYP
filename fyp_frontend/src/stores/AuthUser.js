import { defineStore } from "pinia";
import axios from "axios";

const DEFAULT_AUTH_USER = {
    isAuthenticated: false,
    id: null,
    username: null,
    accessToken: null,
    refreshToken: null,
};

// Define the 'AuthUser' store
export const useAuthUserStore = defineStore({
    id: "AuthUser",
    // Define the initial state of the AuthUser object
    state: () => ({
        AuthUser: { ...DEFAULT_AUTH_USER },
    }),
    actions: {
        setupStore() {
            if (!localStorage.getItem("AuthUser.accessToken")) {
                return;
            }

            const { AuthUser } = this;

            Object.keys(DEFAULT_AUTH_USER).forEach((key) => {
                AuthUser[key] = localStorage.getItem(`AuthUser.${key}`);
            });

            AuthUser.isAuthenticated = true;
            this.updateToken();
            console.log("The user: ", AuthUser, " is authenticated");
        },
        createAuthUser({ id, username }) {
            Object.assign(this.AuthUser, { id, username });

            localStorage.setItem("AuthUser.id", id);
            localStorage.setItem("AuthUser.username", username);

            console.log("Successfully created: ", this.AuthUser);
        },
        createToken({ accessToken, refreshToken }) {
            Object.assign(this.AuthUser, {
                accessToken,
                refreshToken,
                isAuthenticated: true,
            });

            localStorage.setItem("AuthUser.accessToken", accessToken);
            localStorage.setItem("AuthUser.refreshToken", refreshToken);
        },
        async updateToken() {
            try {
                const response = await axios.post("/api/refresh/", {
                    refresh: this.AuthUser.refreshToken,
                });

                console.log("Token updated: ", response.data);

                this.AuthUser.accessToken = response.data.accessToken;
                localStorage.setItem(
                    "AuthUser.accessToken",
                    response.data.accessToken
                );
                axios.defaults.headers.common["Authorization"] =
                    "Bearer " + response.data.accessToken;
            } catch (error) {
                console.error(error);
                this.deleteToken();
                this.$router.push("/login");
            }
        },
        deleteToken() {
            Object.assign(this.AuthUser, { ...DEFAULT_AUTH_USER });

            Object.keys(DEFAULT_AUTH_USER).forEach((key) => {
                localStorage.removeItem(`AuthUser.${key}`);
            });
        },
    },
});
