import { defineStore } from "pinia";

export const useToastStore = defineStore({
  id: "toast", // unique identifier for the store
  state: () => ({
    ms: 0, // time duration of the toast
    message: "", // text message to display in the toast
    classes: "", // CSS classes to apply to the toast
    isVisible: false, // flag to show/hide the toast
  }),
  actions: {
    showToast(ms, message, classes) { // function to show the toast
      this.ms = parseInt(ms); // convert the time duration to an integer to avoid errors
      this.message = message; // set the message to display in the toast - same with classes and isVisible below
      this.classes = classes; 
      this.isVisible = true; 

      // animate the toast to slide up
      setTimeout(() => {
        this.classes += "-translate-y-28";
      }, 20);

      // animate the toast to slide down after the specified duration
      setTimeout(() => {
        this.classes = this.classes.replace("-translate-y-28", "");
      }, this.ms - 750);

      // hide the toast after the specified duration
      setTimeout(() => {
        this.isVisible = false;
      }, this.ms);
    },
  },
});
