# QA and testing

## Acceptance checklist (all "yes")
- [ ] The brief is complete and approved by a human.
- [ ] There is a click driver (emotion / intrigue / awe / stakes / proof) — not "just pretty".
- [ ] The promise is in the video (timecode); no invented screenshots, replies or numbers.
- [ ] 120 px, 168×94, 320×180 — emotion, object and text read (`scripts/check.py`).
- [ ] Feed mock with real neighbours, dark and light theme: ours is found within 1 second (`scripts/feed_mock.py`).
- [ ] Stranger test: without the title — what is in the picture? With the title — what do you expect? Matches the video.
- [ ] Zones are clear; ≤ 3 elements; ≤ 3 colours; text ≤ 5 words and does not repeat the title.
- [ ] The person's face and body are original; no third-party logos; nothing explicit.
- [ ] Files: 1280×720 ≤ 2 MB + 3840×2160.

## A/B
- YouTube Test & Compare: up to 3 thumbnails; the winner is chosen by watch-time share. Needs advanced features and
  desktop Studio; may be unavailable for age-restricted videos.
- Test one variable at a time: face/no face, emotion, warm/cool palette, text/no text, light/dark background,
  gaze left/right. Or three different click drivers when you are searching for a direction.
- After 24–48 h: weak CTR on normal impressions → swap to the backup pair; when news shifts — refresh title and thumbnail.

## Lessons from real clients
- "A frame + caption", a flat "before/after", "how we shot it" without emotion — rejected: no intrigue, no wow.
- A hero in a beautiful location — "fine, but no emotion": it needs peak emotion and light, not just a nice frame.
- Clients approve the brief, not the drawing: layout, palette and accents come first.
