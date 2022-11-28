<template>
  <div class="container" v-if="!loading">
    <p class="title" id="tit">Ogłoszenia</p>
    <div id="announcements" class="box">
      <div>
        <div
          v-for="announcement in paginatedAnnouncements"
          :key="announcement.title"
        >
          <announcement
            :author="announcement.author_username"
            :category="announcement.ann_type"
            :date="announcement.date"
            sortable
            :title="announcement.title"
            :content="announcement.text"
          />
        </div>
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
</template>

<script>
import { mapActions, mapState } from "vuex";
import announcement from "./announcement.vue";

export default {
  name: "announcements",
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
  },

  computed: {
    ...mapState({
      announcements: (state) => state.announcement.announcements,
    }),
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

.container {
  margin: 0 auto;
}

.title {
  padding: 10px;
  font-size: 40px;
}

#tit {
  text-align: left;
}

#announcements {
  padding: 0px;
  width: 100%;
  height: 85%;
  background-color: white;
  overflow: auto;
}

</style>

