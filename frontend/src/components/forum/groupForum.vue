<template>
  <div>
    <div v-if="isAuthenticated && isParticipant">
      <div class="columns mr-3">
        <div class="column is-2 pr-6">
          <p class="subtitle">Forum</p>
        </div>
        <div class="column is-2 is-offset-8 pl-6">
          <b-button class="button is-medium is-success is-rounded" v-on:click="addPost">Utwórz nowy wpis</b-button>
        </div>
      </div>
      <div v-if="adding">
        <AddGroupPost @close="adding = false"></AddGroupPost>
      </div>
      <div v-if="loading">
        <div v-for="post in forumPosts" :key="post.id" class="mb-5">
          <router-link :to="{ name: 'groupPost', params: {groupId: groupId, postId: post.id} }">
            <Post :post="post"></Post>
          </router-link>
        </div>
      </div>
    </div>
    <div v-if="!isAuthenticated">
      <p class="title pr-6">Nie jesteś zalogowny.</p>
      <div class="columns is-flex is-vcentered is-centered">
        <b-button class="is-medium is-rounded column is-2" type="is-success" :to="{ name: 'login' }"
                  tag="router-link" label="Zaloguj się">
        </b-button>
      </div>
    </div>
    <div v-if="isAuthenticated && !isParticipant && loading">
      <p class="title pr-6">Nie członkiem tego koła.</p>
      <div class="columns is-flex is-vcentered is-centered">
        <b-button class="is-medium is-rounded column is-2" type="is-success" v-on:click="$router.back()" label="Powrót">
        </b-button>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from "vuex";
import Post from "@/components/forum/Post";
import AddGroupPost from "@/components/forum/addGroupPost";

export default {
  name: "groupForum",
  props: {
    title: {type: String},
    content: {type: String},
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
    this.getForumPosts({researchGroup: this.groupId, userId: this.authUser.id}).then((data) => {
          this.loading = true,
              this.isParticipant = data.isParticipant
        }
    );
  },
};
</script>