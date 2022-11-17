<template>
    <div class="wrapper">
        <div class="wrapper-content">
            <section>
                <div class="container">
                    
                    <div class="modal__btn-list">
                        <button class="btn btnPrimary" @click="modalValidate = !modalValidate">Modal with form + validate</button>
                    </div>

                    <!-- Modal with validate -->
                    <modalValidate 
                        v-if="modalValidate"
                        @close="modalValidate = false"/>

                </div>
            </section>
        </div>
    </div>
</template>

<script>
import modal from '@/components/popup/Modal.vue'
import modalValidate from '@/components/popup/Popup.vue'

export default {
    components: {
        modal, modalValidate
    },
    data () {
        return {
            modalValidate: false,
        }
    },
}
</script>

<style>

.wrapper-content {
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