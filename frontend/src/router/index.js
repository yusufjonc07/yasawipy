import { createRouter, createWebHistory } from 'vue-router'
import ListUser from "../views/UserView/ListUser.vue"
import ListProduct from "../views/ProductView/ListProduct.vue"
import ListCustomer from "../views/CustomerView/ListCustomer.vue"


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/user:',
      component: ListUser,
    },
    {
      path: '/product:',
      component: ListProduct,
    },
    {
      path: '/customer:',
      component: ListCustomer,
    },
  ]
})

export default router
        