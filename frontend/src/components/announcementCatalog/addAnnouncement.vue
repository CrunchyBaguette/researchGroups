<template>
  <div id="content" v-if="!this.loading">
    <p class="title" style="width: fit-content">Tworzenie ogłoszenia</p>
    <div id="container" style="margin: 70px auto; width: 70%;">
      <div class="box">
        <b-field
          :message="!groupGiven ? 'Proszę wybrać koło naukowe spośród tych do których należysz' : ''"
          :type="!groupGiven ? 'is-danger' : ''"
        >
          <template #label
            ><p style="font-size: 20px">Koło naukowe</p></template
          >
          <b-select
            id="selectGroup"
            @focus="groupGiven = true"
            v-model="announcementGroup"
            expanded
            style="width: 100%"
            placeholder="Wybierz koło"
          >
            <option :value="group.id" v-for="group in userAdminGroups" v-bind:key="group.id">
              {{ group.name }}
            </option>
            
          </b-select>
        </b-field>
        <b-field
          :message="!titleGiven ? 'Proszę podać tytuł ogłoszenia' : ''"
          :type="!titleGiven ? 'is-danger' : ''"
        >
          <template #label
            ><p style="font-size: 20px">Tytuł ogłoszenia</p></template
          >
          <b-input
            @focus="titleGiven = true"
            v-model="announcementTitle"
            style="width: 100%"
            maxlength="120"
          />
        </b-field>
        <b-field
          :message="!categoryGiven ? 'Proszę wybrać kategorię ogłoszenia' : ''"
          :type="!categoryGiven ? 'is-danger' : ''"
        >
          <template #label
            ><p style="font-size: 20px">Kategoria</p></template
          >
          <b-select
            @focus="categoryGiven = true"
            v-model="announcementCategory"
            expanded
            style="width: 100%"
            placeholder="Wybierz kategorię"
          >
            <option value="sponsor">Poszukiwanie sponsora</option>
            <option value="rekrutacja">Poszukiwanie nowych członków</option>
            <option value="projekt">Poszukiwanie osób do projektu</option>
          </b-select>
        </b-field>
        <b-field
          :message="!contentGiven ? 'Proszę podać treść ogłoszenia' : ''"
          :type="!contentGiven ? 'is-danger' : ''"
        >
          <template #label
            ><p style="font-size: 20px">Treść ogłoszenia</p></template
          >
          <b-input
            @focus="contentGiven = true"
            v-model="announcementContent"
            style="width: 100%"
            type="textarea"
          />
        </b-field>
      </div>
      <b-button
        style="margin-top: 50px;"
        expanded
        type="is-success"
        @click="clicked()"
      >
        Stwórz ogłoszenie
      </b-button>
    </div>
  </div>
</template>
  
<script>
import { mapActions, mapState, mapGetters } from "vuex";

export default {
  name: "addAnnouncement",

  data() {
    return {
      loading: true,
      announcementTitle: "",
      announcementContent: "",
      announcementCategory: "",
      announcementGroup: "",
      groupGiven: true,
      titleGiven: true,
      contentGiven: true,
      categoryGiven: true,
      authorGiven: true,
      userAdminGroups: [],
    };
  },

  methods: {
    ...mapActions("announcement", ["addAnnouncement"]),
    ...mapActions("user", ["getUserAdminResearchGroups"]),

    clicked() {
      if (this.announcementGroup == "") this.groupGiven = false;
      if (this.announcementTitle == "") this.titleGiven = false;
      if (this.announcementCategory == "") this.categoryGiven = false;
      if (this.announcementContent == "") this.contentGiven = false;

      if (this.groupGiven && this.titleGiven && this.categoryGiven && this.contentGiven) {
        const researchGroup = document.getElementById('selectGroup');
        
        this.addAnnouncement({
          title: this.announcementTitle,
          text: this.announcementContent,
          ann_type: this.announcementCategory,
          
          author: this.authUser.id,
          research_group_id: researchGroup.value,
        })
          .then((newAnnouncement) => {
            this.$buefy.toast.open({
              message: "Pomyślnie dodano ogłoszenie",
              type: "is-success",
            });

            this.$router.replace(
              this.$route.query.redirect || `/announcement/${newAnnouncement.id}`
            );
          })
          .catch((err) => {
            this.$buefy.toast.open({
              message:
                "Błąd przy dodawaniu ogłoszenia (" +
                (err.response ? err.response.status : 500) +
                ")",
              type: "is-danger",
            });
          });
        
        this.announcementGroup = "";
        this.announcementTitle = "";
        this.announcementContent = "";
        this.announcementCategory = "";
      }
    },
  },
  computed: {
    ...mapState({
      userAdminResearchGroups: (state) => state.user.userAdminResearchGroups,
    }),
    ...mapGetters("auth", ["authUser"]),
  },
  mounted() {
    this.getUserAdminResearchGroups(this.authUser.id)
    .then(
      () => {
        this.userAdminGroups = this.userAdminResearchGroups;
      }
    )
    .then(() => {
      this.loading = false;
    });
  }
}
</script>

