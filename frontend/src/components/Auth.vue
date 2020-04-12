<template>
  <div class="container">
    <button type="button"
            class="btn btn-dark btn-sm"
            @click="loginGithub"
            v-if="!isLogin">Login</button>
    <button type="button"
            class="btn btn-danger btn-sm"
            @click="logoutGithub"
            v-if="isLogin">Logout</button>
    <h1 v-if="isLogin">{{token}} </h1>
    <h1 v-if="isLogin">{{usertoken}}</h1>
    <h1 v-if="isLogin">{{username}}</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Auth',
  data() {
    return {
      token: null,
      usertoken: null,
      username: null,
      isLogin: false,
    };
  },
  methods: {
    loginGithub() {
      const clientID = '56839c6fc326cac8b67c';
      window.location.href = `https://github.com/login/oauth/authorize?client_id=${clientID}`;
    },
    logoutGithub() {
      localStorage.removeItem('usertoken');
      localStorage.removeItem('token');
      this.isLogin = false;
    },
    add_token() {
      const token = this.$route.query.code;
      if (token) {
        localStorage.token = token;
      }
    },
    login() {
      this.add_token();
      if (localStorage.token && localStorage.usertoken == null) {
        const path = `http://localhost:9999/authenticate/${localStorage.token}`;
        axios.get(path)
          .then((res) => {
            localStorage.usertoken = res.data.token;
            fetch('https://api.github.com/user', {
              headers: {
                // Include the token in the Authorization header
                Authorization: `token ${res.data.token}`,
              },
            }).then(result => result.json())
              .then((result) => {
                this.username = result.login;
                this.usertoken = localStorage.usertoken;
                this.isLogin = true;
              });
          });
      } else {
        fetch('https://api.github.com/user', {
          headers: {
            // Include the token in the Authorization header
            Authorization: `token ${localStorage.usertoken}`,
          },
        }).then(result => result.json())
          .then((result) => {
            this.username = result.login;
            this.usertoken = localStorage.usertoken;
            this.isLogin = true;
          });
      }
    },

  },
  mounted() {
    if (localStorage.token) {
      this.token = localStorage.token;
      this.isLogin = true;
    }
  },
  created() {
    this.login();
  },
};
</script>

<style scoped>

</style>
