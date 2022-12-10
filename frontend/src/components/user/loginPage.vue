<template>
  <div
    style="
      height: 100%;
      width: 100%;
      justify-content: center;
      display: flex;
      align-items: center;
    "
  >
    <div class="box login-container">
      <h1 class="title">Logowanie</h1>

      <br />

      <form @submit.prevent="submitLoginForm">
        <b-field label="Login">
          <b-input v-model="login" maxlength="30" required> </b-input>
        </b-field>

        <b-field label="Hasło">
          <b-input
            type="password"
            v-model="password"
            password-reveal
            minlength="8"
            maxlength="30"
            required
          >
          </b-input>
        </b-field>

        <div class="notification is-danger" v-if="loginBtnErrors.length">
          <p v-for="error in loginBtnErrors" v-bind:key="error">{{ error }}</p>
        </div>

        <br />

        <button id="btnLogin" class="button">ZALOGUJ SIĘ</button>
      </form>

      <br />

      <div class="notification is-danger" v-if="remindPasswordError !== ''">
        <p>{{ remindPasswordError }}</p>
      </div>

      <button id="btnOther" class="button" v-on:click="moveToRemindPassword">
        Nie pamiętam hasła.
      </button>

      <br />

      <router-link :to="{ name: 'register' }" id="btnOther">
        Nie masz konta? &nbsp;
        <p class="p-register">Zarejestruj się.</p>
      </router-link>
    </div>
  </div>
</template>

<script>
//import axios from 'axios'
import { mapActions } from "vuex";

export default {
  name: "loginPage",
  data() {
    return {
      login: "",
      password: "",
      loginBtnErrors: [],
      remindPasswordError: "",
    };
  },
  mounted() {
    document.title = "Zaloguj się";
  },
  methods: {
    ...mapActions("auth", ["getTokenPairs"]),
    async submitLoginForm() {
      this.loginBtnErrors = [];
      // if (this.login === '') {
      //   this.errors.push('Nie podałeś loginu!')
      // }
      // if (this.password === '') {
      //   this.errors.push('Nie podałeś hasła!')
      // }
      // axios.defaults.headers.common["Authorization"] = ""
      // localStorage.removeItem("token")
      if (!this.loginBtnErrors.length) {
        this.getTokenPairs({
          username: this.login,
          password: this.password,
        })
          .then(() => {
            this.$buefy.toast.open({
              message: "Zalogowano pomyślnie",
              type: "is-success",
            });

            this.$router.replace(this.$route.query.redirect || "/");
          })
          .catch((err) => {
            this.$buefy.toast.open({
              message: err.response.data[Object.keys(err.response.data)[0]],
              type: "is-danger",
            });
          });
        /*
        const formData = {
          login: this.username,
          password: this.password
        }
        
        await axios
          .post("/api/v1/token/login/", formData)
          .then(response => {
              const token = response.data.auth_token
              this.$store.commit('setToken', token)
              
              axios.defaults.headers.common["Authorization"] = "Token " + token
              localStorage.setItem("token", token)
              const toPath = this.$route.query.to || '/cart'
              this.$router.push(toPath)
          })
          .catch(error => {
              if (error.response) {
                  for (const property in error.response.data) {
                      this.loginBtnErrors.push(`${property}: ${error.response.data[property]}`)
                  }
              } else {
                  this.loginBtnErrors.push('Something went wrong. Please try again')
                  
                  console.log(JSON.stringify(error))
              }
          })
          */
      }
    },
    moveToRemindPassword() {
      this.remindPasswordError = "";
      if (this.login === "") {
        this.remindPasswordError = "Wprowadź login!";
      }
    },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.login-container {
  margin: 0 auto;
  width: 400px;
}

.title {
  text-align: center;
}

.p-register {
  text-decoration: underline;
}

#btnLogin {
  display: flex;
  width: 100%;
  background-color: #7957d5;
  border-color: transparent;
  font-weight: bold;
  color: white;
  transition: 0.3s;
}

#btnLogin:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
}

#btnOther {
  display: flex;
  position: relative;
  padding: 0.5rem 0.75rem;
  line-height: 1.5;
  color: #4a4a4a;
  border: none;
  transition: 0.3s;
  cursor: pointer;
}

#btnOther:hover {
  color: #7957d5;
  background-color: #fafafa;
}
</style>
