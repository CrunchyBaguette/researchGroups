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
        <b-field label="Podaj adres email">
          <b-input type="email" v-model="email" maxlength="30" required>
          </b-input>
        </b-field>

        <br />

        <b-button id="btnMain" class="button-secondary">RESETUJ HASŁO</b-button>
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
  name: "passwordReminder",
  data() {
    return {
      email: "",
      isLoading: false,
    };
  },
  mounted() {
    document.title = "Przypomnienie";
  },
  methods: {
    ...mapActions("register", ["sendResetEmail"]),
    async submitForm() {
      this.isLoading = true;
      this.sendResetEmail({ email: this.email })
        .then(() => {
          this.isLoading = false;
          this.email = "";
          this.$buefy.toast.open({
            message: "Na podany email wysłano link resetujący hasło",
            type: "is-success",
          });
        })
        .catch(() => {
          this.isLoading = false;
          this.$buefy.toast.open({
            message: "Użytkownik z podanym adresem email nie istnieje",
            type: "is-danger",
          });
        });
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