<template>
  <popup title="Wiadomość" @close="$emit('close')">
    <div slot="body">
      <form @submit.prevent="onSubmit">
        <b-field
          v-if="!this.isAuthenticated"
          :message="errorEmail"
          :type="errorEmail ? 'is-danger' : ''"
          label="E-mail"
        >
          <b-input
            @focus="errorEmail = ''"
            v-model="email"
            maxlength="60"
            required
          >
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
        <button id="btnMain" class="button button-secondary">
          WYŚLIJ WIADOMOŚĆ
        </button>
      </form>
    </div>
  </popup>
</template>

<script>
import popup from "@/components/popup/Popup.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "PopupEmail",
  props: {
    objectType: { type: String },
    object: { type: Object },
  },
  components: {
    popup,
  },
  data() {
    return {
      email: "",
      errorEmail: "",
      emailTitle: "",
      message: "",
    };
  },
  methods: {
    ...mapActions("researchGroup", ["sendResearchGroupEmailMessage"]),
    ...mapActions("project", ["sendProjectEmailMessage"]),

    verifyEmail(email) {
      if (
        !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          email
        )
      ) {
        return false;
      }
      return true;
    },

    onSubmit() {
      if (!this.isAuthenticated && !this.verifyEmail(this.email)) {
        this.errorEmail = "Proszę podać poprawny adres e-mail";
        return;
      }
      if (this.objectType == "researchGroup") {
        this.sendResearchGroupEmailMessage({
          researchGroupId: this.$route.params.id,
          creator: this.object.group_owner,
          sender: this.isAuthenticated ? this.authUser.email : this.email,
          subject: this.emailTitle,
          text: this.message,
          research_group_name: this.object.name,
        })
          .then(() => {
            this.emailTitle = "";
            this.message = "";
            this.$buefy.toast.open({
              message: "Pomyślnie wysłano wiadomość",
              type: "is-success",
            });
            this.$emit("close");
          })
          .catch(() => {
            this.$buefy.toast.open({
              message:
                "Błąd przy wysyłaniu wiadomości\nSpróbuj ponownie później",
              type: "is-danger",
            });
          });
      } else {
        this.sendProjectEmailMessage({
          projectId: this.$route.params.id,
          owner: this.object.project_owner,
          sender: this.isAuthenticated ? this.authUser.email : this.email,
          subject: this.emailTitle,
          text: this.message,
          project_name: this.object.name,
        })
          .then(() => {
            this.emailTitle = "";
            this.message = "";
            this.$buefy.toast.open({
              message: "Pomyślnie wysłano wiadomość",
              type: "is-success",
            });
            this.$emit("close");
          })
          .catch(() => {
            this.$buefy.toast.open({
              message:
                "Błąd przy wysyłaniu wiadomości\nSpróbuj ponownie później",
              type: "is-danger",
            });
          });
      }
    },
  },

  computed: {
    ...mapGetters("auth", ["authUser", "isAuthenticated"]),
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