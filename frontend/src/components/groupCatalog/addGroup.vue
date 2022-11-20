<template>
  <div id="content" style="display: flex; flex-flow: column; margin 0">
    <div style="flex: 0 1 auto">
      <p class="title" style="width: fit-content">Tworzenie koła naukowego</p>
    </div>
    <div style="flex: 1 1 auto; overflow: auto; padding: 10px">
      <div class="columns" style="width: 80%; margin: 50px auto">
        <div class="column" style="display: flex; flex-flow: column; margin: 0">
          <div class="box" style="flex: 1 1 auto">
            <b-field
              :message="!nameGiven ? 'Proszę podać nazwę koła' : ''"
              :type="!nameGiven ? 'is-danger' : ''"
            >
              <template #label
                ><p style="font-size: 20px">Nazwa koła naukowego</p></template
              >
              <b-input
                @focus="nameGiven = true"
                v-model="groupName"
                style="width: 100%"
              />
            </b-field>
            <b-field
              :message="!categoryGiven ? 'Proszę podać kategorię koła' : ''"
              :type="!categoryGiven ? 'is-danger' : ''"
            >
              <template #label
                ><p style="font-size: 20px">Kategoria</p></template
              >
              <b-select
                @focus="categoryGiven = true"
                v-model="groupCategory"
                expanded
                style="width: 100%"
                placeholder="Wybierz kategorię"
              >
                <option value="math">Math</option>
                <option value="med">Medical</option>
                <option value="chem">Chemistry</option>
              </b-select>
            </b-field>
            <b-field
              :message="!aboutUsGiven ? 'Proszę podać opis koła' : ''"
              :type="!aboutUsGiven ? 'is-danger' : ''"
            >
              <template #label
                ><p style="font-size: 20px">Opis koła naukowego</p></template
              >
              <b-input
                @focus="aboutUsGiven = true"
                v-model="groupAboutUs"
                style="width: 100%"
                type="textarea"
              />
            </b-field>
          </div>
          <div style="flex: 0 1 auto">
            <b-button
              style="margin-top: 50px"
              expanded
              type="is-success"
              @click="clicked()"
            >
              Stwórz Koło naukowe
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
                v-for="email in groupMembers"
                :key="email"
              >
                <p style="flex: 0 1 auto">
                  {{ email }}
                </p>
                <div
                  style="flex: 1 0 auto; text-align: right"
                  @click="removeMemberFromList(email)"
                >
                  <mdicon name="close" />
                </div>
              </div>
            </div>
            <br />
            <b-field
              :message="invalidEmailMessage"
              :type="invalidEmailMessage ? 'is-danger' : ''"
              label="Dodaj e-maile członków do koła"
            >
              <b-input
                @focus="invalidEmailMessage = ''"
                v-model="groupMemberInput"
                placeholder="Email członka..."
                expanded
              ></b-input>
              <p class="control">
                <b-button
                  class="button is-primary is-success"
                  @click="addToMemberList(groupMemberInput)"
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
import { mapActions } from "vuex";

export default {
  name: "addGroup",

  data() {
    return {
      groupName: "",
      groupCategory: "",
      groupAboutUs: "",
      groupMemberInput: "",
      groupMembers: [],
      nameGiven: true,
      categoryGiven: true,
      aboutUsGiven: true,
      invalidEmailMessage: "",
    };
  },

  methods: {
    ...mapActions("researchGroup", ["addResearchGroup"]),
    clicked() {
      if (this.groupName == "") this.nameGiven = false;
      if (this.groupCategory == "") this.categoryGiven = false;
      if (this.groupAboutUs == "") this.aboutUsGiven = false;

      if (this.nameGiven && this.categoryGiven && this.aboutUsGiven) {
        this.addResearchGroup({
          name: this.groupName,
          about_us: this.groupAboutUs,
          category: this.groupCategory,
          members: this.groupMembers,
        })
          .then(() => {
            this.$buefy.toast.open({
              message: "Pomyślnie dodano koło naukowe",
              type: "is-success",
            });

            this.$router.replace(
              this.$route.query.redirect || "/group-catalog"
            );
          })
          .catch((err) => {
            this.$buefy.toast.open({
              message: "Błąd przy dodawaniu koła naukowego",
              type: "is-danger",
            });
          });

        this.groupName = "";
        this.groupAboutUs = "";
        this.groupCategory = "";
      }
    },
    addToMemberList(memberEmail) {
      if (
        !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          memberEmail
        )
      ) {
        this.invalidEmailMessage = "Podaj poprawny E-mail";
      } else if (this.groupMembers.includes(memberEmail)) {
        this.invalidEmailMessage = "Już podano dany E-mail";
      } else {
        this.groupMembers.push(memberEmail);
      }
      this.groupMemberInput = "";
    },
    removeMemberFromList(email) {
      let index = this.groupMembers.indexOf(email);
      this.groupMembers.splice(index, 1);
    },
  },
};
</script>