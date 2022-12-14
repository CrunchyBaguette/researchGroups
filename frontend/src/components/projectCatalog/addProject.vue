<template>
  <div id="content" style="display: flex; flex-flow: column; margin 0">
    <div style="flex: 0 1 auto">
      <p class="title" style="width: fit-content">Tworzenie projektu</p>
    </div>
    <div
      style="
        display: flex;
        flex: 1 1 auto;
        overflow: auto;
        padding: 10px;
        justify-content: center;
        padding-top: 50px;
      "
    >
      <div class="columns" style="width: 80%; margin: 50px auto">
        <div class="column" style="display: flex; flex-flow: column; margin: 0">
          <div class="box" style="height: fit-content">
            <b-field
              :message="!nameGiven ? 'Proszę podać nazwę koła' : ''"
              :type="!nameGiven ? 'is-danger' : ''"
            >
              <template #label
                ><p style="font-size: 20px">Nazwa projektu</p></template
              >
              <b-input
                @focus="nameGiven = true"
                v-model="projectName"
                style="width: 100%"
              />
            </b-field>
            <b-field
              :message="!categoryGiven ? 'Proszę podać kategorię projektu' : ''"
              :type="!categoryGiven ? 'is-danger' : ''"
            >
              <template #label
                ><p style="font-size: 20px">Kategoria</p></template
              >
              <b-select
                @focus="categoryGiven = true"
                v-model="projectCategory"
                expanded
                style="width: 100%"
                placeholder="Wybierz kategorię"
              >
                <option value="math">Matematyka</option>
                <option value="med">Medycyna</option>
                <option value="chem">Chemia</option>
              </b-select>
            </b-field>
            <b-field
              :message="!descriptionGiven ? 'Proszę podać opis projektu' : ''"
              :type="!descriptionGiven ? 'is-danger' : ''"
            >
              <template #label
                ><p style="font-size: 20px">Opis projektu</p></template
              >
              <b-input
                @focus="descriptionGiven = true"
                v-model="projectDescription"
                style="width: 100%"
                type="textarea"
              />
            </b-field>
          </div>
          <div style="flex: 0 1 auto">
            <b-button
              class="button-secondary"
              style="margin-top: 50px"
              expanded
              @click="clicked()"
            >
              Stwórz projekt
            </b-button>
          </div>
        </div>
        <div
          class="column"
          style="display: flex; flex-flow: column; margin: 0; height: 50%"
        >
          <div style="flex: 1 1 auto" class="box">
            <p style="font-size: 20px; color: #363636; font-weight: 600">
              Lista członków
            </p>
            <div
              style="
                width: 100%;
                height: 400px;
                background-color: #fff;
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
                v-for="email in projectMembers"
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
              label="Dodaj e-maile członków do projektu"
            >
              <b-input
                @focus="invalidEmailMessage = ''"
                v-model="projectMemberInput"
                placeholder="Email członka..."
                expanded
              ></b-input>
              <p class="control">
                <b-button
                  class="button-secondary"
                  @click="addToMemberList(projectMemberInput)"
                  >Dodaj członka</b-button
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
  name: "addProject",

  data() {
    return {
      projectName: "",
      projectCategory: "",
      projectDescription: "",
      projectMemberInput: "",
      projectMembers: [],
      nameGiven: true,
      categoryGiven: true,
      descriptionGiven: true,
      invalidEmailMessage: "",
    };
  },

  methods: {
    ...mapActions("project", ["addProject"]),
    clicked() {
      if (this.projectName == "") this.nameGiven = false;
      if (this.projectCategory == "") this.categoryGiven = false;
      if (this.projectDescription == "") this.descriptionGiven = false;

      if (this.nameGiven && this.categoryGiven && this.descriptionGiven) {
        this.addProject({
          name: this.projectName,
          description: this.projectDescription,
          category: this.projectCategory,
          members: this.projectMembers,
          project_owner: this.authUser.email,
        })
          .then((response) => {
            this.$buefy.toast.open({
              message: "Pomyślnie dodano projekt",
              type: "is-success",
            });

            this.$router.replace(
              this.$route.query.redirect || `/project/${response.id}`
            );
          })
          .catch((err) => {
            this.$buefy.toast.open({
              message: err.response.data[Object.keys(err.response.data)[0]],
              type: "is-danger",
            });
          });

        this.projectName = "";
        this.projectDescription = "";
        this.projectCategory = "";
      }
    },
    addToMemberList(memberEmail) {
      if (
        !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          memberEmail
        )
      ) {
        this.invalidEmailMessage = "Podaj poprawny E-mail";
      } else if (this.projectMembers.includes(memberEmail)) {
        this.invalidEmailMessage = "Już podano dany E-mail";
      } else if (memberEmail == this.authUser.email) {
        this.invalidEmailMessage = "Nie można dodać własnego adresu E-mail";
      } else {
        this.projectMembers.push(memberEmail);
      }
      this.projectMemberInput = "";
    },
    removeMemberFromList(email) {
      let index = this.projectMembers.indexOf(email);
      this.projectMembers.splice(index, 1);
    },
  },

  computed: {
    ...mapGetters("auth", ["authUser"]),
  },
};
</script>