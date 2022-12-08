<template>
  <div v-if="loading">{{ authUser }}
    <div class="columns">
      <div class="column is-4">
        <b-button class="button"
        v-on:click="$router.back()">Powrót</b-button>
        <p class="author-decor">{{ authorName }} {{ forumPost.author }}</p>
      </div>
      <div class="column is-2 is-offset-6">
        <b-button class="button" v-on:click="showEdit">Edytuj</b-button>
        <b-button class="button" v-on:click="deletePost">delete</b-button>
      </div>
    </div>
    <div>
      <h2 v-if="!isUpdate" class="title">{{ forumPost.title }}</h2>
      <p v-if="!isUpdate">{{ forumPost.text }}</p>

      <div v-if="isUpdate">
        <label for="title">Tytuł:</label>
        <b-input id="title" v-model="title"></b-input>
        <label for="text">Treść:</label>
        <b-input type="textarea" id="text" v-model="text" maxlength="1000"></b-input>
        <b-button v-on:click="updatePost">Akceptuj zmiany</b-button>
      </div>
    </div>
    <!--    <div>-->
    <!--      <h2>Komentarze: </h2>-->
    <!--      <div v-for="comment in comments">-->
    <!--        <Comment></Comment>-->
    <!--      </div>-->
    <!--    </div>-->
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from "vuex";

export default {
  name: "postDetails",
  data() {
    return {
      title: "",
      text: "",
      postId: this.$route.params.postId,
      authorName: "autor name",//todo author name
      loading: false,
      isUpdate: false,
    };
  },

  methods: {
    ...mapActions("researchGroupPost", ["getForumPost"]),
    ...mapActions("researchGroupPost", ["updateForumPost"]),
    ...mapActions("researchGroupPost", ["deleteForumPost"]),

    showEdit() {
      this.isUpdate = !this.isUpdate;
      this.title = this.forumPost.title;
      this.text = this.forumPost.text;
    },
    updatePost() {
      if (this.title && this.text) {
        this.updateForumPost({
          id: this.postId,
          title: this.title,
          text: this.text,
        })
            .then((data) => {
              this.$buefy.toast.open({
                message: "Pomyślnie zedytowano posta",
                type: "is-success",
              });
              this.$router.push(
                  this.$route.query.redirect || "/post/" + data.id
              );
            })
            .catch((err) => {
              this.$buefy.toast.open({
                message:
                    "Błąd przy zedytowaniu posta (" +
                    (err.response ? err.response.status : 500) +
                    ")",
                type: "is-danger",
              });
            }).finally(
            this.isUpdate = false
        );

      }
    },
    deletePost() {
      // if (true) {//prompt
      this.deleteForumPost({
        id: this.postId,
      })
          .then(() => {
            this.$buefy.toast.open({
              message: "Pomyślnie usunięto post",
              type: "is-success",
            });
            this.$router.push("forum");
          })
          .catch((err) => {
            this.$buefy.toast.open({
              message:
                  "Błąd przy usuwaniu posta (" +
                  (err.response ? err.response.status : 500) +
                  ")",
              type: "is-danger",
            });
          });
    }


  },

  computed: {
    ...mapGetters("auth", ["authUser"]),
    ...mapGetters("auth", ["accessToken"]),
    ...mapState({
      forumPost: (state) => state.researchGroupPost.forumPost,
      // authorName: (state) => state.auth.authUser,
      // comments: state => state.researchGroupPost.postComment
    }),
  },

  mounted() {
    this.getForumPost({id: this.postId}).then(
      this.loading = true
    );
  },
};
</script>