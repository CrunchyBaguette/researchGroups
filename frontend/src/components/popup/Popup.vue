<!-- <template>
    <div class="container">
      <h1 class="title">Wiadomość</h1>
    
      <br>
  
      <form @submit.prevent="submitForm">
        <b-field label="Email">
            <b-input type="email" v-model="email"
                maxlength="30"
                required>
            </b-input>
        </b-field>
  
        <b-field label="Tytuł">
            <b-input v-model="emailTitle"
                maxlength="60" 
                required>
            </b-input>
        </b-field>
  
        <b-field label="Treść">
            <b-input type="textarea" v-model="message"
                maxlength="600"
                required>
            </b-input>
        </b-field>
  
        <br>
        
        <button id="btnSendEmail" class="button">WYŚLIJ WIADOMOŚĆ</button>
      </form> 
  
    </div>
</template>
  
<script>
//import axios from 'axios'
//import { toast } from 'bulma-toast'

export default {
  name: "Popup",
  data() {
    return {
      email: '',
      emailTitle: '',
      message: '',
    }
  },
  methods: {
    submitForm() {

    }
  }
}

</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.container {
  margin: 0 auto;
  max-width: 320px;
}

.title {
  text-align: center;
}

#btnSendEmail {
  display: flex;
  width: 100%;
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

</style> -->

<!-- <script>
export default {
  name: "Popup",
  props: {
    show: Boolean
  },
  data() {
    return {
      email: '',
      emailTitle: '',
      message: '',
    }
  },
  methods: {
    submitForm() {

    }
  },
}
</script>

<template>
  <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">default header</slot>
          </div>

          <div class="modal-body">
            <slot name="body">default body</slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              default footer
              <button
                class="modal-default-button"
                @click="$emit('close')"
              >OK</button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style> -->


<template>
  <modal
      title="Wiadomość"
      @close="$emit('close')">
      <div slot="body">

        <!-- <form @submit.prevent="submitForm"> -->
        <form @submit.prevent="onSubmit">
          <b-field label="Email">
              <b-input type="email" v-model="email"
                  maxlength="30"
                  required>
              </b-input>
          </b-field>

          <b-field label="Tytuł">
              <b-input v-model="emailTitle"
                  maxlength="60" 
                  required>
              </b-input>
          </b-field>

          <b-field label="Treść">
              <b-input type="textarea" v-model="message"
                  maxlength="600"
                  required>
              </b-input>
          </b-field>

          <br>
          
          <button id="btnSendEmail" class="button">WYŚLIJ WIADOMOŚĆ</button>
        </form>
      </div>
  </modal>
</template>

<script>
import modal from '@/components/popup/Modal.vue'

export default {
  name: "Popup",
  components: {
    modal,
  },
  data () {
      return {
        email: '',
        emailTitle: '',
        message: '',
      }
  },
  methods: {
      onSubmit () {
          this.$v.$touch()
          if(!this.$v.$invalid) {
              const user = {
                  email: this.email,
                  emailTitle: this.emailTitle,
                  message: this.message,
              }
              console.log(user)

              //DONE
              this.email = ''
              this.emailTitle = ''
              this.message = ''
              this.$v.$reset()
              this.$emit('close')
          }
      }
  }
}
</script>

<style>
/* .title {
  line-height: .8;
  margin-bottom: 0px;
} */


</style>