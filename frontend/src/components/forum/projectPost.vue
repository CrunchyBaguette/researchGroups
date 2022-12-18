<template>
  <div
    v-if="loading"
    style="display: flex; flex-flow: column; height: 100%; height: 100%"
  >
    <div style="flex: 0 1 0; display: flex; margin-bottom: 10px">
      <div style="flex: 1 0 0">
        <b-button
          class="button is-success is-rounded is-medium"
          v-on:click="$router.back()"
          >Powrót
        </b-button>
      </div>
      <div>
        <div>
          <b-button
            v-if="forumPost.author.id === authUser.id && !isUpdate"
            class="button is-success is-rounded mr-2 is-medium"
            v-on:click="showEdit"
            >Edytuj
          </b-button>
          <b-button
            v-if="isUpdate"
            class="button is-success is-rounded mr-2 is-medium"
            v-on:click="isUpdate = false"
            >Anuluj
          </b-button>
          <b-button
            class="button is-danger is-rounded is-medium"
            v-if="canDelete"
            v-on:click="confirmDeleting"
            >Usuń</b-button
          >
        </div>
      </div>
    </div>
    <div style="flex: 1 0 0; overflow: hidden">
      <div
        class="box"
        style="
          flex: 1 1 auto;
          overflow: auto;
          height: 100%;
          background-color: rgb(196, 196, 196);
        "
      >
        <div style="display: flex; flex-flow: column; height: 100%">
          <div>
            <p class="author-decor">
              <b
                >{{ forumPost.author.first_name }}
                {{ forumPost.author.last_name }}</b
              >
            </p>
            <p class="author-decor">
              Utworzone:
              {{ new Date(forumPost.added) | dateFormat("DD.MM.YYYY HH:mm") }}
            </p>
            <p class="author-decor">
              Edytowane:
              {{ new Date(forumPost.edited) | dateFormat("DD.MM.YYYY HH:mm") }}
            </p>
          </div>
          <div style="margin-bottom: 10px">
            <p v-if="!isUpdate" class="title">{{ forumPost.title }}</p>
          </div>
          <div style="overflow: auto" v-if="!isUpdate" class="box">
            <markdown-it-vue
              class="md-body"
              :content="forumPost.text"
              :options="markdownOptions"
            />
          </div>

          <div v-if="isUpdate" style="height: 100%">
            <b-field label="Tytuł:"
              ><b-input id="title" v-model="title"></b-input>
            </b-field>
            <b-field>
              <b-input
                v-model="text"
                id="editPostText"
                type="textarea"
              ></b-input>
            </b-field>
            <b-button
              class="button is-success is-rounded mt-2"
              v-on:click="updatePost"
              >Akceptuj zmiany</b-button
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex";

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
      canDelete: false,
    };
  },

  methods: {
    ...mapActions("projectPost", ["getForumPost"]),
    ...mapActions("projectPost", ["updateForumPost"]),
    ...mapActions("projectPost", ["deleteForumPost"]),
    ...mapActions("projectMember", ["getProjectMembers"]),

    showEdit() {
      this.isUpdate = !this.isUpdate;
      this.title = this.forumPost.title;
      this.text = this.forumPost.text;
    },
    updatePost() {
      if (
        this.title &&
        this.text &&
        this.forumPost.author.id === this.authUser.id
      ) {
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
          })
          .finally((this.isUpdate = false));
      }
    },
    isDeleting() {
      if (this.forumPost.author.id === this.authUser.id) {
        this.canDelete = true;
      }
      this.getProjectMembers(this.$route.params.projectId).then((data) => {
        for (let i = 0; i < data.members.length; i++) {
          if (
            data.members[i]["person"] === this.authUser.email &&
            (data.members[i]["role"] === "Owner" ||
              data.members[i]["role"] === "Moderator")
          ) {
            this.canDelete = true;
          }
        }
      });
    },
    confirmDeleting() {
      this.$buefy.dialog.confirm({
        title: "Usuwanie posta",
        message: "Czy na pewno chcesz usunąc post?",
        type: "is-danger",
        hasIcon: true,
        onConfirm: () => this.deletePost(),
      });
    },
    deletePost() {
      if (this.canDelete) {
        this.deleteForumPost({
          id: this.postId,
          groupId: this.groupId,
        })
          .then(() => {
            this.$buefy.toast.open({
              message: "Pomyślnie usunięto post",
              type: "is-success",
            });
            this.$router.push({
              name: "projectForum",
              params: { groupId: this.groupId },
            });
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
  },

  computed: {
    ...mapGetters("auth", ["authUser"]),
    ...mapState({
      forumPost: (state) => state.projectPost.forumPost,
    }),
  },

  mounted() {
    this.getForumPost({ id: this.postId }).then(() => {
      this.isDeleting();
      this.loading = true;
    });
  },
};
</script>

<style>
.postText {
  white-space: pre-line;
}

#editPostText {
  height: 55vh;
  resize: none;
}
</style>