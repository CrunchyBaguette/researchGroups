<template>
    
    <div class="container">  
        <div class="modal__btn-list">
            <button class="btn btnPrimary" @click="modalValidate = !modalValidate">Wyślij wiadomość</button>
        </div>
        <modalValidate 
            v-if="modalValidate"
            @close="modalValidate = false"/>
    </div>
</template>

<script>
import modalValidate from '@/components/popup/Popup.vue'

export default {
    name: "App",
    components: {
        modalValidate
    },
    data () {
        return {
            modalValidate: false,
        }
    },
}
</script>

<style>

.container {
    padding-top: 80px;
}

.modal__btn-list {
    display: flex;
    justify-content: center;  
}

.modal__btn-list .btn {
    margin: 0 20px;
}
</style>