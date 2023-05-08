import { defineStore } from "pinia";
import axios from "axios";

// Define the 'AuthUser' store
export const useAuthUserStore = defineStore({
    id: "AuthUser",

    // Define the initial state of the AuthUser object
    state: () => ({
        AuthUser: {
            id: null,
            username: null,
            accessToken: null,
            refreshToken: null,
            isAuthenticated: false,
        },
    }),

    actions: {
        // Initialise the user store with values from localStorage
        setupStore() {
            // Check if 'AuthUser.accessToken' exists in localStorage
            if (localStorage.getItem("AuthUser.accessToken")) { // add this != null && localStorage.getItem("AuthUser.refreshToken") != null
                // Set AuthUser object properties from localStorage
                this.AuthUser.id = 
                    localStorage.getItem("AuthUser.id");
                this.AuthUser.username =
                    localStorage.getItem("AuthUser.username");
                this.AuthUser.accessToken =
                    localStorage.getItem("AuthUser.accessToken");
                this.AuthUser.refreshToken =
                    localStorage.getItem("AuthUser.refreshToken");
                this.AuthUser.isAuthenticated = true;

                // Call updateToken function to refresh the user's token
                this.updateToken();

                // Log a message indicating the user is authenticated
                console.log("The user: " + this.AuthUser + " is authenticated");
            }
        },

        // Create a new user and store the user's ID and username
        createAuthUser(AuthUser) {
            console.log("Creating user: ", AuthUser);

            // Set AuthUser properties based on the input AuthUser
            this.AuthUser.id = AuthUser.id;
            this.AuthUser.username = AuthUser.username;

            // Save the ID and username to localStorage
            localStorage.setItem("AuthUser.id", this.AuthUser.id);
            localStorage.setItem("AuthUser.username", this.AuthUser.username);

            console.log("Successfully created: ", this.AuthUser);
        },

        // Create and store a new user token
        createToken(data) {
            console.log("Creating token", data);

            // Set the AuthUser properties for accessToken and refreshToken
            this.AuthUser.accessToken = data.accessToken;
            this.AuthUser.refreshToken = data.refreshToken;
            this.AuthUser.isAuthenticated = true;

            // console.log("Access token:", this.AuthUser.accessToken);
            // console.log("Refresh token:", this.AuthUser.refreshToken);
            // console.log("AuthUser:", this.AuthUser);
            // console.log("LocalStorage:", localStorage);

            // Save the accessToken and refreshToken to localStorage
            localStorage.setItem("AuthUser.accessToken", data.accessToken);
            localStorage.setItem("AuthUser.refreshToken", data.refreshToken);
        },

        // Update the user's access token by requesting a new token using the refresh token
        updateToken() {
            // Make an axios POST request to refresh the user's access token
            console.log('Updating token to:' + this.AuthUser.refreshToken)
            axios
                .post("/api/refresh/", {
                    // Pass the user's refresh token in the request body
                    refresh: this.AuthUser.refreshToken,
                })
                .then((response) => {
                    console.log("Token updated: ", response.data); 

                    // Update the AuthUser.accessToken with the new access token from the response
                    this.AuthUser.accessToken = response.data.accessToken;

                    // Save the new accessToken to localStorage
                    localStorage.setItem(
                        "AuthUser.accessToken",
                        response.data.accessToken
                    );

                    // Set the Authorization header for axios requests to include the new access token
                    axios.defaults.headers.common["Authorization"] =
                        "Bearer " + response.data.accessToken;
                })
                .catch((error) => {
                    console.log(error);

                    // If there's an error, call deleteToken() to remove the user's tokens and reset authentication status
                    this.deleteToken();
                });
        },

        // Delete the user token and reset user authentication status
        deleteToken() {
            console.log("Removing token");

            // Reset AuthUser properties related to authentication
            this.AuthUser.id = null;
            this.AuthUser.username = null;
            this.AuthUser.accessToken = null;
            this.AuthUser.refreshToken = null;
            this.AuthUser.isAuthenticated = false; // no longer authenticated

            // Remove the related keys from localStorage
            localStorage.removeItem("AuthUser.id");
            localStorage.removeItem("AuthUser.username");
            localStorage.removeItem("AuthUser.accessToken");
            localStorage.removeItem("AuthUser.refreshToken");
            localStorage.removeItem("AuthUser.isAuthenticated");
        },
    },
});
