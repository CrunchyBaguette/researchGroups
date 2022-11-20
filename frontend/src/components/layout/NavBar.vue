<template>
  <b-navbar>
    <template #brand>
      <b-navbar-item tag="router-link" :to="{ name: 'announcements' }">
        <img
          src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
          alt="Lightweight UI components for Vue.js based on Bulma"
        />
      </b-navbar-item>
    </template>

    <template #start>
      <b-navbar-item :to="{ name: 'groupCatalog' }" tag="router-link">
        Koła naukowe
      </b-navbar-item>
      <b-navbar-item :to="{ name: 'projectCatalog' }" tag="router-link">
        Projekty
      </b-navbar-item>
      <b-navbar-item :to="{ name: 'tutorialCatalog' }" tag="router-link">
        Poradniki
      </b-navbar-item>
    </template>

    <template #end v-if="!loginOrRegister">
      <b-navbar-item tag="div" v-if="!isAuthenticated">
        <div class="buttons">
          <b-button
            type="is-primary"
            :to="{ name: 'register' }"
            tag="router-link"
          >
            <strong>Rejestracja</strong>
          </b-button>
          <b-button type="is-light" :to="{ name: 'login' }" tag="router-link"
            >Zaloguj się</b-button
          >
        </div>
      </b-navbar-item>
      <b-navbar-item tag="div" v-else>
        <p style="margin-right: 10px; font-weight: bold">
          Witaj {{ authUser.username }}!
        </p>
        <div class="buttons">
          <b-button type="is-primary" @click="logout()">
            <strong>Wyloguj</strong>
          </b-button>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "NavBar",
  props: ["loginOrRegister"],

  methods: {
    ...mapActions("auth", ["logOut"]),
    logout() {
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
  background-color: #a0ff42;
}
a {
  color: black;
}
</style>