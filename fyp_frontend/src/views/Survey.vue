<script>
import axios from "axios";
import { useRouter } from "vue-router";
import defaultItem from "@/assets/fyp_blankItem.png";

export default {
    name: "Survey",

    data() {
        return {
            getAllSurveys: [],
            searchText: "",
            defaultItem,
        };
    },

    mounted() {
        this.getAllSurveysCall();
    },

    methods: {
        getImage(survey) {
            if (survey.item_image) {
                console.log("http://localhost:8000/" + survey.item_image)
                return "http://localhost:8000/" + survey.item_image;
            } else {
                return this.defaultItem;
            }
        },

        exportSurveyResponses(surveySlug) {
            const url = `/api/surveys/${surveySlug}/export-responses/`;
            axios
                .get(url, { responseType: "blob" })
                .then((response) => {
                    const url = window.URL.createObjectURL(
                        new Blob([response.data])
                    );
                    const link = document.createElement("a");
                    link.href = url;
                    link.setAttribute("download", "survey-responses.csv");
                    document.body.appendChild(link);
                    link.click();
                })
                .catch((error) => {
                    console.log("Error exporting survey responses: ", error);
                });
        },

        executeSearch() {
            // API call to get the filtered surveys from the backend and store them in the data variable
            axios
                .get("/api/surveys/search?query=" + this.searchText)
                .then((response) => {
                    this.getAllSurveys = response.data.surveys;
                })
                .catch((error) => {
                    console.log("Error fetching filtered surveys: ", error);
                });
        },

        getAllSurveysCall() {
            // API call to get all surveys from the backend and store them in the data variable (list of surveys)
            axios
                .get("/api/surveys/")
                .then((response) => {
                    console.log("data", response.data);

                    this.getAllSurveys = response.data; // an array of objects containing all surveys in the database
                })
                .catch((error) => {
                    console.log("Error fetching surveys: ", error); // show error message if something goes wrong
                });
        },

        // Function to redirect to the survey detail page when a survey is clicked
        selectSurvey(slug) {
            console.log("slug", slug);  
            this.$router.push({ name: "survey", params: { slug: survey. slug } });
        },
    },
};
</script>

<template>
    <div class="container mt-2">
        <div class="d-flex justify-content-center">
            <div class="input-group mb-4 w-50">
                <input
                    type="text"
                    class="form-control"
                    v-model="searchText"
                    placeholder="Find surveys..."
                    aria-label="Find surveys"
                />
                <button
                    class="btn btn-outline-success"
                    type="button"
                    @click="executeSearch"
                >
                    Go
                </button>
            </div>
        </div>
        <div class="row">
            <div
                class="col-sm-4"
                v-for="survey in getAllSurveys"
                :key="survey.id"
            >
                <div class="card mb-3" style="width: 18rem">
                    <img
                        :src="getImage(survey)"
                        class="card-img-top"
                        alt="Survey Image"
                    />
                    <div class="card-body">
                        <h4 class="card-title">{{ survey.title }}</h4>
                        <p class="card-text">
                            This is a survey for the item: {{ survey.title }}
                        </p>
                        <button
                            class="btn btn-primary"
                            @click="selectSurvey(survey.slug)"
                        >
                            Take Survey
                        </button>
                        <button
                            class="btn btn-sm btn-secondary float-end mt-2"
                            @click.stop="exportSurveyResponses(survey.slug)"
                        >
                            Export
                        </button>
                    </div>
                    <div class="card-footer">
                        Posted by
                        {{ survey.created_by?.username ?? "Anonymous" }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
