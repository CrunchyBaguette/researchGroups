<template>
  <div id="content" style="display: flex; flex-flow: column; margin 0">
    <div style="flex: 0 1 auto">
      <p class="title" style="width: fit-content">Tworzenie Poradnika</p>
    </div>
    <div style="flex: 1 1 auto; overflow: auto; padding: 10px">
      <div class="columns" style="width: 80%; margin: 50px auto">
        <div class="column" style="display: flex; flex-flow: column; margin: 0">
          <div class="box" style="flex: 1 1 auto">
            <b-field
              :message="!nameGiven ? 'Proszę podać nazwę poradnika' : ''"
              :type="!nameGiven ? 'is-danger' : ''"
            >
              <template #label
                ><p style="font-size: 20px">Nazwa poradnika</p></template
              >
              <b-input
                @focus="nameGiven = true"
                v-model="tutorialName"
                style="width: 100%"
              />
            </b-field>
            <b-field
              :message="!typeGiven ? 'Proszę podać typ poradnika' : ''"
              :type="!typeGiven ? 'is-danger' : ''"
            >
              <template #label
                ><p style="font-size: 20px">Typ poradnika</p></template
              >
              <b-select
                @focus="typeGiven = true"
                v-model="tutorialType"
                expanded
                style="width: 100%"
                placeholder="Wybierz typ poradnika"
              >
                <option value="def">Default</option>
              </b-select>
            </b-field>
          </div>
          <div style="flex: 0 1 auto">
            <b-button
              style="margin-top: 50px"
              expanded
              type="is-success"
              @click="clicked()"
            >
              Stwórz poradnik
            </b-button>
          </div>
        </div>
        <div
          class="column"
          style="display: flex; flex-flow: column; margin: 0; height: 50%"
        >
          <div style="flex: 1 1 auto" class="box">
            <p style="font-size: 20px; color: #363636; font-weight: 600">
              Lista edytorów
            </p>
            <div
              style="
                width: 100%;
                height: 400px;
                background-color: rgb(240, 240, 240);
                margin-top: 5px;
                overflow: auto;
              "
            >
              <div
                class="box"
                style="
                  border-radius: 25px;
                  width: 95%;
                  height: 40px;
                  margin: 10px auto;
                  padding: 5px 10px;
                  display: flex;
                "
                v-for="email in tutorialEditors"
                :key="email"
              >
                <p style="flex: 0 1 auto">
                  {{ email }}
                </p>
                <div
                  style="flex: 1 0 auto; text-align: right"
                  @click="removeMemberFromList(email)"
                >
                  <b-icon icon="close" />
                </div>
              </div>
            </div>
            <br />
            <b-field
              :message="invalidEmailMessage"
              :type="invalidEmailMessage ? 'is-danger' : ''"
              label="Dodaj e-maile edytorów do poradnika"
            >
              <b-input
                @focus="invalidEmailMessage = ''"
                v-model="tutorialEditorInput"
                placeholder="Email edytora..."
                expanded
                disabled
              ></b-input>
              <p class="control">
                <b-button
                  disabled
                  class="button is-primary is-success"
                  @click="addToMemberList(tutorialEditorInput)"
                  >Dodaj edytora</b-button
                >
              </p>
            </b-field>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "addTutorial",

  data() {
    return {
      tutorialName: "",
      tutorialType: "",
      //   groupAboutUs: "",
      tutorialEditorInput: "",
      tutorialEditors: [],
      nameGiven: true,
      typeGiven: true,
      //   aboutUsGiven: true,
      invalidEmailMessage: "",
    };
  },

  methods: {
    ...mapActions("tutorial", ["addTutorial"]),
    clicked() {
      if (this.tutorialName == "") this.nameGiven = false;
      if (this.tutorialType == "") this.typeGiven = false;

      if (this.nameGiven && this.typeGiven) {
        this.addTutorial({
          title: this.tutorialName,
          type: this.tutorialType,
          editors: [],
          is_public: true,
        })
          .then((response) => {
            this.$buefy.toast.open({
              message: "Pomyślnie dodano poradnik",
              type: "is-success",
            });

            this.$router.replace(
              this.$route.query.redirect || `/tutorial/${response.id}`
            );
          })
          .catch((err) => {
            this.$buefy.toast.open({
              message: err.response.data[Object.keys(err.response.data)[0]],
              type: "is-danger",
            });
          });

        this.tutorialName = "";
        this.tutorialType = "";
      }
    },
    addToMemberList(memberEmail) {
      if (
        !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          memberEmail
        )
      ) {
        this.invalidEmailMessage = "Podaj poprawny E-mail";
      } else if (this.tutorialEditors.includes(memberEmail)) {
        this.invalidEmailMessage = "Już podano dany E-mail";
      } else if (memberEmail == this.authUser.email) {
        this.invalidEmailMessage = "Nie można dodać własnego adresu E-mail";
      } else {
        this.tutorialEditors.push(memberEmail);
      }
      this.tutorialEditorInput = "";
    },
    removeMemberFromList(email) {
      let index = this.tutorialEditors.indexOf(email);
      this.tutorialEditors.splice(index, 1);
    },
  },

  computed: {
    ...mapGetters("auth", ["authUser"]),
  },
};
</script>