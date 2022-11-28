<template>
  <div>
    Forum (koła naukowego)
    <div v-if="!loading">
      {{ forumPosts }}
    </div>
  </div>
</template>
  
<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "forum",

  data() {
    return {
      loading: true,
    };
  },

  methods: {
    ...mapActions("groupForumPost", ["getForumPosts"]),
  },

  computed: {
    ...mapGetters("groupForumPost", ["forumPosts"]),
    // ...mapState({
    //   forumPosts: (state) => state.groupForumPost.forumPosts,
    // }),
  },

  mounted() {
    this.getForumPosts({ researchGroup: 1000 }).then(
      () => (this.loading = false)
    );
  },
};
</script>