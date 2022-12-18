<template>
  <div id="content" style="display: flex; flex-flow: column">
    <div>
      <p class="title" style="float: left">Katalog projektów</p>
      <b-button
        tag="router-link"
        :to="isAuthenticated ? { name: 'addProject' } : { name: 'login' }"
        rounded
        size="is-medium"
        style="float: right; margin-top: 10px; margin-right: 20px"
        type="is-success"
        >Stwórz nowy projekt</b-button
      >
    </div>
    <div style="overflow: auto; height: 100%">
      <div style="height: 100%; width: 100%" class="columns" v-if="loaded">
        <div id="c1" style="max-height: 100%" class="box column is-two-thirds">
          <div class="columns">
            <div class="column">
              <projectTile
                v-for="project in this.splitToTwoColumns(projects)[0]"
                :key="project.name"
                :project="project"
                style="cursor: pointer"
                @click.native="chooseProject(project)"
              />
            </div>
            <div class="column">
              <projectTile
                v-for="project in this.splitToTwoColumns(projects)[1]"
                :key="project.name"
                :project="project"
                style="cursor: pointer"
                @click.native="chooseProject(project)"
              />
            </div>
          </div>
        </div>
        <div id="c2" style="max-height: 100%" class="box column">
          <projectInfoPanel :project="chosenProject" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from "vuex";
import projectTile from "./projectTile.vue";
import projectInfoPanel from "./projectInfoPanel.vue";

export default {
  name: "projectCatalog",
  components: {
    projectTile,
    projectInfoPanel,
  },

  data() {
    return {
      loaded: false,
      chosenProject: null,
    };
  },

  methods: {
    ...mapActions("project", ["getProjects"]),
    splitToTwoColumns(projects) {
      let leftColumn = [];
      let rightColumn = [];

      for (let i = 0; i < projects.length; i++) {
        if (i % 2 == 0) {
          leftColumn.push(projects[i]);
        } else {
          rightColumn.push(projects[i]);
        }
      }

      return [leftColumn, rightColumn];
    },

    chooseProject(project) {
      this.chosenProject = project;
    },
  },

  computed: {
    ...mapState({
      projects: (state) => state.project.projects,
    }),
    ...mapGetters("auth", ["isAuthenticated"]),
  },

  mounted() {
    // this.test ponieważ przed renderem należy poczekać na dane
    this.getProjects().then(() => (this.loaded = true));
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

.columns {
  margin: 0 !important;
}
</style>