<template>
  <div id="content" v-if="!this.loading">
    <div id="titleDiv" v-if="!isBeingEdited">
      <p class="title" id="tit">Panel Ogłoszenia</p>
      <div>
        <b-button
          v-if="!isOwner()"
          id="btnTitle"
          rounded
          size="is-medium"
          type="is-success"
          @click="() => (sendingEmail = true)"
          >Wyślij wiadomość</b-button
        >
        <b-button
          v-if="isOwner()"
          id="btnTitle"
          rounded
          size="is-medium"
          type="is-success"
          @click="changeToEditMode"
          >Edytuj ogłoszenie</b-button
        >
      </div>
    </div>
    <div id="titleDiv" v-else>
      <p class="title" id="tit">Edycja Ogłoszenia</p>
      <div>
        <b-button
          v-if="isOwner()"
          id="btnTitle"
          rounded
          size="is-medium"
          type="is-danger"
          @click="deleteAnnouncementConfirmation"
          >Usuń ogłoszenie</b-button
        ><b-button
          id="btnTitle"
          rounded
          size="is-medium"
          type="is-success"
          @click="changeToPanelMode"
          :disabled="isButtonDisabled"
          ><b-icon icon="arrow-left" />&nbsp;&nbsp;Wróć do panelu
          ogłoszenia</b-button
        >
      </div>
    </div>

    <announcement
      v-if="!isBeingEdited"
      id="annx"
      :author="announcementAuthor"
      :group="announcementGroup"
      :category="announcementCategory"
      :added="announcementAdded"
      :edited="announcementEdited"
      :title="announcementTitle"
      :content="announcementContent"
    />
    <div v-else>
      <div id="root-container" class="box">
        <div class="container">
          <div class="author-category-container">
            <div class="author-group-container">
              <p class="author-in-edit-mode">{{ announcementAuthor }}</p>

              <div class="div-title">
                <p
                  class="group"
                  v-if="!editAnnouncementGroup || !isBeingEdited"
                >
                  {{ announcementGroup }}
                </p>
                <div class="div-edit" v-else>
                  <b-field label="Twoje koła">
                    <b-select
                      v-model="selectedGroup[0]"
                      placeholder="Wybierz koło"
                    >
                      <option
                        :value="group"
                        v-for="group in userAdminGroups"
                        v-bind:key="group.id"
                      >
                        {{ group.name }}
                      </option>
                    </b-select>
                  </b-field>
                  <div id="btnsDiv">
                    <b-button
                      id="btnSave"
                      class="button is-primary is-success"
                      @click="saveAnnouncementGroup"
                      >Zapisz</b-button
                    >
                    <b-button @click="cancelAnnouncementGroup">Anuluj</b-button>
                  </div>
                </div>
                <div id="btnsDiv">
                  <b-button
                    :disabled="isButtonDisabled"
                    id="btnPencil"
                    @click="changeAnnouncementGroup"
                    v-if="!editAnnouncementGroup && isBeingEdited"
                  >
                    <b-icon icon="lead-pencil" />
                  </b-button>
                </div>
              </div>
            </div>

            <div class="div-title">
              <p
                class="category"
                v-if="!editAnnouncementCategory || !isBeingEdited"
              >
                {{ announcementCategory }}
              </p>
              <div class="div-edit" v-else>
                <b-field label="Typ ogłoszenia">
                  <b-select
                    v-model="announcementCategory"
                    placeholder="Wybierz kategorię"
                  >
                    <option value="Poszukiwanie sponsora">
                      Poszukiwanie sponsora
                    </option>
                    <option value="Poszukiwanie nowych członków">
                      Poszukiwanie nowych członków
                    </option>
                    <option value="Poszukiwanie osób do projektu">
                      Poszukiwanie osób do projektu
                    </option>
                  </b-select>
                </b-field>
                <div id="btnsDiv">
                  <b-button
                    id="btnSave"
                    class="button is-primary is-success"
                    @click="saveAnnouncementCategory"
                    >Zapisz</b-button
                  >
                  <b-button @click="cancelAnnouncementCategory"
                    >Anuluj</b-button
                  >
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
            <p class="date-in-edit-mode">
              Utworzone:
              {{ new Date(announcementAdded) | dateFormat("DD.MM.YYYY HH:mm") }}
            </p>
            <p class="date-in-edit-mode">
              Edytowane: {{ new Date() | dateFormat("DD.MM.YYYY HH:mm") }}
            </p>
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
            <div
              class="box content"
              v-if="!editAnnouncementContent || !isBeingEdited"
            >
              <markdown-it-vue
                class="md-body"
                :content="announcementContent"
                :options="markdownOptions"
              />
            </div>
            <div v-else>
              <b-field
                :message="announcementContentGiven"
                :type="announcementContentGiven ? 'is-danger' : ''"
                label="Treść ogłoszenia"
              >
                <b-input
                  @focus="announcementContentGiven = ''"
                  v-model="announcementContent"
                  id="editableAnnContent"
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
    <b-modal has-modal-card :active.sync="this.sendingEmail" trap-focus>
      <template>
        <div class="modal-card">
          <section class="modal-card-body">
            <b-field
              v-if="!this.isAuthenticated"
              :message="errorEmail"
              :type="errorEmail ? 'is-danger' : ''"
              label="E-mail:"
            >
              <b-input
                @focus="errorEmail = ''"
                v-model="email"
                style="width: 100%"
              />
            </b-field>
            <b-field
              :message="!messageGiven ? 'Proszę podać treść wiadomości' : ''"
              :type="!messageGiven ? 'is-danger' : ''"
              label="Treść wiadomości"
            >
              <b-input
                @focus="messageGiven = true"
                v-model="emailMessage"
                style="width: 100%"
                type="textarea"
              />
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <b-button type="is-success" @click="sendEmail"
              >Wyślij wiadomość</b-button
            >
            <b-button
              @click="() => ((sendingEmail = false), (emailMessage = ``))"
              >Anuluj</b-button
            >
          </footer>
        </div>
      </template>
    </b-modal>
  </div>
