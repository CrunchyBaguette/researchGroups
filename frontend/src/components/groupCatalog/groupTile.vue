<template>
  <div id="group-tile">{{ groupName }}</div>
</template>

<script>
export default {
  name: "groupCatalog",

  props: {
    groupName: { type: String },
  },
};
</script>

<style>
#group-tile {
  border-radius: 25px;
  background-color: yellow;
  color: blue;
  border: 5px solid black;
  width: 500px;
  height: 150px;
  text-align: center;
}
</style>