<script>
import SurveyComments from "./SurveyComments.vue";

export default {
	components: {
		SurveyComments,
	},
	computed: {
		surveyId() {
			return this.$route.params.surveyId;
		},
	},
};
</script>

<template>
	<survey-comments :survey-id="surveyId"></survey-comments>
</template>
