<script setup>
import { useToastStore } from "../stores/toast";

// Retrieve the toast store from Pinia
const store = useToastStore();
</script>

<template>
    <!-- Only display the toast if it's visible, and bind custom classes from the store -->
    <div
        v-if="store.isVisible"
        class="toast align-items-center text-white bg-danger border-0"
        :class="store.classes"
        role="alert"
        aria-live="assertive"
        aria-atomic="true"
    >
        <div class="d-flex">
            <!-- Show the message from the store -->
            <div class="toast-body">
                {{ store.message }}
            </div>
            <button
                type="button"
                class="btn-close btn-close-white me-2 m-auto"
                data-bs-dismiss="toast"
                aria-label="Close"
                @click="store.hideToast()"
            ></button>
        </div>
    </div>
</template>
