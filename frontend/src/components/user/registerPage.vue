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
        <b-input type="email" v-model="email" maxlength="30" required>
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

      <button id="btnRegister" class="button">ZAREJESTRUJ SIĘ</button>

      <router-link :to="{ name: 'login' }" id="link">
        Masz już konto? &nbsp;
        <p class="p-login">Zaloguj się.</p>
      </router-link>
    </form>
  </div>
</template>

<script>
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
    };
  },
  mounted() {
    document.title = "Zarejestruj się";
  },
  methods: {
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
        /*
        const formData = {
          name: this.name,
          surname: this.surname,
          email: this.email,
          login: this.login,
          password: this.password
        }

        axios
          .post("api/v1/users/", formData) 
          .then(() => {
            toast({
              message: 'Konto zostało stworzone, można się zalogować!',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right'
            })

            this.$router.push('/login')
          })
          .catch(error => {
            if (error.response){
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
              console.log(error.response.data);
            } else if (error.message) {
              this.errors.push('Coś poszło nie tak. Spróbuj ponownie')
              console.log(JSON.stringify(error));
            }
          })
          */
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

#btnRegister {
  display: flex;
  width: 100%;
  background-color: #7957d5;
  border-color: transparent;
  font-weight: bold;
  color: white;
  transition: 0.3s;
}

#btnRegister:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
}

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