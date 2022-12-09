<template>
  <div class="card mx-4 ">
    <div class="px-5">
      <div class="columns m-0">
        <p class="column is-4 p-1">{{ post.author.first_name }} {{post.author.last_name}}</p>
        <p class="column is-4 title mb-2">{{ post.title }}</p>
        <p class="column is-4"></p>
      </div>
      <div class="postText">{{ post.text }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Post",
  props: ["post"],

}
</script>

<style scoped>
* {
  max-height: 160px;
  overflow: hidden;
  white-space: nowrap;
  text-after-overflow: ellipsis " [..]";
}

.postText {
  white-space: pre-line;
}
</style>