<script setup>
import { useToastStore } from "@/stores/toast";

// Retrieve the toast store from Pinia
const store = useToastStore();

</script>

<template>
    <!-- Only display the toast if it's visible, and bind custom classes from the store -->
    <div
        v-if="store.isVisible"
        class="transition fade show fixed-bottom m-3"
        :class="store.classes"
        style="padding: 1rem; background-color: #fff"
    >
        <!-- Show the message from the store -->
        {{ store.message }}
    </div>
</template>
