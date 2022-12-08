<template>
  <div v-if="isAuthenticated">
    <div class="columns mr-3">
      <div class="column is-2 pr-6">
        <p class="subtitle">Forum</p>
      </div>
      <div class="column is-2 is-offset-8 pl-6">
        <b-button class="button is-medium is-success is-rounded" v-on:click="addPost">Utwórz nowy wpis</b-button>
      </div>
    </div>
    <div v-if="adding">
      <add-post @close="adding = false"></add-post>
    </div>
    <div v-if="loading">
      <div v-for="post in forumPosts.posts" :key="post.id" class="mb-5">
        <router-link :to="{ name: 'post', params: {groupId: groupId, postId: post.id} }">
          <Post :post="post"></Post>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from "vuex";
import Post from "@/components/forum/Post";
import AddPost from "@/components/forum/addPost";

export default {
  name: "forum",
  props: {
    title: {type: String},
    content: {type: String},
  },
  components: {
    AddPost,
    Post,
  },
  data() {
    return {
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
    cancelPost() {
      this.adding = false;
    }
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
    this.getForumPosts({researchGroup: this.groupId}).then(
        () => (this.loading = true)
    );
  },
};
</script>