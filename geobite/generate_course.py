#!/usr/bin/env python3
"""
GeoBite AI Course Generator
用法: python3 generate_course.py "主題" [星期幾]
例如: python3 generate_course.py "南中國海主權爭端" wednesday
"""

import os
import sys
import json
import re
from datetime import datetime

# ========== 設定 ==========
COURSE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(COURSE_DIR, "daily")

DAY_MAP = {
    "monday": "週一",
    "tuesday": "週二", 
    "wednesday": "週三",
    "thursday": "週四",
    "friday": "週五",
    "saturday": "週六",
    "sunday": "週日",
}

# ========== 課程生成 Prompt ==========
COURSE_GENERATION_PROMPT = """你係一位地緣政治專家，幫我生成一份深度課程內容。

主題：{topic}

請用繁體中文生成以下 JSON 格式，**只輸出 JSON，唔好加任何其他文字**：
{{
  "title": "課程標題",
  "overview": "概述，150字左右",
  "background": "背景脈絡，300字左右",
  "analysis": "核心分析，500字左右",
  "implications": "戰略意涵，200字左右",
  "questions": ["思考題1", "思考題2", "思考題3"],
  "quiz": [
    {{
      "question": "題目",
      "options": ["A選項", "B選項", "C選項", "D選項"],
      "answer": 0,
      "explanation": "解釋"
    }}
  ]
}}
"""


def generate_with_openai(prompt: str, topic: str) -> dict:
    """使用 OpenAI API 生成課程內容"""
    import urllib.request
    
    OPENAI_API_KEY = os.environ.get("OPENAI_API", "")
    
    if not OPENAI_API_KEY:
        print("⚠️ 警告: 未設定 OPENAI_API_KEY，使用模擬數據")
        return get_mock_course(topic)
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method="POST")
    
    with urllib.request.urlopen(req, timeout=60) as response:
        result = json.loads(response.read().decode())
        content = result["choices"][0]["message"]["content"]
        
        json_match = re.search(r'\{[\s\S]*\}', content)
        if json_match:
            return json.loads(json_match.group())
        raise ValueError(f"無法解析 JSON: {content[:200]}")


def generate_with_minimax(prompt: str, topic: str) -> dict:
    """使用 MiniMax API 生成課程內容 (text model)"""
    import urllib.request
    
    MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY", "")
    
    if not MINIMAX_API_KEY:
        print("⚠️ 警告: 未設定 MINIMAX_API_KEY，使用模擬數據")
        return get_mock_course(topic)
    
    url = "https://api.minimaxi.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MINIMAX_API_KEY}"
    }
    data = {
        "model": "MiniMax-M2.7",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,  # Low temp for structured output
        "max_tokens": 2500
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=90) as response:
            result = json.loads(response.read().decode())
            content = result["choices"][0]["message"]["content"]
            
            # Strip thinking blocks first
            cleaned = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
            
            # Try direct JSON parse
            try:
                return json.loads(cleaned)
            except json.JSONDecodeError:
                # Fallback: extract first {...} block
                json_match = re.search(r'\{[\s\S]*\}', cleaned)
                if json_match:
                    return json.loads(json_match.group())
            
            raise ValueError(f"無法解析 JSON from content: {cleaned[:200]}")
    except Exception as e:
        print(f"MiniMax API 錯誤: {e}")
        raise


