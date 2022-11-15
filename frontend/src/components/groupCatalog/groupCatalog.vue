<template>
  <div id="content">
    <p class="title">Katalog kół naukowych</p>
    <div id="column-container" class="columns" v-if="loaded">
      <div id="c1" class="column is-two-thirds">
        <div class="columns">
          <div
            class="column"
            v-for="researchGroupList in this.splitToTwoColumns(researchGroups)"
            :key="researchGroupList"
          >
            <groupTile
              v-for="researchGroup in researchGroupList"
              :key="researchGroup"
              :groupName="researchGroup.name"
              style="margin-top: 10px"
            />
          </div>
        </div>
      </div>
      <div id="c2" class="column">
        <groupInfoPanel />
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import groupTile from "./groupTile.vue";
import groupInfoPanel from "./groupInfoPanel.vue";

export default {
  name: "groupCatalog",
  components: {
    groupTile,
    groupInfoPanel,
  },

  data() {
    return {
      loaded: false,
    };
  },

  methods: {
    ...mapActions("researchGroup", ["getResearchGroups"]),
    splitToTwoColumns(groups) {
      let leftColumn = [];
      let rightColumn = [];

      for (let i = 0; i < groups.length; i++) {
        if (i % 2 == 0) {
          leftColumn.push(groups[i]);
        } else {
          rightColumn.push(groups[i]);
        }
      }

      return [leftColumn, rightColumn];
    },
  },

  computed: {
    ...mapState({
      researchGroups: (state) => state.researchGroup.researchGroups,
    }),
  },

  mounted() {
    // this.test ponieważ przed renderem należy poczekać na dane
    this.getResearchGroups().then(() => (this.loaded = true));
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