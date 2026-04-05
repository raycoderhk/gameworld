# 🎮 GameWorld — Interactive Mini-Games & Simulations

A collection of interactive games and simulations — all **single HTML files**, open in any browser. No server, no install, no dependencies.

---

## 🆕 UBI Simulator

**`ubi-sim/index.html`** — *"Could Universal Basic Income actually work?"*

Agent-based economic simulation — 10,000 simulated citizens, 30 years of economic life. Adjust UBI amount, tax phase-out, and labor elasticity. Watch poverty, inequality, employment, and fiscal balance evolve in real time.

- Built on Dr. Jay L. Zagorsky (BU) methodology
- 4 preset scenarios (Baseline, Yang $12k, High $20k, NIT Style)
- Live charts: Gini, Poverty, Employment, Fiscal, Income Shares
- Auto-play, step-by-step, year scrubber
- Think Tank grade + student friendly

**Open:** `ubi-sim/index.html`

---

## 🧬 Cellular Automata Explorer

**`cellular-automata/index.html`** — *"The surprisingly complex world of simple rules"*

Interactive playground for learning Cellular Automata (CA).

- **Elementary CA** (1D) — Rules 0–255, including Rule 30 (chaos) and Rule 110 (Turing complete!)
- **Conway's Game of Life** (2D) — B3/S23, with presets: Glider, Blinker, LWSS, Gosper Glider Gun, Acorn
- Click to draw cells
- Adjustable simulation speed
- See the Python code behind each CA

**Open:** `cellular-automata/index.html`

---

## 🌏 GeoBite

**`geobite/index.html`** — *"地緣政治智慧平台"*

An interactive geopolitics quiz platform (bilingual Chinese/English). Learn about global political events, trade relationships, and international conflicts through bite-sized challenges.

- Daily briefing quizzes
- Course-based learning
- Progress tracking

**Open:** `geobite/index.html`

---

## ➕ Contributing a New Mini-Game

1. Create a new folder under `gameworld/your-game-name/`
2. Add `index.html` (must be fully self-contained — no server needed)
3. Add `README.md` with instructions
4. Add an entry above

**Design principles:**
- Single HTML file (inline CSS + JS)
- No external dependencies except CDN (Bootstrap, Google Fonts)
- Works in Chrome, Firefox, Safari, Edge
- Mobile-friendly
- Fun first, educational second

---

_Created with OpenClaw 🦦_
