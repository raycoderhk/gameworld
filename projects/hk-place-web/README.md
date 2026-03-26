# 香港景點導覽 - Hong Kong Attractions

這是 Raymond 用 **Discord + OpenClaw AI 助手** 打造的香港景點介紹網頁。

## 🎯 影片連結

> 即將上線！敬請期待

## 🛠️ 技術架構

| 項目 | 技術 |
|------|------|
| 前端框架 | Bootstrap 5 (CDN) |
| 字體 | Noto Sans HK (Google Fonts) |
| 圖標 | Bootstrap Icons |
| 部署方式 | Discord 指令控制 OpenClaw 生成 |

## 📁 專案結構

```
hk-place-web/
├── index.html    # 主頁面（單一 HTML 包含所有 CSS/JS）
├── README.md     # 本檔案
└── ...
```

## 🚀 如何重現這個專案

### 步驟 1：在 Discord 向 OpenClaw 發送指令

```
@OpenClaw 幫我用 Bootstrap 5 整一個香港景點介紹頁，包含：
- Hero section with 維多利亞港背景
- 3個景點卡片：維多利亞港、太平山頂、旺角街景
- 深藍色夜景主題
- 卡片式佈局，responsive 設計
```

### 步驟 2：OpenClaw 分析需求並生成代碼

AI 助手會自動：
1. 解析你的廣東話指令
2. 規劃頁面結構
3. 生成完整的 HTML/CSS/JS
4. 寫入 `/projects/hk-place-web/index.html`

### 步驟 3：在瀏覽器打開查看結果

直接在瀏覽器開啟 `index.html` 即可看到靚靚的香港景點頁面！

## 🎨 頁面功能

- ✅ 深藍色夜景主題（香港感覺）
- ✅ Hero Section 背景圖
- ✅ 3個景點卡片（维港、山頂、旺角）
- ✅ 評分系統
- ✅ Hover 動畫效果
- ✅ 滾動視差效果
- ✅ 卡片淡入動畫
- ✅ 響應式設計（支援 mobile）
- ✅ Scroll to top 按鈕

## 📝 開發者備註

本專案由 OpenClaw AI 助手在 Discord 上即時生成，展示了：
- 如何用自然語言（廣東話）控制 AI 寫網頁
- Discord 作為統一的溝通界面
- 從想法到成品只需要幾分鐘

---

*Made with ❤️ by Raymond (raycoderhk) using OpenClaw + Discord*
