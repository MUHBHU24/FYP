<script>
import axios from "axios";
import { useRoute } from "vue-router";
import defaultItem from "@/assets/fyp_blankItem.png";

export default {
    name: "SurveyDetail",

    data() {
        return {
            survey: {},
            question: {},
            answers: [],
            selectedAnswer: null,
            defaultItem,
        };
    },

    async mounted() {
        try {
            // fetch the survey details from the backend
            const route = useRoute();
            const slug = route.params.slug;
            this.fetchSurveyDetails(slug);
        } catch (error) {
            console.log("Error fetching survey details: ", error);
        }
    },

    watch: {
        "$route.params.slug": {
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
                    `/api/survey-details/${slug}/`
                );
                this.survey = response.data;
                this.question = this.survey.question;
                this.answers = this.survey.answers;
                this.selectedAnswer = this.survey.answers[0].id;
            } catch (error) {
                console.log("Error fetching survey details: ", error);
            }
        },

        getImage(survey) {
            if (survey.item_image) {
                return "http://localhost:8000/" + survey.item_image;
            } else {
                return this.defaultItem;
            }
        },

        async submitSurvey() {
            if (!this.selectedAnswer) {
                alert("Please select an answer");
                return;
            }
            try {
                await axios.post("/api/submit-survey", {
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
