<template>
  <div v-if="loading">
    <div class="columns">
      <div class="column is-4">
        <b-button class="button is-success is-rounded"
                  v-on:click="$router.back()">Powrót
        </b-button>
        <p class="author-decor">{{ forumPost.author.first_name }} {{forumPost.author.last_name}}</p>
      </div>
      <div class="column is-2 is-offset-6" v-if="forumPost.author.id === authUser.id">
        <b-button class="button is-success is-rounded mr-2" v-on:click="showEdit">Edytuj</b-button>
        <b-button class="button is-success is-rounded" v-on:click="confirmDeleting">Usuń</b-button>
      </div>
    </div>
    <div>
      <p v-if="!isUpdate" class="title">{{ forumPost.title }}</p>
      <p v-if="!isUpdate" class="postText"> {{ forumPost.text}}</p>

      <div v-if="isUpdate">
        <label for="title">Tytuł:</label>
        <b-input id="title" v-model="title"></b-input>
        <label for="text">Treść:</label>
        <b-input type="textarea" id="text" v-model="text" maxlength="1000"></b-input>
        <b-button v-on:click="updatePost">Akceptuj zmiany</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from "vuex";

export default {
  name: "projectPost",
  data() {
    return {
      title: "",
      text: "",
      postId: this.$route.params.postId,
      projectId: this.$route.params.projectId,
      loading: false,
      isUpdate: false,
    };
  },

  methods: {
    ...mapActions("projectPost", ["getForumPost"]),
    ...mapActions("projectPost", ["updateForumPost"]),
    ...mapActions("projectPost", ["deleteForumPost"]),

    showEdit() {
      this.isUpdate = !this.isUpdate;
      this.title = this.forumPost.title;
      this.text = this.forumPost.text;
    },
    updatePost() {
      if (this.title && this.text && this.forumPost.author.id === this.authUser.id) {
        this.updateForumPost({
          id: this.$route.params.postId,
          title: this.title,
          text: this.text,
        })
            .then((data) => {
              this.$buefy.toast.open({
                message: "Pomyślnie zedytowano posta",
                type: "is-success",
              });
              this.forumPost.text = data.text;
              this.forumPost.title = data.title;
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
    confirmDeleting() {
      this.$buefy.dialog.confirm({
        message: 'Czy na pewno chcesz usunąc post?',
        onConfirm: () => this.deletePost()
      })
    },
    deletePost() {
      if (this.forumPost.author.id === this.authUser.id) {
        this.deleteForumPost({
          id: this.postId,
          groupId: this.groupId,
        })
            .then(() => {
              this.$buefy.toast.open({
                message: "Pomyślnie usunięto post",
                type: "is-success",
              });
              this.$router.push(
                  {name: 'projectForum', params: {groupId: this.groupId}});
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
    }
  },

  computed: {
    ...mapGetters("auth", ["authUser"]),
    ...mapState({
      forumPost: (state) => state.projectPost.forumPost,
    }),
  },

  mounted() {
    this.getForumPost({id: this.postId}).then(() =>
        this.loading = true
    );
  },
};
</script>

<style scoped>
.postText{
  white-space: pre-line;
}
</style>