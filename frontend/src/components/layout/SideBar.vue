<template>
  <b-menu :activable="false" :accordion="false">
    <b-menu-list>
      <b-menu-item label="Koła naukowe">
        <b-menu-item
          label="Koło 1"
          tag="router-link"
          to="/group/1000"
        ></b-menu-item>
        <b-menu-item label="Koło 2"></b-menu-item>
      </b-menu-item>
      <b-menu-item label="Projekty">
        <b-menu-item label="Projekt 1"></b-menu-item>
        <b-menu-item label="Projekt 2"></b-menu-item>
      </b-menu-item>
    </b-menu-list>
  </b-menu>
</template>

<script>
export default {
  name: "SideBar",
};
</script>

<style>
.menu {
  padding-top: 10px;
  padding-left: 10px;
  padding-right: 10px;
  height: 100%;
}
</style>
