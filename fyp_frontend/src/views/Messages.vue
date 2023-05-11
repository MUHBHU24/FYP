<script>
import axios from "axios";

export default {
    name: "Messages",

    components: {},

    // this function is called when the page is loaded
    async mounted() {
        await this.allMessages();
    },

    data() {
        return {
            messages: [],
            main: "",
            selectedFile: null,
        };
    },

    methods: {
        // this function retrieves all the messages from the database
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

        // this function creates a new message and adds it to the database and the page
        async createMsg() {
            console.log("you have created a new message: ", this.main);

            const formData = new FormData();
            formData.append("main", this.main);

            if (this.selectedFile) {
                formData.append("pic", this.selectedFile);
            }

            try {
                const response = await axios.post(
                    "/api/messages/new/",
                    formData,
                    {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        },
                    }
                );
                console.log("data");
                console.log(response.data);
                this.messages.push(response.data);
                this.main = "";
                this.selectedFile = null;
            } catch (error) {
                this.handleError(error);
            }
        },

        // used to format the date into human readable format
        formatDate(dateString) {
            const options = { year: "numeric", month: "long", day: "numeric" };
            const date = new Date(dateString);
            return date.toLocaleDateString(undefined, options);
        },

        // handle/log any errors
        handleError(error) {
            console.log("problem occured");
            console.log(error);
        },
        onFileSelected(event) {
            this.selectedFile = event.target.files[0];
        },

        // this function is used to upvote a message and update the upvote count on the page
        async upvoteMsg(id) {
            try {
                const response = await axios.post(
                    `/api/messages/${id}/upvote/`
                );
                console.log(response.data);

                // to update the upvote count on the page without refreshing
                if (response.data.UpvoteStatus === "This has been upvoted!") {
                    const message = this.messages.find(
                        (message) => message.id === id
                    );
                    // increment the upvote count by 1
                    if (message) {
                        message.upvoteCount += 1;
                    }
                    // if it has already been upvoted, do nothing
                } else if (
                    response.data.UpvoteStatus ===
                    "You have already upvoted this message!"
                ) {
                    console.log("You have already upvoted this message!");
                    // if there is an error, print it out
                } else if (response.data.error) {
                    console.error(response.data.error);
                }
            } catch (error) {
                console.error(error);
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
                            <h5 class="mb-0 fs-1">Message board</h5>
                        </div>
                        <div class="card-body">
                            <form @submit.prevent="createMsg">
                                <div class="mb-3">
                                    <label for="main" class="form-label"
                                        >Heard something interesting? Let people
                                        know!</label
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
                        <div class="row">
                            <!-- Message details -->
                            <div class="col-md-10">
                                <!-- Display the image if it exists -->
                                <div v-if="message.messagePic" class="mb-3">
                                    <img
                                        :src="message.messagePic"
                                        alt="Message Image"
                                        class="img-fluid rounded"
                                        style="max-width: 100px; max-height:100px;"
                                    />
                                </div>
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
                                <RouterLink
                                    :to="{
                                        name: 'reply',
                                        params: { id: message.id },
                                    }"
                                    class="btn btn-link p-0"
                                    >Check Replies</RouterLink
                                >
                            </div>
                            <!-- Upvote button -->
                            <div
                                class="col-md-2 d-flex align-items-start justify-content-end"
                            >
                                <button
                                    class="btn btn-primary"
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
