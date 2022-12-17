  <template>
  <div id="root-container" class="box">
    <div class="container">
      <div class="author-category-container">
        <p class="author">
          {{ author }} <span id="spanGroup">(koło: </span> {{ group
          }}<span id="spanGroup">)</span>
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
      <div style="margin-bottom: 5px">
        <p class="title">{{ title }}</p>
      </div>
      <div class="box content-container" v-if="$route.name == 'announcement'">
        <p class="content">
          <markdown-it-vue
            class="md-body"
            :content="content"
            :options="markdownOptions"
          />
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
    group: { type: String },
    added: { type: String },
    edited: { type: String },
    title: { type: String },
    category: { type: String },
    content: { type: String },
  },

  data() {
    return {
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
};
</script>
  
  <style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
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

#spanGroup {
  font-size: 20px;
  font-weight: normal;
}
</style>