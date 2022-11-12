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
    </b-navbar>
  </template>
  
  <script>
  export default {
    name: "NavBarWithLogin",
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