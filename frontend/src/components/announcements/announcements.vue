<template>
  <div id="content" v-if="!loading">
    <p class="title" id="tit">Ogłoszenia</p>
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
    <div id="announcements">
      <div class="card text-center m-3">
        <div class="card-body">
          <div
            v-for="announcement in paginatedAnnouncements"
            :key="announcement.title"
          >
            <announcement
              id="a1"
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
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import announcement from "./announcement.vue";

// an example array of items to be paged
const exampleItems = [
  document.getElementById("a1"),
  document.getElementById("a2"),
  document.getElementById("a3"),
  document.getElementById("a4"),
  document.getElementById("a5"),
  document.getElementById("a6"),
  document.getElementById("a7"),
  document.getElementById("a8"),
  document.getElementById("a9"),
  document.getElementById("a10"),
  document.getElementById("a11"),
  document.getElementById("a12"),
].map((i) => ({ id: i + 1 }));
//const exampleItems = [...Array(150).keys()].map(i => ({ id: (i+1), name: 'Item ' + (i+1) }));

export default {
  name: "announcements",
  components: {
    announcement,
  },
  data() {
    return {
      current: 1,
      perPage: 5,
      loading: true,
      exampleItems,
      pageOfItems: [],
      annAuthor: "Jan Kowalski",
      annCategory: "Poszukiwanie sponsora",
      annDate: "12.08.2022r. 17:20",
      annTitle: "Poszukiwany inwestor",
      annContent:
        "Treść Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci sit, dolor rerum repudiandae accusamus porro ea cum! Corrupti laboriosam facere debitis libero deserunt minus at, iure consequuntur eaque nesciunt nostrum exercitationem praesentium, molestias aliquam perferendis rem enim porro illum recusandae possimus nobis inventore. Treść Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci sit, dolor rerum repudiandae accusamus porro ea cum! Corrupti laboriosam facere debitis libero deserunt minus at, iure consequuntur eaque nesciunt nostrum exercitationem praesentium, molestias aliquam perferendis rem enim porro illum recusandae possimus nobis inventore.",
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
.title {
  padding: 10px;
  font-size: 40px;
}

#tit {
  text-align: left;
}

#announcements {
  width: 100%;
  height: 80%;
  background-color: white;
  overflow: auto;
}
</style>

