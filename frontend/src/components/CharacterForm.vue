<!-- frontend/src/components/CharacterForm.vue -->
<template>
    <div class="form-container">
      <h2>🎭 캐릭터 설정</h2>
  
      <label for="name">이름</label>
      <input id="name" type="text" v-model="name" placeholder="예: 백도현, 시이나" />
  
      <label for="desc">설명</label>
      <textarea
        id="desc"
        rows="2"
        v-model="description"
        placeholder="캐릭터 소개 또는 배경설정"
      ></textarea>
  
      <label for="prompt">시스템 프롬프트</label>
      <textarea
        id="prompt"
        rows="10"
        v-model="systemPrompt"
        placeholder="캐릭터 성격, 말투, 대화 방식 등을 서술하세요."
      ></textarea>
    </div>
  </template>
  
  <script setup>
  const name = defineModel('name')
  const description = defineModel('description')
  const systemPrompt = defineModel('systemPrompt')
  </script>
  