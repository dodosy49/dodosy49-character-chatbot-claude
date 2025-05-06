<template>
  <div class="chat-container">
    <div class="chat-box">
       <!-- 사용자 메시지만 출력 -->
       <div v-for="(msg, index) in messages" :key="index">
  <div
    v-if="msg.role === 'user'"
    class="user-message"
    v-html="renderMarkdown(msg.text)"
  ></div>
</div>

      <!-- Claude 응답 (타이핑 효과) -->
      <ChatTyping
        v-if="latestBotReply"
        :text="latestBotReply"
        class="bot-message"
        
      />
    </div>

    <div class="input-area">
      <textarea
        class="user-input"
        v-model="userInput"
        placeholder="메시지를 입력하세요 (Shift+Enter: 줄바꿈)"
        @keydown.enter.exact.prevent="sendMessage"
        @keydown.shift.enter.prevent
      ></textarea>
      <button class="send-btn" @click="sendMessage">전송</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { marked } from 'marked'
import ChatTyping from '@/components/ChatTyping.vue'


const userInput = ref('')
const messages = ref([])

const latestBotReply = computed(() => {
  const botMessages = messages.value.filter(msg => msg.role === 'bot')
  return botMessages.length ? botMessages[botMessages.length - 1].text : ''
})

function renderMarkdown(text) {
  return marked.parse(text || '')
}

async function sendMessage() {
  if (!userInput.value.trim()) return

  // 사용자 메시지 추가
  messages.value.push({ role: 'user', text: userInput.value })

  const inputText = userInput.value
  userInput.value = ''

  try {
    const res = await axios.post('http://localhost:5000/api/chat', {
      message: inputText,
    })

    messages.value.push({ role: 'bot', text: res.data.reply })
  } catch (err) {
    messages.value.push({ role: 'bot', text: `❗ 오류 발생: ${err.message}` })
  }
}
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  padding: 20px;
  font-family: sans-serif;
}

.chat-box {
  flex: 1;
  overflow-y: auto;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 10px;
}

.user-message {
  text-align: right;
  background: #eee;
  padding: 6px 10px;
  border-radius: 12px;
  margin: 5px 0;
  max-width: 75%;
  margin-left: auto;
}

.bot-message {
  text-align: left;
  background: #d8f1ff;
  padding: 6px 10px;
  border-radius: 12px;
  margin: 5px 0;
  max-width: 75%;
  margin-right: auto;
}

.input-area {
  display: flex;
  gap: 10px;
}

.textarea {
  flex: 1;
  height: 60px;
  resize: none;
  padding: 8px;
  font-size: 16px;
}

.button {
  width: 80px;
  font-size: 16px;
  background-color: #69c;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
</style>