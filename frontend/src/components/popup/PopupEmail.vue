<template>
  <popup title="Wiadomość" @close="$emit('close')">
    <div slot="body">
      <!-- <form @submit.prevent="submitForm"> -->
      <form @submit.prevent="onSubmit">
        <b-field label="Email">
          <b-input type="email" v-model="email" maxlength="30" required>
          </b-input>
        </b-field>

        <b-field label="Tytuł">
          <b-input v-model="emailTitle" maxlength="60" required> </b-input>
        </b-field>

        <b-field label="Treść">
          <b-input type="textarea" v-model="message" maxlength="600" required>
          </b-input>
        </b-field>

        <br />

        <button id="btnSendMessage" class="button">WYŚLIJ WIADOMOŚĆ</button>
      </form>
    </div>
  </popup>
</template>

<script>
import popup from "@/components/popup/Popup.vue";

export default {
  name: "PopupEmail",
  components: {
    popup,
  },
  data() {
    return {
      email: "",
      emailTitle: "",
      message: "",
    };
  },
  methods: {
    onSubmit() {
      this.$v.$touch();
      if (!this.$v.$invalid) {
        const user = {
          email: this.email,
          emailTitle: this.emailTitle,
          message: this.message,
        };
        console.log(user);

        //DONE
        this.email = "";
        this.emailTitle = "";
        this.message = "";
        this.$v.$reset();
        this.$emit("close");
      }
    },
  },
};
</script>

<style>
#btnSendMessage {
  display: flex;
  width: 100%;
  background-color: #7957d5;
  border-color: transparent;
  font-weight: bold;
  color: white;
  transition: 0.3s;
}

#btnSendMessage:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
}
</style>