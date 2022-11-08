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

    <template #end>
      <b-navbar-item tag="div">
        <div class="buttons">
          <a class="button is-primary">
            <strong>Rejestracja</strong>
          </a>
          <a class="button is-light">Zaloguj się</a>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
export default {
  name: "NavBar",
  props: {
    groups: { type: Object },
    projects: { type: Object },
  },

  ready: function () {
    "b-navbar-item.test".on("click", function (e) {
      this.next("ul").toggle();
      e.stopPropagation();
      e.preventDefault();
    });
  },
};
</script>

<style>
.navbar {
  background-color: #a0ff42;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -1px;
}
</style>