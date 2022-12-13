<template>
  <div class="container" id="content" v-if="!this.loading">
    <div class="columns" style="width: 100%">
      <div class="column is-3"></div>
      <div class="column is-6">
        <div class="div-title">
          <h1 class="title" id="title" v-if="!editGroupName || !isBeingEdited">
            {{ groupName }}
          </h1>
          <div class="div-edit" v-else>
            <b-field
              :message="invalidGroupName"
              :type="invalidGroupName ? 'is-danger' : ''"
              label="Nazwa koła"
            >
              <b-input
                @focus="invalidGroupName = ''"
                v-model="groupName"
                placeholder="Podaj nazwę koła"
                maxlength="120"
              ></b-input>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button is-primary is-success"
                @click="saveGroupName"
                >Zapisz</b-button
              >
              <b-button @click="cancelGroupName">Anuluj</b-button>
            </div>
          </div>
          <div id="btnsDiv">
            <b-button
              :disabled="isButtonDisabled"
              id="btnPencil"
              @click="changeGroupName"
              v-if="!editGroupName && isBeingEdited"
            >
              <mdicon name="lead-pencil" />
            </b-button>
          </div>
        </div>

        <div class="div-title">
          <p class="p-category" v-if="!editGroupCategory || !isBeingEdited">
            {{ groupCategory }}
          </p>
          <div class="div-edit" v-else>
            <b-field label="Kategoria koła">
              <b-select v-model="groupCategory" placeholder="Wybierz kategorię">
                <option value="Matematyka">Matematyka</option>
                <option value="Medycyna">Medycyna</option>
                <option value="Chemia">Chemia</option>
              </b-select>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button is-primary is-success"
                @click="saveGroupCategory"
                >Zapisz</b-button
              >
              <b-button @click="cancelGroupCategory">Anuluj</b-button>
            </div>
          </div>
          <div id="btnsDiv">
            <b-button
              :disabled="isButtonDisabled"
              id="btnPencil"
              @click="changeGroupCategory"
              v-if="!editGroupCategory && isBeingEdited"
            >
              <mdicon name="lead-pencil" />
            </b-button>
          </div>
        </div>
        <br />
      </div>
      <div class="column is-3" id="col" v-if="isBeingEdited">
        <b-button
          id="title"
          rounded
          size="is-medium"
          type="is-success"
          @click="changeToPanelMode"
          :disabled="isButtonDisabled"
          ><mdicon name="arrow-left" /> Wróć do panelu koła</b-button
        >
      </div>
      <div class="column is-3" id="col" v-else>
        <b-button
          id="title"
          rounded
          size="is-medium"
          type="is-success"
          v-if="isAdminOrOwner()"
          @click="changeToEditMode"
          >Edytuj koło naukowe</b-button
        >
      </div>
      <div class="columns"></div>
    </div>
    <div class="columns" style="width: 100%">
      <div class="box column is-3">
        <b-button
          id="btn"
          size="is-medium"
          tag="router-link"
          to="/forum"
          v-if="isMember()"
          :disabled="isButtonDisabled"
          >Forum</b-button
        >
        <b-button
          id="btn"
          size="is-medium"
          v-on:click="showAboutUs"
          :disabled="isButtonDisabled"
          >O Nas</b-button
        >
        <b-button
          id="btn"
          size="is-medium"
          v-on:click="showWhatWeDo"
          :disabled="isButtonDisabled"
          >Czym się zajmujemy</b-button
        >
        <b-button
          id="btn"
          size="is-medium"
          v-on:click="showMembers"
          :disabled="isButtonDisabled"
          >Członkowie</b-button
        >
        <b-button
          id="btn"
          size="is-medium"
          v-on:click="showContact"
          :disabled="isButtonDisabled"
          >Kontakt</b-button
        >
        <b-button
          id="btn"
          size="is-medium"
          tag="router-link"
          to="/group-tutorials"
          :disabled="isButtonDisabled"
          >Materiały dydaktyczne</b-button
        >
      </div>
      <div class="box column is-6" id="centerDiv">
        <div class="outer" v-if="selectedTabTitle === 'Czym się zajmujemy'">
          <div class="div-title">
            <h2 class="centerDivHeader">{{ selectedTabTitle }}</h2>
            <div id="btnsDiv">
              <b-button
                :disabled="isButtonDisabled"
                id="btnPencil"
                @click="changeWhatWeDo"
                v-if="!editWhatWeDo && isBeingEdited"
              >
                <mdicon name="lead-pencil" />
              </b-button>
            </div>
          </div>
          <div class="inner" v-if="!editWhatWeDo">
            <markdown-it-vue
              class="md-body"
              :content="whatWeDo"
              :options="markdownOptions"
            />
          </div>
          <div v-else>
            <b-field>
              <b-input
                v-model="whatWeDo"
                id="editableText"
                type="textarea"
                size="is-medium"
              >
              </b-input>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button is-primary is-success"
                @click="saveWhatWeDo"
                >Zapisz</b-button
              >
              <b-button @click="cancelWhatWeDo">Anuluj</b-button>
            </div>
          </div>
        </div>

        <div class="outer" v-if="selectedTabTitle === 'Członkowie'">
          <div class="div-title">
            <h2 class="centerDivHeader">{{ selectedTabTitle }}</h2>
            <div id="btnsDiv">
              <b-button
                :disabled="isButtonDisabled"
                id="btnPencil"
                @click="changeMembers"
                v-if="!editMembers && isBeingEdited"
              >
                <mdicon name="lead-pencil" />
              </b-button>
            </div>
          </div>
          <div class="inner">
            <div
              style="
                width: 100%;
                height: 80%;
                background-color: rgb(240, 240, 240);
                margin-top: 5px;
                margin-bottom: 10px;
                overflow: auto;
              "
            >
              <div
                class="box"
                style="
                  border-radius: 25px;
                  width: 95%;
                  height: 40px;
                  margin: 10px auto;
                  padding: 5px 10px;
                  display: flex;
                "
                v-for="member in members"
                :key="member.person"
              >
                <p style="flex: 0 1 auto">
                  {{ member.person }}
                </p>
                <div
                  style="flex: 1 0 auto; text-align: right; margin-right: 10px"
                  v-if="!editMembers"
                >
                  {{ member.role }}
                </div>
                <div style="flex: 1 0 auto; text-align: right" v-else>
                  <b-dropdown
                    v-model="member.role"
                    aria-role="list"
                    position="is-bottom-left"
                    style="bottom: 5px; margin-right: 10px"
                  >
                    <template #trigger>
                      <b-button icon-right="menu-down">
                        {{ member.role }}
                      </b-button>
                    </template>
                    <b-dropdown-item value="Creator" aria-role="listitem">
                      <span>Creator</span>
                    </b-dropdown-item>
                    <b-dropdown-item value="Moderator" aria-role="listitem">
                      <span>Moderator</span>
                    </b-dropdown-item>
                    <b-dropdown-item value="Member" aria-role="listitem">
                      <span>Member</span>
                    </b-dropdown-item>
                  </b-dropdown>
                  <b-icon
                    icon="close"
                    @click.native="removeMemberFromList(member.person)"
                  />
                </div>
              </div>
              <div
                class="box"
                style="
                  border-radius: 25px;
                  width: 95%;
                  height: 40px;
                  margin: 10px auto;
                  padding: 5px 10px;
                  display: flex;
                "
                v-if="editMembers"
              >
                <div style="flex: 0 1 auto">
                  <b-input v-model="addEmail" style="bottom: 5px"></b-input>
                </div>
                <div style="flex: 1 0 auto; text-align: right">
                  <b-dropdown
                    v-model="addRole"
                    aria-role="list"
                    position="is-bottom-left"
                    style="bottom: 5px; margin-right: 10px"
                  >
                    <template #trigger>
                      <b-button icon-right="menu-down">
                        {{ addRole }}
                      </b-button>
                    </template>
                    <b-dropdown-item value="Creator" aria-role="listitem">
                      <span>Creator</span>
                    </b-dropdown-item>
                    <b-dropdown-item value="Moderator" aria-role="listitem">
                      <span>Moderator</span>
                    </b-dropdown-item>
                    <b-dropdown-item value="Member" aria-role="listitem">
                      <span>Member</span>
                    </b-dropdown-item>
                  </b-dropdown>
                  <b-icon icon="plus" @click.native="addMemberToList()" />
                </div>
              </div>
            </div>
            <div id="btnsDiv" v-if="editMembers">
              <b-button
                id="btnSave"
                class="button is-primary is-success"
                @click="saveMembers"
                >Zapisz</b-button
              >
              <b-button @click="cancelMembers">Anuluj</b-button>
            </div>
          </div>
        </div>

        <div class="outer" v-if="selectedTabTitle === 'O Nas'">
          <div class="div-title">
            <h2 class="centerDivHeader">{{ selectedTabTitle }}</h2>
            <div id="btnsDiv">
              <b-button
                :disabled="isButtonDisabled"
                id="btnPencil"
                @click="changeAboutUs"
                v-if="!editAboutUs && isBeingEdited"
              >
                <mdicon name="lead-pencil" />
              </b-button>
            </div>
          </div>
          <div class="inner" v-if="!editAboutUs">
            <markdown-it-vue
              class="md-body"
              :content="aboutUs"
              :options="markdownOptions"
            />
          </div>
          <div v-else>
            <b-field
              :message="aboutUsGiven"
              :type="aboutUsGiven ? 'is-danger' : ''"
            >
              <b-input
                @focus="aboutUsGiven = ''"
                v-model="aboutUs"
                id="editableText"
                type="textarea"
                size="is-medium"
              ></b-input>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button is-primary is-success"
                @click="saveAboutUs"
                >Zapisz</b-button
              >
              <b-button @click="cancelAboutUs">Anuluj</b-button>
            </div>
          </div>
        </div>
        <div class="outer" v-if="selectedTabTitle === 'Kontakt'">
          <div class="div-title">
            <h2 class="centerDivHeader">{{ selectedTabTitle }}</h2>
            <div id="btnsDiv">
              <b-button
                :disabled="isButtonDisabled"
                id="btnPencil"
                @click="changeContact"
                v-if="!editContact && isBeingEdited"
              >
                <mdicon name="lead-pencil" />
              </b-button>
            </div>
          </div>
          <div class="inner" v-if="!editContact">
            <markdown-it-vue
              class="md-body"
              :content="contact"
              :options="markdownOptions"
            />
            <div class="container-send-email">
              <button
                class="button"
                id="btnSendEmail"
                @click="popupEmail = !popupEmail"
              >
                WYŚLIJ WIADOMOŚĆ
              </button>

              <popupEmail v-if="popupEmail" @close="popupEmail = false" />
            </div>
          </div>
          <div v-else>
            <b-field>
              <b-input
                v-model="contact"
                id="editableText"
                type="textarea"
                size="is-medium"
              >
              </b-input>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button is-primary is-success"
                @click="saveContact"
                >Zapisz</b-button
              >
              <b-button @click="cancelContact">Anuluj</b-button>
            </div>
          </div>
        </div>
      </div>
      <div class="box column is-3" id="divLinks">
        <b-menu :activable="false" :accordion="false" id="menu">
          <b-menu-list>
            <b-menu-item label="Linki">
              <b-menu-item
                label="Github"
                target="_blank"
                href="https://github.com"
              ></b-menu-item>
              <b-menu-item
                label="Facebook"
                target="_blank"
                href="https://facebook.com"
              ></b-menu-item>
              <b-menu-item
                label="Discord"
                target="_blank"
                href="https://discord.com"
              ></b-menu-item>
            </b-menu-item>
            <b-menu-item label="Dyski">
              <b-menu-item
                label="Dysk 1"
                target="_blank"
                href="https://drive.google.com/drive/folders/1QMHnaSuOPcfOX16190I9D8q_Fa5pzeOF?usp=sharing"
              ></b-menu-item>
              <b-menu-item
                label="Dysk 2"
                target="_blank"
                href="https://drive.google.com/drive/folders/1vGf8f0nVkJcAZQ6S7mZ74vFhpJK0Gbeo?usp=sharing"
              ></b-menu-item>
            </b-menu-item>
          </b-menu-list>
        </b-menu>
      </div>
    </div>
  </div>
