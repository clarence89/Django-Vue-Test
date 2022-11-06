<template>
    <LoginView v-if="view == 1"  @view="getView"/>
    <RegisterView v-else-if="view == 0"  @view="getView"/>
</template>

<script>

import { store } from './store.js'
import LoginView from './LoginView.vue'
import RegisterView from './RegisterView.vue'
export default {
  components: { LoginView, RegisterView },
  name: 'AppContainer',
  props: {
    msg: String
  },
  data() {
    return {
      store,
      view: 0,
      title: '',
    }
  },
  mounted() {
    this.setTitle()
  },
  methods: {
    getView(value){
      this.view = value
      this.setTitle()
    },
    setTitle(){
      if(this.view == 0){
        this.titled = "Login"
      }else{
        this.titled = "Register"
      }
      document.title = this.titled
    },
    getOne(){

    },
    deleteOne(){

    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
