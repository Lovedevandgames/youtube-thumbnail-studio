# Prompts and models

| Task | Woso `model` | Why |
|---|---|---|
| Final: photoreal, editing a real frame by reference, 2K/4K | **`nano-banana-pro`** | holds the reference and the face, fine detail |
| Fast concept variants, iterations | `nano-banana` (default), `nano-banana-2` | speed and price (≈ 0.8 credit) |
| Poster layouts, graphics, text in frame | **`gpt-image-2-5`** / `gpt-image-2` | follows complex briefs, renders text, keeps faces |
| Alternative that keeps the hero's face | `chatgpt-5` | identity-preserving |
| Backgrounds, restyles, scenes without the hero | `seedream-4-5` / `seedream-5-lite` | realism and price; **does not keep faces** |
| Cut out the hero / an object | `bg-remove` | transparent background for compositing |
| 4K master | `topaz-image-upscale` | upscale the final |

Call: `generate_image(model, prompt, aspect_ratio="16:9", resolution="1K|2K|4K", image_urls=[…], quantity=…)`;
"NOT FINISHED" → `generation_status(generation_id)` until "Completed". Details — `06-woso-engine.md`.

## The 4 mandatory prompt parts
Anything you leave out, the model invents — and it invents average.
1. **Subject and action** — who/what is in frame, what they do, where they stand ("woman on the right third, waist-up").
2. **Emotion as a word** — "triumphant", "shocked", "tearful hope". Not "looking at camera": that gives a dead face.
3. **Text verbatim** in quotes + style, or "no text" (final text is better composited by script).
4. **Composition** — where the hero is, where the text is, which background (a darkened real scene, not a flat fill),
   annotations, 16:9 / 9:16, bottom-right corner empty.

Plus: palette (HEX/words), light (key, rim), lens/angle, "photorealistic, cinematic grade".

## Template
```
YouTube thumbnail, 16:9. [Subject and action, position]. Expression: [emotion], [face details].
[Main object/graphic: what, where, size]. Background: [real scene], darkened/graded, [depth].
Palette: [3 colours]. Lighting: [key + rim]. Text: "[EXACT WORDS]" in [style], [where] — or no text.
Keep the bottom-right corner empty. Photorealistic, high contrast, readable at small size.
```

## References — order and labels
- First the hero photo (the face is the source of truth), then the concept's objects, last 1–2 niche thumbnails.
- Name each one in the prompt: "The first image is the person — keep the exact face and body unchanged.
  The second image is the composition reference — follow layout and mood, do not copy text or logos."
- A composition reference from niche winners does more than any prompt polishing.

## Examples (weak vs strong)
- Weak: "AI SEO tools video". Strong: "Man on the left half, hands on face, shocked, looking at camera. Right half plain
  white. Large black condensed text "7 AI SEO TOOLS" with "THE TRUTH" in a red block. Row of small logos along the bottom,
  one circled in orange."
- Before → after: "Hard vertical split. Left desaturated, slouched man, "DAY 1" top-left. Right warm, same man upright,
  "DAY 90" top-right in yellow. Thin white arrow across the divide."

## Iterations
```
Edit this YouTube thumbnail. Keep the same composition and style.
The first image is the person — keep the face exactly. The second image is the current thumbnail.
Change only: [list of edits].
```
Save as v2, v3…; change one or two things at a time. A previous result's URL can be passed back as `image_url`.

## Real people
- Never generate or "improve" the hero's face/body; generate the world around them and bring the hero back from the original.
- Identity-preserving generation of a real person — only with that person's explicit consent.
- Moderation blocks lingerie/swimwear: crop higher or mask the body — a thumbnail rarely needs it anyway.
- Real signs, lettering and logos are never redrawn by AI — only taken from the original.
