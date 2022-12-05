<template>
  <div>
    <div class="columns mr-3">
      <div class="column is-2 pr-6">
        <p class="subtitle">Forum</p>
      </div>
      <div class="column is-2 is-offset-8 pl-6">
        <b-button v-if="!adding" class="is-primary" v-on:click="addPost">Utwórz nowy wpis</b-button>
      </div>
    </div>
    <div v-if="adding">
      <add-post></add-post>
      <b-button v-on:click="cancelPost">Anuluj</b-button>
    </div>
    <div v-if="loading">
      <div v-for="post in forumPosts" :key="post.id">
        <router-link :to="{ name: 'post' }">
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
    content: {type: String}
  },
  components: {
    AddPost,
    Post,
  },
  data() {
    return {
      loading: false,
      adding: false,
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
    ...mapGetters("researchGroupPost", ["forumPosts"]),
    ...mapState({
      forumPosts: (state) => state.researchGroupPost.forumPosts,
    }),
  },

  mounted() {
    this.getForumPosts({post: 1000}).then(
        () => (this.loading = true)
    );
  },
};
</script>