</template>

<script>
import popupEmail from "@/components/popup/PopupEmail.vue";
import { mapActions, mapState, mapGetters } from "vuex";

export default {
  name: "groupPanel",
  components: {
    popupEmail,
  },
  data() {
    return {
      loading: true,
      addEmail: "",
      addRole: "Member",

      selectedTabTitle: "O Nas",

      // beforeEditGroupName: "Koło naukowe", //aktualna nazwa koła z bazy
      groupName: "",
      editGroupName: false,
      invalidGroupName: "",

      groupCategory: "",
      editGroupCategory: false,

      whatWeDo: "",
      testMarkdown: "::: success\nTest success.\n:::",
      editWhatWeDo: false,

      members: [],
      editMembers: false,

      aboutUs: "",
      aboutUsGiven: "",
      editAboutUs: false,

      contact: "",
      editContact: false,

      popupEmail: false,

      isBeingEdited: false,
      isButtonDisabled: false,

      markdownOptions: {
        markdownIt: {
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
    document.title = "Edycja koła";
    this.getResearchGroup(this.$route.params.id)
      .then(
        () => (
          (this.groupName = this.researchGroup.name),
          (this.groupCategory = this.researchGroup.category),
          (this.whatWeDo = this.researchGroup.what_we_do),
          (this.aboutUs = this.researchGroup.about_us),
          (this.contact = this.researchGroup.contact)
        )
      )
      .then(() => {
        this.getResearchGroupMembers(this.researchGroup.id).then(
          () => (this.members = this.researchGroupMembers)
        );
      })
      .then(() => {
        this.loading = false;
      });
  },
  methods: {
    ...mapActions("researchGroup", ["getResearchGroup", "updateResearchGroup"]),
    ...mapActions("researchGroupMember", [
      "getResearchGroupMembers",
      "updateResearchGroupMembers",
    ]),

    isMember() {
      if (this.isAuthenticated) {
        if (this.researchGroup.members.includes(this.authUser.email)) {
          return true;
        }
      }
      return false;
    },

    isAdminOrOwner() {
      for (var i = 0; i < this.researchGroupMembers.length; i++) {
        if (
          this.isMember() &&
          this.researchGroupMembers[i]["person"] == this.authUser.email
        ) {
          if (
            this.researchGroupMembers[i]["role"] == "Creator" ||
            this.researchGroupMembers[i]["role"] == "Moderator"
          ) {
            return true;
          }
        }
      }
      return false;
    },

    removeMemberFromList(email) {
      let index = this.members.indexOf(email);
      this.members.splice(index, 1);
    },

    updateGroupInfo() {
      this.updateResearchGroup({
        id: this.$route.params.id,
        payload: {
          name: this.groupName,
          category: this.groupCategory,
          about_us: this.aboutUs,
          what_we_do: this.whatWeDo,
          contact: this.contact,
        },
      }).catch((err) => {
        this.groupName = this.researchGroup.name;
        this.groupCategory = this.researchGroup.category;
        this.aboutUs = this.researchGroup.about_us;
        this.whatWeDo = this.researchGroup.what_we_do;
        this.contact = this.researchGroup.contact;
        this.$buefy.toast.open({
          message: err.response.data[Object.keys(err.response.data)[0]],
          type: "is-danger",
        });
      });

      this.updateResearchGroupMembers({
        researchGroupId: this.$route.params.id,
        members: this.members,
      })
        .then((response) => {
          this.members = response.members;
        })
        .catch((err) => {
          this.getResearchGroupMembers(this.$route.params.id).then(
            (response) => {
              this.members = response.members;
            }
          );
          this.$buefy.toast.open({
            message: err.response.data[Object.keys(err.response.data)[0]],
            type: "is-danger",
          });
        });

      // this.getResearchGroupMembers(this.$route.params.id).then((response) => {
      //   this.members = response.members;
      // });
    },

    addMemberToList() {
      if (
        !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          this.addEmail
        )
      ) {
        this.$buefy.toast.open({
          message: "Podano niepoprawny E-mail",
          type: "is-danger",
        });
      } else if (this.members.includes(this.addEmail)) {
        this.$buefy.toast.open({
          message: "Podany E-mail już znajduje się na liście",
          type: "is-danger",
        });
      } else {
        this.members.push({ person: this.addEmail, role: this.addRole });
      }
      this.addEmail = "";
    },

    showAboutUs() {
      this.selectedTabTitle = "O Nas";
    },
    showWhatWeDo() {
      this.selectedTabTitle = "Czym się zajmujemy";
    },
    showMembers() {
      this.selectedTabTitle = "Członkowie";
    },
    showContact() {
      this.selectedTabTitle = "Kontakt";
    },

    changeGroupName() {
      this.editGroupName = !this.editGroupName;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    changeGroupCategory() {
      this.editGroupCategory = !this.editGroupCategory;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveGroupName() {
      if (this.groupName === "") {
        this.invalidGroupName = "Podaj nazwę koła";
      }
      // if nazwa koła już istnieje w bazie ...
      else {
        this.updateGroupInfo();
        this.changeGroupName();
      }
    },
    saveGroupCategory() {
      this.updateGroupInfo();
      this.changeGroupCategory();
    },
    cancelGroupName() {
      this.groupName = this.researchGroup.name;
      this.changeGroupName();
    },
    cancelGroupCategory() {
      this.groupCategory = this.researchGroup.category;
      this.changeGroupCategory();
    },

    changeWhatWeDo() {
      this.editWhatWeDo = !this.editWhatWeDo;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveWhatWeDo() {
      this.updateGroupInfo();
      this.changeWhatWeDo();
    },
    cancelWhatWeDo() {
      this.whatWeDo = this.researchGroup.what_we_do;
      this.changeWhatWeDo();
    },
    changeMembers() {
      this.editMembers = !this.editMembers;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveMembers() {
      this.updateGroupInfo();
      this.changeMembers();
    },
    cancelMembers() {
      this.getResearchGroupMembers(this.$route.params.id).then((response) => {
        this.members = response.members;
      });
      this.changeMembers();
    },
    changeAboutUs() {
      this.editAboutUs = !this.editAboutUs;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveAboutUs() {
      if (this.aboutUs === "") {
        this.aboutUsGiven = "Wypełnij sekcję o nas";
      } else {
        this.updateGroupInfo();
        this.changeAboutUs();
      }
    },
    cancelAboutUs() {
      this.aboutUs = this.researchGroup.about_us;
      this.changeAboutUs();
    },
    changeContact() {
      this.editContact = !this.editContact;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveContact() {
      this.updateGroupInfo();
      this.changeContact();
    },
    cancelContact() {
      this.contact = this.researchGroup.contact;
      this.changeContact();
    },
    changeToPanelMode() {
      this.isBeingEdited = false;
    },
    changeToEditMode() {
      this.isBeingEdited = true;
    },
  },

  watch: {
    $route() {
      this.loading = true;
      this.isBeingEdited = false;
      this.getResearchGroup(this.$route.params.id)
        .then(
          () => (
            (this.groupName = this.researchGroup.name),
            (this.groupCategory = this.researchGroup.category),
            (this.whatWeDo = this.researchGroup.what_we_do),
            (this.aboutUs = this.researchGroup.about_us),
            (this.contact = this.researchGroup.contact)
          )
        )
        .then(() => {
          this.getResearchGroupMembers(this.researchGroup.id).then(
            () => (this.members = this.researchGroupMembers)
          );
        })
        .then(() => {
          this.loading = false;
        });
    },
  },

  computed: {
    ...mapState({
      researchGroup: (state) => state.researchGroup.researchGroup,
    }),
    ...mapState({
      researchGroupMembers: (state) =>
        state.researchGroupMember.researchGroupMembers,
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

.container {
  margin: 0 auto;
}

.title {
  /* padding-bottom: 8px; 
  text-decoration: none; */
  /* padding-left: 50px; */
  text-align: center;
  /* color: #333;
  font-size: 2.15rem;
  font-weight: 650; 
  line-height: 1.125; */
}

#title {
  line-height: 1.6;
  margin-bottom: 0px;
}

.p-category {
  padding: 7px;
  /* padding-left: 50px; */
  text-align: center;
  font-size: 16px;
  color: grey;
}

#btn {
  position: relative;
  justify-content: center;
  margin-bottom: 8px;
  width: 100%;
  justify-content: left;
  color: black;
  background-color: rgb(165, 232, 163);
}

#menu {
  padding: 10px;
}

#divLinks {
  height: 100%;
  right: 0;
  width: 20%;
  min-width: 100px;
  background-color: rgb(203, 203, 203);
}

#centerDiv {
  margin-right: 15px;
  margin-left: 15px;
  height: 68vh;
  /* border: 5px solid rgb(203, 203, 203); */
}

.btn-email {
  width: 50%;
  background-color: #7957d5;
  border-color: transparent;
  font-weight: bold;
  color: white;
  transition: 0.3s;
}

.btn-email:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
}

.div-email {
  display: flex;
  justify-content: center;
}

/* #col {
  display: flex;
  justify-content: center;
  align-items: center;
} */

.div-title {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

#btnPencil {
  background: transparent;
  border: none;
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

#btnSave {
  margin: 10px;
  /* display: flex;
  width: 100%;
  background-color: #7957d5;
  border-color: transparent;
  font-weight: bold;
  color: white;
  transition: 0.3s; */
}

/* #btnSave:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
} */

#btnsDiv {
  display: flex;
  justify-content: center;
  align-items: center;
}

#editableText {
  height: 54vh;
  /* width: 800px !important; */
}

.centerDivHeader {
  padding-left: 10px;
  padding-bottom: 10px;
  font-size: 1.5rem !important;
  line-height: 1.2;
}

.container-send-email {
  display: flex;
  margin-top: 20px;
  text-align: center;
  justify-content: center;
}

#btnSendEmail {
  display: flex;
  width: 50%;
  font-size: 20px;
  background-color: #7957d5;
  border-color: transparent;
  font-weight: bold;
  color: white;
  transition: 0.3s;
}

#btnSendEmail:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
}

.outer {
  height: 100%;
}

.inner {
  height: 93%;
  width: 100%;
  overflow: auto;
  font-size: 1.25rem;
}

#col {
  display: flex;
  justify-content: center;
  align-items: center;
}

@media screen and (min-width: 1408px) {
  .container:not(.is-max-desktop):not(.is-max-widescreen) {
    max-width: 6644px !important;
  }
}
</style>




