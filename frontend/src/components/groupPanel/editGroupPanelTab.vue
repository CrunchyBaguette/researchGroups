<template>
    <div class="outer">
        <div class="div-title">
            <h2 class="centerDivHeader">{{ title }}</h2>
            <div id="col">
                <b-button class="btn-edit" id="btnEditGroupTab"></b-button>
            </div>
        </div>
        <div class="inner">
            {{ content }}
        </div>
    </div>
</template>
  
<script>
export default {
    name: "editGroupPanelTab",
    props: {
        title: {type: String},
        content: {type: String} 
    }
};
</script>

<style>
.centerDivHeader {
  padding: 10px;
  font-size: 1.5rem !important;
  line-height: 1.2;
  text-align: center;
}

.outer {
    height: 100%;
}

.inner {
    height: 93%; 
    width: 100%; 
    overflow: auto;
    font-size: 20px;
}

#col {
    display: flex;
    justify-content: center;
    align-items: center;
}

.btn-edit {
    background-repeat: no-repeat;
}

#btnEditGroupTab {
    /* background-size: cover; */
    height: 30px;
    background-position: 50%;
    background-image: url("../../assets/edit-7.jpg");
}

.div-title {
    display: flex; 
    flex-direction: row; 
    justify-content: center;
}
</style>