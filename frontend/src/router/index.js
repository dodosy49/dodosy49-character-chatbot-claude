// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'

// 👇 우리가 실제 사용할 View 컴포넌트
import MainMenuView from '../views/MainMenuView.vue'
import ChatView from '../views/ChatView.vue'
import CharacterSelectView from '../views/CharacterSelectView.vue'
import CharacterCreateView from '../views/CharacterCreateView.vue'

const routes = [
  { path: '/', component: MainMenuView },
  { path: '/chat', component: ChatView },
  { path: '/character-select', component: CharacterSelectView },
  { path: '/character-create', component: CharacterCreateView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
