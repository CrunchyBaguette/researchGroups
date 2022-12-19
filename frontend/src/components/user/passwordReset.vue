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
      <h1 class="title">Zresetuj hasło</h1>

      <br />

      <form @submit.prevent="submitForm">
        <b-field label="Podaj nowe hasło">
          <b-input type="password" v-model="password" maxlength="30" required>
          </b-input>
        </b-field>
        <b-field label="Powtórz nowe hasło">
          <b-input
            type="password"
            v-model="repeatedPassword"
            maxlength="30"
            required
          >
          </b-input>
        </b-field>

        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>

        <br />

        <button id="btnReset" class="button button-secondary">
          Zmień hasło
        </button>
      </form>
    </div>
    <b-loading
      :is-full-page="true"
      v-model="isLoading"
      :can-cancel="false"
    ></b-loading>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "passwordReset",
  data() {
    return {
      password: "",
      repeatedPassword: "",
      errors: [],
      isLoading: false,
    };
  },
  mounted() {
    document.title = "Resetowanie hasła";
  },
  methods: {
    ...mapActions("register", ["resetUserPassword"]),
    async submitForm() {
      this.errors = [];
      if (this.password != this.repeatedPassword) {
        this.errors.push("Hasła się nie zgadzają");
        return;
      }
      this.isLoading = true;
      this.resetUserPassword({
        token: this.$route.query.token,
        password: this.password,
      })
        .then(() => {
          this.isLoading = false;
          this.$buefy.toast.open({
            message: "Pomyślnie zmieniono hasło",
            type: "is-success",
          });
          this.$router.replace(this.$route.query.redirect || "/login");
        })
        .catch((err) => {
          this.isLoading = false;
          this.$buefy.toast.open({
            message: err.response.data[Object.keys(err.response.data)[0]],
            type: "is-danger",
          });
        });
    },
  },
};
</script>