<template>
  <div id="app">
    <div>
      <NavBar :loginOrRegister="this.isLoginOrRegister()" />
    </div>
    <div style="height: 100%">
      <div class="columns" style="height: 100%; margin-top: 0">
        <div id="sidebar" class="column is-2" v-if="!this.isLoginOrRegister()">
          <SideBar />
        </div>
        <div class="column" style="padding: 0">
          <div id="content">
            <router-view />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var head = document.getElementsByTagName("head")[0];
var mdiLink = document.createElement("link");
mdiLink.id = "MaterialDesign";
mdiLink.rel = "stylesheet";
mdiLink.type = "text/css";
mdiLink.media = "all";

var mdiRequest = new Request(
  "https://cdn.materialdesignicons.com/5.8.55/css/materialdesignicons.min.css"
);

fetch(mdiRequest)
  .then(function (value) {
    if (value.status == 404) {
      throw new Error("Redirected page not found");
    }
    mdiLink.href =
      "https://cdn.materialdesignicons.com/5.8.55/css/materialdesignicons.min.css";
  })
  .catch(() => {
    mdiLink.href =
      "https://cdnjs.cloudflare.com/ajax/libs/materialDesign-Webfont/5.8.55/css/materialdesignicons.min.css";
  });

head.appendChild(mdiLink);

import NavBar from "./components/layout/NavBar.vue";
import SideBar from "./components/layout/SideBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
    SideBar,
  },

  data() {
    return {
      markdownOptions: {
        markdownIt: {
          html: true,
          linkify: true,
        },
        linkAttributes: {
          attrs: {
            target: "_self",
            rel: "noopener",
          },
        },
      },
    };
  },

  methods: {
    isLoginOrRegister() {
      return (
        this.$route.name == "login" ||
        this.$route.name == "register" ||
        this.$route.name == "passwordReminder" ||
        this.$route.name == "passwordReset"
      );
    },
  },
};
</script>

<style>
@import '@/styles/colors.css';
html {
  overflow: auto;
  background-color: var(--first-color);
}

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
  display: flex;
  flex-flow: column;
}

#sidebar {
  float: left;
  height: 100%;
  left: 0;
  width: 13%;
  min-width: 100px;
  background-color: var(--first-color);
  filter: brightness(98%);
  border-right-style: solid;
  border-right-color: var(--fourth-color);
  border-right-width: 1px;
}
#sidebar a:hover {
  background-color: var(--first-color);
  filter: brightness(95%);
}

#navbar {
  z-index: 40;
}

#content {
  padding: 10px;
  height: 100%;
  position: relative;
  word-wrap: anywhere;
  white-space: normal;
  background-color: var(--first-color);
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
