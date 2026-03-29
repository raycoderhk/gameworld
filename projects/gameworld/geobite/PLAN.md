# GeoBite — Project Plan

## Concept
**GeoBite** is a micro-learning app under GameWorld brand — delivering geopolitics insights in 10 min/day, similar to Nibble's format. AI-powered daily content, Cantonese/English bilingual, shareable with friends & family.

## Structure
```
projects/gameworld/
├── hk-place-web/     ← existing, moves under gameworld
└── geobite/          ← NEW
    ├── index.html   ← Landing page (Nibble-style hook)
    ├── quiz.html    ← Entry quiz (5 Qs)
    ├── css/
    │   └── style.css
    ├── daily/
    │   ├── monday.html    ← US-China Tech War
    │   ├── tuesday.html   ← Middle East Water Crisis
    │   ├── wednesday.html ← AI & Global Power
    │   ├── thursday.html  ← China Manufacturing
    │   └── friday.html    ← EU Strategy
    └── README.md
```

## Tech Stack
- **Framework:** Bootstrap 5 (CDN)
- **Theme:** Dark, professional — like reading a premium intelligence briefing
- **Font:** Noto Sans HK / Inter
- **Content source:** AI News project (existing) + fresh AI-generated summaries
- **Mobile-first:** Yes

## Content — 5 Daily Lessons

### Monday: 🌏 US-China Tech War
- AI chip bans, Huawei, semiconductor supply chains
- Source: existing AI News content

### Tuesday: 💧 Middle East Water Crisis
- Iran threatens Gulf desalination plants
- Source: Guardian Iran Water article (already scraped)

### Wednesday: 🤖 AI & Global Power
- How AI is reshaping geopolitical influence
- Source: Bloomberg AI China Welfare article

### Thursday: 🏭 China Manufacturing
- Supply chain dependencies, "world's factory" risks

### Friday: 🌍 EU Strategy
- Europe's position between US and China

## Landing Page (index.html)
- **Hook:** "Only 15% understand geopolitics. Will you join them?"
- **CTA:** Start with 5-min quiz → Get your first daily briefing
- **Style:** Clean, curiosity-gap, Nibble-style

## Quiz Flow (quiz.html)
5 quick questions:
1. "Who controls the Taiwan Strait?" (China / USA / Both)
2. "Which country has the most desalination capacity?" (Saudi / UAE / Israel)
3. "Where does most rare earth mining happen?" (China / Australia / Brazil)
4. "What is NATO's article 5?" (Collective defense / Trade / Climate)
5. "Which nation threatens Gulf desalination?" (Iran / Iraq / Syria)

Result: Personalized daily briefing recommendation + email/share CTA

## To Execute
1. Create folder structure under `projects/gameworld/geobite/`
2. Build `index.html` — landing page with Bootstrap 5, dark theme, hook + CTA
3. Build `quiz.html` — 5-question quiz flow
4. Build `css/style.css` — custom dark theme styling
5. Create 5 daily lesson pages in `daily/` using content from AI News project
6. Create `README.md`

## Design Guidelines
- **Colors:** Dark background (#0f172a), accent blue (#3b82f6), alert red (#ef4444)
- **Typography:** Clean, readable, intelligence-briefing feel
- **Cards:** Rounded, subtle borders, hover effects
- **Mobile:** Single column, full-width cards
