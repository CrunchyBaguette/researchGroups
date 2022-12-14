<template>
  <div
    v-if="loading"
    style="
      display: flex;
      flex-flow: column;
      height: 100%;
      height: 100%;
      margin-right: 10px;
    "
  >
    <div style="flex: 0 1 0; display: flex; margin-bottom: 10px">
      <div style="flex: 1 0 0">
        <b-button
          class="button-secondary is-rounded is-medium"
          v-on:click="$router.back()"
          >Powrót
        </b-button>
      </div>
      <div>
        <div>
          <b-button
            v-if="forumPost.author.id === authUser.id && !isUpdate"
            class="button-secondary is-rounded mr-2 is-medium"
            v-on:click="showEdit"
            >Edytuj
          </b-button>
          <b-button
            v-if="isUpdate"
            class="button-secondary is-rounded mr-2 is-medium"
            v-on:click="isUpdate = false"
            >Anuluj
          </b-button>
          <b-button
            class="button-red is-rounded is-medium"
            v-if="canDelete"
            v-on:click="confirmDeleting"
            >Usuń</b-button
          >
        </div>
      </div>
    </div>
    <div style="flex: 1 0 0; overflow: hidden">
      <div class="box post-box">
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
          <div
            style="overflow: auto; height: 100%"
            v-if="!isUpdate"
            class="box white"
          >
            <markdown-it-vue
              class="md-body"
              :content="forumPost.text"
              :options="markdownOptions"
            />
          </div>

          <div v-if="isUpdate" style="height: 100%">
            <b-field
              label="Tytuł:"
              :message="titleError"
              :type="titleError ? 'is-danger' : ''"
              ><b-input
                @focus="titleError = ''"
                id="title"
                v-model="title"
              ></b-input>
            </b-field>
            <b-field :message="textError" :type="textError ? 'is-danger' : ''">
              <b-input
                @focus="textError = ''"
                v-model="text"
                id="editPostText"
                type="textarea"
              ></b-input>
            </b-field>
            <b-button
              class="button-secondary is-rounded mt-2"
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
  name: "groupPost",
  data() {
    return {
      title: "",
      titleError: "",
      text: "",
      textError: "",
      postId: this.$route.params.postId,
      groupId: this.$route.params.groupId,
      loading: false,
      isUpdate: false,
      canDelete: false,
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
    ...mapActions("researchGroupPost", ["getForumPost"]),
    ...mapActions("researchGroupPost", ["updateForumPost"]),
    ...mapActions("researchGroupPost", ["deleteForumPost"]),
    ...mapActions("researchGroupMember", ["getResearchGroupMembers"]),

    showEdit() {
      this.isUpdate = !this.isUpdate;
      this.title = this.forumPost.title;
      this.text = this.forumPost.text;
    },
    updatePost() {
      if (!this.title) this.titleError = "Proszę podać tytuł wpisu";
      if (!this.text) this.textError = "Proszę podać treść wpisu";
      if (this.title && this.text) {
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
      this.getResearchGroupMembers(this.$route.params.groupId).then((data) => {
        for (let i = 0; i < data.members.length; i++) {
          if (
            data.members[i]["person"] === this.authUser.email &&
            (data.members[i]["role"] === "Creator" ||
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
              name: "groupForum",
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
      forumPost: (state) => state.researchGroupPost.forumPost,
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
#editPostText {
  height: 55vh;
  resize: none;
}
</style>