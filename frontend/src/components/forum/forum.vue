<template>
  <div>
    <div class="columns">
      <div>
        <h2>Forum</h2>
      </div>
      <div>
        <button>add new</button>
      </div>
    </div>
    <div v-if="loading">
      <div v-for="post in forumPosts" :key="post.id">
        <Post></Post>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from "vuex";
import Post from "@/components/forum/Post";

export default {
  name: "forum",
  components: {
    Post,
  },
  data() {
    return {
      loading: false,
    };
  },

  methods: {
    ...mapActions("researchGroupPost", ["getForumPosts"]),
  },

  computed: {
    ...mapGetters("researchGroupPost", ["forumPosts"]),
    ...mapState({
      forumPosts: (state) => state.researchGroupPost.forumPosts,
    }),
  },

  mounted() {
    this.getForumPosts({researchGroup: 1000}).then(
        () => (this.loading = true)
    );
  },
};
</script>