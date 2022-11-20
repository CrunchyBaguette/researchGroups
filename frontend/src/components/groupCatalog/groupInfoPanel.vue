<template>
  <div id="group-info-panel" v-if="researchGroup">
    <p class="group-info-panel-title">{{ researchGroup.name }}</p>
    <div
      class="box group-info-panel-desc-container"
      style="background-color: white"
    >
      <p
        style="
          font-size: 30px;
          position: sticky;
          top: 0;
          background-color: rgb(196, 196, 196);
          border-radius: 10px;
          padding-left: 5px;
        "
      >
        O nas:
      </p>
      <p style="font-size: 20px">
        {{ researchGroup.about_us }}
      </p>
    </div>
    <div style="width: 100%; text-align: center; margin-top: 40px">
      <b-button size="is-medium" style="text-align: center"
        >Przejdź do panelu koła</b-button
      >
    </div>
  </div>
  <div v-else class="no-research-group">
    <p>Wybierz koło naukowe z listy</p>
    <img src="@/assets/arrow-down-left.png" width="100" />
  </div>
</template>

<script>
export default {
  name: "groupInfoPanel",

  props: {
    researchGroup: { type: Object },
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
  margin-top: 40%;
}

.no-research-group p {
  width: 100%;
  font-size: 30px;
  margin-bottom: 50px;
}
</style>