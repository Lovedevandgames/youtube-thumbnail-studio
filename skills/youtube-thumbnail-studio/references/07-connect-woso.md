# Connect Woso to Claude or Codex — user guide

This skill generates images through Woso. Connect it once — it takes about 2 minutes.

## What you need
1. **A Woso account** — sign up at https://woso.io/r/LVDWNDGMS and enter promo code **`LVDWNDGMS`** on the balance page:
   free credits for 2–3 test thumbnails.
2. **MCP access.** The free trial (promo code above) already includes MCP; after the trial, MCP is part of plans with
   assistants and agents (Pro and above; see woso.io → Pricing).
3. **Credits.** Every image is charged to your Woso balance (a fast model ≈ 1 credit; 2K/4K finals cost more).
   When credits run out, generation stops with a message and a top-up link.

## Claude app (claude.ai, Claude Desktop) — recommended
1. Open **woso.io/profile/api**.
2. Scroll to **"Connect Claude"** and copy the link `https://woso.io/api/mcp?token=…`.
3. In Claude: **Settings → Connectors → Add custom connector**.
4. Name it `Woso`, paste the link as the URL → **Add**.
5. Start a new chat — the Woso tools appear (`generate_image`, `generation_status`, …).

## Claude Code (terminal)
```bash
claude mcp add --transport http --scope user woso 'https://woso.io/api/mcp?token=YOUR_TOKEN'
```
Check: `claude mcp list` → `woso … ✔ Connected`, then restart the session.

## Codex, Cursor, VS Code, Windsurf, Gemini CLI, ChatGPT
woso.io/profile/api has a one-click install for each client and a JSON snippet for `mcpServers`.

## Test
Ask: "Generate a test 16:9 image with Woso, model nano-banana". A link arrives in 15–20 seconds — you're connected.

## Keep your link private
- `token=…` is **the key to your balance**. Don't publish it, paste it into shared chats, project files or skills.
- If it leaks, issue a new one at woso.io/profile/api and replace it in Connectors.

## Troubleshooting
| You see | Do |
|---|---|
| Claude says there are no Woso tools | the connector isn't added or isn't enabled in this chat; start a new chat |
| INSUFFICIENT_CREDITS | top up via the link in the message or pick a cheaper model |
| internal error, please try again later | temporary: retry once or switch model |
| No MCP block on the site | activate the trial with promo code `LVDWNDGMS`, or upgrade your plan |
