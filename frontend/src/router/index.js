import Vue from 'vue';
import Router from 'vue-router';
import HomeView from '@/views/HomeView.vue';

import Notification from '@/views/NotificationView.vue';
import Production from '@/views/ProductionView.vue';
import Publications from '@/views/PublicationView.vue';
import Aboutus from '@/views/AboutusView.vue';
import NotFound from '@/components/NotFound.vue'; // 404页面组件
import SinglePublication from '@/views/SinglePublication.vue'; // 404页面组件
// 确保引入了所有需要的Vue组件

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path:"/test",
      name:"SinglePublication",
      component:SinglePublication,
      props:true
    },
    {
      path: '/',
      name: "Root",
      redirect: '/home',
    },
    {
      path: '/home',
      name: 'Home',
      component: HomeView,
    },
    {
      path: '/notifications',
      name: 'Dashboard',
      component: Notification,
    },
    {
      path: '/publications',
      name: 'Publication',
      component: Publications,
      children:[
        {
          path: '/singlepublication', 
          name: 'SinglePublication', 
          component: SinglePublication, 
          props:true
        },
      ]
    },
    {
      path: '/productions',
      name: 'Production',
      component: Production,
    },
    {
      path: '/aboutus',
      name: 'Aboutus',
      component: Aboutus,
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound // 捕获所有未定义的路由
    }
  ]
});

// 全局前置守卫
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

// 全局后置钩子
router.afterEach((to, from) => {
  console.log(to,from)
});

export default router;