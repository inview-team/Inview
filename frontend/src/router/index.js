import Vue from 'vue';
import Router from 'vue-router';
import Auth from '../components/Auth';
import Projects from '../components/Projects';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Auth,
    },
    {
      path: '/projects',
      name: 'Projects',
      component: Projects,
    },
  ],
  mode: 'history',
});
