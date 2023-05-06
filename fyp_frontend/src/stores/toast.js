import { defineStore } from "pinia";

export const useToastStore = defineStore({
    id: "toast", // unique identifier for the store
    state: () => ({
        ms: 0, // time duration of the toast
        title: "", // title of the toast
        message: "", // text message to display in the toast
        classes: "", // CSS classes to apply to the toast
        isVisible: false, // flag to show/hide the toast
    }),
    actions: {
        // Add a new toast with the specified properties
        addToast({ ms, title, message, classes }) {
            this.ms = parseInt(ms); // convert the time duration to an integer to avoid errors
            this.title = title;
            this.message = message; 
            this.classes = classes; 
            this.isVisible = true; // set the toast to be visible

            // animate the toast to slide up
            setTimeout(() => {
                this.classes += "translate-y-3";
            }, 20);

            // animate the toast to slide down after the specified duration
            setTimeout(() => {
                this.classes = this.classes.replace("translate-y-3", "");
            }, this.ms - 750);

            // hide the toast after the specified duration
            setTimeout(() => {
                this.isVisible = false;
            }, this.ms);
        },
    },
});
