---
date: 2026-10-22
project: claude-build-day
tags: [learning, 3d, game]
---
Project:: [[PROJECT]]
Related:: [[FEAT - Feed or Dont game]]

In a behind-the-player runner, ground within `d * headHeight / (camHeight - headHeight)` of the player is hidden behind the player's head (d = camera distance behind). With cam 3.4 m up and 6.5 m back that was 13.6 m, which hid every cat in the feeding range. Fix: camera 6.2 m up, 5 m back, pitched about 27 degrees down, focal length lowered so feet and horizon both fit. Check this formula before tuning visuals.