</template>

<script>
import announcement from "../announcementCatalog/announcement.vue";
import { mapActions, mapState, mapGetters } from "vuex";

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
      announcementAuthorId: 0,

      userAdminGroups: [],

      announcementGroup: "",
      announcementGroupId: 0,
      selectedGroup: [{}],
      editAnnouncementGroup: false,

      //beforeEditAnnouncementDate: "12.08.2022 21:21",
      announcementAdded: "",
      announcementEdited: "",

      isBeingEdited: false,
      isButtonDisabled: false,

      sendingEmail: false,
      email: "",
      errorEmail: "",
      emailMessage: "",
      messageGiven: true,

      markdownOptions: {
        markdownIt: {
          html: true,
          linkify: true,
        },
        linkAttributes: {
          attrs: {
            target: "_self",
            rel: "noopener",
          },
        },
      },
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
          (this.announcementAuthor = this.announcement.author_full_name),
          (this.announcementAuthorId = this.announcement.author),
          (this.announcementGroup = this.announcement.research_group_name),
          (this.announcementGroupId = this.announcement.research_group_id),
          (this.announcementAdded = this.announcement.added),
          (this.announcementEdited = this.announcement.edited)
        )
      )
      .then(() => {
        this.loading = false;
      });
    if (this.isAuthenticated) {
      this.getUserAdminResearchGroups(this.authUser.id)
        .then(() => {
          this.userAdminGroups = this.userAdminResearchGroups;
          this.selectedGroup = this.userAdminGroups.filter(
            (element) => element.id == this.announcementGroupId
          );
        })
        .then(() => {
          this.loading = false;
        });
    }
  },
  methods: {
    ...mapActions("announcement", [
      "getAnnouncement",
      "updateAnnouncement",
      "removeAnnouncement",
      "sendEmailMessage",
    ]),
    ...mapActions("user", ["getUserAdminResearchGroups"]),

    isOwner() {
      if (
        this.isAuthenticated &&
        this.announcementAuthorId === this.authUser.id
      ) {
        return true;
      } else {
        return false;
      }
    },

    verifyEmail(email) {
      if (
        !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          email
        )
      ) {
        return false;
      }
      return true;
    },

    updateAnnouncementInfo() {
      this.announcementGroupId = this.selectedGroup[0].id;
      this.announcementGroup = this.selectedGroup[0].name;
      this.updateAnnouncement({
        id: this.$route.params.id,
        payload: {
          title: this.announcementTitle,
          ann_type: this.announcementCategory,
          text: this.announcementContent,
          research_group_id: this.announcementGroupId,
          //author_full_name: this.announcementAuthor,
          //author: this.authUser.id,
          //edited: this.announcementEdited,
          //research_group_id: 1,
        },
      }).catch((err) => {
        this.announcementTitle = this.announcement.title;
        this.announcementCategory = this.announcement.ann_type;
        this.announcementContent = this.announcement.text;
        this.announcementGroupId = this.announcement.research_group_id;
        //this.announcementEdited = this.announcement.edited;

        this.$buefy.toast.open({
          message: err.response.data[Object.keys(err.response.data)[0]],
          type: "is-danger",
        });
      });
    },

    deleteAnnouncementConfirmation() {
      this.$buefy.dialog.confirm({
        title: "Usuwanie ogłoszenia",
        message: "<b>Czy na pewno chcesz usunąć ogłosznie?",
        confirmText: "Usuń ogłoszenie",
        type: "is-danger",
        hasIcon: true,
        onConfirm: () => this.deleteAnnouncement(),
      });
    },

    deleteAnnouncement() {
      this.removeAnnouncement(this.$route.params.id)
        .then(() => {
          this.$router.push("/");
          this.$buefy.toast.open({
            message: "Ogłoszenie zostało usunięte",
            type: "is-success",
          });
        })
        .catch((err) => {
          this.$buefy.toast.open({
            message: err.response.data[Object.keys(err.response.data)[0]],
            type: "is-danger",
          });
        });
    },

    sendEmail() {
      if (!this.isAuthenticated) {
        if (!this.verifyEmail(this.email))
          this.errorEmail = "Proszę podać poprawny adres e-mail";
        if (this.email == "") this.errorEmail = "Proszę podać adres e-mail";
      }
      if (this.emailMessage == "") this.messageGiven = false;

      if (this.messageGiven && !this.errorEmail) {
        this.sendEmailMessage({
          annId: this.$route.params.id,
          annTitle: this.announcement.title,
          author: this.announcement.author_email,
          sender: this.isAuthenticated ? this.authUser.email : this.email,
          text: this.emailMessage,
        })
          .then(() => {
            this.email = "";
            this.emailMessage = "";
            this.sendingEmail = false;
            this.$buefy.toast.open({
              message: "Pomyślnie wysłano wiadomość",
              type: "is-success",
            });
          })
          .catch(() => {
            this.$buefy.toast.open({
              message:
                "Błąd przy wysyłaniu wiadomości\nSpróbuj ponownie później",
              type: "is-danger",
            });
          });
      }
    },

    changeToPanelMode() {
      //this.announcementEdited = this.announcementAdded;
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
      // const p = document.getElementsByClassName('date-in-edit-mode');
      // this.announcementDate = p.content;
      this.updateAnnouncementInfo();
      this.changeAnnouncementCategory();
    },
    cancelAnnouncementCategory() {
      this.announcementCategory = this.announcement.ann_type;
      this.changeAnnouncementCategory();
    },
    changeAnnouncementGroup() {
      this.editAnnouncementGroup = !this.editAnnouncementGroup;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveAnnouncementGroup() {
      this.updateAnnouncementInfo();
      this.changeAnnouncementGroup();
    },
    cancelAnnouncementGroup() {
      this.announcementGroup = this.announcement.research_group_name;
      this.changeAnnouncementGroup();
    },
    changeAnnouncementTitle() {
      this.editAnnouncementTitle = !this.editAnnouncementTitle;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveAnnouncementTitle() {
      if (this.announcementTitle === "") {
        this.announcementTitleGiven = "Podaj tytuł ogłoszenia";
      } else {
        // const p = document.getElementsByClassName('date-in-edit-mode');
        // this.announcementDate = p.content;
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
        // const p = document.getElementsByClassName('date-in-edit-mode');
        // this.announcementDate = p.content;
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
            (this.announcementAuthor = this.announcement.author_full_name), //
            (this.announcementAuthorId = this.announcement.author),
            (this.announcementGroup = this.announcement.research_group_name), //
            (this.announcementGroupId = this.announcement.research_group_id),
            (this.announcementAdded = this.announcement.added),
            (this.announcementEdited = this.announcement.edited)
          )
        )
        .then(() => {
          this.loading = false;
        });
    },
  },

  computed: {
    ...mapState({
      announcement: (state) => state.announcement.announcement,
    }),
    ...mapState({
      userAdminResearchGroups: (state) => state.user.userAdminResearchGroups,
    }),
    ...mapGetters("auth", ["authUser", "isAuthenticated"]),
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

#annx {
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

/* .di {
  display: flex;
  flex-direction: row;
  justify-content: center;
} */

.title-edit-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.btnEditContent {
  text-align: left;
}

#editableAnnContent {
  height: 36vh;
  /* width: 800px !important; */
}

.group {
  padding-left: 5px;
  font-weight: bold;
  font-size: 20px;
}

.author-group-container {
  display: flex;
  flex-direction: row;
}
</style>

