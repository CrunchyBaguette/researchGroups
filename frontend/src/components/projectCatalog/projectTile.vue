<template>
  <div id="group-tile" class="box">
    <div class="groupTileContainer">
      <div class="groupTileTitleContainer">
        <p class="groupTileTitle">{{ project.name }}</p>
        <p class="groupTileCategory">{{ project.category }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "projectTile",

  props: {
    project: { type: Object },
  },
};
</script>

<style>
#group-tile {
  background-color: rgb(196, 196, 196);
  color: black;
  width: 100%;
  height: fit-content;
  min-height: 150px;
  text-align: center;
}

.groupTileContainer {
  width: auto;
  height: 85%;
}

.groupTileTitleContainer {
  display: flex;
  width: 100%;
  height: 30%;
}

.groupTileTitle {
  flex: 1;
  text-align: left;
  padding-left: 5px;
  font-weight: bold;
  font-size: 25px;
}

.groupTileCategory {
  color: rgb(139, 139, 139);
  padding-right: 5px;
  text-align: right;
  font-weight: bold;
  font-size: 25px;
  width: fit-content;
  margin-left: 10px;
  word-wrap: break-word;
  float: right;
}

.groupTileDescContainer {
  width: 100%;
  height: 70%;
  overflow: hidden;
}

.groupTileDesc {
  text-align: left;
  padding: 5px;
}
</style>