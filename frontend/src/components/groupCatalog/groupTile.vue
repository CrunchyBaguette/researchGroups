<template>
  <div id="group-tile">
    <div class="groupTileContainer">
      <div class="groupTileTitleContainer">
        <p class="groupTileTitle">{{ groupName }}</p>
        <p class="groupTileCategory">Category</p>
      </div>
      <div class="groupTileDescContainer">
        <p class="groupTileDesc">
          DescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDescDesc
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "groupTile",

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