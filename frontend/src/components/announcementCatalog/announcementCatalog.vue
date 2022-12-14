<template>
  <div
    id="content"
    style="display: flex; flex-flow: column"
    v-if="!this.loading"
  >
    <div id="titleDiv">
      <p class="title" id="tit">Ogłoszenia</p>
      <b-button
        v-if="isAdminOrOwner()"
        id="btnTitle"
        tag="router-link"
        :to="{ name: 'addAnnouncement' }"
        rounded
        size="is-medium"
        class="button-secondary"
        >Dodaj nowe ogłoszenie</b-button
      >
    </div>
    <div
      id="announcementsContainer"
      style="flex: 1 0 0; display: flex; flex-flow: column"
    >
      <div class="box" id="box" style="flex: 1 0 0; overflow: auto">
        <div
          style="margin-bottom: 20px"
          v-for="announcement in paginatedAnnouncements"
          :key="announcement.title"
        >
          <announcement
            id="ann"
            :author="announcement.author_full_name"
            :group="announcement.research_group_name"
            :category="announcement.ann_type"
            :added="announcement.added"
            :edited="announcement.edited"
            :title="announcement.title"
            :content="announcement.text"
            @click.native="moveToAnnouncement(announcement.id)"
          />
        </div>
      </div>

      <br />

      <div class="columns" style="width: 100%; padding-bottom: 20px; padding-right: 5px">
        <div class="column is-two-thirds"></div>
        <div class="box column is-one-third">
          <b-pagination
            order="is-centered"
            :total="announcements.length"
            :per-page="perPage"
            :current.sync="current"
            @change="scrollToTop"
          ></b-pagination>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from "vuex";
import announcement from "./announcement.vue";

export default {
  name: "announcementsCatalog",
  components: {
    announcement,
  },
  data() {
    return {
      current: 1,
      perPage: 20,
      loading: true,
      pageOfItems: [],
      userAdminGroups: [],
    };
  },
  methods: {
    ...mapActions("announcement", ["getAnnouncements"]),
    ...mapActions("user", ["getUserAdminResearchGroups"]),

    isAdminOrOwner() {
      if (this.isAuthenticated && this.userAdminGroups.length >= 1) {
        return true;
      } else {
        return false;
      }
    },

    onChangePage(pageOfItems) {
      // update page of items
      this.pageOfItems = pageOfItems;
    },
    moveToAnnouncement(announcementId) {
      this.$router.push(`/announcement/${announcementId}`);
    },

    scrollToTop() {
      document.getElementById("box").scrollTo(0, 0);
    },
  },

  computed: {
    ...mapState({
      announcements: (state) => state.announcement.announcements,
    }),
    ...mapState({
      userAdminResearchGroups: (state) => state.user.userAdminResearchGroups,
    }),
    ...mapGetters("auth", ["isAuthenticated", "authUser"]),

    paginatedAnnouncements() {
      let page_number = this.current - 1;

      return this.announcements.slice(
        page_number * this.perPage,
        (page_number + 1) * this.perPage
      );
    },
  },

  mounted() {
    this.getAnnouncements().then(() => (this.loading = false));
    if (this.isAuthenticated) {
      this.getUserAdminResearchGroups(this.authUser.id)
        .then(() => {
          this.userAdminGroups = this.userAdminResearchGroups;
        })
        .then(() => {
          this.loading = false;
        });
    }
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.title {
  padding: 10px;
  font-size: 40px;
}

#tit {
  text-align: left;
  margin-bottom: 20px;
}

#announcementsContainer {
  padding: 0px;
  width: 100%;
  height: 85%;
  overflow: auto;
}

#box {
  min-height: 80%;
  background-color: var(--first-color);
  box-shadow: var(--box-shadow);
  margin: 10px
}

#titleDiv {
  display: flex;
  width: 100%;
  flex-direction: row;
  justify-content: space-between;
}

#btnTitle {
  margin-top: 10px;
  margin-right: 20px;
}

#ann {
  margin-bottom: 20px;
  margin-left: 10px;
  margin-right: 10px;
  background-color: var(--first-color);
  border-style: solid;
  border-color: var(--fourth-color);
  transition: 0.3s;
  cursor: pointer;
}

/* #ann:hover {
  background-color: #7a7a7a;
  box-shadow: 0 0 10px #7a7a7a;
} */
</style>

