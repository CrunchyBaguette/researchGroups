<template>
  <div
    id="content"
    style="display: flex; flex-flow: column"
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
            v-if="this.editing"
            @click="deleteTutorialConfirmation"
            >Usuń poradnik</b-button
          >
          <b-button id="btnTitle" rounded size="is-medium" v-if="this.editing"
            >Lista edytorów</b-button
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
            v-if="!this.editing"
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
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "tutorialPanel",

  data() {
    return {
      loading: true,
      editing: false,
      title: "",
      editingTitle: false,
      category: "",
      text: "",
      editingText: false,
      editors: [],
      markdownOptions: {
        markdownIt: {
          html: true,
          linkify: true,
        },
        linkAttributes: {
          attrs: {
            target: "_self",
            rel: "noopener",
          },
        },
      },
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
      this.editors = this.tutorial.editors;
    },

    saveTutorial() {
      this.updateTutorial({
        tutorialId: this.$route.params.id,
        tutorial: {
          title: this.title,
          type: this.category,
          text: this.text,
        },
      })
        .then((response) => {
          this.title = response.name;
          this.category = response.type;
          this.text = response.text;
          this.editors = response.editors;
          this.editingTitle = false;
          this.editingText = false;
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
      this.editors = response.editors;
      this.loading = false;
    });
  },

  computed: {
    ...mapGetters("tutorial", ["tutorial"]),
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