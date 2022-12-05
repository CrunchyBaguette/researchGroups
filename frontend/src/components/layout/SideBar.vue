<template>
  <b-menu :activable="false" :accordion="false">
    <b-menu-list>
      <b-menu-item label="Koła naukowe">
        <b-menu-item
          v-for="researchGroup in this.userResearchGroups"
          :key="researchGroup.name"
          :label="researchGroup.name"
          tag="router-link"
          :to="
            isAuthenticated
              ? { name: 'group', params: { id: researchGroup.id } }
              : { name: 'login' }
          "
        ></b-menu-item>
      </b-menu-item>
      <b-menu-item label="Projekty">
        <b-menu-item
          v-for="project in this.userProjects"
          :key="project.name"
          :label="project.name"
          tag="router-link"
          :to="{ name: 'project', params: { id: project.id } }"
        ></b-menu-item>
      </b-menu-item>
    </b-menu-list>
  </b-menu>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex";

export default {
  name: "SideBar",

  methods: {
    ...mapActions("user", ["getUserResearchGroups", "getUserProjects"]),
  },

  computed: {
    ...mapGetters("auth", ["authUser", "isAuthenticated"]),
    ...mapGetters("researchGroup", ["researchGroups"]),
    ...mapGetters("project", ["projects"]),
    ...mapState({
      userResearchGroups: (state) => state.user.userResearchGroups,
    }),
    ...mapState({
      userProjects: (state) => state.user.userProjects,
    }),
  },

  watch: {
    researchGroups() {
      if (this.isAuthenticated) {
        this.getUserResearchGroups(this.authUser.id);
      }
    },
    projects() {
      if (this.isAuthenticated) {
        this.getUserProjects(this.authUser.id);
      }
    },
  },

  mounted() {
    if (this.isAuthenticated) {
      this.getUserResearchGroups(this.authUser.id);
      this.getUserProjects(this.authUser.id);
    }
  },
};
</script>

<style>
.menu {
  padding-top: 10px;
  padding-left: 10px;
  padding-right: 10px;
  height: 100%;
}
</style>