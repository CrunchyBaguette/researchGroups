<template>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">{{ message }}</p>
    </header>
    <section class="modal-card-body">
      <b-field label="Nazwa">
        <b-input v-model="newTitle"></b-input>
      </b-field>
      <b-field label="Link">
        <b-input v-model="newUrl"></b-input>
      </b-field>
      <b-field label="Publiczne">
        <b-switch v-model="newPublic" :true-value="true" :false-value="false">
          {{ newPublic == true ? "Tak" : "Nie" }}
        </b-switch>
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
    </section>
    <footer class="modal-card-foot">
      <b-button type="is-success" @click="save">Zapisz</b-button>
      <b-button v-if="linkId" type="is-danger" @click="remove">Usuń</b-button>
      <b-button @click="cancel">Anuluj</b-button>
    </footer>
  </div>
</template>

<script>
import { mapActions } from "vuex";
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
    };
  },

  methods: {
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
  },
};
</script>