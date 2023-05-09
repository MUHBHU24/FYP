<script>
import axios from "axios";
import SurveyComments from "./SurveyComments.vue";

export default {
    name: "SurveyDetail",

    props: {
        slug: {
            type: String,
            required: true,
        },
    },

    data() {
        return {
            survey: {},
            question: {},
            answers: [],
            selectedAnswer: null,
        };
    },

    mounted() {
        try {
            // API call to get the survey, question, and answers for slug from the backend and store them in the data variables
            const response = axios.get(`/api/survey-details/${this.slug}/`);
            this.survey = response.data.survey;
            this.question = response.data.question;
            this.answers = response.data.answers;
        } catch (error) {
            console.log("Error fetching survey details: ", error);
        }
    },

    watch: {
        slug: {
            handler(newSlug) {
                if (newSlug) {
                    this.fetchSurveyDetails(newSlug);
                }
            },
            immediate: true,
        },
    },

    methods: {
        async fetchSurveyDetails(slug) {
            try {
                const response = await axios.get(
                    `/api/surveys/${slug}/`
                );
                this.survey = response.data.survey;
                this.question = response.data.question;
                this.answers = response.data.answers;
            } catch (error) {
                console.log("Error fetching survey details: ", error);
            }
        },

        async submitSurvey() {
            // Check if the user has selected an answer before submitting the survey response to the backend
            if (!this.selectedAnswer) {
                alert("Please select an answer");
                return;
            }
            // API call to submit the survey response to the backend, or display an error message if the API call fails
            try {
                await axios.post("/api/submit", {
                    question: this.question.id,
                    answer: this.selectedAnswer,
                });
                alert("Survey submitted successfully");
            } catch (error) {
                console.log("Error submitting survey: ", error);
                alert("Error submitting survey");
            }
        },
    },

    // components: { SurveyComments },
};
</script>

<template>
    <template>
        <div class="container">
            <div class="row">
                <div class="col">
                    <div class="card mt-4">
                        <div v-if="survey.item_image" class="card-header">
                            <img
                                :src="survey.item_image"
                                class="card-img-top"
                                alt="Survey image"
                            />
                        </div>
                        <div class="card-body">
                            <h5 class="card-title">{{ survey.title }}</h5>
                            <p class="card-text">
                                {{ question.question_text }}
                            </p>
                            <form @submit.prevent="submitSurvey">
                                <div
                                    class="mb-3"
                                    v-for="(answer, index) in answers"
                                    :key="answer.id"
                                >
                                    <input
                                        type="radio"
                                        :id="'answer' + index"
                                        :value="answer.selected_answer"
                                        v-model="selectedAnswer"
                                        name="answer"
                                        class="form-check-input"
                                    />
                                    <label
                                        :for="'answer' + index"
                                        class="form-check-label"
                                    >
                                        {{ answer.selected_answer }}
                                    </label>
                                </div>
                                <button type="submit" class="btn btn-primary">
                                    Submit
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </template>

    <!-- <SurveyComments :survey-id="surveyId"></survey-comments> -->
</template>
