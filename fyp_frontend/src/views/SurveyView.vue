<script>
import axios from "axios";
import { useRouter } from "vue-router";
import SurveyDetail from "../components/SurveyDetail.vue";
import { ref, watchEffect } from "vue";

export default {
    name: "SurveyView",

    components: {
        SurveyDetail,
    },

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

    // async created() {
    //     try {
    //         // Uncomment the following line and replace the placeholder with actual API call to fetch the surveys
    //         // const response = await axios.get("/api/surveys/");
    //         // this.surveys = response.data.surveys;

    //         this.surveys = [
    //             {
    //                 id: 1,
    //                 title: "Sample Survey 1",
    //                 createdBy: "User1",
    //                 createdAt: "2023-05-07T10:00:00Z",
    //             },
    //             {
    //                 id: 2,
    //                 title: "Sample Survey 2",
    //                 createdBy: "User2",
    //                 createdAt: "2023-05-06T10:00:00Z",
    //             },
    //             {
    //                 id: 3,
    //                 title: "Sample Survey 3",
    //                 createdBy: "User3",
    //                 createdAt: "2023-05-05T10:00:00Z",
    //             },
    //         ];
    //     } catch (error) {
    //         console.log("Error fetching surveys:", error);
    //     }
    // },
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
        <div
            class="row row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3 gy-4"
        >
            <div
                v-for="survey in getAllSurveys"
                :key="survey.id"
                @click="selectSurvey(survey.slug)"
            >
            <template v-if="survey.id">
                test
                <SurveyDetail
                    :survey="survey"
                    :image="survey.item_image"
                    :title="survey.title"
                    :createdBy="survey.created_by?.username ?? 'Anonymous'"
                    :slug="survey.slug"
                />
            </template>
            </div>
        </div>
    </div>
</template>
