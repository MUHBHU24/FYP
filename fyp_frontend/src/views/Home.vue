<template>
    <div class="p-5">
        <h1 class="mb-4 text-center display-4">
            What kind of questions should you expect on Vocabularious?
        </h1>

        <div class="row row-cols-1 row-cols-md-2 g-4">
            <div class="col" v-for="card in cards" :key="card.id">
                <div
                    class="card h-100 text-white text-center d-flex align-items-center justify-content-center"
                    :class="card.colorClass"
                    style="cursor: pointer"
                    data-bs-toggle="modal"
                    :data-bs-target="'#' + card.modalId"
                >
                    <h5 class="card-title">{{ card.question }}</h5>
                </div>
            </div>
        </div>

        <!-- Modal for each card -->
        <div
            class="modal fade"
            :id="card.modalId"
            tabindex="-1"
            v-for="card in cards"
            :key="card.id + 'modal'"
            aria-labelledby="modalLabel"
            aria-hidden="true"
        >
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="modalLabel">
                            {{ card.question }}
                        </h5>
                        <button
                            type="button"
                            class="btn-close"
                            data-bs-dismiss="modal"
                            aria-label="Close"
                        ></button>
                    </div>
                    <div class="modal-body">
                        {{ card.answer }}
                    </div>
                    <div class="modal-footer">
                        <button
                            type="button"
                            class="btn btn-secondary"
                            data-bs-dismiss="modal"
                        >
                            Close
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Home",
    data() {
        return {
            cards: [
                {
                    id: 1,
                    question: "Example 1",
                    answer: "Do you call it pop, soda, or fizzy drinks?",
                    modalId: "modal1",
                    colorClass: "bg-primary",
                },
                {
                    id: 2,
                    question: "Example 2",
                    answer: "How do you refer to the term 'bathroom'?",
                    modalId: "modal2",
                    colorClass: "bg-danger",
                },
                {
                    id: 3,
                    question: "Example 3",
                    answer: "Trousers or pants, which one is correct?",
                    modalId: "modal3",
                    colorClass: "bg-success",
                },
                {
                    id: 4,
                    question: "Example 4",
                    answer: "Is it tea time or dinner time?",
                    modalId: "modal4",
                    colorClass: "bg-warning",
                },
            ],
        };
    },
};
</script>

<style scoped>
.card {
    height: 300px; /* Set the height of the card */
    font-size: 1.5rem; /* Increase the font size */
}
</style>
