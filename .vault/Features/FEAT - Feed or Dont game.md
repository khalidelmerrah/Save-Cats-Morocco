---
date: 2026-10-22
project: claude-build-day
status: done
tags: [feature, game]
---
Project:: [[PROJECT]]
Session:: [[2026-10-22 - Halcyra star system]]

## What
`feed-or-dont.html`, a single-file retro stealth game for Claude Community Build Day. Satire of Morocco's Law 19.25 (adopted July 2026; fine for feeding strays in public 500 to 2,000 MAD).

## How
- 320x180 buffer, integer-scaled canvas, sprites as string arrays, own 3x5 font (M, N, W wider).
- Watchers cycle hidden -> warn -> watch; caught only while feeding inside the cone width at the player's feet.
- Street layout seeded (same every game); watcher timing random and tightens as more cats are fed.
- Lose at empty wallet (start 6,000 MAD) or three hungry cats.

## Verified (Chromium, scripted)
Feeding, bust and fine, safe just outside the cone, three-hungry game over, title and over screens render.

## v0.3.0: 3D runner rewrite
- User preferred 3D retro over 2D, asked for more vibrant colours and bigger visuals. 2D kept as `feed-or-dont-2d.html`.
- Software renderer: camera-space transform, near-plane clip, painter's order (ground, buildings far to near, cones, items far to near), per-face flat shading plus distance fog to a haze colour.
- Rules verified by script: window cop watching -> caught; hidden -> safe; walker back turned -> safe, facing -> caught; bump cop -> fine; jump clears crate.

## v0.4.0: Three.js cartoon rebuild
- User found the box renderer too Minecraft-like; chose Three.js inlined, stylized cartoon, camera toggle (C).
- Source in `src/`, `python build.py` inlines `vendor/three.min.js` (r149, last version with build/three.min.js and no deprecation warning).
- `mergeStatic()` merges static meshes per material per group; animated parts (limbs, shutters, cat head/tail, window cops) passed in a keep set.
- Headless test browser has no GPU (3 fps); logic verified by script, real-GPU performance not yet measured.
- Repo: https://github.com/khalidelmerrah/Save-Cats-Morocco (public).
