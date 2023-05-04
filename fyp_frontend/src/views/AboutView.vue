<template>
  <div class="container">
    <div class="row mt-5">
      <div class="col-12 text-center">
        <h1 class="display-4">About Vocabularious</h1>
      </div>
    </div>
    <div class="row mt-5">
      <div class="col-md-6 mb-3">
        <div class="embed-responsive embed-responsive-16by9">
          <iframe
            class="embed-responsive-item"
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d9581951.253777225!2d-15.00464572445363!3d54.10311305732506!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x25a3b1142c791a9%3A0xc4f8a0433288257a!2sUnited%20Kingdom!5e0!3m2!1sen!2suk!4v1683158841160!5m2!1sen!2suk"
            width="600"
            height="450"
            style="border: 0"
            allowfullscreen=""
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
          ></iframe>
        </div>
      </div>
      <div class="col-md-6">
        <p class="lead">
          Vocabularious is a platform dedicated to the study of language and
          dialects. We provide a comprehensive resource for linguistic
          enthusiasts and researchers to explore and understand the complexities
          of language variation.
        </p>
        <p>
          Our mission is to foster a global community where people can share
          their knowledge, insights, and experiences about language and
          dialects. We aim to make the study of language more accessible and
          engaging for everyone.
        </p>
        <p>
          Join our community to participate in surveys, view linguistic data on
          interactive maps, and learn more about the fascinating world of
          language variation.
        </p>
        <p>
          <small
            ><em
              >Please note: Vocabularious is solely focused on the theme of
              lexical variation at this point in time.</em
            ></small
          >
        </p>
        <button
          type="button"
          class="btn btn-info btn-sm mt-3 mb-3 text-white fw-bold fs-6 px-3 py-2 rounded-pill"
          data-bs-toggle="modal"
          data-bs-target="#lexicalVariationModal"
        >
          What exactly is lexical variation anyway?
        </button>
      </div>
    </div>
    <!-- Lexical Variation Modal -->
    <div
      class="modal fade"
      id="lexicalVariationModal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="lexicalVariationModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title fw-bold" id="lexicalVariationModalLabel">
              Lexical Variation
            </h5>
            <button
              type="button"
              class="close"
              data-bs-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            Variations in vocabulary, known as lexical variation, arise among
            different dialects, regions, or social groups, resulting in unique
            words, phrases, or expressions that convey similar meanings. This
            natural aspect of language evolution allows us to gain insights into
            the historical background, cultural influences, and social dynamics
            of speakers. Studying lexical variation enables researchers to delve
            deeper into the forces that shape linguistic change and the factors
            that contribute to the diversity of languages. Investigating and
            documenting lexical variation not only helps preserve our linguistic
            heritage but also encourages understanding and appreciation for the
            complexity and richness of human language.
            <br /><br />
            Common examples: <br /><br />
            (1) Regional variations: Vocabulary differences based on
            geographical location, often influenced by a combination of
            historical, cultural, and social factors. <br /><br />
            (2) Social variations: Vocabulary distinctions that stem from
            various social factors, such as age, gender, education, and
            socioeconomic status. <br /><br />
            (3) Temporal variations: Vocabulary changes that develop over time,
            reflecting ongoing advancements in culture, technology, and society.
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-info text-white"
              data-bs-dismiss="modal"
              aria-label="Close"
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
  name: "AboutView",
};
</script>
<style scoped>
.modal-dialog {
  max-width: 800px;
}
</style>
