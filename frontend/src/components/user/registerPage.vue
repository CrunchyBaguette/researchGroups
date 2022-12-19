<template>
  <div class="box register-container">
    <h1 class="title">Rejestracja</h1>

    <form @submit.prevent="submitForm">
      <b-field label="Imię">
        <b-input v-model="name" maxlength="30" required> </b-input>
      </b-field>

      <b-field label="Nazwisko">
        <b-input v-model="surname" maxlength="30" required> </b-input>
      </b-field>

      <b-field label="Email">
        <b-input
          :disabled="this.joining"
          type="email"
          v-model="email"
          maxlength="30"
          required
        >
        </b-input>
      </b-field>

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

      <b-field label="Powtórz hasło">
        <b-input
          type="password"
          v-model="repeatedPassword"
          password-reveal
          minlength="8"
          maxlength="30"
          required
        >
        </b-input>
      </b-field>

      <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>

      <b-button id="btnMain" class="button-secondary">ZAREJESTRUJ SIĘ</b-button>

      <router-link :to="{ name: 'login' }" id="btnOther">
        Masz już konto? &nbsp;
        <p class="p-login">Zaloguj się.</p>
      </router-link>
    </form>
    <b-loading
      :is-full-page="true"
      v-model="isLoading"
      :can-cancel="false"
    ></b-loading>
  </div>
</template>

<script>
import { mapActions } from "vuex";
//import axios from 'axios'
//import { toast } from 'bulma-toast'

export default {
  name: "registerPage",
  data() {
    return {
      name: "",
      surname: "",
      email: "",
      login: "",
      password: "",
      repeatedPassword: "",
      errors: [],
      isLoading: false,
      joining: false,
      researchGroupId: "",
      projectId: "",
    };
  },
  mounted() {
    document.title = "Zarejestruj się";
    if (this.$route.query.email) {
      this.email = this.$route.query.email;
      this.joining = true;
    }
  },
  methods: {
    ...mapActions("register", ["registerUser", "registerUserFromInvite"]),
    submitForm() {
      this.errors = [];

      // if (this.surname === '') {
      //   this.errors.push('Nie podałeś nazwiska!')
      // }
      // if (this.email === '') {
      //   this.errors.push('Nie podałeś emaila!')
      // }
      // if (this.login === '') {
      //   this.errors.push('Nie podałeś loginu!')
      // }
      // if (this.password === '') {
      //   this.errors.push('Nie podałeś hasła!')
      // }
      if (this.password !== this.repeatedPassword) {
        this.errors.push("Hasła się nie zgadzają!");
      }
      if (!this.errors.length) {
        this.isLoading = true;
        this.registerUser({
          joining: this.joining,
          user: {
            first_name: this.name,
            last_name: this.surname,
            email: this.email,
            username: this.login,
            password: this.password,
          },
        })
          .then(() => {
            this.name = "";
            this.surname = "";
            this.email = "";
            this.login = "";
            this.password = "";
            this.repeatedPassword = "";
            this.isLoading = false;
            this.researchGroupId = "";
            this.projectId = "";
            this.$buefy.toast.open({
              message: "Wysłano email z linkiem aktywacyjnym",
              type: "is-success",
            });
          })
          .catch((err) => {
            this.isLoading = false;
            this.$buefy.toast.open({
              message: err.response.data[Object.keys(err.response.data)[0]],
              type: "is-danger",
            });
          });
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

.register-container {
  margin: 0 auto;
  max-width: 400px;
}

.title {
  text-align: center;
}

.p-login {
  text-decoration: underline;
}

/* #btnRegister {
  display: flex;
  width: 100%;
  border-color: transparent;
  font-weight: bold;
  color: white;
  transition: 0.3s;
}

#btnRegister:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
} */

#link {
  display: flex;
  position: relative;
  padding: 0.5rem 0.75rem;
  line-height: 1.5;
  color: #4a4a4a;
  border: none;
  transition: 0.3s;
  cursor: pointer;
}

#link:hover {
  color: #7957d5;
  background-color: #fafafa;
}

/* #b-input {
  display: flex;
  height: 40px; 
  
} 

.label {
    
} */
</style>