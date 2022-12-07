<template>
  <div class="card m-4 pb-2">
    <div class="px-5">
      <div class="columns">
        <p class="column is-4 p-1">{{ post.author }}</p>
        <p class="column is-4 title">{{ post.title }}</p>
        <p class="column is-4"></p>
      </div>
      <p>{{ post.text }}</p>
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

</style>