def get_mock_course(topic: str) -> dict:
    """模擬課程數據 (當沒有 API key 時使用)"""
    return {
        "title": f"【{topic}】深度解析",
        "day": "monday",
        "overview": f"{topic}是當今國際關係中最複雜的議題之一，涉及多方利益衝突與地緣戰略考量。",
        "background": f"近年來，{topic}的緊張局勢持續升溫，成為國際媒體關注的焦點。各主要國家都在積極調整策略以維護自身利益。",
        "analysis": f"針對{topic}的分析需要考慮多個層面：歷史淵源、經濟利益、安全考量以及國際法框架。每一個因素都會影響最終的局勢走向。",
        "implications": f"{topic}的發展將深刻影響區域安全格局和各國的戰略部署。持續關注此議題對於理解國際事務至關重要。",
        "questions": [
            f"{topic}的主要參與者有哪些？他們的核心利益是什麼？",
            f"從歷史上看，{topic}經歷了哪些關鍵轉折點？",
            f"未來10年，{topic}可能如何發展？"
        ],
        "quiz": [
            {
                "question": f"關於{topic}，以下哪項描述最準確？",
                "options": [
                    "這是一個純粹的雙邊問題",
                    "涉及多方利益和複雜的歷史因素",
                    "只需要經濟手段即可解決",
                    "與國際法無關"
                ],
                "answer": 1,
                "explanation": "正確答案為B，因為這是一個涉及多方利益和複雜歷史因素的地緣政治問題。"
            },
            {
                "question": f"{topic}對全球經濟最直接的影響是什麼？",
                "options": [
                    "沒有任何影響",
                    "貿易路線和供應鏈穩定性",
                    "只影響當事國",
                    "貨幣匯率"
                ],
                "answer": 1,
                "explanation": "地緣政治緊張通常會影響貿易路線和供應鏈的穩定性。"
            },
            {
                "question": f"面對{topic}的挑戰，國際社會通常如何應對？",
                "options": [
                    "忽視問題存在",
                    "通過外交談判和制裁並行",
                    "只使用軍事手段",
                    "交由單一國家處理"
                ],
                "answer": 1,
                "explanation": "國際社會通常會綜合使用外交談判和制裁等手段來應對地緣政治挑戰。"
            },
            {
                "question": f"{topic}的解決方案最可能來自於？",
                "options": [
                    "單一強國的單邊行動",
                    "多邊國際組織的協調",
                    "完全市場自我調節",
                    "武力衝突後的既成事實"
                ],
                "answer": 1,
                "explanation": "多邊國際組織的協調是解決複雜地緣政治問題的可持續途徑。"
            }
        ]
    }


def generate_html(course: dict, day: str, topic: str = "") -> str:
    """生成 HTML 頁面"""
    day_cn = DAY_MAP.get(day, day)
    
    # 構建 quiz HTML
    quiz_html = ""
    for i, q in enumerate(course.get("quiz", []), 1):
        options_html = ""
        for j, opt in enumerate(q["options"]):
            letter = ["A", "B", "C", "D"][j] if j < 4 else chr(65 + j)
            options_html += f'<li class="list-group-item bg-transparent text-light">{letter}. {opt}</li>\n'
        
        quiz_html += f'''
            <div class="card mb-3 bg-dark border-warning">
                <div class="card-header">
                    <h4 class="text-warning">問題 {i}</h4>
                </div>
                <div class="card-body">
                    <p class="lead">{q["question"]}</p>
                    <ul class="list-group list-group-flush mb-3">
                        {options_html}
                    </ul>
                    <button class="btn btn-outline-info" onclick="toggleAnswer('answer{i}')">顯示答案</button>
                    <div id="answer{i}" class="mt-3 alert alert-success" style="display:none;">
                        <strong>答案：{["A", "B", "C", "D"][q["answer"]]}</strong>
                        <p class="mb-0 mt-2">{q.get("explanation", "")}</p>
                    </div>
                </div>
            </div>
        '''
    
    # 構建思考題 HTML
    questions_html = ""
    for q in course.get("questions", []):
        questions_html += f'<li class="list-group-item bg-transparent text-light">💭 {q}</li>\n'
    
    html = f'''<!DOCTYPE html>
<html lang="zh-HK">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{course.get("title", topic)} - GeoBite {day_cn}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@300;400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
    <style>
        .thinking-section {{ background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); }}
        .quiz-section {{ background: linear-gradient(135deg, #16213e 0%, #1a1a2e 100%); }}
    </style>
</head>
<body>
    <div class="container-fluid">
        <header class="text-center py-4">
            <h1 class="display-5 text-primary">GeoBite Intelligence Report</h1>
            <p class="lead text-secondary">AI 即時生成課程 | {datetime.now().strftime("%Y年%m月%d日")}</p>
            <span class="badge bg-primary">{day_cn}課程</span>
            <span class="badge bg-success ms-2">🤖 AI 生成</span>
        </header>

        <nav aria-label="breadcrumb" class="mb-4">
            <ol class="breadcrumb justify-content-center">
                <li class="breadcrumb-item"><a href="../index.html">Home</a></li>
                <li class="breadcrumb-item"><a href="../index.html#daily">每日課程</a></li>
                <li class="breadcrumb-item active">{course.get("title", topic)[:30]}</li>
            </ol>
        </nav>

        <main class="content">
            <!-- 課程內容 -->
            <div class="card mb-4 bg-dark border-primary">
                <div class="card-header">
                    <h2 class="text-primary">📚 {course.get("title", "課程")}</h2>
                </div>
                <div class="card-body">
                    <p class="lead">{course.get("overview", "")}</p>
                    
                    <h3 class="text-warning mt-4">📖 背景脈絡</h3>
                    <p>{course.get("background", "")}</p>
                    
                    <h3 class="text-warning mt-4">🔍 核心分析</h3>
                    <p>{course.get("analysis", "")}</p>
                    
                    <h3 class="text-warning mt-4">🌐 戰略意涵</h3>
                    <p>{course.get("implications", "")}</p>
                </div>
            </div>

            <!-- 思考題 -->
            <div class="card mb-4 bg-dark border-info thinking-section">
                <div class="card-header">
                    <h3 class="text-info">🤔 深度思考題</h3>
                </div>
                <div class="card-body">
                    <ul class="list-group list-group-flush">
                        {questions_html}
                    </ul>
                </div>
            </div>

            <!-- Quiz -->
            <div class="card mb-4 bg-dark border-warning quiz-section">
                <div class="card-header">
                    <h3 class="text-warning">📝 測驗</h3>
                </div>
                <div class="card-body">
                    {quiz_html}
                </div>
            </div>
        </main>

        <footer class="text-center py-4 text-muted">
            <p>&copy; {datetime.now().year} GeoBite Intelligence. All rights reserved.</p>
            <p>🤖 此課程由 AI 即時生成 | <a href="../index.html" class="btn btn-outline-primary">返回首頁</a></p>
        </footer>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        function toggleAnswer(id) {{
            var el = document.getElementById(id);
            if (el.style.display === 'none') {{
                el.style.display = 'block';
            }} else {{
                el.style.display = 'none';
            }}
        }}
    </script>
</body>
</html>'''
    return html


