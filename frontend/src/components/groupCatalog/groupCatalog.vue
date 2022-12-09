<template>
  <div id="content">
    <div style="width: 100%">
      <p class="title" style="float: left">Katalog kół naukowych</p>
      <b-button
        tag="router-link"
        :to="isAuthenticated ? { name: 'addGroup' } : { name: 'login' }"
        rounded
        size="is-medium"
        style="float: right; margin-top: 10px; margin-right: 20px"
        type="is-success"
        >Dodaj nowe koło naukowe</b-button
      >
    </div>
    <div id="column-container" class="columns" v-if="loaded">
      <div id="c1" class="box column is-two-thirds">
        <div class="columns">
          <div class="column">
            <groupTile
              v-for="researchGroup in this.splitToTwoColumns(researchGroups)[0]"
              :key="researchGroup.name"
              :group="researchGroup"
              style="margin-top: 10px; cursor: pointer"
              @click.native="chooseGroup(researchGroup)"
            />
          </div>
          <div class="column">
            <groupTile
              v-for="researchGroup in this.splitToTwoColumns(researchGroups)[1]"
              :key="researchGroup.name"
              :group="researchGroup"
              style="margin-top: 10px; cursor: pointer"
              @click.native="chooseGroup(researchGroup)"
            />
          </div>
        </div>
      </div>
      <div id="c2" class="box column">
        <groupInfoPanel :researchGroup="chosenResearchGroup" />
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

#c1 {
  background-color: white;
  overflow: auto;
}

#c2 {
  margin-left: 10px;
  margin-bottom: 1.5rem;
  background-color: rgb(196, 196, 196);
  overflow: auto;
}

#column-container {
  width: 100%;
  height: 90%;
}
</style>