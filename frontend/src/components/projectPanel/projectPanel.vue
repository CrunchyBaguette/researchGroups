<template>
  <div class="container" id="content" v-if="!this.loading">
    <div class="columns" style="width: 100%">
      <div class="column is-3"></div>
      <div class="column is-6">
        <div class="div-title">
          <h1
            class="title"
            id="title"
            v-if="!editProjectName || !isBeingEdited"
          >
            {{ projectName }}
          </h1>
          <div class="div-edit" v-else>
            <b-field
              :message="invalidProjectName"
              :type="invalidProjectName ? 'is-danger' : ''"
              label="Nazwa koła"
            >
              <b-input
                @focus="invalidProjectName = ''"
                v-model="projectName"
                placeholder="Podaj nazwę koła"
                maxlength="120"
              ></b-input>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button is-primary is-success"
                @click="saveProjectName"
                >Zapisz</b-button
              >
              <b-button @click="cancelProjectName">Anuluj</b-button>
            </div>
          </div>
          <div id="btnsDiv">
            <b-button
              :disabled="isButtonDisabled"
              id="btnPencil"
              @click="changeProjectName"
              v-if="!editProjectName && isBeingEdited"
            >
              <mdicon name="lead-pencil" />
            </b-button>
          </div>
        </div>

        <div class="div-title">
          <p class="p-category" v-if="!editProjectCategory || !isBeingEdited">
            {{ projectCategory }}
          </p>
          <div class="div-edit" v-else>
            <b-field label="Kategoria koła">
              <b-select
                v-model="projectCategory"
                placeholder="Wybierz kategorię"
              >
                <option value="Default">Default</option>
              </b-select>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button is-primary is-success"
                @click="saveProjectCategory"
                >Zapisz</b-button
              >
              <b-button @click="cancelProjectCategory">Anuluj</b-button>
            </div>
          </div>
          <div id="btnsDiv">
            <b-button
              :disabled="isButtonDisabled"
              id="btnPencil"
              @click="changeProjectCategory"
              v-if="!editProjectCategory && isBeingEdited"
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
          ><mdicon name="arrow-left" /> Wróć do panelu projektu</b-button
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
          >Edytuj projekt</b-button
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
          v-on:click="showProjectDescription"
          :disabled="isButtonDisabled"
          >Opis projektu</b-button
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
          tag="router-link"
          to="/project-tutorials"
          :disabled="isButtonDisabled"
          >Materiały dydaktyczne</b-button
        >
      </div>
      <div class="box column is-6" id="centerDiv">
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
                    <b-dropdown-item value="Owner" aria-role="listitem">
                      <span>Owner</span>
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
                    <b-dropdown-item value="Owner" aria-role="listitem">
                      <span>Owner</span>
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

        <div class="outer" v-if="selectedTabTitle === 'Opis projektu'">
          <div class="div-title">
            <h2 class="centerDivHeader">{{ selectedTabTitle }}</h2>
            <div id="btnsDiv">
              <b-button
                :disabled="isButtonDisabled"
                id="btnPencil"
                @click="changeProjectDescription"
                v-if="!editProjectDescription && isBeingEdited"
              >
                <mdicon name="lead-pencil" />
              </b-button>
            </div>
          </div>
          <div class="inner" v-if="!editProjectDescription">
            <markdown-it-vue
              class="md-body"
              :content="projectDescription"
              :options="markdownOptions"
            />
          </div>
          <div v-else>
            <b-field
              :message="projectDescriptionGiven"
              :type="projectDescriptionGiven ? 'is-danger' : ''"
            >
              <b-input
                @focus="projectDescriptionGiven = ''"
                v-model="projectDescription"
                id="editableText"
                type="textarea"
                size="is-medium"
              ></b-input>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button is-primary is-success"
                @click="saveDescription"
                >Zapisz</b-button
              >
              <b-button @click="cancelDescription">Anuluj</b-button>
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
import { mapActions, mapState, mapGetters } from "vuex";

