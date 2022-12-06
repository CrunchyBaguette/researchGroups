<template>
  <div id="content">
    <div id="titleDiv">
      <p class="title" id="tit">Ogłoszenia</p>
      <b-button
          id="btnTitle"
          tag="router-link"
          :to="isAuthenticated ? { name: 'addAnnouncement' } : { name: 'login' }"
          rounded
          size="is-medium"
          type="is-success"
          >Dodaj nowe ogłoszenie</b-button
        >
    </div>
    <div id="announcementsContainer" v-if="!loading">
      <div class="box" id="box">
          <div
            v-for="announcement in paginatedAnnouncements"
            :key="announcement.title"
          >
            <announcement
              id="ann"
              :author="announcement.author_full_name"
              :category="announcement.ann_type"
              :date="announcement.date"
              sortable
              :title="announcement.title"
              :content="announcement.text"
              @click.native="moveToAnnouncement(announcement.id)"
            />
          </div>
      </div>

      <br>

      <div class="columns" style="width: 100%">
        <div class="column is-two-thirds"></div>
        <div class="box column is-one-third">
          <b-pagination
            order="is-centered"
            :total="announcements.length"
            :per-page="perPage"
            :current.sync="current"
          ></b-pagination>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from "vuex";
import announcement from "./announcement.vue"

export default {
  name: "announcementCatalog",
  components: {
    announcement,
  },
  data() {
    return {
      current: 1,
      perPage: 20,
      loading: true,
      pageOfItems: [],
    };
  },
  methods: {
    ...mapActions("announcement", ["getAnnouncements"]),
    onChangePage(pageOfItems) {
      // update page of items
      this.pageOfItems = pageOfItems;
    },
    moveToAnnouncement(announcementId) {
      this.$router.push(`/announcement/${announcementId}`)
    }
  },

  computed: {
    ...mapState({
      announcements: (state) => state.announcement.announcements,
    }),
    ...mapGetters("auth", ["isAuthenticated"]),
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
}

#announcementsContainer {
  padding: 0px;
  width: 100%;
  height: 85%;
  overflow: auto;
}

#box {
  min-height: 80%;
}

#titleDiv {
  display: flex;
  width: 100%;
  flex-direction: row;
  justify-content: space-between;
}

#btnTitle {
  margin-top: 10px;
  margin-right: 20px
}

#ann {
  margin-bottom: 20px;
  margin-left: 10px;
  margin-right: 10px;
  background-color: rgb(196, 196, 196);
}

</style>

