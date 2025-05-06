<!-- src/components/ChatPreview.vue -->
<template>
  <div class="chat-preview">
    <h3>🧠 Claude 미리보기</h3>
   
    <button @click="fetchPreview" class="preview-button">미리보기 요청</button>
    <p>{{ systemPrompt }}</p>
  </div>
</template>

<script setup>
defineProps({
  systemPrompt: String
})
</script>