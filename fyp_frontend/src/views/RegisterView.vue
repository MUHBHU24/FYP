<script>
import axios from "axios";

export default {
    setup() {
        const toastStore = useToastStore();

        return {
            toastStore,
        };
    },

    data() {
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
        submitForm() {
            this.entryErrors = [];

            if (this.form.name === "") {
                this.errors.push("Name required!");
            }

            if (this.form.city === "") {
                this.errors.push("City required!");
            }

            if (this.form.username === "") {
                this.errors.push("Username required!");
            }

            if (this.form.password1 === "") {
                this.errors.push("Password required!");
            }

            if (this.form.password2 === "") {
                this.errors.push("Please confirm your password!");
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push("The passwords you entered must match!");
            }

            if (this.entryErrors.length === 0) {
                axios
                    .post("/api/register/", this.form)
                    .then((response) => {
                        if (response.data.msg === "Success") {
                            this.toastStore.addToast({
                                title: "Success!",
                                message: "You have successfully registered!",
                                variant: "success",
                            });
                            this.form.name = "";
                            this.form.city = "";
                            this.form.username = "";
                            this.form.password1 = "";
                            this.form.password2 = "";
                        } else {
                            this.toastStore.addToast({
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
                    }
                    )
                    .catch((error) => {
                        this.toastStore.addToast({
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
    <div class="container">
        <div class="row g-5">
            <div class="col-lg-6 main-left">
                <div
                    class="p-4 bg-light border border-1 border-secondary rounded"
                >
                    <h1 class="mb-4 display-4">
                        Register to become a Vocabularious member!
                    </h1>

                    <p class="mb-4 fst-italic text-muted">
                        Welcome to <strong>Vocabularious</strong>!
                    </p>

                    <p class="mb-4 text-muted">
                        Please fill in the form provided to register as a
                        member. By signing up, you will have full access to our
                        site and be able to contribute to numerous surveys.
                    </p>

                    <p class="mb-4 text-muted">
                        Regardless of whether you are a seasoned researcher or a
                        curious individual interested in exploring the field of
                        lexical variation, we welcome you to take interest and
                        join us!
                    </p>

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

            <div class="col-lg-6 main-right">
                <div
                    class="p-4 bg-white border border-1 border-secondary rounded"
                >
                    <form>
                        <div class="mb-3">
                            <label class="form-label">Name</label>
                            <input
                                type="text"
                                placeholder="Enter your name..."
                                class="form-control"
                            />
                        </div>

                        <div class="mb-3">
                            <label class="form-label">City</label>
                            <input
                                type="text"
                                placeholder="Your location..."
                                class="form-control"
                            />
                        </div>

                        <div class="mb-3">
                            <label class="form-label">Username</label>
                            <input
                                type="text"
                                placeholder="Create a username..."
                                class="form-control"
                            />
                        </div>

                        <div class="mb-3">
                            <label class="form-label">Password</label>
                            <input
                                type="password"
                                placeholder="Create a password..."
                                class="form-control"
                            />
                        </div>

                        <div class="mb-3">
                            <label class="form-label">Repeat password</label>
                            <input
                                type="password"
                                placeholder="Confirm password..."
                                class="form-control"
                            />
                        </div>

                        <div>
                            <button class="btn btn-primary">Sign up</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
