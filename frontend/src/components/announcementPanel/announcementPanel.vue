<template>
  <div id="content" v-if="!this.loading">
    <div id="titleDiv" v-if="!isBeingEdited">
      <p class="title" id="tit">Panel Ogłoszenia</p>
      <b-button
          id="btnTitle"
          rounded
          size="is-medium"
          type="is-success"
          @click="changeToEditMode"
          >Edytuj ogłoszenie</b-button
        >
    </div>
    <div id="titleDiv" v-else>
      <p class="title" id="tit">Edycja Ogłoszenia</p>
      <b-button
        id="btnTitle"
        rounded
        size="is-medium"
        type="is-success"
        @click="changeToPanelMode"
        :disabled="isButtonDisabled"
        ><b-icon icon="arrow-left" />&nbsp;&nbsp;Wróć do panelu ogłoszenia</b-button
      >
    </div>
    
    
    <announcement v-if="!isBeingEdited" 
      id="ann"
      :author="announcementAuthor"
      :category="announcementCategory"
      :date="announcementDate"
      sortable
      :title="announcementTitle"
      :content="announcementContent"
    />
    <div v-else>
      <div id="root-container" class="box">
        <div class="container">
          <div class="author-category-container">
            <p class="author-in-edit-mode">{{ announcementAuthor }}</p>
            <div class="category-edit-container">
              <p class="category" v-if="!editAnnouncementCategory || !isBeingEdited">
                {{ announcementCategory }}
              </p>
              <div class="div-edit" v-else>
                <b-field label="Typ ogłoszenia">
                  <b-select v-model="announcementCategory" placeholder="Wybierz kategorię">
                    <option value="Poszukiwanie sponsora">Poszukiwanie sponsora</option>
                    <option value="Rekrutacja">Poszukiwanie nowych członków</option>
                    <option value="Poszukiwanie osób do projektu">Poszukiwanie osób do projektu</option>
                  </b-select>
                </b-field>
                <div id="btnsDiv">
                  <b-button
                    id="btnSave"
                    class="button is-primary is-success"
                    @click="saveAnnouncementCategory"
                    >Zapisz</b-button
                  >
                  <b-button @click="cancelAnnouncementCategory">Anuluj</b-button>
                </div>
              </div>
              <div id="btnsDiv">
                <b-button
                  :disabled="isButtonDisabled"
                  id="btnPencil"
                  @click="changeAnnouncementCategory"
                  v-if="!editAnnouncementCategory && isBeingEdited"
                >
                  <b-icon icon="lead-pencil" />
                </b-button>
              </div>
            </div>
          </div>
          <div class="date-container">
              <p class="date-in-edit-mode">{{ announcementDate }}</p> 
          </div>
          <div class="title-container">
            <div class="title-edit-container">
              <p class="title" v-if="!editAnnouncementTitle || !isBeingEdited">
                {{ announcementTitle }}
              </p>
              <div class="div-edit" v-else>
                <b-field
                  :message="announcementTitleGiven"
                  :type="announcementTitleGiven ? 'is-danger' : ''"
                  label="Tytuł ogłoszenia"
                >
                  <b-input
                    @focus="announcementTitleGiven = ''"
                    v-model="announcementTitle"
                    maxlength="120"
                  ></b-input>
                </b-field>
                <div id="btnsDiv">
                  <b-button
                    id="btnSave"
                    class="button is-primary is-success"
                    @click="saveAnnouncementTitle"
                    >Zapisz</b-button
                  >
                  <b-button @click="cancelAnnouncementTitle">Anuluj</b-button>
                </div>
              </div>
              <div id="btnsDiv">
                <b-button
                  :disabled="isButtonDisabled"
                  id="btnPencil"
                  @click="changeAnnouncementTitle"
                  v-if="!editAnnouncementTitle && isBeingEdited"
                >
                  <b-icon icon="lead-pencil" />
                </b-button>
              </div>
            </div>
          </div>
          
          <div class="content-container">
            <div id="btnEditContent">
              <b-button
                :disabled="isButtonDisabled"
                id="btnPencil"
                @click="changeAnnouncementContent"
                v-if="!editAnnouncementContent && isBeingEdited"
              >
                <b-icon icon="lead-pencil" />
              </b-button>
            </div>
            <p class="content" v-if="!editAnnouncementContent || !isBeingEdited">
              {{ announcementContent }}
            </p>
            <div v-else>
              <b-field
                :message="announcementContentGiven"
                :type="announcementContentGiven ? 'is-danger' : ''"
                label="Treść ogłoszenia"
              >
                <b-input
                  @focus="announcementContentGiven = ''"
                  v-model="announcementContent"
                  id="editableText"
                  type="textarea"
                  size="is-medium"
                ></b-input>
              </b-field>
              <div id="btnsDiv">
                <b-button
                  id="btnSave"
                  class="button is-primary is-success"
                  @click="saveAnnouncementContent"
                  >Zapisz</b-button
                >
                <b-button @click="cancelAnnouncementContent">Anuluj</b-button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import announcement from "../announcementCatalog/announcement.vue";
