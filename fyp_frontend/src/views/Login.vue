<script>
import axios from "axios";
import { useAuthUserStore } from "../stores/AuthUser";
import jwt_decode from "jwt-decode";

export default {
    setup() {
        // Initialize the AuthUserStore to handle the user's authentication status and profile
        const AuthUserStore = useAuthUserStore();

        return {
            AuthUserStore,
        };
    },

    data() {
        return {
            form: {
                // Initialize the form object
                username: "",
                password: "",
            },
            // Initialize the entryErrors array for handling form validation errors
            entryErrors: [],
            userId: null,
        };
    },

    methods: {
        // Method to handle form submission
        async loginForm() {
            // Reset the entryErrors array
            this.entryErrors = [];

            // Validate form fields, adding error messages if necessary (in this case, if the fields are empty) and pushing them to the entryErrors array
            if (!this.form.username) {
                this.entryErrors.push("Username required!");
            }

            if (!this.form.password) {
                this.entryErrors.push("Password required!");
            }

            // If there are no errors, send a POST request to the API to log the user in and create a token
            if (!this.entryErrors.length) {
                try {
                    const response = await axios.post("/api/login/", this.form);
                    // Handle successful login
                    // this.AuthUserStore.createToken(response.data);
                    this.AuthUserStore.createToken({
                        accessToken: response.data.access,
                        refreshToken: response.data.refresh,
                    });

                    console.log(response.data.access);

                    axios.defaults.headers.common["Authorization"] =
                        "Bearer " + response.data.access;

                    // Decode the token to get the user ID
                    const decodedToken = jwt_decode(response.data.access);
                    const userId = decodedToken.user_id;
                    this.userId = userId;

                    console.log(userId);

                    console.log(
                        "Authorization header:",
                        axios.defaults.headers.common["Authorization"]
                    );
                    const response2 = await axios.get(
                        `/api/account/${this.userId}/`
                    );
                    // Handle successful profile retrieval
                    this.AuthUserStore.createAuthUser(response2.data);

                    // Try to redirect the user to their account page
                    this.$router.push({
                        name: "account",
                        params: { id: this.userId },
                    });
                } catch (error) {
                    // Log the error
                    console.log("We have encountered a problem: ", error);
                    this.entryErrors.push("Invalid login credentials!");
                }
            }
        },
    },
};
</script>

<template>
    <div class="container">
        <div class="row g-5">
            <div class="col-lg-6 main-left">
                <div
                    class="p-4 bg-light border border-1 border-secondary rounded"
                >
                    <h1 class="mb-4 display-4">Login to your account!</h1>

                    <p class="mb-4 fst-italic text-muted">
                        Welcome to <strong>Vocabularious</strong>!
                    </p>

                    <p class="mb-4 text-muted">
                        Please enter your login credentials to access your
                        account.
                    </p>

                    <p class="fw-bold">
                        <small>
                            Don't have an account yet? Click
                            <RouterLink to="/register" class="text-primary"
                                ><mark>here</mark></RouterLink
                            >
                            to register!
                        </small>
                    </p>
                </div>
            </div>
            <div class="col-lg-6 main-right">
                <div
                    class="p-4 bg-white border border-1 border-secondary rounded"
                >
                    <form @submit.prevent="loginForm">
                        <div class="mb-3">
                            <label class="form-label">Username</label>
                            <input
                                type="text"
                                placeholder="Enter your username..."
                                class="form-control"
                                v-model="form.username"
                            />
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Password</label>
                            <input
                                type="password"
                                placeholder="Enter your password..."
                                class="form-control"
                                v-model="form.password"
                            />
                        </div>
                        <!-- Display validation errors -->
                        <div
                            class="alert alert-danger border border-danger rounded-3 p-4"
                            v-for="(err, index) in entryErrors"
                            :key="index"
                        >
                            {{ err }}
                        </div>
                        <div>
                            <button class="btn btn-primary">Log in</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
