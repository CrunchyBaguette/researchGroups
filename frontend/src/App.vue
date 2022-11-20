<!-- <template>
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
  methods: {
    isLoginOrRegister() {
      return this.$route.name == "login" || this.$route.name == "register" || this.$route.name == "passwordReminder";
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
} -->

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

<!-- </style> -->



<template>
  <div id="editor">
      <div>
          {{ markdown }}
      </div>
      <textarea v-model="markdown"></textarea>
      <div v-html="markdownToHtml"></div>
      <h1>Coś tam</h1>
      <p>coś tam</p>
      <span>coś tam</span>
      <u>sadjfkbdabj</u>
  </div>
</template>

<script>
import {marked} from 'marked';

export default {
  name: 'App',
  data() {
      return {
          markdown: '# hello world',
      };
  },
  computed: {
      markdownToHtml() {
          return marked(this.markdown);
      },
  },
}
</script>


<style>
/*
html,
body,
#editor {
  margin: 0;
  height: 100%;
  font-family: "Helvetica Neue", Arial, sans-serif;
  color: #333;
}

textarea,
#editor div {
  display: inline-block;
  width: 49%;
  height: 100%;
  vertical-align: top;
  box-sizing: border-box;
  padding: 0 20px;
}

textarea {
  border: none;
  border-right: 1px solid #ccc;
  resize: none;
  outline: none;
  background-color: #f6f6f6;
  font-size: 14px;
  font-family: "Monaco", courier, monospace;
  padding: 20px;
}

code {
  color: #f66;
}
*/
</style>  