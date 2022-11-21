<template>
    <div class="outer">
        
        <div class="div-title">
            <h2 class="centerDivHeader">{{ title }}</h2>
            <div id="col">
                <b-button id="btnPencil">
                    <mdicon name="lead-pencil"/>
                </b-button>
            </div>
        </div>
        <div class="inner">
            {{ content }}
            <div class="container-send-email">  
                <button class="button" id="btnSendEmail" @click="popupEmail = !popupEmail">WYŚLIJ WIADOMOŚĆ</button>
                
                <popupEmail 
                    v-if="popupEmail"
                    @close="popupEmail = false"/>
            </div>
        </div>
    </div>
</template>
  
<script>
import popupEmail from '@/components/popup/PopupEmail.vue'

export default {
name: "editGroupPanelTabContact",
props: {
    title: {type: String},
    content: {type: String} 
},
components: {
    popupEmail,
},
data() {
    return {
        popupEmail: false,
    }
},
};
</script>

<style>
.centerDivHeader {
  padding-left: 10px;
  padding-bottom: 10px;
  font-size: 1.5rem !important;
  line-height: 1.2;
}

.container-send-email {
    display: flex;
    margin-top: 20px;
    text-align: center;
    justify-content: center;
}


#btnSendEmail {
  display: flex;
  width: 50%;
  font-size: 20px;
  background-color: #7957d5;
  border-color: transparent;
  font-weight: bold;
  color: white;
  transition: .3s;
}

#btnSendEmail:hover {
  background-color: #7957d5;
  box-shadow: 0 0 5px #7957d5;
}

.outer {
    height: 100%;
}

.inner {
    height: 93%; 
    width: 100%; 
    overflow: auto;
}

#col {
    display: flex;
    justify-content: center;
    align-items: center;
}

.div-title {
    display: flex; 
    flex-direction: row; 
    justify-content: center;
}

#btnPencil {
    background: transparent;
    border: none;
}

</style>