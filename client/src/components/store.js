// store.js
import { reactive } from 'vue'

export const store = reactive({
  username: 'username22',
  password: 'pass22word',
  login(username,password) {
    this.username = username;
    this.password = password;
  },
  logout() {
    this.username = null;
    this.password = null;
  }
})
