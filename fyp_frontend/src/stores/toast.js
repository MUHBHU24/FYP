import { defineStore } from "pinia";

export const useToastStore = defineStore({
    id: "toast", // unique identifier for the store
    state: () => ({
        duration: 0, // time duration of the toast in ms
        title: "", // title of the toast
        text: "", // text message to display in the toast
        styling: "", // Bootstrap styling to apply to the toast
        isVisible: false, // flag to show/hide the toast
    }),
    actions: {
        // Add a new toast with the specified properties
        displayToast({ duration, title, text, styling }) {
            this.duration = parseInt(duration); // convert the time duration to an integer to avoid errors
            this.title = title;
            this.text = text; 
            this.styling = styling; 
            this.isVisible = true; // set the toast to be visible
            // this.toggleToast();
        },
        // Toggle the visibility of the toast (show/hide), if its on, turn it off, if its off, turn it on (currently not used as redundant)
        // toggleToast() {
        //   this.isVisible = !this.isVisible;
        // },
    },
});
