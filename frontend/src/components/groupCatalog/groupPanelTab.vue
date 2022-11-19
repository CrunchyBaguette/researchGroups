<template>
    <div class="outer">
        <h2 class="centerDivHeader">{{ title }}</h2>
        <div class="inner">
            {{ content }}
        </div>
    </div>
</template>
  
<script>
export default {
name: "groupPanelTab",
props: {
    title: {type: String},
    content: {type: String} 
}
};
</script>

<style>
.centerDivHeader {
  padding-left: 10px;
  padding-bottom: 10px;
  font-size: 1.5rem !important;
  line-height: 1.2;
  
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

</style>