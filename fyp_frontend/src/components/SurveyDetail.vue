<script>
import SurveyComments from "./SurveyComments.vue";

export default {
	components: {
		SurveyComments,
	},
	data() {
		return {
			surveyId: null, // This should be set to the actual survey ID
		};
	},
	// other methods and lifecycle hooks
};
</script>

<template>
	  <survey-comments :survey-id="surveyId"></survey-comments> <!-- change surveyId to use vue router, maybe this.$route.params.surveyId -->
</template>
