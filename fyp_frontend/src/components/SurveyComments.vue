<script>
export default {
    data() {
        return {
            comments: [],
        };
    },
    props: ["surveyId"],

    // async created() {
    //     try {
    //         const response = await fetch(`/api/survey_comments/${this.surveyId}/`);

    //         this.comments = await response.json();
    //     } catch (error) {
    //         console.log("Error fetching comments:", error);
    //     }
    // },
};
</script>

<template>
    <div class="comments">
        <div
            v-for="comment in comments"
            :key="comment.created_at"
            class="comment"
        >
            <img
                :src="comment.avatar"
                :alt="comment.username + ' avatar'"
                class="avatar"
            />
            <div class="username">{{ comment.username }}</div>
            <div class="text">{{ comment.text }}</div>
            <div class="timestamp">{{ comment.created_at }}</div>
        </div>
    </div>
</template>

<style scoped>
/* styling/bootstrap to do*/
</style>
