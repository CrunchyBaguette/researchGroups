<template>
  <div id="content">
    <p class="title">Katalog kół naukowych</p>
    <div id="column-container" class="columns" v-if="test">
      <div id="c1" class="column is-two-thirds">
        <groupTile
          :groupName="researchGroups[0].name"
          style="float: left; margin: 10px"
        />
        <groupTile
          :groupName="researchGroups[1].name"
          style="float: right; margin: 10px"
        />
      </div>
      <div id="c2" class="column"></div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import groupTile from "./groupTile.vue";

export default {
  name: "groupCatalog",
  components: {
    groupTile,
  },

  data() {
    return {
      test: false,
    };
  },

  methods: {
    ...mapActions("researchGroup", ["getResearchGroups"]),
  },

  computed: {
    ...mapState({
      researchGroups: (state) => state.researchGroup.researchGroups,
    }),
  },

  mounted() {
    // this.test ponieważ przed renderem należy poczekać na dane
    this.getResearchGroups().then(() => (this.test = true));
  },
};
</script>

<style>
.title {
  font-size: 40px;
  padding: 10px;
}

#c1 {
  background-color: aquamarine;
  overflow: auto;
}

#c2 {
  background-color: rgb(255, 73, 204);
}

#column-container {
  width: 100%;
  height: 90%;
}
</style>