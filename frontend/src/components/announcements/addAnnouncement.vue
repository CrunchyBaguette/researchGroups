<template>
    <div id="content" style="display: flex; flex-flow: column; margin 0">
      <div style="flex: 0 1 auto">
        <p class="title" style="width: fit-content">Tworzenie ogłoszenia</p>
      </div>
      <div style="flex: 1 1 auto; overflow: auto; padding: 10px">
        <div class="columns" style="width: 80%; margin: 50px auto">
          <div class="column" style="display: flex; flex-flow: column; margin: 0">
            <div class="box" style="flex: 1 1 auto">
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
            <div style="flex: 0 1 auto">
              <b-button
                style="margin-top: 50px"
                expanded
                type="is-success"
                @click="clicked()"
              >
                Stwórz ogłoszenie
              </b-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { mapActions } from "vuex";
  
  export default {
    name: "addAnnouncement",
  
    data() {
      return {
        announcementTitle: "",
        announcementContent: "",
        announcementAuthor: "", // chyba do wywalenia
        announcementDate: "", // - // -
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
            
            author: 2,
            research_group_id: 1,
          })
            .then(() => {
              this.$buefy.toast.open({
                message: "Pomyślnie dodano ogłoszenie",
                type: "is-success",
              });
  
              this.$router.replace(
                this.$route.query.redirect || "/"
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
          //inne chyba nie
        }
      },
    },
  }
</script>