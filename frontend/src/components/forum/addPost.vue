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
            <b-input v-model="title"></b-input>
            <b-field label="Treść:"></b-field>
            <b-input v-model="text" type="textarea"></b-input>
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
  name: "addPost",
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

          if (this.title !== "" && this.text !== "" && this.authUser.id) {
            this.addForumPost( {
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

                  this.$router.push("/post/" + data.id);
                })
                .catch((err) => {
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
  data() {
    return {
      title: "",
      text: "",
    };
  },
}
</script>

<style scoped>

</style>