<template>
  <div class="container" id="content" v-if="!this.loading">
    <div class="columns" style="width: 100%">
      <div class="column is-one-fifth"></div>
      <div class="column is-7" id="centerDivHead" style="margin-left: 15px">
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
              label="Nazwa projektu"
            >
              <b-input
                @focus="invalidProjectName = ''"
                v-model="projectName"
                placeholder="Podaj nazwę projektu"
                maxlength="120"
              ></b-input>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button-secondary"
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
              <b-icon icon="lead-pencil" />
            </b-button>
          </div>
        </div>

        <div class="div-title">
          <p class="p-category" v-if="!editProjectCategory || !isBeingEdited">
            {{ projectCategory }}
          </p>
          <div class="div-edit" v-else>
            <b-field label="Kategoria projektu">
              <b-select
                v-model="projectCategory"
                placeholder="Wybierz kategorię"
              >
                <option value="Matematyka">Matematyka</option>
                <option value="Medycyna">Medycyna</option>
                <option value="Chemia">Chemia</option>
              </b-select>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button-secondary"
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
              <b-icon icon="lead-pencil" />
            </b-button>
          </div>
        </div>
        <br />
      </div>
      <div class="column is-3" id="col" v-if="isBeingEdited">
        <div style="display: flex; flex-direction: column">
          <b-button
            id="title"
            class="button-secondary"
            rounded
            size="is-medium"
            @click="changeToPanelMode"
            :disabled="isButtonDisabled"
            ><b-icon icon="arrow-left" />&nbsp;&nbsp;Wróć do panelu
            projektu</b-button
          >
          <b-button
            id="title"
            rounded
            style="margin-top: 10px"
            size="is-medium"
            class="button-red"
            v-if="this.project.project_owner == this.authUser.email"
            @click="deleteProjectConfirmation"
            >Usuń projekt</b-button
          >
        </div>
      </div>
      <div class="column is-3" id="col" v-else>
        <b-button
          id="title"
          class="button-secondary"
          rounded
          size="is-medium"
          v-if="isAdminOrOwner()"
          @click="changeToEditMode"
          >Edytuj projekt</b-button
        >
      </div>
      <div class="columns"></div>
    </div>
    <div class="columns" style="width: 100%">
      <div class="box column is-one-fifth">
        <b-button
          id="btn"
          size="is-medium"
          tag="router-link"
          :to="{
            name: 'projectForum',
            params: { projectId: this.$route.params.id },
          }"
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
          v-on:click="showContact"
          :disabled="isButtonDisabled"
          >Kontakt</b-button
        >
      </div>
      <div class="box column is-7" id="centerDiv">
        <div class="outer" v-if="selectedTabTitle === 'Członkowie'">
          <div class="div-title">
            <h2 class="centerDivHeader">{{ selectedTabTitle }}</h2>
            <div id="btnsDiv">
              <b-button
                :disabled="isButtonDisabled"
                id="btnPencil"
                @click="changeMembers"
                v-if="!editMembers && isBeingEdited && isOwner()"
              >
                <b-icon icon="lead-pencil" />
              </b-button>
            </div>
          </div>
          <div class="inner">
            <div class="box member-list-box">
              <div
                class="box member-tile"
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
                      <b-button icon-right="menu-down" @click="pullUp">
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
              <div class="box member-tile" v-if="editMembers">
                <div style="flex: 0 1 50%">
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
                class="button-secondary"
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
                <b-icon icon="lead-pencil" />
              </b-button>
            </div>
          </div>
          <div class="box white inner" v-if="!editProjectDescription">
            <markdown-it-vue
              class="md-body"
              :content="projectDescription"
              :options="markdownOptions"
            />
          </div>
          <div v-else>
            <b-field :type="this.projectDescription ? '' : 'is-danger'">
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
                class="button-secondary"
                @click="saveProjectDescription"
                >Zapisz</b-button
              >
              <b-button @click="cancelProjectDescription">Anuluj</b-button>
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
                @click="changeProjectContact"
                v-if="!editProjectContact && isBeingEdited"
              >
                <b-icon icon="lead-pencil" />
              </b-button>
            </div>
          </div>
          <div class="box white inner" v-if="!editProjectContact">
            <markdown-it-vue
              class="md-body"
              :content="projectContact"
              :options="markdownOptions"
            />
            <div class="container-send-email">
              <b-button
                class="button-secondary"
                id="btnEmail"
                @click="popupEmail = !popupEmail"
              >
                WYŚLIJ WIADOMOŚĆ
              </b-button>
            </div>
          </div>
          <div v-else>
            <b-field>
              <b-input
                v-model="projectContact"
                id="editableText"
                type="textarea"
                size="is-medium"
              >
              </b-input>
            </b-field>
            <div id="btnsDiv">
              <b-button
                id="btnSave"
                class="button-secondary"
                @click="saveProjectContact"
                >Zapisz</b-button
              >
              <b-button @click="cancelProjectContact">Anuluj</b-button>
            </div>
          </div>
        </div>
      </div>

      <div class="box column is-3" id="divLinks">
        <b-menu :activable="false" :accordion="false" id="menu">
          <b-menu-list>
            <b-menu-item label="Linki" v-if="!isBeingEdited">
              <b-menu-item
                v-for="link in this.canAccessLinks(links)"
                :key="link.name"
                :label="link.name"
                :icon="link.is_public ? '' : 'lock'"
                target="_blank"
                :href="link.link"
              ></b-menu-item>
            </b-menu-item>
            <b-menu-item label="Linki" v-else>
              <b-menu-item
                v-for="link in links"
                :key="link.name"
                :label="link.name"
                :icon="link.is_public ? '' : 'lock'"
                @click="
                  openLinkModal(
                    `Edytuj link`,
                    `link`,
                    link.id,
                    link.name,
                    link.link,
                    link.is_public,
                    link.users
                  )
                "
              ></b-menu-item>
              <b-menu-item
                label="+"
                @click="openLinkModal(`Dodaj link`, `link`)"
              ></b-menu-item>
            </b-menu-item>
            <b-menu-item label="Dyski" v-if="!isBeingEdited">
              <b-menu-item
                v-for="disk in this.canAccessLinks(disks)"
                :key="disk.name"
                :label="disk.name"
                :icon="disk.is_public ? '' : 'lock'"
                target="_blank"
                :href="disk.link"
              ></b-menu-item>
            </b-menu-item>
            <b-menu-item label="Dyski" v-else>
              <b-menu-item
                v-for="disk in this.canAccessLinks(disks)"
                :key="disk.name"
                :label="disk.name"
                :icon="disk.is_public ? '' : 'lock'"
                @click="
                  openLinkModal(
                    `Edytuj dysk`,
                    `disk`,
                    disk.id,
                    disk.name,
                    disk.link,
                    disk.is_public,
                    disk.users
                  )
                "
              ></b-menu-item>
              <b-menu-item
                label="+"
                @click="openLinkModal(`Dodaj dysk`, `disk`)"
              ></b-menu-item>
            </b-menu-item>
          </b-menu-list>
        </b-menu>
      </div>
    </div>
    <b-modal has-modal-card :active.sync="this.editLink" trap-focus>
      <editLinkModal
        :message="this.modalMessage"
        :linkId="this.linkId"
        :linkTitle="this.linkTitle"
        :linkUrl="this.linkUrl"
        :linkPublic="this.linkPublic"
        :linkUsers="this.linkUsers"
        :linkType="this.linkType"
        v-on:save="updateLink"
        v-on:cancel="closeEditLinkModal"
        v-on:delete="deleteLink"
      />
    </b-modal>
    <popupEmail
      objectType="project"
      :object="this.project"
      v-if="popupEmail"
      @close="popupEmail = false"
    />
  </div>
