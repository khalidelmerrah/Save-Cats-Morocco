# Changelog

## [0.6.0] - 2026-10-22 (commit: 9a936c6)
### Added
- Phone and touch controls: hold a thumb to walk, swipe left or right to change lane, swipe up to jump, a big Feed button, on-screen Pause and Camera buttons.
- Optional tilt steering (device motion): lean forward to walk, left or right to pick a lane; asks for permission on iPhone.
- `index.html` redirect so the game opens at the GitHub Pages root.
### Changed
- Phone layout: compact HUD and cards, touch instructions on the menu, wider field of view in portrait.
- Lighter graphics on touch devices (pixel ratio 1.5, 1024 shadow map, shorter fog distance).

## [0.5.0] - 2026-10-22 (commit: 056045b)
### Added
- Intro slides explaining Law 19.25 (what it says, why it is debated, your turn); skippable, replayable via "About the law".
- Difficulty levels Easy / Normal / Hard (watcher density, how often they look, warning length, fine range, 1x/2x/3x points).
- Security cameras on walls: sweep, swivel to the street, red recording light.
- Points (cat fed, streak bonus, distance), live rank titles from Passer-by to Saver of Cats and Legend of the Strays.
- Local top-10 leaderboard with name entry (names sanitized, rendered as text).
- More cats, sometimes two per row.
### Changed
- Police density on Normal roughly halved; sight cones are now red.
- Characters: faces (eyes, brows, smile, cheeks), hoodie with hood and pocket, sneakers, police uniform with peaked cap, epaulettes, buttons, belt and holster; cats with inner ears, whiskers, stripes, white chests.
- Animation: torso twist and breathing, police turn their head before looking, cats look at you, hop and raise their tail when fed.

## [0.4.0] - 2026-10-22 (commit: c692238)
### Changed
- `feed-or-dont.html` rebuilt on Three.js r149 (inlined, still one offline file): smooth cartoon models with animated limbs, cats with ears and tails, swinging shutters, arched doors, zellige bands, striped awnings, soft shadows, clouds and a distant minaret.
- Modern HTML UI (HUD pills, title, caught, game-over cards) replaces the pixel font.
- Static geometry merged per building and prop (about 1,000 draw calls down to about 370).
### Added
- Camera toggle with C: third person (default) or first person.
- `src/feed-or-dont.src.html` + `build.py` + `vendor/three.min.js` build pipeline; README and .gitignore.
- `feed-or-dont-retro.html`: the previous blocky 3D version kept as a fallback.

## [0.3.1] - 2026-10-22 (commit: none, not a git repo)
### Changed
- `feed-or-dont.html`: you now control pace. Hold UP (or W) to walk, release to stop; top speed lowered from 18 to 6.5 m/s. Jump moved to Shift (or J). "Hold up to walk" prompt at the start.

## [0.3.0] - 2026-10-22 (commit: none, not a git repo)
### Changed
- `feed-or-dont.html` rewritten as a 3D low-poly street runner (Subway Surfers style) with its own tiny software 3D renderer, no libraries: three lanes, jump, toss food to cats, crates and fruit carts to dodge.
- Police now watch from windows and alleys, walk down the street and turn around, and cross the street; sight cones on the ground match the catch rules exactly.
- Vivid Moroccan palette (terracotta, saffron, Majorelle blue, emerald), high close camera, canvas fills the window.
### Added
- `feed-or-dont-2d.html`: the previous 2D version kept as a fallback.

## [0.2.0] - 2026-10-22 (commit: none, not a git repo)
### Added
- `feed-or-dont.html`: retro pixel-art stealth game about Morocco's Law 19.25. Feed street cats while police watch from windows, alleys, a cafe and a parked car; getting seen costs a 500 to 2,000 MAD fine.
- Telegraphed warnings (rattling shutters, eyes in alleys, lowering newspaper, cap over a car), sight cones, hunger meters, minimap, wallet and hungry-cat lose conditions, best score.
- Synthesized chiptune music and sound effects (Web Audio), custom 3x5 pixel font, keyboard controls.

## [0.1.0] - 2026-10-22 (commit: none, not a git repo)
### Added
- `star-system.html`: self-contained animated model of the fictional Halcyra system (one star, six planets) using velocity Verlet Newtonian gravity.
- Live table per planet: osculating semi-major axis, measured period, Kepler period, percentage difference; rows turn green within 1%.
- Total energy readout with drift since start, click-to-follow, scroll zoom, time-speed slider, add-random-planet button.
- Console self-test of period and energy accuracy on load.
