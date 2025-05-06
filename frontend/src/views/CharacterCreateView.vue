<!-- frontend/src/views/CharacterCreateView.vue -->
<template>
  <div class="create-container">
    <!-- 왼쪽: 캐릭터 입력 폼 -->
    <CharacterForm
      v-model:name="characterName"
      v-model:description="characterDesc"
      v-model:systemPrompt="systemPrompt"
    />

    <!-- 오른쪽: Claude 응답 미리보기 -->
    <ChatPreview :system-prompt="systemPrompt" />

    <!-- 하단: 저장 버튼 -->
    <div class="save-button-area">
      <button @click="saveCharacter">저장</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CharacterForm from '@/components/CharacterForm.vue'
import ChatPreview from '@/components/ChatPreview.vue'

const characterName = ref('')
const characterDesc = ref('')
const systemPrompt = ref('')

function saveCharacter() {
  console.log('✅ 캐릭터 저장됨:', {
    name: characterName.value,
    desc: characterDesc.value,
    prompt: systemPrompt.value,
  })
  alert('캐릭터가 저장되었습니다!')
}
</script>