import { mapActions, mapState, mapGetters} from "vuex";

export default {
  name: "announcementPanel",
  components: {
    announcement,
  },
  data() {
    return {
      loading: true,

      //beforeEditAnnouncementTitle: "Ogłoszenie 1", //aktualny tytuł z bazy
      announcementTitle: "",
      editAnnouncementTitle: false,
      announcementTitleGiven: "",

      //beforeEditAnnouncementCategory: "Poszukiwanie sponsora", //aktualna kategoria z bazy
      announcementCategory: "",
      editAnnouncementCategory: false,

      //beforeEditAnnouncementContent:
        //"Co robimy Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae tenetur distinctio voluptatem molestias sapiente eum voluptatum perspiciatis adipisci? Adipisci voluptates ducimus in nulla quibusdam animi aspernatur dignissimos laboriosam ipsam nihil eveniet impedit dolorem ipsum ea nam, laborum incidunt assumenda voluptatum perferendis illo natus saepe obcaecati. Consequuntur ipsum nesciunt unde recusandae, dolor reiciendis veritatis sint excepturi repudiandae enim sequi, molestiae nobis neque perferendis. Illum molestias perspiciatis placeat totam, animi nostrum est exercitationem ad maxime! Amet modi possimus culpa neque consequatur quasi corporis optio veniam exercitationem voluptatibus fugit iure dicta ex quo facilis molestiae inventore atque, officiis maiores dolore a sapiente! Voluptates corporis voluptatum impedit. Praesentium, animi consequatur? Tenetur, expedita culpa accusantium non corporis autem rem unde eos tempore deleniti suscipit repellat repellendus quasi porro ullam veniam nulla quos eligendi, praesentium quaerat! Esse dolores totam, eaque temporibus quis itaque delectus dolor odio minima, natus adipisci laborum animi nesciunt architecto assumenda quae. Itaque cupiditate alias vitae molestiae harum enim ipsam possimus sapiente, qui hic vero odit velit amet autem, est doloribus ea soluta quasi voluptas! Suscipit officia vel doloremque, accusantium, soluta dolorem delectus at culpa aperiam laudantium non similique corrupti expedita earum hic quibusdam cum, sunt repudiandae! Ipsa nam quasi possimus aliquid, dignissimos eveniet, sed blanditiis nulla enim obcaecati labore mollitia dolor ullam magni praesentium reiciendis quibusdam molestias adipisci neque, ducimus maxime a corrupti. Reiciendis, non magnam! Quibusdam nulla veniam a quae, nemo, velit dicta reprehenderit animi maxime, sequi nihil sapiente obcaecati reiciendis quas doloribus! Iure voluptas explicabo fuga sunt labore voluptatibus ullam consequuntur ea, quisquam consequatur tenetur iste! Eos quod libero eveniet minima vel cupiditate animi impedit tempora recusandae, possimus iste facilis dolorem excepturi ipsam in delectus numquam quos iure earum aliquid quibusdam inventore illum pariatur repellendus? Qui possimus reiciendis aliquid, asperiores dolore incidunt amet repudiandae quia eaque quisquam eligendi iste repellat deleniti voluptatibus a commodi voluptate corrupti hic? Aperiam consequatur eveniet laboriosam veritatis, saepe minima, laudantium tempora aliquam nostrum provident sed aspernatur nisi? Quibusdam ratione soluta impedit harum libero quam recusandae eaque, reprehenderit obcaecati magni iure labore unde nobis aperiam distinctio perferendis est nulla, totam ipsam aliquid consequatur voluptas sed cupiditate. Molestias nisi error blanditiis cum inventore delectus debitis quia labore nostrum ullam accusantium modi qui, id aliquid repudiandae magni aperiam officiis fugit deserunt unde quaerat. Earum, aut? Obcaecati delectus eos voluptates optio iste amet modi distinctio harum voluptate excepturi fugiat debitis similique incidunt sapiente dicta vel maxime at enim, sunt adipisci aut vitae repellat? Dolores nostrum, obcaecati necessitatibus est asperiores dolorum repellendus numquam modi voluptatum nemo voluptatibus maxime, dolore impedit iste porro eveniet exercitationem quaerat. Vitae saepe quasi cumque necessitatibus alias officia corrupti suscipit ducimus quae magni. Commodi molestiae vel rem temporibus recusandae sit, vero doloribus earum cupiditate est odit veritatis iusto quidem tempore asperiores illum tempora, corrupti quos doloremque hic placeat eaque minus consectetur? Itaque quidem nostrum odit reiciendis ab consequuntur asperiores aperiam magni dolor eveniet odio eos quibusdam aliquid veritatis non modi excepturi dolorem deserunt iure explicabo, perferendis, quo quos blanditiis praesentium. Laborum blanditiis laudantium quae sapiente voluptatum nam a explicabo eius molestias nihil repudiandae quod ipsa aliquam rerum sint voluptates ipsum fugiat quasi, inventore dolore perferendis quia mollitia? Delectus a exercitationem nemo aliquid sed at facilis omnis cupiditate repellat laborum, temporibus placeat neque reiciendis maxime esse ex suscipit corrupti tenetur doloremque quo assumenda commodi debitis porro? Sed, amet cum. Expedita, deserunt officiis. Minus, ex maxime explicabo deserunt quia excepturi placeat in consequatur doloremque natus corrupti vero dicta reiciendis recusandae sequi est cupiditate magnam laudantium facere accusantium blanditiis quam. Similique eum rerum aut ipsum deserunt explicabo accusantium animi laborum expedita, veritatis atque impedit obcaecati sequi possimus non quod aliquam fugit minus nostrum iste quasi facilis asperiores blanditiis provident! Ex, sint, esse obcaecati commodi aliquam ullam assumenda possimus expedita repudiandae doloribus dolorem incidunt eum cum nobis sapiente in, reiciendis laboriosam cupiditate cumque iure corrupti excepturi ipsum natus ratione? Repellat impedit voluptatem, qui necessitatibus ex vitae magni, praesentium rem dolores aperiam odio. Ullam possimus itaque voluptatem id aut, ipsum tenetur impedit modi earum laboriosam, doloremque commodi porro, facere rerum ipsam pariatur odit? Eaque pariatur asperiores dolores natus accusantium laborum commodi hic, culpa illum, voluptas incidunt ea sequi maxime adipisci est necessitatibus blanditiis id doloremque. Consequatur amet fugit voluptate, unde molestiae aut harum consequuntur blanditiis doloribus repellendus dolor ratione laboriosam doloremque dolores tempore porro, maxime, aperiam exercitationem vero quae voluptatibus eum totam illo ut! Impedit, dolores. Quaerat fugiat cum aliquid, culpa nam adipisci quibusdam, modi nemo nesciunt beatae consequuntur omnis molestiae tenetur? Nobis laboriosam aliquam repellat temporibus maiores unde, quas harum ipsa iure repellendus aspernatur, tempora laborum maxime porro culpa magnam ab quos fugit dignissimos explicabo beatae voluptas, rem nihil. Est debitis quae commodi! Veniam vero consequatur ad voluptatem minima, omnis sint dolorem in amet. Deserunt commodi asperiores porro molestiae explicabo voluptatum alias voluptatem consequuntur modi laborum, iure nesciunt quidem cumque.",
      announcementContent: "",
        //"Co robimy Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae tenetur distinctio voluptatem molestias sapiente eum voluptatum perspiciatis adipisci? Adipisci voluptates ducimus in nulla quibusdam animi aspernatur dignissimos laboriosam ipsam nihil eveniet impedit dolorem ipsum ea nam, laborum incidunt assumenda voluptatum perferendis illo natus saepe obcaecati. Consequuntur ipsum nesciunt unde recusandae, dolor reiciendis veritatis sint excepturi repudiandae enim sequi, molestiae nobis neque perferendis. Illum molestias perspiciatis placeat totam, animi nostrum est exercitationem ad maxime! Amet modi possimus culpa neque consequatur quasi corporis optio veniam exercitationem voluptatibus fugit iure dicta ex quo facilis molestiae inventore atque, officiis maiores dolore a sapiente! Voluptates corporis voluptatum impedit. Praesentium, animi consequatur? Tenetur, expedita culpa accusantium non corporis autem rem unde eos tempore deleniti suscipit repellat repellendus quasi porro ullam veniam nulla quos eligendi, praesentium quaerat! Esse dolores totam, eaque temporibus quis itaque delectus dolor odio minima, natus adipisci laborum animi nesciunt architecto assumenda quae. Itaque cupiditate alias vitae molestiae harum enim ipsam possimus sapiente, qui hic vero odit velit amet autem, est doloribus ea soluta quasi voluptas! Suscipit officia vel doloremque, accusantium, soluta dolorem delectus at culpa aperiam laudantium non similique corrupti expedita earum hic quibusdam cum, sunt repudiandae! Ipsa nam quasi possimus aliquid, dignissimos eveniet, sed blanditiis nulla enim obcaecati labore mollitia dolor ullam magni praesentium reiciendis quibusdam molestias adipisci neque, ducimus maxime a corrupti. Reiciendis, non magnam! Quibusdam nulla veniam a quae, nemo, velit dicta reprehenderit animi maxime, sequi nihil sapiente obcaecati reiciendis quas doloribus! Iure voluptas explicabo fuga sunt labore voluptatibus ullam consequuntur ea, quisquam consequatur tenetur iste! Eos quod libero eveniet minima vel cupiditate animi impedit tempora recusandae, possimus iste facilis dolorem excepturi ipsam in delectus numquam quos iure earum aliquid quibusdam inventore illum pariatur repellendus? Qui possimus reiciendis aliquid, asperiores dolore incidunt amet repudiandae quia eaque quisquam eligendi iste repellat deleniti voluptatibus a commodi voluptate corrupti hic? Aperiam consequatur eveniet laboriosam veritatis, saepe minima, laudantium tempora aliquam nostrum provident sed aspernatur nisi? Quibusdam ratione soluta impedit harum libero quam recusandae eaque, reprehenderit obcaecati magni iure labore unde nobis aperiam distinctio perferendis est nulla, totam ipsam aliquid consequatur voluptas sed cupiditate. Molestias nisi error blanditiis cum inventore delectus debitis quia labore nostrum ullam accusantium modi qui, id aliquid repudiandae magni aperiam officiis fugit deserunt unde quaerat. Earum, aut? Obcaecati delectus eos voluptates optio iste amet modi distinctio harum voluptate excepturi fugiat debitis similique incidunt sapiente dicta vel maxime at enim, sunt adipisci aut vitae repellat? Dolores nostrum, obcaecati necessitatibus est asperiores dolorum repellendus numquam modi voluptatum nemo voluptatibus maxime, dolore impedit iste porro eveniet exercitationem quaerat. Vitae saepe quasi cumque necessitatibus alias officia corrupti suscipit ducimus quae magni. Commodi molestiae vel rem temporibus recusandae sit, vero doloribus earum cupiditate est odit veritatis iusto quidem tempore asperiores illum tempora, corrupti quos doloremque hic placeat eaque minus consectetur? Itaque quidem nostrum odit reiciendis ab consequuntur asperiores aperiam magni dolor eveniet odio eos quibusdam aliquid veritatis non modi excepturi dolorem deserunt iure explicabo, perferendis, quo quos blanditiis praesentium. Laborum blanditiis laudantium quae sapiente voluptatum nam a explicabo eius molestias nihil repudiandae quod ipsa aliquam rerum sint voluptates ipsum fugiat quasi, inventore dolore perferendis quia mollitia? Delectus a exercitationem nemo aliquid sed at facilis omnis cupiditate repellat laborum, temporibus placeat neque reiciendis maxime esse ex suscipit corrupti tenetur doloremque quo assumenda commodi debitis porro? Sed, amet cum. Expedita, deserunt officiis. Minus, ex maxime explicabo deserunt quia excepturi placeat in consequatur doloremque natus corrupti vero dicta reiciendis recusandae sequi est cupiditate magnam laudantium facere accusantium blanditiis quam. Similique eum rerum aut ipsum deserunt explicabo accusantium animi laborum expedita, veritatis atque impedit obcaecati sequi possimus non quod aliquam fugit minus nostrum iste quasi facilis asperiores blanditiis provident! Ex, sint, esse obcaecati commodi aliquam ullam assumenda possimus expedita repudiandae doloribus dolorem incidunt eum cum nobis sapiente in, reiciendis laboriosam cupiditate cumque iure corrupti excepturi ipsum natus ratione? Repellat impedit voluptatem, qui necessitatibus ex vitae magni, praesentium rem dolores aperiam odio. Ullam possimus itaque voluptatem id aut, ipsum tenetur impedit modi earum laboriosam, doloremque commodi porro, facere rerum ipsam pariatur odit? Eaque pariatur asperiores dolores natus accusantium laborum commodi hic, culpa illum, voluptas incidunt ea sequi maxime adipisci est necessitatibus blanditiis id doloremque. Consequatur amet fugit voluptate, unde molestiae aut harum consequuntur blanditiis doloribus repellendus dolor ratione laboriosam doloremque dolores tempore porro, maxime, aperiam exercitationem vero quae voluptatibus eum totam illo ut! Impedit, dolores. Quaerat fugiat cum aliquid, culpa nam adipisci quibusdam, modi nemo nesciunt beatae consequuntur omnis molestiae tenetur? Nobis laboriosam aliquam repellat temporibus maiores unde, quas harum ipsa iure repellendus aspernatur, tempora laborum maxime porro culpa magnam ab quos fugit dignissimos explicabo beatae voluptas, rem nihil. Est debitis quae commodi! Veniam vero consequatur ad voluptatem minima, omnis sint dolorem in amet. Deserunt commodi asperiores porro molestiae explicabo voluptatum alias voluptatem consequuntur modi laborum, iure nesciunt quidem cumque.",
      editAnnouncementContent: false,
      announcementContentGiven: "",

      announcementAuthor: "",

      //beforeEditAnnouncementDate: "12.08.2022 21:21",
      announcementDate: "",

      isBeingEdited: false,
      isButtonDisabled: false,
    };
  },
  mounted() {
    document.title = "Panel ogłoszenia";
    this.getAnnouncement(this.$route.params.id)
      .then(
        () => (
          (this.announcementTitle = this.announcement.title),
          (this.announcementCategory = this.announcement.ann_type),
          (this.announcementContent = this.announcement.text),
          (this.announcementAuthor = this.announcement.author),
          (this.announcementDate = this.announcement.date)
        )
      )
      .then(() => {
        this.loading = false;
      });
  },
  methods: {
    ...mapActions("announcement", ["getAnnouncement", "updateAnnouncement"]),

    updateAnnouncementInfo() {
      this.updateAnnouncement({
        id: this.$route.params.id,
        payload: {
          title: this.announcementTitle,
          ann_type: this.announcementCategory,
          text: this.announcementContent,
          author: this.announcementAuthor,
          date: this.announcementDate,
        },
      }).catch((err) => {
        this.announcementTitle = this.announcement.title;
        this.announcementCategory = this.announcement.ann_type;
        this.announcementContent = this.announcement.text;
        this.announcementAuthor = this.announcement.author;
        this.announcementDate = this.announcement.date;
        this.$buefy.toast.open({
          message: err.response.data[Object.keys(err.response.data)[0]],
          type: "is-danger",
        });
      });
    },

    changeToPanelMode() {
      this.isBeingEdited = false;
    },
    changeToEditMode() {
      this.isBeingEdited = true;
    },
    changeAnnouncementCategory() {
      this.editAnnouncementCategory = !this.editAnnouncementCategory;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveAnnouncementCategory() {
      this.updateAnnouncementInfo();
      this.changeAnnouncementCategory();
    },
    cancelAnnouncementCategory() {
      this.announcementCategory = this.announcement.ann_type;
      this.changeAnnouncementCategory();
    },
    changeAnnouncementTitle() {
      this.editAnnouncementTitle = !this.editAnnouncementTitle;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveAnnouncementTitle() {
      if (this.announcementTitle === "") {
        this.announcementTitleGiven = "Podaj tytuł ogłoszenia";
      }
      else {
        this.updateAnnouncementInfo();
        this.changeAnnouncementTitle();
      }
    },
    cancelAnnouncementTitle() {
      this.announcementTitle = this.announcement.title;
      this.changeAnnouncementTitle();
    },
    changeAnnouncementContent() {
      this.editAnnouncementContent = !this.editAnnouncementContent;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveAnnouncementContent() {
      if (this.announcementContent === "") {
        this.announcementContentGiven = "Podaj treść";
      } else {
        this.updateAnnouncementInfo();
        this.changeAnnouncementContent();
      }
    }, 
    cancelAnnouncementContent() {
      this.announcementContent = this.announcement.text;
      this.changeAnnouncementContent();
    },
  },

  watch: {
    $route() {
      this.loading = true;
      this.isBeingEdited = false;
      this.getAnnouncement(this.$route.params.id)
        .then(
          () => (
            (this.announcementTitle = this.announcement.title),
            (this.announcementCategory = this.announcement.ann_type),
            (this.announcementContent = this.announcement.text),
            (this.announcementAuthor = this.announcement.author),
            (this.announcementDate = this.announcement.date)
          )
        )
        .then(() => {
          this.loading = false;
        });
    }
  },

  computed: {
    ...mapState({
      announcement: (state) => state.announcement.announcement,
    }),
    ...mapGetters("auth", ["isAuthenticated", "authUser"]),
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

#root-container {
  margin: 20px;
  width: 97%;
  background-color: rgb(196, 196, 196);
  color: black;
}

.container {
  width: auto;
  height: 85%;
} 

.author-category-container {
  display: flex;
  justify-content: space-between;
  width: 100%;
  height: 30%;
}

.author-in-edit-mode {
  padding-left: 5px;
  font-weight: bold;
  font-size: 20px;
  color: rgb(139, 139, 139);
}

.category {
  padding-right: 5px;
  color: rgb(139, 139, 139);
  font-weight: bold;
  font-size: 20px;
}

.date-in-edit-mode {
  padding-left: 5px;
  color: rgb(139, 139, 139);
}

.content-container {
  width: 100%;
  height: 70%;
  overflow: hidden;
}

.content {
  padding: 5px;
}

.div-edit {
  margin-right: 5px;
  padding: 10px;
  border-radius: 6px;
  box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%),
    0 0px 0 1px rgb(10 10 10 / 2%);
  color: #4a4a4a;
  background-color: #fff;
}

#btnsDiv {
  display: flex;
  justify-content: center;
  align-items: center;
}

.category-edit-container {
  display: flex;
}

.title-edit-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.btnEditContent {
  text-align: left;
}

</style>

