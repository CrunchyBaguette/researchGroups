<template>
  <div class="card mx-4 pb-2;">
    <div class="px-5">
      <div class="columns m-0">
        <div class="column is-4 p-1" style="display: flex; flex-flow: column">
          <p>
            <b>{{ post.author.first_name }} {{ post.author.last_name }}</b>
          </p>
          <p>
            Utworzone:
            {{ new Date(post.added) | dateFormat("DD.MM.YYYY HH:mm") }}
          </p>
          <p>
            Edytowane:
            {{ new Date(post.edited) | dateFormat("DD.MM.YYYY HH:mm") }}
          </p>
        </div>
      </div>
      <div class="postText">
        <p class="title" style="margin-bottom: 15px">
          {{ post.title }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Post",
  props: {
    post: { type: Object },
  },
};
</script>

<style scoped>
* {
  max-height: 170px;
  overflow: hidden;
  white-space: nowrap;
  text-after-overflow: ellipsis " [..]";
}

.postText {
  margin-top: 10px;
  white-space: pre-line;
}
</style>