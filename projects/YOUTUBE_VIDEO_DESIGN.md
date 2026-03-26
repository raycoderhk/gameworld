# 🎬 YouTube Video: Build HK Place Web Page via Discord + OpenClaw

## Video Concept

**Title:** 用 Discord 教 AI 整香港景點網頁！OpenClaw 助手超簡單設定 | 2025 教程

**Hook (0:00-0:30):**
> "唔使識寫 Code！今集教你用 Discord 指令 AI 助手幫你整一個香港景點網頁"

**Duration:** ~8-10 minutes
**Tone:** Casual, beginner-friendly, Hong Kong Cantonese vibe

---

## Storyboard / Script

### Section 1: Introduction (0:00-1:30)
```
🎬 On camera / B-roll: Discord logo, OpenClaw logo, HK skyline
🎤 Voiceover or on-camera

內容：
- 自我介紹：Raymond (raycoderhk)
- 今日目標：用 Discord 控制 OpenClaw AI 助手整一個香港景點介紹頁
- 前置需求：已安裝 OpenClaw + 已設定 Discord 插件
- 為什麼用 Discord：你日常已經在用，唔洗再開另一個 App
```

### Section 2: System Architecture Overview (1:30-3:00)
```
🎬 動畫或圖表：User → Discord → OpenClaw Gateway → AI Model → 網頁生成

腳本：
"原理好簡單：
1. 你喺 Discord 打字指令（例如：幫我整一個介紹香港迪士尼嘅網頁）
2. OpenClaw 收到指令，分析你想要咩
3. AI 模型理解指令，生成 HTML/CSS/JavaScript
4. OpenClaw 自動寫入檔案，你直接睇結果"

可視化流程圖（可放 screen recording）
```

### Section 3: Live Demo - Step by Step (3:00-7:00)

**Step 3.1 開波：叫出助手 (30s)**
```
Discord message: @OpenClaw 你好！
Expected response: AI 助手打招呼 + 話準備好幫你
```

**Step 3.2 告訴助手想要咩網頁 (1min)**
```
Discord message: 幫我用 Bootstrap 5 整一個香港景點介紹頁，
                 包含：維多利亞港、太平山頂、旺角街景
                 用深藍色主題，卡片式佈局
Expected: AI 分析需求，話 "收到！我幫你整"
```

**Step 3.3 助手規劃並執行 (1.5min)**
```
AI 思考過程（show Discord messages）：
- 分析需求：Bootstrap 5、3個景點、深藍色主題
- 規劃頁面結構：header、景點cards、responsive設計
- 開始生成代碼（show 打字過程/streaming）

Discord message from AI:
"我幫你整緊... 頁面會有：
✅ Hero section with 維多利亞港背景
✅ 3張景點卡片
✅ 底部版權
搞掂！"
```

**Step 3.4 展示結果 (1min)**
```
Screen record：browser 開啟 generated index.html
展示：
- 靚靚深藍色主題
- 3個景點卡片有圖有文字
- 係 responsive，mobile都睇到
- 全部係 Bootstrap 5 class，唔洗自己寫 CSS
```

### Section 4: How It Works Under The Hood (7:00-8:00)
```
🎬 Screen share of OpenClaw workspace structure

腳本：
"其實呢個係我喺 Discord 同 OpenClaw 對話，佢幫我建立嘅 workspace：
- /projects/hk-place-web/index.html
- /projects/hk-place-web/style.css
- /projects/hk-place-web/script.js

OpenClaw 自動：
1. 分析我嘅廣東話指令
2. 轉化為具體嘅技術需求
3. 寫入正確嘅檔案
4. 保證代碼係有效嘅 HTML5

你喺 Discord 打字，AI 幫你寫 code — 就係咁簡單"
```

### Section 5: Outro + CTA (8:00-9:00)
```
腳本：
"如果你覺得呢個 workflow 幾正，歡迎：
✅ Subscribe + 點讚
✅ 喺下面留言話我想睇咩其他教程
✅ 分享俾朋友

下一集我想整：
- 加入 Gemini API 實時天氣資料
- 加入香港地鐵圖
你估下會幾快整好？"

片尾：OpenClaw Discord link + 個人 social links
```

---

## Technical Details

### Demo Web Page Requirements
- **Framework:** Bootstrap 5 (CDN)
- **Theme:** Dark blue (midnight/香港夜景 feel)
- **Sections:**
  1. Hero with Victoria Harbour background
  2. 3 attraction cards (Victoria Peak, Mong Kok, Disneyland)
  3. Footer with credits
- **Responsive:** Yes, mobile-friendly
- **Font:** Noto Sans HK (Google Fonts)

### Discord Commands Used
1. `@OpenClaw` - mention to get attention
2. Natural language instructions in Cantonese
3. `!status` - check OpenClaw status
4. `!commit` - commit changes to git

### Tools to Screen Record
- Discord (show the chat)
- VS Code or file explorer (show generated files)
- Browser (show final result)
- Optional: OBS Studio for recording

---

## Thumbnail Ideas
- Left: Discord logo + OpenClaw logo
- Center: HK skyline silhouette
- Right: Code snippet / web page preview
- Text overlay: "Discord 控制 AI 整網頁！"

---

## Recommended Video Specs
- **Aspect ratio:** 16:9
- **Resolution:** 1920x1080
- **Frame rate:** 30fps
- **Audio:** Condenser mic for voiceover
- **Subtitles:** 繁體中文 CC recommended
- **Tags:** OpenClaw, Discord, AI網頁, 香港旅遊, Bootstrap5, AI助手
