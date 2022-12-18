<template>
  <div
    id="content"
    style="display: flex; flex-flow: column; margin-right: 10px"
    v-if="!this.loading"
  >
    <div>
      <div id="titleDiv">
        <div style="display: flex; flex-flow: row">
          <div style="display: flex; flex-flow: column">
            <p style="margin-bottom: 0" class="title">
              {{ this.tutorial.title }}
            </p>
            <p style="margin-bottom: 30px; margin-left: 13px">
              {{ this.tutorial.type }}
            </p>
          </div>
          <div style="width: 50px">
            <b-icon
              v-if="this.editing && !this.editingTitle && !this.editingText"
              style="margin-top: 18px; margin-left: 15px"
              icon="lead-pencil"
              @click.native="() => (editingTitle = !editingTitle)"
            />
          </div>
        </div>
        <div>
          <b-button
            id="btnTitle"
            rounded
            size="is-medium"
            type="is-danger"
            v-if="this.editing && this.tutorial.owner.id == this.authUser.id"
            @click="deleteTutorialConfirmation"
            >Usuń poradnik</b-button
          >
          <b-button
            id="btnTitle"
            rounded
            size="is-medium"
            v-if="this.editing && this.tutorial.owner.id == this.authUser.id"
            @click="() => (tutorialSettings = !tutorialSettings)"
            >Ustawienia</b-button
          >
          <b-button
            id="btnTitle"
            rounded
            size="is-medium"
            type="is-success"
            v-if="this.editing"
            @click="endEditTutorial()"
            >Wróć do poradnika</b-button
          >
          <b-button
            id="btnTitle"
            rounded
            size="is-medium"
            type="is-success"
            v-if="!this.editing && this.canEdit"
            @click="startEditTutorial()"
            >Edytuj poradnik</b-button
          >
        </div>
      </div>
    </div>
    <div class="box" style="flex: 1 0 auto; overflow: auto">
      <div id="box-content">
        <b-icon
          v-if="this.editing && !this.editingTitle && !this.editingText"
          icon="lead-pencil"
          @click.native="() => (editingText = !editingText)"
        />
        <div style="overflow: auto">
          <markdown-it-vue
            v-if="!this.editingText"
            class="md-body"
            :content="this.tutorial.text"
            :options="markdownOptions"
          />
        </div>
        <div v-if="this.editingText">
          <b-field>
            <b-input
              v-model="text"
              id="editTutorialText"
              type="textarea"
              size="is-large"
            >
            </b-input>
          </b-field>
          <div id="btnsDiv">
            <b-button id="btnSave" type="is-success" @click="saveTutorial"
              >Zapisz</b-button
            >
            <b-button
              @click="
                () => ((text = tutorial.text), (editingText = !editingText))
              "
              >Anuluj</b-button
            >
          </div>
        </div>
      </div>
    </div>
    <b-modal has-modal-card :active.sync="this.editingTitle" trap-focus>
      <template>
        <div class="modal-card">
          <section class="modal-card-body">
            <b-field label="Nazwa poradnika">
              <b-input v-model="title"></b-input>
            </b-field>
            <b-field label="Typ poradnika">
              <b-select v-model="category" expanded>
                <option value="Default">Default</option>
              </b-select>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <b-button type="is-success" @click="saveTutorial">Zapis</b-button>
            <b-button
              @click="
                () => (
                  (title = tutorial.title),
                  (category = tutorial.type),
                  (editingTitle = !editingTitle)
                )
              "
              >Anuluj</b-button
            >
          </footer>
        </div>
      </template>
    </b-modal>
    <b-modal has-modal-card :active.sync="this.tutorialSettings" trap-focus>
      <template>
        <div class="modal-card">
          <section class="modal-card-body">
            <b-field label="Wersja robocza">
              <b-switch
                v-model="is_draft"
                :true-value="true"
                :false-value="false"
              >
                {{ is_draft ? "Tak" : "Nie" }}
              </b-switch>
            </b-field>
            <b-field label="Lista edytorów">
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
                  v-for="editor in editors"
                  :key="editor"
                >
                  <b-icon
                    style="padding-top: 5px; margin-right: 5px"
                    v-if="tutorial.owner.email == editor"
                    icon="star"
                  />
                  <p style="flex: 0 1 auto; padding-top: 3px">
                    {{ editor }}
                  </p>
                  <div style="flex: 1 0 auto; text-align: right">
                    <b-icon
                      icon="close"
                      @click.native="removeEditorFromList(editor)"
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
                    <b-icon icon="plus" @click.native="addEditorToList()" />
                  </div>
                </div>
              </div>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <b-button type="is-success" @click="saveTutorial">Zapis</b-button>
            <b-button
              @click="
                () => (
                  (is_draft = tutorial.is_draft),
                  (editors = extractEmails(tutorial.editors)),
                  (tutorialSettings = false)
                )
              "
              >Anuluj</b-button
            >
          </footer>
        </div>
      </template>
    </b-modal>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "tutorialPanel",

  data() {
    return {
      loading: true,
      canEdit: false,
      editing: false,
      title: "",
      editingTitle: false,
      category: "",
      is_draft: false,
      text: "",
      editingText: false,
      editors: [],
      addEmail: "",
      tutorialSettings: false,
    };
  },

  methods: {
    ...mapActions("tutorial", [
      "getTutorial",
      "updateTutorial",
      "removeTutorial",
    ]),
    startEditTutorial() {
      this.editing = true;
    },
    endEditTutorial() {
      this.editing = false;
      this.editingText = false;

      this.title = this.tutorial.title;
      this.category = this.tutorial.type;
      this.text = this.tutorial.text;
      this.editors = this.extractEmails(this.tutorial.editors);
    },

    addEditorToList() {
      if (
        !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          this.addEmail
        )
      ) {
        this.$buefy.toast.open({
          message: "Podano niepoprawny E-mail",
          type: "is-danger",
        });
      } else if (this.editors.includes(this.addEmail)) {
        this.$buefy.toast.open({
          message: "Podany E-mail już znajduje się na liście",
          type: "is-danger",
        });
      } else {
        this.editors.push(this.addEmail);
      }
      this.addEmail = "";
    },

    removeEditorFromList(editor) {
      let index = this.editors.indexOf(editor);
      this.editors.splice(index, 1);
    },

    saveTutorial() {
      if (!this.editors.includes(this.tutorial.owner.email)) {
        this.editors = this.extractEmails(this.tutorial.editors);
        this.$buefy.toast.open({
          message: "Nie można usunąć twórcy poradnika",
          type: "is-danger",
        });
        return;
      }
      this.updateTutorial({
        tutorialId: this.$route.params.id,
        tutorial: {
          title: this.title,
          type: this.category,
          text: this.text,
          editor_emails: this.editors,
          is_public: !this.is_draft,
          is_draft: this.is_draft,
        },
      })
        .then((response) => {
          this.title = response.name;
          this.category = response.type;
          this.text = response.text;
          this.is_draft = response.is_draft;
          this.editingTitle = false;
          this.editingText = false;
          this.tutorialSettings = false;
          this.$buefy.toast.open({
            message: "Pomyślnie zapisano poradnik",
            type: "is-success",
          });
        })
        .catch((err) => {
          this.$buefy.toast.open({
            message: err.response.data[Object.keys(err.response.data)[0]],
            type: "is-danger",
          });
        });
    },

    extractEmails(editors) {
      let editor_emails = [];
      for (let i = 0; i < editors.length; i++) {
        editor_emails.push(editors[i]["email"]);
      }
      return editor_emails;
    },

    deleteTutorialConfirmation() {
      this.$buefy.dialog.confirm({
        title: "Usuwanie poradnika",
        message: "<b>Czy na pewno chcesz usunąć poradnik?</b>",
        confirmText: "Usuń poradnik",
        type: "is-danger",
        hasIcon: true,
        onConfirm: () => this.deleteTutorial(),
      });
    },

    deleteTutorial() {
      this.removeTutorial(this.$route.params.id)
        .then(() => {
          this.$router.push("/tutorial-catalog");
          this.$buefy.toast.open({
            message: "Poradnik został usunięty",
            type: "is-success",
          });
        })
        .catch((err) => {
          this.$buefy.toast.open({
            message: err.response.data[Object.keys(err.response.data)[0]],
            type: "is-danger",
          });
        });
    },
  },

  mounted() {
    this.getTutorial(this.$route.params.id).then((response) => {
      this.title = response.title;
      this.category = response.type;
      this.text = response.text;
      this.editors = this.extractEmails(response.editors);
      this.canEdit = response.editable;
      this.is_draft = response.is_draft;
      this.loading = false;
    });
  },

  computed: {
    ...mapGetters("tutorial", ["tutorial"]),
    ...mapGetters("auth", ["authUser"]),
  },

  watch: {
    tutorial() {
      this.editors = this.extractEmails(this.tutorial.editors);
    },
  },
};
</script>

<style>
#box-content {
  height: 60vh;
}

#editTutorialText {
  height: 65vh;
  resize: none;
}
</style>