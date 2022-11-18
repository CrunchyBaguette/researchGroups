<template>
  <div id="group-tile">
    <div class="groupTileContainer">
      <div class="groupTileTitleContainer">
        <p class="groupTileTitle">{{ group.name }}</p>
        <p class="groupTileCategory">{{ group.category }}</p>
      </div>
      <div class="groupTileDescContainer">
        <p class="groupTileDesc">
          {{ group.description }}
        </p>
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
  border-radius: 25px;
  background-color: rgb(196, 196, 196);
  color: black;
  border: 5px solid black;
  width: 100%;
  height: 150px;
  text-align: center;
}

.groupTileContainer {
  width: auto;
  height: 85%;
  margin: 10px;
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
  text-align: left;
  padding: 5px;
}
</style>