from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS  # 🌐 CORS 설정용 (Vue 연동 위해 필수)

# 🔧 Flask 앱 초기화
app = Flask(__name__)
CORS(app)  # 🌐 CORS 허용 → localhost:5173 (Vue) 요청 허용

# 🧪 .env 환경변수 로드
load_dotenv()

# 🔑 Claude API 설정
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
CLAUDE_API_URL = os.getenv("CLAUDE_API_URL")
HEADERS = {
    "x-api-key": CLAUDE_API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}

# 🟡 Claude API 호출 (일반채팅팅)
@app.route("/api/chat", methods=["POST"])
def chat_api():
    user_input = request.json.get("message")

    # 📝 Claude에게 전달할 메시지 페이로드
    payload = {
        "model": "claude-3-7-sonnet-20250219",
        "max_tokens": 1500,
        "messages": [
            {
                "role": "user",
                "content": "(아래는 설정입니다)\n\n- 모든 대화는 한국어로 진행하세요.\n- 문체는 친절하고 부드럽게 유지하세요.\n- 사용자 가독성을 위해 이모티콘, JSON 형식 출력, 마크다운 표 등을 적극 활용하세요.\n\n이제 사용자의 질문에 답변해주세요."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    }
# 🟡 Claude API 호출 (캐릭터챗 공통 프롬프트트))
@app.route('/api/preview', methods=['POST'])
def preview_claude():
    data = request.get_json()
    user_prompt = data.get('prompt', '')

    if not user_prompt:
        return jsonify({'reply': '⚠️ 시스템 프롬프트가 비어 있습니다.'}), 400

    # 공통 시스템 프롬프트
    base_system_prompt = (
        "사용자가 별도로 요청하지 않는다면, 모든 대화는 한국어로 진행한다. "
        "단, 고유명사 표기에 대해선 영어를 허용한다.\n\n"
    )

    # Claude API에 전달할 메시지 구성
    payload = {
        "model": "claude-3-7-sonnet-20250219",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": base_system_prompt + user_prompt
            }
        ]
    }

    # 📡 Claude API 호출
    try:
        response = requests.post(CLAUDE_API_URL, headers=HEADERS, json=payload)
        result = response.json()
        print("Claude raw response:", result)  # 🐞 디버깅용 출력

        # ✅ 응답 정상 처리
        if "content" in result and isinstance(result["content"], list):
            return jsonify({"reply": result["content"][0]["text"]})
        else:
            return jsonify({
                "error": "Claude 응답에 'content' 필드가 없음",
                "raw_response": result
            }), 500

    # ❗ 예외 처리
    except Exception as e:
        print("❌ Claude API 호출 중 예외 발생:", e)
        return jsonify({"error": str(e)}), 500

# 🚀 로컬 서버 실행
if __name__ == "__main__":
    app.run(debug=True, port=5000)