</template>

<script>
import editLinkModal from "@/components/projectPanel/editLink.vue";
import popupEmail from "@/components/popup/PopupEmail.vue";
import { mapActions, mapState, mapGetters } from "vuex";

export default {
  name: "projectPanel",
  components: {
    editLinkModal,
    popupEmail,
  },
  data() {
    return {
      loading: true,
      addEmail: "",
      addRole: "Member",

      modalMessage: "",
      linkId: null,
      linkTitle: "",
      linkUrl: "",
      linkPublic: false,
      linkUsers: [],
      linkType: "",
      editLink: false,

      selectedTabTitle: "Opis projektu",

      // beforeEditGroupName: "Koło naukowe", //aktualna nazwa koła z bazy
      projectName: "",
      editProjectName: false,
      invalidProjectName: "",

      projectCategory: "",
      editProjectCategory: false,

      projectDescription: "",
      editProjectDescription: false,

      projectContact: "",
      editProjectContact: false,

      popupEmail: false,

      members: [],
      editMembers: false,

      links: [],
      disks: [],

      isBeingEdited: false,
      isButtonDisabled: false,

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
    document.title = "Edycja projektu";
    this.getProject(this.$route.params.id)
      .then(
        () => (
          (this.projectName = this.project.name),
          (this.projectCategory = this.project.category),
          (this.projectDescription = this.project.description),
          (this.projectContact = this.project.contact)
        )
      )
      .then(() => {
        this.getProjectMembers(this.project.id).then(
          () => (this.members = this.projectMembers)
        );
      })
      .then(() => {
        this.getProjectLinks({
          projectId: this.project.id,
        }).then(() => (this.links = this.projectLinks));
      })
      .then(() => {
        this.getProjectDisks({
          projectId: this.project.id,
        }).then(() => (this.disks = this.projectDisks));
      })
      .then(() => {
        this.loading = false;
      });
  },
  methods: {
    ...mapActions("project", ["getProject", "updateProject", "removeProject"]),
    ...mapActions("projectMember", [
      "getProjectMembers",
      "updateProjectMembers",
    ]),
    ...mapActions("projectLink", [
      "getProjectLinks",
      "addProjectLink",
      "deleteProjectLink",
      "updateProjectLink",
    ]),
    ...mapActions("projectDisk", [
      "getProjectDisks",
      "addProjectDisk",
      "deleteProjectDisk",
      "updateProjectDisk",
    ]),

    pullUp(event) {
      let divs = document.getElementsByClassName("member-tile");
      for (let i = 0; i < divs.length; i++) {
        divs[i].style.zIndex = -1;
      }
      event.target.closest(".member-tile").style.zIndex = 0;
    },

    canAccessLinks(links) {
      let canAccessLinks = [];
      for (let i = 0; i < links.length; i++) {
        if (links[i].is_public) {
          canAccessLinks.push(links[i]);
        } else if (
          this.isMember() ||
          (this.isAuthenticated && links[i].users.includes(this.authUser.email))
        ) {
          canAccessLinks.push(links[i]);
        }
      }
      return canAccessLinks;
    },

    openLinkModal(
      modalMessage,
      linkType,
      linkId = null,
      linkTitle = null,
      linkUrl = null,
      linkPublic = true,
      linkUsers = []
    ) {
      this.modalMessage = modalMessage;
      this.linkId = linkId;
      this.linkTitle = linkTitle;
      this.linkUrl = linkUrl;
      this.linkPublic = linkPublic;
      this.linkUsers = linkUsers;
      this.linkType = linkType;
      this.editLink = true;
    },

    openAddLinkModal() {
      this.editLink = true;
    },

    updateLinkInList(list, newTitle, newUrl, newPublic, newUsers) {
      for (let i = 0; i < list.length; i++) {
        if (list[i].id == this.linkId) {
          list[i].name = newTitle;
          list[i].link = newUrl;
          list[i].is_public = newPublic;
          list[i].users = newUsers;
          break;
        }
      }
    },

    addLinkToList(
      list,
      newId,
      newTitle,
      newUrl,
      newPublic,
      newUsers,
      newResearch_group
    ) {
      list.push({
        id: newId,
        name: newTitle,
        link: newUrl,
        is_public: newPublic,
        users: newUsers,
        research_group: newResearch_group,
      });
    },

    updateLink(event) {
      if (event["linkType"] == "link") {
        if (this.linkId != null) {
          this.updateProjectLink({
            linkId: this.linkId,
            projectId: this.$route.params.id,
            link: {
              name: event["newTitle"],
              link: event["newUrl"],
              is_public: event["newPublic"],
              users: event["newUsers"],
            },
          })
            .then(() => {
              this.updateLinkInList(
                this.links,
                event["newTitle"],
                event["newUrl"],
                event["newPublic"],
                event["newUsers"]
              );
              this.closeEditLinkModal();
            })
            .catch((err) => {
              this.$buefy.toast.open({
                message: err.response.data[Object.keys(err.response.data)[0]],
                type: "is-danger",
              });
            });
        } else {
          this.addProjectLink({
            projectId: this.$route.params.id,
            link: {
              name: event["newTitle"],
              link: event["newUrl"],
              is_public: event["newPublic"],
              users: event["newUsers"],
              project: this.$route.params.id,
            },
          })
            .then((response) => {
              this.addLinkToList(
                this.links,
                response["id"],
                response["name"],
                response["link"],
                response["is_public"],
                response["users"],
                response["project"]
              );
              this.closeEditLinkModal();
            })
            .catch((err) => {
              this.$buefy.toast.open({
                message: err.response.data[Object.keys(err.response.data)[0]],
                type: "is-danger",
              });
            });
        }
      } else {
        if (this.linkId != null) {
          this.updateProjectDisk({
            diskId: this.linkId,
            projectId: this.$route.params.id,
            disk: {
              name: event["newTitle"],
              link: event["newUrl"],
              is_public: event["newPublic"],
              users: event["newUsers"],
            },
          })
            .then(() => {
              this.updateLinkInList(
                this.disks,
                event["newTitle"],
                event["newUrl"],
                event["newPublic"],
                event["newUsers"]
              );
              this.closeEditLinkModal();
            })
            .catch((err) => {
              this.$buefy.toast.open({
                message: err.response.data[Object.keys(err.response.data)[0]],
                type: "is-danger",
              });
            });
        } else {
          this.addProjectDisk({
            projectId: this.$route.params.id,
            disk: {
              name: event["newTitle"],
              link: event["newUrl"],
              is_public: event["newPublic"],
              users: event["newUsers"],
              project: this.$route.params.id,
            },
          })
            .then((response) => {
              this.addLinkToList(
                this.disks,
                response["id"],
                response["name"],
                response["link"],
                response["is_public"],
                response["users"],
                response["project"]
              );
              this.closeEditLinkModal();
            })
            .catch((err) => {
              this.$buefy.toast.open({
                message: err.response.data[Object.keys(err.response.data)[0]],
                type: "is-danger",
              });
            });
        }
      }
    },

    deleteLink(event) {
      if (event["linkType"] == "link") {
        this.deleteProjectLink({
          projectId: this.$route.params.id,
          linkId: this.linkId,
        })
          .then(() => {
            for (let i = 0; i < this.links.length; i++) {
              if (this.links[i].id == this.linkId) {
                this.links.splice(i, 1);
                break;
              }
            }
            this.closeEditLinkModal();
          })
          .catch((err) => {
            this.$buefy.toast.open({
              message: err.response.data[Object.keys(err.response.data)[0]],
              type: "is-danger",
            });
          });
      } else {
        this.deleteProjectDisk({
          projectId: this.$route.params.id,
          diskId: this.linkId,
        })
          .then(() => {
            for (let i = 0; i < this.disks.length; i++) {
              if (this.disks[i].id == this.linkId) {
                this.disks.splice(i, 1);
                break;
              }
            }
            this.closeEditLinkModal();
          })
          .catch((err) => {
            this.$buefy.toast.open({
              message: err.response.data[Object.keys(err.response.data)[0]],
              type: "is-danger",
            });
          });
      }
    },

    closeEditLinkModal() {
      this.linkId = null;
      this.linkTitle = "";
      this.linkUrl = "";
      this.linkUsers = [];
      this.linkType = "";
      this.editLink = false;
    },

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
          this.projectMembers[i]["person"] == this.authUser.email
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

    isOwner() {
      if (
        this.isAuthenticated &&
        this.project.project_owner == this.authUser.email
      ) {
        return true;
      } else {
        return false;
      }
    },

    removeMemberFromList(email) {
      for (let i = 0; i < this.members.length; i++) {
        if (this.members[i].person == email) {
          this.members.splice(i, 1);
          break;
        }
      }
    },

    updateProjectInfo() {
      this.updateProject({
        id: this.$route.params.id,
        payload: {
          name: this.projectName,
          description: this.projectDescription,
          category: this.projectCategory,
          contact: this.projectContact,
        },
      })
        .then((response) => {
          this.projectName = response.name;
          this.projectCategory = response.category;
          this.projectDescription = response.description;
          this.projectContact = response.contact;
        })
        .catch((err) => {
          this.projectName = this.project.name;
          this.projectDescription = this.project.description;
          this.projectCategory = this.project.category;
          this.projectContact = this.project.contact;
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
    },

    deleteProjectConfirmation() {
      this.$buefy.dialog.confirm({
        title: "Usuwanie projektu",
        message:
          "<b>Czy na pewno chcesz usunąć projekt?</b></br>Wraz z projektem usunięte zostaną wpisy forum, linki oraz dyski",
        confirmText: "Usuń projekt",
        type: "is-danger",
        hasIcon: true,
        onConfirm: () => this.deleteProject(),
      });
    },

    deleteProject() {
      this.removeProject(this.$route.params.id)
        .then(() => {
          this.$router.push("/project-catalog");
          this.$buefy.toast.open({
            message: "Projekt został usunięty",
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
    showContact() {
      this.selectedTabTitle = "Kontakt";
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
      if (this.projectDescription != "") {
        this.updateProjectInfo();
        this.changeProjectDescription();
      }
    },
    cancelProjectDescription() {
      this.projectDescription = this.project.description;
      this.changeProjectDescription();
    },
    changeProjectContact() {
      this.editProjectContact = !this.editProjectContact;
      this.isButtonDisabled = !this.isButtonDisabled;
    },
    saveProjectContact() {
      this.updateProjectInfo();
      this.changeProjectContact();
    },
    cancelProjectContact() {
      this.projectContact = this.project.contact;
      this.changeProjectContact();
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
            (this.projectDescription = this.project.description),
            (this.projectContact = this.project.contact)
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
    members() {
      this.getProject(this.$route.params.id);
    },
  },

  computed: {
    ...mapState({
      project: (state) => state.project.project,
    }),
    ...mapState({
      projectMembers: (state) => state.projectMember.projectMembers,
    }),
    ...mapState({
      projectLinks: (state) => state.projectLink.projectLinks,
    }),
    ...mapState({
      projectDisks: (state) => state.projectDisk.projectDisks,
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
  background-color: var(--first-color);
  box-shadow: var(--second-color);
  filter: brightness(98%);
}

#btn:focus {
  border-color: var(--fourth-color);
}

#menu {
  padding: 10px;
}

#divLinks {
  height: 100%;
  right: 0;
  width: 20%;
  min-width: 100px;
  background-color: var(--first-color);
}

#centerDivHead {
  margin-right: 15px;
  margin-left: 15px;
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
  overflow: auto;
}

.inner {
  height: 93%;
  width: 100%;
  overflow: auto;
  font-size: 1.25rem;
}

#col {
  width: 20%;
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




