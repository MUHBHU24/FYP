<script>
import axios from "axios";

export default {
    name: "Account",

    components: {

    },

    data() {
        return {
            user: null,
        };
    },

    async mounted() {
        try {
            const response = await axios.get(`/api/account/${this.$route.params.id}/`);
            this.user = response.data;
            console.log(this.user);
        } catch (error) {
            console.log(error);
        }
    },

    methods: {
        async allMessages() {
            try {
                const response = await axios.get("/api/messages/");
                console.log("data");
                console.log(response.data);
                this.messages = response.data;
            } catch (error) {
                this.handleError(error);
            }
        },

        async createMsg() {
            console.log("you have created a new message: ", this.main);

            try {
                const response = await axios.post("/api/messages/new/", {
                    main: this.main,
                });
                console.log("data");
                console.log(response.data);
                this.messages.push(response.data);
            } catch (error) {
                this.handleError(error);
            }
        },

        formatDate(dateString) {
            const options = { year: "numeric", month: "long", day: "numeric" };
            const date = new Date(dateString);
            return date.toLocaleDateString(undefined, options);
        },

        handleError(error) {
            console.log("problem occured");
            console.log(error);
        },
    },
};
</script>

<template>
    <div>
        <h1>{{ user.username }}</h1>
        <p>{{ user.first_name }}</p>
        <p>{{ user.city }}</p>
        <p>{{ user.age }}</p>
        <p>{{ user.bio }}</p>
    </div>
</template>
