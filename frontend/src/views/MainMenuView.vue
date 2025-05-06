<!-- MainMenuView.vue -->
<template>
  <div class="main-menu">
    <h1>⸜(*º𓂍º*)⸝DODOSY 캐릭터 챗봇에 오신 걸 환영해⸜(*º𓂍º*)⸝</h1>

    <ul>
      <li><router-link to="/chat"><button>💬 기본 채팅하기</button></router-link></li>
      <li><router-link to="/character-create"><button>🛠️ 캐릭터챗 만들기</button></router-link></li>
      <li><router-link to="/character-select"><button>🎭 캐릭터챗 대화하기</button></router-link></li>
    </ul>
  </div>
</template>

<script setup>
// 별도 스크립트 없음
</script>

<style scoped>
.main-menu {
  text-align: center;
  margin-top: 80px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin: 12px 0;
}

button {
  padding: 12px 20px;
  font-size: 18px;
  border-radius: 8px;
  border: none;
  background-color: #f5f5f5;
  cursor: pointer;
  transition: 0.3s;
}

button:hover {
  background-color: #d8eaff;
}
</style>
