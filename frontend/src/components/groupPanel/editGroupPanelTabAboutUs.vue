<template>
    <div class="outer">
        <div class="div-title">
            <h2 class="centerDivHeader">{{ title }}</h2>
            <div id="col">
                <b-button
                    id="btnPencil"
                    @click="changeTabContent"
                    v-if="!editTabContent">
                    <mdicon name="lead-pencil"/>
                </b-button>
            </div>
        </div>
        <div class="inner" v-if="!editTabContent">
            {{ content }}
        </div>
        <div v-else>
            <b-field
                  :message="aboutUsGiven"
                  :type="aboutUsGiven ? 'is-danger' : ''"
                >
                <b-input
                    @focus="aboutUsGiven = ''"
                    placeholder="Wypełnij sekcję o nas"
                    id="editableText" 
                    type="textarea"
                    size="is-medium"
                    :value="changingContent"
                  ></b-input>
            
            <div id="btnsDiv">
                <p class="control"> <!-- sprawdzić styl potem -->
                    <b-button
                    id="btnSave"
                    class="button is-primary is-success"
                    @click="saveTabContent"
                    >Zapisz</b-button
                    >
                </p>
                <b-button>Anuluj</b-button>
            </div>
        </b-field>
            <!-- <b-field>
                <b-input
                    id="editableText" 
                    type="textarea"
                    size="is-medium"
                    :value="changingContent">
                </b-input>
            </b-field>
            <div id="btnsDiv">
                <p class="control"> sprawdzić styl potem
                    <b-button
                      id="btnSave"
                      class="button is-primary is-success"
                      @click="saveTabContent"
                      >Zapisz</b-button
                    >
                </p>
                <b-button>Anuluj</b-button>
            </div> -->
        </div>
    </div>
</template>
  
<script>
export default {
    name: "editGroupPanelTabAboutUs",
    props: {
        title: {type: String},
        content: {type: String},
        changingContent: {type: String}, 
    },
    data() {
        return {
            //beforeEditTabContent: '...', //przycisk anuluj
            //changingContent: this.tabContent,
            editTabContent: false,
            aboutUsGiven: "",
        }
    },
    methods: {
        changeTabContent() {
            this.editTabContent = !this.editTabContent;
        },
        saveTabContent() {
            if (this.changingContent === "") {
                this.aboutUsGiven = "Wypełnij sekcję o nas";
                console.log('cos')
            }
            else {
                this.changeTabContent();
            }
        },    
    }, 
    
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

.div-title {
    display: flex; 
    flex-direction: row; 
    justify-content: center;
}

#btnPencil {
    background: transparent;
    border: none;
}

#btnsDiv {
    display: flex;
    justify-content: center;
    align-items: center;
}

#editableText {
    height: 560px;
}

</style>