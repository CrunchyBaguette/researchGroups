<template>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">Edytuj link</p>
    </header>
    <section class="modal-card-body">
      <p>{{ linkTitle }}</p>
      <p>{{ linkUrl }}</p>
    </section>
  </div>
</template>

<script>
export default {
  name: "editLinkModal",
  props: {
    linkTitle: { type: String },
    linkUrl: { type: String },
  },
};
</script>