<script>
// Import the toast store and axios for handling API requests
import { useToastStore } from "../stores/toast";
import axios from "axios";

export default {
    setup() {
        // Initialize the toast store to handle toasts (pop-up notifications)
        const toastStore = useToastStore();

        // Make toastStore available to the template
        return {
            toastStore,
        };
    },

    data() {
        // Define the form object and entryErrors array for handling form input and validation errors
        return {
            form: {
                name: "",
                city: "",
                username: "",
                password1: "",
                password2: "",
            },
            entryErrors: [],
        };
    },

    methods: {
        // Method to handle form submission
        registerForm() {
            // Reset the entryErrors array
            this.entryErrors = [];

            // Validate form fields, adding error messages if necessary
            if (this.form.name === "") {
                this.entryErrors.push("Name required!");
            }

            if (this.form.city === "") {
                this.entryErrors.push("City required!");
            }

            if (this.form.username === "") {
                this.entryErrors.push("Username required!");
            }

            if (this.form.password1 === "") {
                this.entryErrors.push("Password required!");
            }

            if (this.form.password2 === "") {
                this.entryErrors.push("Please confirm your password!");
            }

            if (this.form.password1 !== this.form.password2) {
                this.entryErrors.push("The passwords you entered must match!");
            }

            // If no errors, submit the form data to the API
            if (this.entryErrors.length === 0) {
                axios
                    .post("/api/register/", this.form)
                    .then((response) => {
                        // Handle successful registration
                        if (response.data.msg === "Success") {
                            this.toastStore.addToast({
                                ms: 7500,
                                title: "Success!",
                                message: "You have successfully registered!",
                                variant: "success",
                            });

                            // Reset the form
                            this.form.name = "";
                            this.form.city = "";
                            this.form.username = "";
                            this.form.password1 = "";
                            this.form.password2 = "";
                        } else {
                            // Handle registration errors
                            this.toastStore.addToast({
                                ms: 7500,
                                title: "Error!",
                                message: "An error occurred while registering!",
                                variant: "danger",
                            });
                        }
                        // if (response.data.msg === "Success") {
                        //     this.toastStore.showToast(
                        //         7500,
                        //         "You have successfully registered!",
                        //         "bg-emerald-500"
                        //     );
                        // } else {
                        //     this.toastStore.showToast(
                        //         7500,
                        //         "An error occurred while registering!",
                        //         "bg-red-500"
                        //     );
                        // }
                    })
                    .catch((error) => {
                        // Handle errors that occurred during API request
                        this.toastStore.addToast({
                            ms: 7500,
                            title: "Error!",
                            message: "An error occurred while registering!",
                            variant: "danger",
                        });
                    });
            }
        },
    },
};
</script>

<template>
    <!-- Main container for the registration form -->
    <div class="container">
        <div class="row g-5">
            <!-- Left column with information about registration -->
            <div class="col-lg-6 main-left">
                <div
                    class="p-4 bg-light border border-1 border-secondary rounded"
                >
                    <!-- Information about the benefits of registration -->
                    <h1 class="mb-4 display-4">
                        Register to become a Vocabularious member!
                    </h1>

                    <!-- Welcome message -->
                    <p class="mb-4 fst-italic text-muted">
                        Welcome to <strong>Vocabularious</strong>!
                    </p>

                    <!-- Form instructions -->
                    <p class="mb-4 text-muted">
                        Please fill in the form provided to register as a
                        member. By signing up, you will have full access to our
                        site and be able to contribute to numerous surveys.
                    </p>

                    <!-- Additional information about the community -->
                    <p class="mb-4 text-muted">
                        Regardless of whether you are a seasoned researcher or a
                        curious individual interested in exploring the field of
                        lexical variation, we welcome you to take interest and
                        join us!
                    </p>

                    <!-- Link to log in for existing users -->
                    <p class="fw-bold">
                        <small>
                            Already have an account? Click
                            <RouterLink to="/login" class="text-primary"
                                ><mark>here</mark></RouterLink
                            >
                            to log in!
                        </small>
                    </p>
                </div>
            </div>

            <!-- Right column with the registration form -->
            <div class="col-lg-6 main-right">
                <div
                    class="p-4 bg-white border border-1 border-secondary rounded"
                >
                    <!-- Form element -->
                    <form @submit.prevent="registerForm">
                        <!-- Name input field -->
                        <div class="mb-3">
                            <label class="form-label">Name</label>
                            <input
                                type="text"
                                placeholder="Enter your name..."
                                class="form-control"
                                v-model="form.name"
                            />
                        </div>

                        <!-- City input field -->
                        <div class="mb-3">
                            <label class="form-label">City</label>
                            <input
                                type="text"
                                placeholder="Your location..."
                                class="form-control"
                                v-model="form.city"
                            />
                        </div>

                        <!-- Username input field -->
                        <div class="mb-3">
                            <label class="form-label">Username</label>
                            <input
                                type="text"
                                placeholder="Create a username..."
                                class="form-control"
                                v-model="form.username"
                            />
                        </div>

                        <!-- Password input field -->
                        <div class="mb-3">
                            <label class="form-label">Password</label>
                            <input
                                type="password"
                                placeholder="Create a password..."
                                class="form-control"
                                v-model="form.password1"
                            />
                        </div>

                        <!-- Repeat password input field -->
                        <div class="mb-3">
                            <label class="form-label">Repeat password</label>
                            <input
                                type="password"
                                placeholder="Confirm password..."
                                class="form-control"
                                v-model="form.password2"
                            />
                        </div>

                        <!-- Display validation errors -->
                        <template>
                            <div
                                class="alert alert-danger border border-danger rounded-3 p-4"
                                v-if="entryErrors.length > 0"
                            >
                                <p
                                    v-for="error in entryErrors"
                                    :key="error"
                                    class="mb-0"
                                >
                                    {{ error }}
                                </p>
                            </div>
                        </template>

                        <!-- Sign up button -->
                        <div>
                            <button class="btn btn-primary">Sign up</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
