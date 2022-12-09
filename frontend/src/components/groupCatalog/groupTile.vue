<template>
  <div id="group-tile" class="box">
    <div class="groupTileContainer">
      <div class="groupTileTitleContainer">
        <p class="groupTileTitle">{{ group.name }}</p>
        <p class="groupTileCategory">{{ group.category }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "groupTile",

  props: {
    group: { type: Object },
  },
};
</script>

<style>
#group-tile {
  background-color: rgb(196, 196, 196);
  color: black;
  width: 100%;
  height: 150px;
  text-align: center;
}

.groupTileContainer {
  width: auto;
  height: 85%;
}

.groupTileTitleContainer {
  width: 100%;
  height: 30%;
}

.groupTileTitle {
  float: left;
  text-align: left;
  padding-left: 5px;
  font-weight: bold;
  font-size: 25px;
  width: fit-content;
}

.groupTileCategory {
  color: rgb(139, 139, 139);
  padding-right: 5px;
  text-align: right;
  font-weight: bold;
  font-size: 25px;
  width: fit-content;
  float: right;
}

.groupTileDescContainer {
  width: 100%;
  height: 70%;
  overflow: hidden;
}

.groupTileDesc {
  height: 80%;
  overflow: hidden;
  text-align: left;
  padding: 5px;
}
</style>