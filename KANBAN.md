# 🗂️ Kanban Board — HK Place Web Project

## 📋 Backlog (To Review)

| # | Task | Status | Notes |
|---|------|--------|-------|
| 1 | **True Image-to-Image (I2I)** | 🔴 Blocked | MiniMax `image-01` doesn't support I2I. `image_url` only works as text reference. Need to find working I2I solution |
| 2 | **Download MiniMax Video** | 🔴 Blocked | Generated 2 videos (task IDs: 380712348176463, 380709053321322) but can't download via API. Need OAuth login to hailuoai.video |
| 3 | **OAuth Login for MiniMax** | 🔴 Pending | Need to set up `minimax-portal-auth` to enable web UI access |
| 4 | **Video-to-Image Extraction** | ⏳ Waiting | Once video download works, extract frames for use |

---

## ✅ Done

| # | Task | Notes |
|---|------|-------|
| 1 | Website Design | Bootstrap 5, dark blue HK theme, St. Barnabas' Church hero |
| 2 | 10 Style T2I Images | Cyberpunk, Golden Hour, Watercolor, Snow, Oil Paint, Anime, Ink Wash, Stormy, Vintage, Neon |
| 3 | I2I Attempt x3 | Verified MiniMax doesn't support true I2I |
| 4 | Video Generation x2 | Successfully generated HK Harbour + HK Tram (6s each) |

---

## 🔜 Next Steps Options

### Option A: Solve OAuth Login
```bash
openclaw plugins enable minimax-portal-auth
openclaw gateway restart
openclaw models auth login --provider minimax-portal
```
→ Enables web UI access → can download videos + use Hailuo web for I2I

### Option B: Use External I2I Provider
- **DALL-E 3** (OpenAI) — if Ray has API key
- **Flux.1** (Replicate/Fal) — if Ray has API key  
- **Stable Diffusion** (via API) — various options
- **Leonardo.ai** — if Ray has account

### Option C: Manual Workflow (Currently)
- Generate styles via MiniMax T2I with very detailed text prompts
- Use hailuoai.video web UI manually for true I2I
- Download videos from web UI manually

---

## 💡 Discussion Points for Ray
1. Does he have other AI API keys (OpenAI, Replicate, etc.)?
2. Does he want to set up OAuth for MiniMax?
3. Priority: I2I images or video download?