def main():
    if len(sys.argv) < 2:
        print("用法: python3 generate_course.py <主題> [星期]")
        print("例如: python3 generate_course.py '南中國海主權爭端' wednesday")
        print(f"可用星期: {', '.join(DAY_MAP.keys())}")
        sys.exit(1)
    
    topic = sys.argv[1]
    day = sys.argv[2] if len(sys.argv) > 2 else "monday"
    
    if day not in DAY_MAP:
        print(f"未知嘅星期: {day}")
        print(f"可用選項: {', '.join(DAY_MAP.keys())}")
        sys.exit(1)
    
    print(f"🎯 為「{topic}」生成{DAY_MAP[day]}課程...")
    
    # 生成內容
    prompt = COURSE_GENERATION_PROMPT.format(topic=topic)
    
    # 嘗試用 OpenAI 或 MiniMax
    course = None
    
    # 先試 MiniMax (因為佢係 default key)
    try:
        course = generate_with_minimax(prompt, topic)
        print("✅ 使用 MiniMax 生成")
    except Exception as e:
        print(f"MiniMax 失敗 ({e})")
    
    # 如果 MiniMax 失敗，先嘗試 OpenAI
    if course is None:
        try:
            course = generate_with_openai(prompt, topic)
            print("✅ 使用 OpenAI 生成")
        except Exception as e:
            print(f"OpenAI 也失敗 ({e})")
    
    # 如果都失敗，用 mock
    if course is None:
        print("⚠️ 使用模擬數據")
        course = get_mock_course(topic)
    
    # 生成 HTML
    html = generate_html(course, day, topic)
    
    # 儲存
    output_file = os.path.join(OUTPUT_DIR, f"{day}.html")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✅ 課程已生成: {output_file}")
    print(f"📝 標題: {course.get('title', 'N/A')}")
    print(f"❓ 思考題: {len(course.get('questions', []))} 題")
    print(f"📝 Quiz: {len(course.get('quiz', []))} 題")


if __name__ == "__main__":
    main()
