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
      <h1 class="title">Przypomnienie hasła</h1>

      <br />

      <form @submit.prevent="submitForm">
        <b-field label="Podaj emaila/jeden z emaili">
          <b-input type="email" v-model="email" maxlength="30" required>
          </b-input>
        </b-field>

        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>

        <br />

        <button id="btnReset" class="button">RESETUJ HASŁO</button>
      </form>
    </div>
  </div>
</template>
  
<script>
export default {
  name: "passwordReminder",
  data() {
    return {
      email: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Przypomnienie";
  },
  methods: {
    async submitForm() {
      this.errors = [];
      // if (this.login === '') {
      //   this.errors.push('Nie podałeś emaila!')
      // }
      // axios.defaults.headers.common["Authorization"] = ""
      // localStorage.removeItem("token")
      if (!this.errors.length) {
        // const formData = {
        //   login: this.username,
        //   password: this.password
        // }
        //code for sending email
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
  max-width: 400px;
}

.title {
  text-align: center;
}

#btnReset {
  display: flex;
  width: 100%;
  background-color: #7957d5;
  border-color: transparent;
  font-weight: bold;
  color: white;
  transition: 0.3s;
}

#btnReset:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
}
</style>