# Save Cats Morocco: Feed or Don't

A 3D street runner made for Claude Community Build Day. Walk a colourful Moroccan medina and feed the street cats, but only when the police aren't looking. Under Morocco's Law 19.25 (2026), feeding stray animals in public can cost a fine of 500 to 2,000 MAD.

## Play

Play online (phone or computer): https://khalidelmerrah.github.io/Save-Cats-Morocco/

Or open `feed-or-dont.html` in a browser. It is a single file with Three.js inlined, so it works offline. A decent GPU is recommended.

On a phone: hold your thumb on the screen to walk, swipe left or right to change lane, swipe up to jump, and tap Feed. Tap "Tilt" to steer by leaning the phone instead (needs the HTTPS link above).

| Key | Action |
| --- | --- |
| Hold Up / W | Walk (release to stop) |
| Left / Right | Change lane |
| Space | Feed the cat ahead of you |
| Shift / J | Jump over crates |
| C | Switch third / first person |
| P | Pause |
| M | Sound on / off |

The game opens with a short intro on what Law 19.25 says and why it is debated. Pick Easy, Normal or Hard (keys 1 to 3); harder levels have more watchers and multiply your points.

Police watch from windows and alleys, walk down the street and cross it, and security cameras film it. A yellow `!` warns you before they look; a red cone on the ground shows exactly what they can see.

Feeding cats earns points, with a bonus for streaks. Your score earns titles from Passer-by up to Saver of Cats and Legend of the Strays, and the top 10 scores are kept on this device's leaderboard.

## Files

- `feed-or-dont.html`: the game (built file, open this).
- `src/feed-or-dont.src.html`: game source. Run `python build.py` to inline `vendor/three.min.js` and regenerate the game file.
- `feed-or-dont-retro.html`, `feed-or-dont-2d.html`: earlier blocky 3D and 2D pixel versions, kept as fallbacks.
- `star-system.html`: an unrelated build-day warm-up (Newtonian star system simulation).

## Credits

Three.js r149 (MIT), see `vendor/THREE-LICENSE.txt`. Everything else (models, textures, music) is generated in code.
