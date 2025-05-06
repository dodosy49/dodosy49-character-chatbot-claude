
# Claude 기반 캐릭터 챗봇 (Vue + Flask 프로젝트)

> 비개발자가 Claude API를 활용해 직접 구축한 캐릭터 챗봇 SaaS 구조의 실험 프로젝트입니다.

---

## 📌 프로젝트 개요

- **Claude API**를 활용한 웹 기반 캐릭터 챗봇 플랫폼
- 사용자는 직접 캐릭터를 생성하고, 설정한 프롬프트 기반으로 Claude와 대화 가능
- **SPA 구조**로 프론트(Vue)와 백엔드(Flask)를 완전히 분리

---

## 🛠 사용 기술 스택

| 구분        | 기술                                    |
|-------------|-----------------------------------------|
| 프론트엔드  | Vue 3, Vite, JavaScript, CSS (scoped)  |
| 백엔드      | Python 3.x, Flask                       |
| API 연동    | Claude API (Anthropic)                  |
| 개발 환경   | VS Code, Git, Live Server               |

---

## 📁 프로젝트 구조

```
claude_chatbot/
├── backend/
│   ├── app.py                    # Flask API 서버
│   └── .env                      # Claude API 키 & URL 설정
│
├── frontend/
│   ├── index.html
│   ├── package.json              # Vue 프로젝트 설정
│   ├── vite.config.js           # Vite 설정
│   ├── README.md
│   ├── public/
│   │   └── favicon.ico
│   ├── src/
│   │   ├── main.js               # 앱 진입점
│   │   ├── App.vue               # 메인 App 컴포넌트
│   │   ├── assets/               # 스타일 및 이미지
│   │   │   ├── base.css
│   │   │   ├── logo.svg
│   │   │   ├── style_chat.css
│   │   │   ├── style_create.css
│   │   │   ├── style_index.css
│   │   └── components/           # 주요 컴포넌트
│   │       ├── CharacterForm.vue
│   │       └── ChatPreview.vue
│
└── .gitignore
```

---

## ✅ 구현 기능

- [x] Claude API 연동 및 POST 요청 처리
- [x] 사용자 캐릭터 프롬프트 입력 → 미리보기 응답 반환
- [x] 캐릭터 생성 화면 구성 (`CharacterForm.vue`)
- [x] 미리보기 응답 컴포넌트 (`ChatPreview.vue`)
- [ ] Stable Diffusion 이미지 삽입 기능 (구현 예정)
- [ ] 채팅 UI 연결 + 시뮬레이션 기능 구현

---

## 🧠 제작자 메모

> "연휴 3일 동안 Vue와 Flask를 처음 배우며 구축한 Claude API 기반 캐릭터 챗봇 플랫폼입니다.  
> 백엔드 연동, API 설계, 컴포넌트 분리까지 직접 해보며 개발자 실무 감각을 체험했습니다."

---

## 🚀 향후 계획

- ✅ 캐릭터 생성 저장 기능 추가
- ✅ Stable Diffusion 연동 테스트
- ⏳ 실제 캐릭터 챗봇 대화 기능 구현
- ⏳ GitHub Actions + 데모 배포 자동화
