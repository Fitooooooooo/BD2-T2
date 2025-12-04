import EditUser from '@/views/EditUser.vue'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import CreateUser from '@/views/CreateUser.vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    { name: 'home', path: '/', component: Home },
    { name: 'login', path: '/login', component: Login },
    { name: 'userCreate', path: '/users/create', component: CreateUser },
    { name: 'userEdit', path: '/users/:id/edit/', component: EditUser },
]

export const router = createRouter({
    history: createWebHistory(),
    routes,
})
