import Vue from 'vue';
import Router from 'vue-router';
import Login from '@/components/LoginPage.vue';
import HomeView from '@/views/HomeView.vue';
import Dashboard from '@/components/DashboardPage.vue';
import NotFound from '@/components/NotFound.vue'; // 404页面组件

// 确保引入了所有需要的Vue组件

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: HomeView,
      meta: { requiresAuth: false } // 标记该路由需要认证
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: { requiresAuth: false } // 标记该路由不需要认证
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
      meta: { requiresAuth: true } // 标记该路由需要认证
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