<script>
import axios from "axios";

export default {
    name: "Reply",

    async mounted() {
        await this.retrieveCorrectMessage();
    },

    data() {
        return {
            message: {
                id: null,
                replies: [],
            },
            main: "",
            reply: "",

        };
    },

    methods: {
        async retrieveCorrectMessage(id) {
            try {
                const response = await axios.get(`/api/messages/${id}/reply/`);
                this.message = response.data;
            } catch (error) {
                this.handleError(error);
            }
        },

        async postReply() {
            try {
                const response = await axios.post(
                    `/api/messages/${this.$route.params.id}/sendReply/`,
                    {
                        reply: this.reply,
                    }
                );
                this.message.replies.push(response.data);
                this.reply = "";
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
            // this.error = "A problem occurred. Please try again later.";
            console.log("problem occured: ");
            console.log(error);
        },
    },
};
</script>


<template>
    <div class="container mt-2">
        <div class="row justify-content-center">
            <div class="col-md-8">


                <!-- Display the specific message -->


                <!-- Reply form -->
                <div class="card shadow-sm mb-4">
                    <div class="card-body">
                        <form @submit.prevent="postReply">
                            <div class="mb-3 text-center">
                                <label
                                    for="reply"
                                    class="form-label fs-1 fw-bold"
                                    >Care to reply?</label
                                >
                                <textarea
                                    id="reply"
                                    placeholder="say something..."
                                    class="form-control"
                                    v-model="reply"
                                    rows="3"
                                    {{ message.id }}
                                ></textarea>
                            </div>
                            <button class="btn btn-primary" type="submit">
                                Respond
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>
