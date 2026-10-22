# Save Cats Morocco: Feed or Don't

A 3D street runner made for Claude Community Build Day. Walk a colourful Moroccan medina and feed the street cats, but only when the police aren't looking. Under Morocco's Law 19.25 (2026), feeding stray animals in public can cost a fine of 500 to 2,000 MAD.

## Play

Open `feed-or-dont.html` in a browser. It is a single file with Three.js inlined, so it works offline. A decent GPU is recommended.

| Key | Action |
| --- | --- |
| Hold Up / W | Walk (release to stop) |
| Left / Right | Change lane |
| Space | Feed the cat ahead of you |
| Shift / J | Jump over crates |
| C | Switch third / first person |
| P | Pause |
| M | Sound on / off |

Police watch from windows and alleys, walk down the street and cross it. A yellow `!` warns you before they look; a yellow cone on the ground shows exactly what they can see.

## Files

- `feed-or-dont.html`: the game (built file, open this).
- `src/feed-or-dont.src.html`: game source. Run `python build.py` to inline `vendor/three.min.js` and regenerate the game file.
- `feed-or-dont-retro.html`, `feed-or-dont-2d.html`: earlier blocky 3D and 2D pixel versions, kept as fallbacks.
- `star-system.html`: an unrelated build-day warm-up (Newtonian star system simulation).

## Credits

Three.js r149 (MIT), see `vendor/THREE-LICENSE.txt`. Everything else (models, textures, music) is generated in code.