export default {
  name: "projectPanel",
  data() {
    return {
      loading: true,
      addEmail: "",
      addRole: "Member",

      selectedTabTitle: "Opis projektu",

      // beforeEditGroupName: "Koło naukowe", //aktualna nazwa koła z bazy
      projectName: "",
      editProjectName: false,
      invalidProjectName: "",

      projectCategory: "",
      editProjectCategory: false,

      projectDescription: "",
      editProjectDescription: false,

      members: [],
      editMembers: false,

      isBeingEdited: false,
      isButtonDisabled: false,
    };
  },
  mounted() {
    document.title = "Edycja projektu";
    this.getProject(this.$route.params.id)
      .then(
        () => (
          (this.projectName = this.project.name),
          (this.projectCategory = this.project.category),
          (this.projectDescription = this.project.description)
        )
      )
      .then(() => {
        this.getProjectMembers(this.project.id).then(
          () => (this.members = this.projectMembers)
        );
      })
      .then(() => {
        this.loading = false;
      });
  },
  methods: {
    ...mapActions("project", ["getProject", "updateProject"]),
    ...mapActions("projectMember", [
      "getProjectMembers",
      "updateProjectMembers",
    ]),

    isMember() {
      if (this.isAuthenticated) {
        if (this.project.members.includes(this.authUser.email)) {
          return true;
        }
      }
      return false;
    },

    isAdminOrOwner() {
      for (var i = 0; i < this.projectMembers.length; i++) {
        if (
          this.isMember() &&
          this.researchGroupMembers[i]["person"] == this.authUser.email
        ) {
          if (
            this.projectMembers[i]["role"] == "Owner" ||
            this.projectMembers[i]["role"] == "Moderator"
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

    updateProjectInfo() {
      this.updateProject({
        id: this.$route.params.id,
        payload: {
          name: this.projectName,
          description: this.projectDescription,
          category: this.projectCategory,
        },
      }).catch((err) => {
        this.projectName = this.project.name;
        this.projectDescription = this.project.description;
        this.projectCategory = this.project.category;
        this.$buefy.toast.open({
          message: err.response.data[Object.keys(err.response.data)[0]],
          type: "is-danger",
        });
      });

      this.updateProjectMembers({
        projectId: this.$route.params.id,
        members: this.members,
      })
        .then((response) => {
          this.members = response.members;
        })
        .catch((err) => {
          this.getProjectMembers(this.$route.params.id).then((response) => {
            this.members = response.members;
          });
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

    showProjectDescription() {
      this.selectedTabTitle = "Opis projektu";
    },
    showMembers() {
      this.selectedTabTitle = "Członkowie";
    },

    changeProjectName() {
      this.editProjectName = !this.editProjectName;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    changeProjectCategory() {
      this.editProjectCategory = !this.editProjectCategory;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveProjectName() {
      if (this.projectName === "") {
        this.invalidProjectName = "Podaj nazwę Projektu";
      }
      // if nazwa koła już istnieje w bazie ...
      else {
        this.updateProjectInfo();
        this.changeProjectName();
      }
    },
    saveProjectCategory() {
      this.updateProjectInfo();
      this.changeProjectCategory();
    },
    cancelProjectName() {
      this.projectName = this.project.name;
      this.changeProjectName();
    },
    cancelProjectCategory() {
      this.projectCategory = this.project.category;
      this.changeProjectCategory();
    },
    changeMembers() {
      this.editMembers = !this.editMembers;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveMembers() {
      this.updateProjectInfo();
      this.changeMembers();
    },
    cancelMembers() {
      this.getProjectMembers(this.$route.params.id).then((response) => {
        this.members = response.members;
      });
      this.changeMembers();
    },
    changeProjectDescription() {
      this.editProjectDescription = !this.editProjectDescription;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveProjectDescription() {
      if (this.projectDescription === "") {
        this.projectDescriptionGiven = "Wypełnij sekcję o nas";
      } else {
        this.updateProjectInfo();
        this.changeProjectDescription();
      }
    },
    cancelProjectDescription() {
      this.projectDescription = this.project.description;
      this.changeProjectDescription();
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
      this.getProject(this.$route.params.id)
        .then(
          () => (
            (this.projectName = this.project.name),
            (this.projectCategory = this.project.category),
            (this.projectDescription = this.project.description)
          )
        )
        .then(() => {
          this.getProjectMembers(this.project.id).then(
            () => (this.members = this.projectMembers)
          );
        })
        .then(() => {
          this.loading = false;
        });
    },
  },

  computed: {
    ...mapState({
      project: (state) => state.project.project,
    }),
    ...mapState({
      projectMembers: (state) => state.projectMember.projectMembers,
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
  padding-left: 50px;
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
  padding-left: 50px;
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




