  <template>
  <div id="root-container" style="height: fit-content" class="box">
    <div class="container">
      <div class="author-category-container">
        <p class="author">
          {{ author }}
        </p>
        <p class="category">{{ category }}</p>
      </div>
      <div class="date-container">
        <p class="added" id="da">
          Utworzone: {{ new Date(added) | dateFormat("DD.MM.YYYY HH:mm") }}
        </p>
        <p class="edited" id="da">
          Edytowane: {{ new Date(edited) | dateFormat("DD.MM.YYYY HH:mm") }}
        </p>
      </div>
      <div class="title-container">
        <p class="title">
          <b-icon style="margin-right: 10px" icon="wrench" v-if="draft" />
          {{ title }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "announcement",
  props: {
    author: { type: String },
    title: { type: String },
    added: { type: String },
    edited: { type: String },
    category: { type: String },
    draft: { type: Boolean },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

#root-container {
  /* margin: 20px; */
  /* width: 97%; */
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
}

.author {
  padding-left: 5px;
  font-weight: bold;
  font-size: 20px;
}

.category {
  padding-right: 5px;
  color: rgb(139, 139, 139);
  font-weight: bold;
  font-size: 20px;
}

.added .edited {
  padding-left: 5px;
}

.content-container {
  width: 100%;
  height: 70%;
  overflow: hidden;
}

.content {
  padding: 5px;
}

#da {
  color: grey;
}
</style>