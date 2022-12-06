<template>
  <div id="content">
    <p class="title" style="width: fit-content">Tworzenie ogłoszenia</p>
      <div id="container" style="margin: 70px auto; width: 70%;">
        <div class="box">
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
            :message="!categoryGiven ? 'Proszę podać kategorię ogłoszenia' : ''"
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
          <br>
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
  import { mapActions, mapGetters } from "vuex";
  
  export default {
    name: "addAnnouncement",
  
    data() {
      return {
        announcementTitle: "",
        announcementContent: "",
        announcementCategory: "",
        titleGiven: true,
        contentGiven: true,
        categoryGiven: true,
        authorGiven: true,

      };
    },
  
    methods: {
      ...mapActions("announcement", ["addAnnouncement"]),
      clicked() {
        if (this.announcementTitle == "") this.titleGiven = false;
        if (this.announcementCategory == "") this.categoryGiven = false;
        if (this.announcementContent == "") this.contentGiven = false;
  
        if (this.titleGiven && this.categoryGiven && this.contentGiven) {
          this.addAnnouncement({
            title: this.announcementTitle,
            text: this.announcementContent,
            ann_type: this.announcementCategory,
            
            author: this.authUser.id,
            research_group_id: 1, //todo
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
  
          this.announcementTitle = "";
          this.announcementContent = "";
          this.announcementCategory = "";
        }
      },
    },
    computed: {
    ...mapGetters("auth", ["authUser"]),
  },
  }
</script>
