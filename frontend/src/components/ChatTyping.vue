<!-- frontend/src/components/ChatTyping.vue -->
<template>
    <div class="chat-typing" v-html="renderedText"></div>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue'
  import { marked } from 'marked'
  
  const props = defineProps({
    text: {
      type: String,
      required: true,
    },
  })
  
  const renderedText = ref('')
  let index = 0
  let intervalId = null
  
  function startTypingEffect(input) {
    renderedText.value = ''
    index = 0
    clearInterval(intervalId)
  
    intervalId = setInterval(() => {
      if (index <= input.length) {
        renderedText.value = marked.parse(input.slice(0, index))
        index++
      } else {
        clearInterval(intervalId)
      }
    }, 20) // 타이핑 속도 (ms)
  }
  
  watch(
    () => props.text,
    (newVal) => {
      if (newVal) startTypingEffect(newVal)
    },
    { immediate: true }
  )
  </script>
  
  <style scoped>
  .chat-typing {
    white-space: pre-wrap;
    line-height: 1.6;
  }
  </style>
  