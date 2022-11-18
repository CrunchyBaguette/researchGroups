<template>
  <div id="content">
    <p class="title">Katalog kół naukowych</p>
    <div id="column-container" class="columns" v-if="loaded">
      <div id="c1" class="column is-two-thirds">
        <div class="columns">
          <div
            class="column"
            v-for="researchGroupList in this.splitToTwoColumns(researchGroups)"
            :key="researchGroupList[0].name"
          >
            <groupTile
              v-for="researchGroup in researchGroupList"
              :key="researchGroup.name"
              :group="researchGroup"
              style="margin-top: 10px; cursor: pointer"
              @click.native="cliced(researchGroup)"
            />
          </div>
        </div>
      </div>
      <div id="c2" class="column">
        <groupInfoPanel :researchGroup="chosenResearchGroup" />
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
      chosenResearchGroup: null,
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

    cliced(researchGroup) {
      console.log(researchGroup.id);
      this.chosenResearchGroup = researchGroup;
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
  border: 5px solid black;
  background-color: white;
  overflow: auto;
}

#c2 {
  border: 5px solid black;
  background-color: rgb(196, 196, 196);
  overflow: auto;
}

#column-container {
  width: 100%;
  height: 90%;
}
</style>