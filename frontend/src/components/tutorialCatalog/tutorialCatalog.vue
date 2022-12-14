<template>
  <div id="content" style="display: flex; flex-flow: column" v-if="this.loaded">
    <div>
      <div id="titleDiv">
        <p class="title" id="tit">Katalog Poradników</p>
        <b-button
          id="btnTitle"
          tag="router-link"
          :to="isAuthenticated ? { name: 'addTutorial' } : { name: 'login' }"
          rounded
          size="is-medium"
          type="is-success"
          >Dodaj nowy poradnik</b-button
        >
      </div>
    </div>
    <div class="box" style="flex: 1 0 auto; overflow: auto">
      <div>
        <div class="columns" id="box-content">
          <div class="column">
            <tutorialTile
              v-for="tutorial in this.splitToThreeColumns(tutorials)[0]"
              :key="tutorial.title"
              :author="tutorial.owner.full_name"
              :title="tutorial.title"
              :added="tutorial.created"
              :edited="tutorial.edited"
              :category="tutorial.type"
              style="margin-top: 10px; cursor: pointer"
              @click.native="goToTutorial(tutorial.id)"
            />
          </div>
          <div class="column">
            <tutorialTile
              v-for="tutorial in this.splitToThreeColumns(tutorials)[1]"
              :key="tutorial.title"
              :author="tutorial.owner.full_name"
              :title="tutorial.title"
              :added="tutorial.created"
              :edited="tutorial.edited"
              :category="tutorial.type"
              style="margin-top: 10px; cursor: pointer"
              @click.native="goToTutorial(tutorial.id)"
            />
          </div>
          <div class="column">
            <tutorialTile
              v-for="tutorial in this.splitToThreeColumns(tutorials)[2]"
              :key="tutorial.title"
              :author="tutorial.owner.full_name"
              :title="tutorial.title"
              :added="tutorial.created"
              :edited="tutorial.edited"
              :category="tutorial.type"
              style="margin-top: 10px; cursor: pointer"
              @click.native="goToTutorial(tutorial.id)"
            />
          </div>
        </div>
      </div>
    </div>
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
      loaded: false,
    };
  },

  methods: {
    ...mapActions("tutorial", ["getTutorials"]),
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

    goToTutorial(tutorialId) {
      this.$router.push(`/tutorial/${tutorialId}`);
    },
  },

  computed: {
    ...mapState({
      tutorials: (state) => state.tutorial.tutorials,
    }),
    ...mapGetters("auth", ["isAuthenticated"]),
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