<script>
import axios from "axios";
import { useRouter } from "vue-router";

export default {
    name: "SurveyView",

    data() {
        return {
            getAllSurveys: [],
            searchText: "",
        };
    },

    mounted() {
        this.getAllSurveysCall();
    },

    methods: {
        getImage(survey) {
            if (survey.item_image) {
                return survey.item_image;
            } else {
                return "../assets/fyp_blankItem.png";
            }
        },

        handleImageError(event) {
            event.target.src = "../assets/fyp_blankItem.png";
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

        selectSurvey(slug) {
            const router = useRouter();
            router.push({ name: "surveys", params: { slug: slug } });
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
                <div
                    class="card"
                    style="width: 18rem"
                    @click="selectSurvey(survey.slug)"
                >
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
                        <button class="btn btn-primary">Take Survey</button>
                    </div>
                    <div class="card-footer">
                        Posted by {{ survey.author?.username ?? "Anonymous" }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
