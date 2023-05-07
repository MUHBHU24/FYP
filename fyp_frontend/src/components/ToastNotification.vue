<script setup>
import { useToastStore } from "../stores/toast";
import { ref, watch } from "vue";

// Retrieve the toast store from Pinia
const store = useToastStore();
const toastElement = ref(null);

// Watch for changes to the toast store's isVisible property and show the toast if it's visible and hide it if it's not
watch(
    () => store.isVisible,
    (newValue) => {
        if (newValue) {
            const toast = new bootstrap.Toast(toastElement.value, {
                autohide: true,
                delay: store.duration, // Set the duration of the toast to the value in the store
            });
            toast.show();
            toastElement.value.addEventListener("hidden.bs.toast", () => {
                store.toggleToast();
            });
        }
    }
);
</script>

<template>
    <!-- Add a toast element to the template -->
    <div
        v-if="store.isVisible"
        class="toast align-items-center"
        :class="store.styling"
        role="alert"
        aria-live="assertive"
        aria-atomic="true"
        ref="toastElement"
    >
        <div class="d-flex">
            <div class="toast-body">
                {{ store.text }}
                <!-- Display the text from the store -->
            </div>
            <!-- add a white close button to the toast-->
            <button
                type="button"
                class="btn-close btn-close-white me-2 m-auto"
                data-bs-dismiss="toast"
                aria-label="Close"
                @click="store.toggleToast()"
            ></button>
        </div>
    </div>
</template>
