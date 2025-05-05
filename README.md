# Claude 기반 캐릭터 챗봇 (GPT + Flask 프로젝트)

## 📌 프로젝트 소개
Claude API를 활용한 웹 기반 캐릭터 챗봇 플랫폼입니다.  
사용자는 일반 LLM과 대화하거나, 자신만의 캐릭터 챗봇을 생성하고 대화할 수 있습니다.  
프론트엔드와 백엔드를 완전히 분리하여 SPA 구조로 구성했습니다.

---

## 🧰 사용 기술 스택

| 구분 | 기술 |
|------|------|
| 프론트엔드 | HTML5, CSS3, JavaScript, Markdown |
| 백엔드 | Python 3.x, Flask |
| API 연동 | Claude API (Anthropic) |
| 기타 | VS Code, Live Server (로컬 테스트용) |

---

## 📂 프로젝트 구조

claude_chatbot/
├── static_frontend/
│ ├── css/
│ │ └── style_chat.css
│ ├── js/
│ │ └── chat.js
│ ├── chat.html
│ ├── index.html
│ └── ...
├── app.py
└── README.md


---

## 💡 주요 기능

- 기본 채팅: Claude API와 직접 대화
- 캐릭터 챗 생성: 시스템 프롬프트 입력으로 캐릭터 정의
- 캐릭터 챗 선택: 만든 캐릭터 중 하나를 선택해 대화
- 마크다운 응답 처리 (`marked.js` 활용)
- SPA 기반 구조 설계 (HTML + API 비동기 처리)
- 모바일 접속을 고려한 구조로 확장 가능

---

## 📷 화면 미리보기

> ![index 화면](static_frontend/images/index_sample.png)

---

## 🛠 실행 방법 (개발용)

```bash
# 1. 가상환경 설정 (옵션)
python -m venv venv
source venv/bin/activate  # 또는 venv\Scripts\activate

# 2. 패키지 설치
pip install flask

# 3. 서버 실행
python app.py
http://127.0.0.1:5000 에서 확인 가능