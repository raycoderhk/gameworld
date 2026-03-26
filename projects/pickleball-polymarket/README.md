# 🏓 Pickleball Polymarket

A simple, fun prediction market for your pickleball group — bet push-ups, not money!

## Quick Start

Just open `index.html` in any browser. No server needed.

**URL:** `https://[your-server]/projects/pickleball-polymarket/`

## How It Works

1. **Place a bet** — Enter your name, pick a color, choose 1–10 push-ups to bet
2. **Watch the odds** — See live odds update as everyone bets
3. **Admin reveals** — When the color is known, enter the admin password and select the winner
4. **Winners collect** — Pool of push-ups is split equally among correct guesses

## Admin Password

Default: `pickle2024`

To change it, edit the `ADMIN_PWD` constant at the top of the `<script>` section.

## Data Storage

All bets are stored in **browser LocalStorage**. This means:
- ✅ Easy — no database needed
- ⚠️ Each user sees the same page but different local data
- ⚠️ For true shared state, serve from one static host OR use a shared computer
- 💡 To reset: clear localStorage for that page

## Best Use Case

Open on a shared device (tablet/laptop) at the court, or share the URL with the group. Everyone can see the live odds.

## Customization

Edit the HTML directly to change:
- Question text (search for `questionBox`)
- Color options (edit the COLORS array in JS + the button HTML)
- Admin password (edit `ADMIN_PWD` constant)
- Max push-ups (change the `< 10` check in the inc button handler)

---

Have fun! 🏋️🏓
