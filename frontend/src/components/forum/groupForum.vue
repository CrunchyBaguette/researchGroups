<template>
  <div style="height: 100%; margin-right: 10px">
    <div
      style="display: flex; flex-flow: column; height: 100%"
      v-if="isAuthenticated && isParticipant"
    >
      <div style="display: flex; margin-bottom: 10px">
        <div style="flex: 1 0 0">
          <p class="title" style="text-align: left">Forum</p>
        </div>
        <div style="margin-right: 10px">
          <b-button
            class="button-secondary is-medium is-rounded"
            v-on:click="addPost"
            >Utwórz nowy wpis</b-button
          >
        </div>
      </div>
      <div v-if="adding">
        <AddGroupPost @close="adding = false"></AddGroupPost>
      </div>
      <div class="box" style="flex: 1 0 0; overflow: auto" v-if="loading">
        <div v-for="post in forumPosts" :key="post.id" class="mb-5">
          <router-link
            :to="{
              name: 'groupPost',
              params: { groupId: groupId, postId: post.id },
            }"
          >
            <Post class="post" :post="post"></Post>
          </router-link>
        </div>
      </div>
    </div>
    <div v-if="!isAuthenticated">
      <p class="title pr-6">Nie jesteś zalogowny.</p>
      <div class="columns is-flex is-vcentered is-centered">
        <b-button
          class="is-medium is-rounded column is-2"
          type="is-success"
          :to="{ name: 'login' }"
          tag="router-link"
          label="Zaloguj się"
        >
        </b-button>
      </div>
    </div>
    <div v-if="isAuthenticated && !isParticipant && loading">
      <p class="title pr-6">Nie członkiem tego koła.</p>
      <div class="columns is-flex is-vcentered is-centered">
        <b-button
          class="is-medium is-rounded column is-2"
          type="is-success"
          v-on:click="$router.back()"
          label="Powrót"
        >
        </b-button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapState } from "vuex";
import Post from "@/components/forum/Post";
import AddGroupPost from "@/components/forum/addGroupPost";

export default {
  name: "groupForum",
  props: {
    title: { type: String },
    content: { type: String },
  },
  components: {
    AddGroupPost,
    Post,
  },
  data() {
    return {
      isParticipant: false,
      loading: false,
      adding: false,
      groupId: this.$route.params.groupId,
    };
  },

  methods: {
    ...mapActions("researchGroupPost", ["getForumPosts"]),

    addPost() {
      this.adding = true;
    },
  },

  computed: {
    ...mapGetters("auth", ["authUser"]),
    ...mapGetters("auth", ["isAuthenticated"]),
    ...mapState({
      forumPosts: (state) => state.researchGroupPost.forumPosts,
    }),
  },

  mounted() {
    document.title = "Forum koła naukowego";
    this.getForumPosts({
      researchGroup: this.groupId,
      userId: this.authUser.id,
    }).then((data) => {
      (this.loading = true), (this.isParticipant = data.isParticipant);
    });
  },
};
</script>

<style>
.post {
  background-color: var(--first-color) !important;
  border-style: solid;
  border-color: var(--fourth-color);
  cursor: pointer;
}
</style>