<template>
  <div id="content" style="display: flex; flex-flow: column">
    <div>
      <p class="title" style="float: left">Katalog kół naukowych</p>
      <b-button
        class="button-secondary"
        tag="router-link"
        :to="isAuthenticated ? { name: 'addGroup' } : { name: 'login' }"
        rounded
        size="is-medium"
        style="float: right; margin-top: 10px; margin-right: 20px"
        >Dodaj nowe koło naukowe</b-button
      >
    </div>
    <div style="overflow: auto; height: 100%">
      <div style="height: 100%; width: 100%" class="columns" v-if="loaded">
        <div
          style="max-height: 100%; overflow: auto"
          class="box column is-two-thirds"
        >
          <div class="columns">
            <div class="column">
              <groupTile
                v-for="researchGroup in this.splitToTwoColumns(
                  researchGroups
                )[0]"
                :key="researchGroup.name"
                :group="researchGroup"
                style="cursor: pointer"
                @click.native="chooseGroup(researchGroup)"
              />
            </div>
            <div class="column">
              <groupTile
                v-for="researchGroup in this.splitToTwoColumns(
                  researchGroups
                )[1]"
                :key="researchGroup.name"
                :group="researchGroup"
                style="cursor: pointer"
                @click.native="chooseGroup(researchGroup)"
              />
            </div>
          </div>
        </div>
        <div
          style="
            max-height: 100%;
            overflow: auto;
            margin-left: 10px;
            margin-bottom: 1.5rem;
          "
          class="box column"
        >
          <groupInfoPanel :researchGroup="chosenResearchGroup" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from "vuex";
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

    chooseGroup(researchGroup) {
      this.chosenResearchGroup = researchGroup;
    },
  },

  computed: {
    ...mapState({
      researchGroups: (state) => state.researchGroup.researchGroups,
    }),
    ...mapGetters("auth", ["isAuthenticated"]),
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

#column-container {
  width: 100%;
  height: 90%;
}

.columns {
  margin: 0 !important;
}
</style>