# Image engine — Woso MCP

[Woso](https://woso.io/r/LVDWNDGMS) is an AI aggregator: one MCP connector gives this skill Nano Banana Pro, Nano Banana 2,
GPT Image 2.5, Seedream, background removal and Topaz upscaling, billed from one credit balance.

## Tools (verified October 2026)
| Tool | Purpose | Key parameters |
|---|---|---|
| `generate_image` | generate and edit images, remove backgrounds, upscale | `model` (required), `prompt` (required), `aspect_ratio` ("16:9", "9:16"), `resolution` (1K / 2K / 4K, model-dependent), `image_url` / `image_urls` (references as URLs), `quantity`, `quality`, `seed`, `output_format` |
| `generation_status` | wait for a result | `generation_id` — call again until "Completed" |
| `generate_video`, `generate_audio` | video and music (not needed for thumbnails) | — |

`generate_image` models: `nano-banana` (default, fast) · `nano-banana-pro` (quality, 2K/4K) · `nano-banana-2` ·
`gpt-image-2` · `gpt-image-2-5` · `chatgpt-5` · `seedream`, `seedream-4-0`, `seedream-4-5`, `seedream-5-lite` ·
`bg-remove` · `topaz-image-upscale`.

## Service rules
- "NOT FINISHED" + `generation_id` → poll `generation_status` every few seconds until "Completed";
  only show the user the finished link.
- **To keep a specific face from a reference** use only `nano-banana-2`, `nano-banana-pro`, `gpt-image-2`,
  `gpt-image-2-5` or `chatgpt-5`. `seedream` does not keep faces.
- 2K/4K only for finals: slower and more credits.
- "internal error, please try again later" — retry once or switch model.
- "INSUFFICIENT_CREDITS" — don't retry: pass the account, balance and top-up link from the message to the user.
- The result is an image URL: download it right away (`curl -sL <url> -o file`) and keep it locally;
  the result URL can be fed back as `image_url` for the next iteration.

## References are URLs
The MCP has no file upload: `image_url(s)` take public URLs.
- YouTube neighbours — `https://i.ytimg.com/vi/<id>/maxresdefault.jpg`.
- Previous Woso results — their URLs.
- Your own photos: upload them in the Woso web app ("edit by reference" / "photo by reference") and work there,
  or host them at a URL the owner approves (personal photos only with consent).

## Manual mode (connector not connected)
For each concept give the user: the Woso web section and model, aspect ratio, quality, which files to upload and in
which order, the full prompt; ask them to send the results back and continue from step 7.
