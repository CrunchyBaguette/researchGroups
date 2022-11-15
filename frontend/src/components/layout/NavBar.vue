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
      <b-navbar-item tag="div">
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
    </template>
  </b-navbar>
</template>

<script>
export default {
  name: "NavBar",
  props: ['loginOrRegister'],
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