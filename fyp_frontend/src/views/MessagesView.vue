<script>
import axios from "axios";

export default {
    name: "MessagesView",

    components: {},
    async mounted() {
        await this.allMessages();
    },

    data() {
        return {
            messages: [],
            main: "",
        };
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

        upvoteMsg(id) {
            console.log("you have upvoted a message: ", id);

            try {
                const response = axios
                    .post(`/api/messages/${id}/upvote/`)
                    .then((response) => {
                        console.log(response.data);
                    });
            } catch (error) {
                this.handleError(error);
            }
        },
    },
};
</script>

<template>
    <div class="container mt-2">
        <div class="row justify-content-center">
            <div class="row justify-content-center mb-4">
                <div class="col-md-8">
                    <div class="card">
                        <div class="card-header align-items-center text-center">
                            <h5 class="mb-0 fs-1">Post your thoughts here!</h5>
                        </div>
                        <div class="card-body">
                            <form @submit.prevent="createMsg">
                                <div class="mb-3">
                                    <label for="main" class="form-label"
                                        >Message:</label
                                    >
                                    <textarea
                                        id="main"
                                        class="form-control"
                                        placeholder="Type a new message here..."
                                        v-model="main"
                                        rows="3"
                                    ></textarea>
                                </div>
                                <div class="mb-3">
                                    <label for="messageImage" class="form-label"
                                        >Need to add a picture?</label
                                    >
                                    <input
                                        id="messageImage"
                                        type="file"
                                        class="form-control"
                                        accept="image/*"
                                        v-on:change="onFileSelected"
                                    />
                                </div>
                                <div class="d-flex justify-content-end">
                                    <button
                                        class="btn btn-primary"
                                        type="submit"
                                    >
                                        Send message
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-8">
                <div
                    v-for="message in messages"
                    :key="message.id"
                    class="card shadow-sm mb-4"
                >
                    <div class="card-body">
                        <div
                            class="d-flex justify-content-between align-items-start"
                        >
                            <div class="d-flex align-items-center">
                                <!-- <img :src="getImage(message)" alt="User Image" class="rounded-circle me-3" width="50" height="50"> -->
                                <div>
                                    <h5 class="mb-0">{{ message.main }}</h5>
                                    <p class="mb-0">
                                        <small class="text-muted">
                                            Posted by
                                            {{
                                                message.author
                                                    ? message.author.username
                                                    : ""
                                            }}
                                            from
                                            <strong>{{
                                                message.author.city
                                            }}</strong>
                                            on
                                            {{ formatDate(message.timePosted) }}
                                        </small>
                                    </p>
                                </div>
                            </div>
                            <div>
                                <button
                                    class="btn btn-sm btn-primary"
                                    @click="upvoteMsg(message.id)"
                                >
                                    <i class="bi bi-hand-thumbs-up-fill"></i>
                                    {{ message.upvoteCount }} Upvotes
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
