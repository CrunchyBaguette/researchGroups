<template>
  <div id="group-info-panel" v-if="project">
    <p class="group-info-panel-title">{{ project.name }}</p>
    <div
      class="box group-info-panel-desc-container"
      style="background-color: white; overflow-x: hidden"
    >
      <p class="box-title">Opis projektu:</p>
      <p style="font-size: 20px">
        <markdown-it-vue
          class="md-body"
          :content="project.description"
          :options="markdownOptions"
        />
      </p>
    </div>
    <div
      style="
        width: 100%;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
      "
    >
      <b-button
        class="button-secondary"
        rounded
        size="is-medium"
        style="text-align: center"
        tag="router-link"
        :to="{ name: 'project', params: { id: project.id } }"
        >Przejdź do panelu projektu</b-button
      >
    </div>
  </div>
  <div v-else class="no-research-group">
    <p>Wybierz projekt z listy</p>
    <img src="@/assets/arrow-down-left.png" width="100" />
  </div>
</template>

<script>
export default {
  name: "projectInfoPanel",

  props: {
    project: { type: Object },
  },

  data() {
    return {
      markdownOptions: {
        markdownIt: {
          html: true,
          linkify: true,
        },
        linkAttributes: {
          attrs: {
            target: "_self",
            rel: "noopener",
          },
        },
      },
    };
  },
};
</script>

<style>
#group-info-panel {
  width: 100%;
  height: 100%;
}

.group-info-panel-title {
  font-size: 50px;
  padding: 10px;
}

.group-info-panel-desc-container {
  height: 70%;
  padding: 10px;
  border-radius: 25px;
  /* border: 5px solid black; */
  overflow: auto;
}

.no-research-group {
  text-align: center;
  margin-top: 35%;
}

.no-research-group p {
  width: 100%;
  font-size: 30px;
  margin-bottom: 50px;
}
</style>