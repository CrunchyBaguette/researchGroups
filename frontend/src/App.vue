<template>
  <div id="app">
    <div class="columns" style="height: 100%">
      <div class="column">
        <NavBar />
        <div class="columns" style="height: 100%">
          <div class="column is-2">
            <SideBar />
          </div>
          <div class="column">
            <div id="content">
              <router-view />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "./components/layout/NavBar.vue";
import SideBar from "./components/layout/SideBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
    SideBar,
  },
};
</script>

<style>
html,
body {
  height: 100%;
}

#navbar {
  position: sticky;
  top: 0;
}

#app {
  height: 100%;
  overflow: hidden;
}

#sidebar {
  float: left;
  height: 100%;
  left: 0;
  width: 13%;
  min-width: 100px;
  background-color: rgb(224, 224, 224);
}

#navbar {
  z-index: 40;
}

#content {
  /* float: left; */
  padding: 10px;
  height: 100%;
  position: relative;
  overflow: auto;
  word-wrap: anywhere;
  white-space: normal;
  background-color: red;
}
</style>
