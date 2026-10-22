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

## v0.5.0: intro, difficulty, cameras, points, leaderboard
- LEVELS table drives spawn chance (chance(base) * police), hiddenTime / look, warnTime * warn, fine range, points multiplier.
- Security camera = wall watcher with CONE [2, 5.5]; window/alley CONE [3, 8]. sees() and cone meshes both read CONE.
- Score = feed points (100 + 20 per streak step, cap 10) * mult + distance/2 * mult. TITLES thresholds 0/400/1200/2500/5000/9000.
- Leaderboard: localStorage `feed-or-dont-board-v1`, entries validated on load, names stripped of control chars and < >, rendered with textContent. Verified a hostile name renders as text.
- Headless screenshots time out on GPU-less browser; capture via renderer.domElement.toDataURL right after render instead.

## v0.6.0: phones
- TOUCH = pointer:coarse or maxTouchPoints; body.touch shows #touchUI and touch help, lowers pixel ratio/shadows/fog.
- Walking input = held.up || touchWalk || tiltWalk. Swipes re-arm inside one drag. Tilt maps beta/gamma by screen orientation angle, calibrated to the pose when tilt is switched on; iOS needs DeviceOrientationEvent.requestPermission from a tap, and HTTPS.
- GitHub Pages serves the repo root; index.html redirects to feed-or-dont.html.

## v0.7.0: emotion
- player.feed = { cat, phase: approach -> kneel -> eat }, FEED_GAP 1.75 m; sees() checked every frame while feeding.
- finishFeed(): hearts (sprite particles), #warm flash, caption, setMood happy, cheer. bust(): cat.flee, spawnOfficer (reuses nearby walking cop position), body.sad CSS desaturation, updateCaught timeline (card after 2.4 s), endCaught().
- Faces: makeFace({expressive}) returns brows/smile/grin/frown/tear kept out of mergeStatic so setMood can toggle them.
- Cinematic camera blends toward shot targets with `cine`; side shot for feeding, two-shot for caught.
