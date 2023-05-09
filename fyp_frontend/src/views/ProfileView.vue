<script>
import axios from "axios";

export default {
    data() {
        return {
            user: {
                avatar: "",
                first_name: "",
                city: "",
                age: "",
                bio: "",
            },
        };
    },
    methods: {
        async updateUserProfile() {
            // Update user profile using API call
            try {
                // Replace the following line with API call to update the user profile
                await axios.put(
                    `/api/myAccount/${this.$route.params.id}/`,
                    this.user
                );
                console.log("User profile updated successfully");
            } catch (error) {
                console.error(
                    "An error occurred while updating the user profile:",
                    error
                );
            }
        },
    },
    async created() {
        // Fetch user profile using API call
        try {
            // Replace the following line with API call to fetch the user profile
            const response = await axios.get(
                `/api/myAccount/${this.$route.params.id}/`
            );
            this.user = response.data;
            console.log("User profile fetched successfully");
        } catch (error) {
            console.log(
                "An error occurred while fetching the user profile:",
                error
            );
        }
    },
};
</script>

<template>
    <div class="container mt-5">
        <h2 class="mb-4">User Profile</h2>
        <form @submit.prevent="updateUserProfile">
            <div class="mb-3">
                <label for="avatar" class="form-label">Avatar</label>
                <input type="file" class="form-control" id="avatar" />
            </div>
            <div class="mb-3">
                <label for="first_name" class="form-label">First Name</label>
                <input
                    type="text"
                    class="form-control"
                    id="first_name"
                    v-model="user.first_name"
                />
                {{ user.first_name }}
            </div>
            <div class="mb-3">
                <label for="location" class="form-label">Location</label>
                <input
                    type="text"
                    class="form-control"
                    id="location"
                    v-model="user.location"
                />
            </div>
            <div class="mb-3">
                <label for="age" class="form-label">Age</label>
                <input
                    type="number"
                    class="form-control"
                    id="age"
                    v-model="user.age"
                />
            </div>
            <div class="mb-3">
                <label for="city" class="form-label">City</label>
                <input
                    type="text"
                    class="form-control"
                    id="city"
                    v-model="user.city"
                />
            </div>
            <div class="mb-3">
                <label for="bio" class="form-label">Bio</label>
                <textarea
                    class="form-control"
                    id="bio"
                    rows="3"
                    v-model="user.bio"
                ></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Save Profile</button>
        </form>
    </div>
</template>
