<template>
  <div>
    <form>
      <label for="title">Tytuł:</label>
      <b-input id="title" v-model="title"></b-input>
      <label for="text">Treść:</label>
      <b-input id="text" v-model="text"></b-input>
      <b-button v-on:click="savePost">Dodaj wpis</b-button>
    </form>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "addPost",
  methods:
      {
    ...mapActions("researchGroupPost", ["addForumPost"]),
        savePost() {
          // if (this.title == "") this.nameGiven = false;
          // if (this.text == "") this.categoryGiven = false;

          if (this.title && this.text) {
            this.addForumPost({
              title: this.title,
              text: this.text,
              author: 1,//todo
            })
                .then((data) => {
                  this.$buefy.toast.open({
                    message: "Pomyślnie dodano post",
                    type: "is-success",
                  });

                  this.$router.push("/post/"+data.id);
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