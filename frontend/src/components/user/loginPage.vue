<template>
  <div class="login-container">
    <h1 class="title">Logowanie</h1>

    <br>

    <form @submit.prevent="submitForm">
      <b-field label="Login">
          <b-input v-model="login"
              maxlength="30"
              required>
          </b-input>
      </b-field>

      <b-field label="Hasło">
          <b-input type="password" v-model="password"
              password-reveal
              minlength="8"
              maxlength="30"
              required>
          </b-input>
      </b-field>

      <b-navbar-item :to="{ name: 'passwordReminder' }" tag="router-link">
          Nie pamiętam hasła.
      </b-navbar-item>

      <br>

      <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>

      <br>

      <button id="btnLogin" class="button">ZALOGUJ SIĘ</button>

      <br>
      <br>

      <b-navbar-item :to="{ name: 'register' }" tag="router-link">
          Nie masz konta? &nbsp;<p class="p-register"> Zarejestruj się. </p>
      </b-navbar-item>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "loginPage",
  data() {
    return {
      login: '',
      password: '',
      errors: []
    }
  },
  mounted() {
      document.title = 'Zaloguj się'
  },
  methods: {
    async submitForm() {
      this.errors = []
      // if (this.login === '') {
      //   this.errors.push('Nie podałeś loginu!')
      // }
      // if (this.password === '') {
      //   this.errors.push('Nie podałeś hasła!')
      // }
      // axios.defaults.headers.common["Authorization"] = ""
      // localStorage.removeItem("token")
      if (!this.errors.length) {
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
                      this.errors.push(`${property}: ${error.response.data[property]}`)
                  }
              } else {
                  this.errors.push('Something went wrong. Please try again')
                  
                  console.log(JSON.stringify(error))
              }
          })
      }
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.login-container {
  margin: 0 auto;
  max-width: 320px;
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
  transition: .3s;
}

#btnLogin:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
}

</style>