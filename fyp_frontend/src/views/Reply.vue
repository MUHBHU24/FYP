<script>
import axios from "axios";

export default {
    name: "Reply",

    async mounted() {
        await this.retrieveCorrectMessage();
    },

    data() {
        return {
            message: {},
            reply: "",
        };
    },

    methods: {
        retrieveCorrectMessage() {
            try {
                const response = axios.get(
                    `/api/messages/${this.$route.params.id}/`
                ).then((response) => {
                    this.message = response.data;
                });
                // this.message = response.data;
                // console.log("data");
                // console.log(response.data);
            } catch (error) {
                this.handleError(error);
            }
        },

        postReply() {
            try {
                const response =  axios.post(
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
                <div class="card shadow-sm mb-4" v-for="message in messages">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-10">
                                <h5 class="mb-2">{{ message.main }}</h5>
                                <p class="mb-1 text-muted">
                                    Posted by
                                    {{
                                        message.author
                                            ? message.author.username
                                            : ""
                                    }}
                                    from
                                    <strong>{{ message.author.city }}</strong>
                                    on
                                    {{ formatDate(message.timePosted) }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Reply form -->
                <div class="card shadow-sm mb-4">
                    <div class="card-body">
                        <form @submit.prevent="postReply">
                            <div class="mb-3">
                                <label for="reply" class="form-label"
                                    >Reply to this message:</label
                                >
                                <textarea
                                    id="reply"
                                    class="form-control"
                                    v-model="reply"
                                    rows="3"
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
