# FYP
Final Year Project

A web application exploring the theme of lexical variation and its regional differences in the UK. The main purpose of the app is providing a tool for researchers and language enthusiasts alike in surveying a wider population and demographic of users, thus exploring cultural differences through verbal communication and dialect.


--- TODO LIST ---

maybe allow users to add comments to surveys they partake in, and allow them to view other users comments on the same survey
allow surveys to expire after a certain amount of time

create conda env, install python, django, vite, etc
create the project and configure 
setup database
create superuser

Project setup:
-Create a new directory for your project and set up a virtual environment for Python.
-Install Django and create a new Django project using django-admin startproject projectName.
-Set up Vue.js by installing Node.js, Vue CLI, and create a new Vue project using vue create projectName.
-Install the necessary dependencies like Axios, Vue Router, and Bootstrap-Vue.

Django backend:
-Create a new Django app using python manage.py startapp appName.
-Define the models for the survey, questions, and answers. Models: basic user, researcher (admin), survey, question, answer, comments etc
-Set up the Django REST Framework for the API and create serializers for the models.
-Create the views and URLs for the API endpoints.

Vue.js frontend:
-Set up Vue Router for navigation between pages.
-Create components for the main page, survey creation, survey update, and survey display.
-Use Axios to communicate with the Django backend and fetch/create/update surveys.
-Use Bootstrap-Vue to style the components.

Geographical graphing:
-Integrate a mapping library like Leaflet or Mapbox into your Vue app.
-Use the collected data to display regional trends on the map.
-Customize the map style to make it simple and clear.
-Here's a rough outline of the components and their functionalities:

MainPage.vue:
-Display the list of available surveys.
-Provide links to create a new survey or take an existing one.

CreateSurvey.vue:
-Allow the admin user to create a new survey with an image, question, and pre-defined answers.
-Send the survey data to the Django backend for storage.

UpdateSurvey.vue:
-Allow the admin user to update an existing survey by adding more answers.
-Send the updated survey data to the Django backend.

TakeSurvey.vue:
-Display the survey question, image, and available answers.
-Allow users to submit their answers.
-Send the user's answer to the Django backend for storage and analysis.

MapView.vue:
-Display the collected data on a map using a geographical graphing tool.
-Show regional trends and variation in a simple, clear manner.







<!-- <script>
import axios from "axios";

export default {
    name: "ReplyView",

    components: {},

    // this function is called when the page is loaded
    async mounted() {
        console.log(this.$route.params.id); // this is the id of the message that was clicked on
        await this.highlightedMessage();
    },

    data() {
        return {
            highlightedMessageData: {
                id: "",
                main: "",
            },
        };
    },

    methods: {
        // this function retrieves all the messages from the database
        async highlightedMessage() {
            try {
                const response = await axios
                    .get(`/api/messages/${this.$route.params.id}`)
                    .then((response) => {
                        console.log(response.data);
                        this.highlightedMessageData = response.data.message;
                    });
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
                    `/api/messages/${this.$route.params.id}/reply/`,
                    {
                        main: this.main,
                    }.then((response) => {
                        console.log("info");
                        console.log(response.data);
                        this.main = "";
                    })
                    // formData,
                    // {
                    //     headers: {
                    //         "Content-Type": "multipart/form-data",
                    //     },
                    // }
                );
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
        <!-- Highlighted Message -->
        <div class="row justify-content-center mb-4">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ highlightedMessageData.main }}</h5>
                        <!-- Add more fields from highlightedMessageData as needed -->
                    </div>
                </div>
            </div>
        </div>

        <!-- Reply Form -->
        <div class="row justify-content-center mb-4">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header align-items-center text-center">
                        <h5 class="mb-0 fs-1">Leave a Reply!</h5>
                    </div>
                    <div class="card-body">
                        <form @submit.prevent="createMsg">
                            <div class="mb-3">
                                <label for="main" class="form-label">
                                    Have something to say? Reply to the message!
                                </label>
                                <textarea
                                    id="main"
                                    class="form-control"
                                    placeholder="Type your reply here..."
                                    v-model="main"
                                    rows="3"
                                ></textarea>
                            </div>
                            <div class="d-flex justify-content-end">
                                <button class="btn btn-primary" type="submit">
                                    Send Reply
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <!-- Replies -->
        <div class="row justify-content-center">
            <div class="col-md-8">
                <!-- Replace 'replies' with your actual data variable -->
                <div v-for="reply in replies" :key="reply.id" class="card shadow-sm mb-4">
                    <div class="card-body">
                        <h5 class="card-title">{{ reply.main }}</h5>
                        <!-- Add more fields from reply as needed -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template> -->

