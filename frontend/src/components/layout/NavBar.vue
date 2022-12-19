<template>
  <b-navbar>
    <template #brand>
      <b-navbar-item tag="router-link" :to="{ name: 'announcements' }">
        <img
          src="../../assets/logo.png"
          style="transform: scale(1.5); margin-left: 10px; margin-right: 10px"
        />
      </b-navbar-item>
    </template>

    <template #start>
      <b-navbar-item :to="{ name: 'groupCatalog' }" tag="router-link">
        <strong>Koła naukowe</strong>
      </b-navbar-item>
      <b-navbar-item :to="{ name: 'projectCatalog' }" tag="router-link">
        <strong>Projekty</strong>
      </b-navbar-item>
      <b-navbar-item :to="{ name: 'tutorialCatalog' }" tag="router-link">
        <strong>Poradniki</strong>
      </b-navbar-item>
    </template>

    <template #end v-if="!loginOrRegister">
      <b-navbar-item tag="div" v-if="!isAuthenticated">
        <div class="buttons">
          <b-button
            class="button-primary"
            :to="{ name: 'register' }"
            tag="router-link"
          >
            <strong>Rejestracja</strong>
          </b-button>
          <b-button type="is-light" :to="{ name: 'login' }" tag="router-link"
            >Zaloguj się
          </b-button>
        </div>
      </b-navbar-item>
      <b-navbar-item tag="div" v-else>
        <p style="margin-right: 10px; font-weight: bold">
          Witaj {{ authUser.username }}!
        </p>
        <div class="buttons">
          <b-button class="button-primary" @click="logout()">
            <strong>Wyloguj</strong>
          </b-button>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from "vuex";

export default {
  name: "NavBar",
  props: ["loginOrRegister"],

  methods: {
    ...mapActions("auth", ["logOut"]),
    ...mapMutations("user", ["setUserResearchGroups", "setUserProjects"]),
    logout() {
      this.setUserResearchGroups([]);
      this.setUserProjects([]);
      this.logOut();
      if (this.$route.path != "/") {
        this.$router.replace(this.$route.query.redirect || "/");
      }
    },
  },

  computed: {
    ...mapGetters("auth", ["isAuthenticated", "authUser"]),
  },
};
</script>

<style>
.navbar {
  background-color: var(--third-color-green);
}

a {
  color: black;
}
</style>