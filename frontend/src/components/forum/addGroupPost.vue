<template>

  <transition name="modal">
    <div class="modal__wrapper" @click="$emit('close')">
      <div class="modal-content" @click.stop="">
        <div class="modal-header">
          <span class="modal-title"> Dodaj Wpis </span>
          <span class="button-close" @click="$emit('close')">×</span>
        </div>
        <div>
          <form class="form">
            <b-field label="Tytuł:"></b-field>
            <b-input v-on:focus="isTitleValid = true" v-model="title"></b-input>
            <b-field
                :message="!isTitleValid ? 'Proszę podać tytuł' : '\b'"
                :type="!isTitleValid ? 'is-danger' : ''"/>
            <b-field label="Treść:"></b-field>
            <b-input v-on:focus="isTextValid = true" v-model="text" type="textarea"></b-input>
            <b-field
                :message="!isTextValid ? 'Proszę podać treść' : '\b'"
                :type="!isTextValid ? 'is-danger' : ''"/>
            <b-button class="mt-4" type="is-primary" expanded v-on:click="savePost">Dodaj wpis</b-button>
          </form>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "addGroupPost",
  data() {
    return {
      title: "",
      text: "",
      isTitleValid: true,
      isTextValid: true,
    };
  },
  mounted() {
    document.body.addEventListener('keyup', e => {
      if (e.key === 'Escape') this.$emit('close')
    })
  },
  computed: {
    ...mapGetters("auth", ["authUser"]),
  },
  methods:
      {
        ...mapActions("researchGroupPost", ["addForumPost"]),
        savePost() {
          if (this.title === "") this.isTitleValid = false;
          if (this.text === "") this.isTextValid = false;
          if (this.isTitleValid && this.isTextValid && this.authUser.id) {
            this.addForumPost({
              title: this.title,
              text: this.text,
              author: this.authUser.id,
              research_group: this.$route.params.groupId,
            })
                .then((data) => {
                  this.$buefy.toast.open({
                    message: "Pomyślnie dodano post",
                    type: "is-success",
                  });
                  this.$router.push({name: 'groupPost', params: {groupId: data.research_group, postId: data.id}});
                })
                .catch((err) => {
                  // if(err.response.status === 403){
                  //   refreshToken()
                  //   this.savePost()
                  // }
                  this.$buefy.toast.open({
                    message:
                        "Błąd przy dodawaniu posta (" +
                        (err.response ? err.response.status : 500) +
                        ")",
                    type: "is-danger",
                  });
                });
          }
        },
      },
}
</script>

<style scoped>

</style>