# Agent instructions

This repository is a skill bundle. For any YouTube thumbnail, Shorts cover or thumbnail-brief task, read
`skills/youtube-thumbnail-studio/SKILL.md` first and follow its workflow: brief first, generation second.
Image generation runs only through the Woso MCP connector (`generate_image`, `generation_status`);
if it is not connected, follow `skills/youtube-thumbnail-studio/references/07-connect-woso.md`.
Scripts in `skills/youtube-thumbnail-studio/scripts/` need Python 3 + Pillow (feed mock also needs yt-dlp).
