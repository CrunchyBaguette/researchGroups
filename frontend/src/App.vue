<template>
  <div id="app">
    <div class="columns" style="height: 100%">
      <div class="column">
        <div>
          <NavBar :loginOrRegister="this.isLoginOrRegister()" />
        </div>
        <div class="columns" style="height: 100%">
          <div
            id="sidebar"
            class="column is-2"
            v-if="!this.isLoginOrRegister()"
          >
            <SideBar />
          </div>
          <div class="column" style="background-color: rgb(165, 255, 179)">
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
  methods: {
    isLoginOrRegister() {
      return (
        this.$route.name == "login" ||
        this.$route.name == "register" ||
        this.$route.name == "passwordReminder"
      );
    },
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
  background-color: rgb(203, 203, 203);
}

#navbar {
  z-index: 40;
}

#content {
  padding: 10px;
  height: 100%;
  position: relative;
  overflow: auto;
  word-wrap: anywhere;
  white-space: normal;
}

/* .wrapper-content {
    padding-top: 80px;
}

.modal__btn-list {
    display: flex;
    justify-content: center;  
}

.modal__btn-list .btn {
    margin: 0 20px;
} */

</style> 
