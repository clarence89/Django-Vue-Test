<template>

  <main class="form-signin text-center">
    <form>

      <h1 class="h3 mb-3 fw-normal">Contact Form</h1>

      <div class="form-floating mb-2">
        <input required v-model="email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
        <label for="floatingInput">Email address</label>
      </div>
      <div class="form-floating mb-2">
        <input required v-model="username" type="text" class="form-control" id="floatingInput" placeholder="Username">
        <label for="floatingInput">Username</label>
      </div>
      <div class="form-floating">
        <input minlength="8" required v-model="password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
        <label for="floatingPassword">Password</label>
      </div>
      <div required class="form-floating mb-1">
        <input minlength="8" v-model="password2" type="password" class="form-control" id="floatingConfirmPassword" placeholder="Confirm Password">
        <label for="floatingPassword">Confirm Password</label>
      </div>
      <div class="form-floating mb-1">
        <select v-model="colour" class="form-select" aria-label="Default select example">
          <option value="Blue">Blue</option>
          <option value="Green">Green</option>
          <option value="Red">Red</option>
          <option value="Black ">Black </option>
          <option value="Brown">Brown</option>
        </select>
      </div>
      <div class="form-floating mb-1">
        <select required v-model="animal" multiple class="form-select " style="height:20vh" aria-label="Default select example">
          <option v-for="animal1 in animals" v-bind:key="animal1.id" v-bind:value="animal1.url">{{ animal1.name }}</option>
        </select>
      </div>
      <div v-if="animal.includes(tigerurl.url)" class="form-floating">
        <input required v-model="tigertype" type="type_of_tiger" class="form-control" id="type_of_tiger" placeholder="Type of Tiger">
        <label for="type_of_tiger">Type of Tiger</label>
      </div>
      <button @click="Submit()" class="w-100 btn btn-lg btn-primary mt-5" type="submit">Register</button>
      <div @click="$emit('view', 1)" class="text-muted align-left mt-2">
        <p>Login</p>
      </div>
      <p class="mt-5 mb-3 text-muted">&copy; 2017–2021</p>
    </form>
  </main>
</template>

<script>

export default {
  name: 'RegisterView',
  data() {
    return {
      email: '',
      username: '',
      password: '',
      password2: '',
      colour: "Blue",
      animals: [],
      animal: [],
      tigerurl: '',
      tigertype: '',
    }
  },
  mounted() {
    this.getAnimals()
  },
  methods: {
    getAnimals() {
      this.axios.get('http://127.0.0.1:8000/models/animals/')
        .then(res => {
          this.animals = res.data;
          this.tigerurl = this.animals.find(animald => animald.name == 'Tiger' ? animald.url : '')
        })
    },
    warningSign() {
      this.$swal.fire(
        'Empty Fields Detected!',
        'Please fill up the empty Fields.',
        'warning'
      )
    },
    submitForm() {
      var data = new FormData();
      data.append('email', this.email);
      data.append('username', this.username);
      data.append('password', this.password);
      data.append('colour', this.colour);
      data.append('animals', this.animal);
      data.append('tiger_type', this.tigertype);
      this.axios.post("http://localhost:8000/models/users/", data)
        .then(res => {
          if (res.status == 201) {
            this.$swal.fire(
              'Success!',
              'Contact Info Submitted',
              'success'
            )
            this.email = ''
            this.username = ''
            this.password = ''
            this.colour = ''
            this.animal = []
            this.tigertype = ''
          } else {
            this.$swal.fire(
              'Denied!',
              'Please Contact Administrator',
              'danger'
            )
            this.email = ''
            this.username = ''
            this.password = ''
            this.colour = ''
            this.animal = []
            this.tigertype = ''
          }
        }).catch(e => console.log(e))
    },
    Submit() {
      if (this.email == '' || this.password == '' || this.password2 == '') {
        this.warningSign();
      } else {
        if (this.animal.includes("Tiger")) {
          if (this.tigertype == '') {
            console.log("tiger")
            this.warningSign();
          }
          else {
            if (this.password == this.password2) {
              if (this.password.length <= 8) {
                this.$swal.fire(
                  'Invalid Password!',
                  'Passwords should be 8+ Characters',
                  'warning'
                )
              } else {
                this.submitForm()
              }
            }
            else {
              this.$swal.fire(
                'Password Mismatch!',
                'Please provide matched Passwords',
                'warning'
              )
            }
          }
        }
        else {
          if (this.password == this.password2) {
            if (this.password.length <= 8) {
              this.$swal.fire(
                'Invalid Password!',
                'Passwords should be min of 8 and a max of 150 characters. Letters, digits and @/./+/-/_ only.',
                'warning'
              )
            } else {
              this.submitForm()
            }
          }
          else {
            this.$swal.fire(
              'Password Mismatch!',
              'Please provide matched Passwords',
              'warning'
            )
          }
        }
      }
    }
  },

}
</script>

<style>
html,
body {
  height: 100%;
}

body {
  display: flex;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
