<script>
import axios from "axios";

export default {
    name: "MessagesView",

    components: {},
    mounted() {
        this.allMessages();
    },

    methods: {
        allMessages() {
            axios
                .get("/api/messages/")
                .then((response) => {
                    console.log("data", response.data);
                })
                .catch((error) => {
                    console.log("problem: ", error);
                });
        },
    },
};
</script>

<template>
    <div class="results">
        <h1>This is a messages page</h1>
    </div>
</template>
