<template>
  <div
    id="content"
    style="display: flex; flex-flow: column; margin-right: 10px"
    v-if="this.loaded"
  >
    <div>
      <div id="titleDiv">
        <p class="title" id="tit">Katalog Poradników</p>
        <b-button
          id="btnTitle"
          rounded
          size="is-medium"
          type="is-success"
          @click="openCreateTutorial"
          >Dodaj nowy poradnik</b-button
        >
      </div>
    </div>
    <div style="margin-bottom: 5px" v-if="this.isAuthenticated">
      <b-field>
        <b-select v-model="selectedFilter">
          <option value="pub">Publiczne poradniki</option>
          <option value="edit">Edytowalne poradniki</option>
          <option value="my">Moje poradniki</option>
          <option value="draft">Moje wersje robocze</option>
        </b-select>
      </b-field>
    </div>
    <div class="box" style="flex: 1 0 auto; overflow: auto">
      <div>
        <div class="columns" id="box-content">
          <div class="column">
            <tutorialTile
              v-for="tutorial in this.splitToThreeColumns(filteredTutorials)[0]"
              :key="tutorial.title"
              :author="tutorial.owner.full_name"
              :title="tutorial.title"
              :added="tutorial.created"
              :edited="tutorial.edited"
              :type="tutorial.type"
              :draft="tutorial.is_draft"
              style="margin-top: 10px; cursor: pointer"
              @click.native="goToTutorial(tutorial.id)"
            />
          </div>
          <div class="column">
            <tutorialTile
              v-for="tutorial in this.splitToThreeColumns(filteredTutorials)[1]"
              :key="tutorial.title"
              :author="tutorial.owner.full_name"
              :title="tutorial.title"
              :added="tutorial.created"
              :edited="tutorial.edited"
              :type="tutorial.type"
              :draft="tutorial.is_draft"
              style="margin-top: 10px; cursor: pointer"
              @click.native="goToTutorial(tutorial.id)"
            />
          </div>
          <div class="column">
            <tutorialTile
              v-for="tutorial in this.splitToThreeColumns(filteredTutorials)[2]"
              :key="tutorial.title"
              :author="tutorial.owner.full_name"
              :title="tutorial.title"
              :added="tutorial.created"
              :edited="tutorial.edited"
              :type="tutorial.type"
              :draft="tutorial.is_draft"
              style="margin-top: 10px; cursor: pointer"
              @click.native="goToTutorial(tutorial.id)"
            />
          </div>
        </div>
      </div>
    </div>
    <b-modal has-modal-card :active.sync="this.addingTutorial" trap-focus>
      <template>
        <div class="modal-card">
          <section class="modal-card-body">
            <b-field
              :message="!nameGiven ? 'Proszę podać nazwę poradnika' : ''"
              :type="!nameGiven ? 'is-danger' : ''"
              label="Stwórz poradnik"
            >
              <b-input
                @focus="nameGiven = true"
                v-model="tutorialName"
              ></b-input>
            </b-field>
            <b-field
              :message="!typeGiven ? 'Proszę podać typ poradnika' : ''"
              :type="!typeGiven ? 'is-danger' : ''"
              label="Typ poradnika"
            >
              <b-select
                @focus="typeGiven = true"
                v-model="tutorialType"
                expanded
              >
                <option value="Default">Default</option>
              </b-select>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <b-button type="is-success" @click="createTutorial"
              >Stwórz poradnik</b-button
            >
            <b-button
              @click="
                () => (
                  (addingTutorial = false),
                  (tutorialName = ``),
                  (tutorialType = ``)
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
import { mapActions, mapState, mapGetters } from "vuex";
import tutorialTile from "@/components/tutorialCatalog/tutorialTile.vue";

export default {
  name: "tutorialCatalog",
  components: {
    tutorialTile,
  },

  data() {
    return {
      selectedFilter: "pub",
      addingTutorial: false,
      tutorialName: "",
      nameGiven: true,
      tutorialType: "",
      typeGiven: true,
      loaded: false,
    };
  },

  methods: {
    ...mapActions("tutorial", ["getTutorials", "addTutorial"]),
    splitToThreeColumns(tutorials) {
      let leftColumn = [];
      let middleColumn = [];
      let rightColumn = [];

      for (let i = 0; i < tutorials.length; i++) {
        if (i % 3 == 0) {
          leftColumn.push(tutorials[i]);
        } else if (i % 3 == 1) {
          middleColumn.push(tutorials[i]);
        } else {
          rightColumn.push(tutorials[i]);
        }
      }

      return [leftColumn, middleColumn, rightColumn];
    },

    openCreateTutorial() {
      if (this.isAuthenticated) {
        this.addingTutorial = true;
      } else {
        this.$router.replace(this.$route.query.redirect || "/login");
      }
    },

    createTutorial() {
      if (this.tutorialName == "") this.nameGiven = false;
      if (this.tutorialType == "") this.typeGiven = false;

      if (this.nameGiven && this.typeGiven) {
        this.addTutorial({
          title: this.tutorialName,
          type: this.tutorialType,
          editors_emails: [],
          editors: [],
          is_public: false,
          is_draft: true,
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

    goToTutorial(tutorialId) {
      this.$router.push(`/tutorial/${tutorialId}`);
    },
  },

  computed: {
    ...mapState({
      tutorials: (state) => state.tutorial.tutorials,
    }),
    ...mapGetters("auth", ["authUser", "isAuthenticated"]),
    publicTutorials() {
      return this.tutorials.filter((tut) => {
        return tut.is_public;
      });
    },
    myTutorials() {
      return this.tutorials.filter((tut) => {
        return tut.owner.email == this.authUser.email;
      });
    },
    draftTutorials() {
      return this.tutorials.filter((tut) => {
        return tut.is_draft && tut.editable;
      });
    },
    filteredTutorials() {
      if (this.selectedFilter == "pub") {
        return this.tutorials.filter((tut) => {
          return tut.is_public;
        });
      } else if (this.selectedFilter == "edit") {
        return this.tutorials.filter((tut) => {
          return tut.editable;
        });
      } else if (this.selectedFilter == "my") {
        return this.tutorials.filter((tut) => {
          return tut.owner.email == this.authUser.email;
        });
      } else {
        return this.tutorials.filter((tut) => {
          return tut.owner.email == this.authUser.email && tut.is_draft;
        });
      }
    },
  },

  mounted() {
    this.getTutorials().then(() => (this.loaded = true));
  },
};
</script>

<style>
#tutorial-column-container {
  height: 87%;
  overflow: auto;
}

#box-content {
  height: 60vh;
}

#editTutorialText {
  height: 65vh;
  resize: none;
}
</style>