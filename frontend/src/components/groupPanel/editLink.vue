<template>
  <div style="width: 100vh" class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">{{ message }}</p>
    </header>
    <section class="modal-card-body">
      <div class="columns">
        <div class="column">
          <b-field label="Nazwa">
            <b-input v-model="newTitle"></b-input>
          </b-field>
          <b-field label="Link">
            <b-input v-model="newUrl"></b-input>
          </b-field>
          <b-field label="Publiczne">
            <b-switch
              v-model="newPublic"
              :true-value="true"
              :false-value="false"
            >
              {{ newPublic == true ? "Tak" : "Nie" }}
            </b-switch>
          </b-field>
        </div>
        <div v-if="!this.newPublic" class="column">
          <b-field v-if="!this.newPublic" label="Dodaj członków koła naukowego">
            <b-autocomplete
              rounded
              v-model="researchGroupName"
              :data="filteredResearchGroupNames"
              placeholder="nazwa koła naukowego..."
              icon="magnify"
              clearable
              @focus="getResearchGroups()"
              @select="(option) => (selectedResearchGroup = option)"
              ><template #empty>Brak koła naukowego</template>
            </b-autocomplete>
            <b-button
              class="button button-secondary"
              @click="addResearchGroupMembers(researchGroupName)"
              >Dodaj członków</b-button
            >
          </b-field>
          <b-field v-if="!this.newPublic" label="Użytkownicy z dostępem">
            <div
              style="
                width: 100%;
                height: 400px;
                background-color: rgb(240, 240, 240);
                margin-top: 5px;
                margin-bottom: 10px;
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
                v-for="newUser in newUsers"
                :key="newUser"
              >
                <p style="flex: 0 1 auto">
                  {{ newUser }}
                </p>
                <div style="flex: 1 0 auto; text-align: right">
                  <b-icon
                    icon="close"
                    @click.native="removeMemberFromList(newUser)"
                  />
                </div>
              </div>
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
              >
                <div style="flex: 0 1 75%">
                  <b-input v-model="addEmail" style="bottom: 5px"></b-input>
                </div>
                <div style="flex: 1 0 auto; text-align: right">
                  <b-icon icon="plus" @click.native="addMemberToList()" />
                </div>
              </div>
            </div>
          </b-field>
        </div>
      </div>
    </section>
    <footer class="modal-card-foot">
      <b-button class="button-secondary" @click="save">Zapisz</b-button>
      <b-button v-if="linkId" type="is-danger" @click="remove">Usuń</b-button>
      <b-button @click="cancel">Anuluj</b-button>
    </footer>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  name: "editLinkModal",
  props: {
    message: { type: String },
    linkId: { type: Number },
    linkTitle: { type: String },
    linkUrl: { type: String },
    linkPublic: { type: Boolean },
    linkUsers: { type: Array },
    linkType: { type: String },
  },
  data() {
    return {
      newTitle: this.linkTitle,
      newUrl: this.linkUrl,
      newPublic: this.linkPublic,
      newUsers: this.linkUsers,
      addEmail: "",

      researchGroupName: "",
      selectedResearchGroup: null,
    };
  },

  methods: {
    ...mapActions("researchGroup", ["getResearchGroups"]),
    ...mapActions("researchGroupLink", ["updateResearchGroupLink"]),
    ...mapActions("researchGroupDisk", ["updateResearchGroupDisk"]),
    addMemberToList() {
      if (
        !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          this.addEmail
        )
      ) {
        this.$buefy.toast.open({
          message: "Podano niepoprawny E-mail",
          type: "is-danger",
        });
      } else if (this.newUsers.includes(this.addEmail)) {
        this.$buefy.toast.open({
          message: "Podany E-mail już znajduje się na liście",
          type: "is-danger",
        });
      } else {
        this.newUsers.push(this.addEmail);
      }
      this.addEmail = "";
    },

    removeMemberFromList(email) {
      let index = this.newUsers.indexOf(email);
      this.newUsers.splice(index, 1);
    },

    save() {
      this.$emit("save", {
        newTitle: this.newTitle,
        newUrl: this.newUrl,
        newPublic: this.newPublic,
        newUsers: this.newUsers,
        linkType: this.linkType,
      });
    },

    cancel() {
      this.$emit("cancel");
    },

    remove() {
      this.$emit("delete", {
        linkType: this.linkType,
      });
    },

    addResearchGroupMembers(researchGroupName) {
      for (let i = 0; i < this.researchGroups.length; i++) {
        if (this.researchGroups[i].name == researchGroupName) {
          this.selectedResearchGroup = this.researchGroups[i];
          break;
        }
      }
      this.selectedResearchGroup.members.forEach((element) => {
        this.addEmail = element;
        this.addMemberToList();
      });
      this.researchGroupName = "";
    },
  },

  computed: {
    filteredResearchGroupNames() {
      let listNames = [];
      this.filteredResearchGroupArray.map((rg) => {
        if (rg.id != this.$route.params.id) {
          listNames.push(rg.name);
        }
      });
      return listNames;
    },
    filteredResearchGroupArray() {
      return this.researchGroups.filter((option) => {
        return (
          option.name
            .toString()
            .toLowerCase()
            .indexOf(this.researchGroupName.toLowerCase()) >= 0
        );
      });
    },
    ...mapState({
      researchGroups: (state) => state.researchGroup.researchGroups,
    }),
  },
};
</script>

<style>
.autocomplete.control {
  width: -webkit-fill-available;
  width: -moz-available;
}
</style>