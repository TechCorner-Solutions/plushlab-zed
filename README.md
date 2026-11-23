<p align="center"><img src="assets/banner.png" alt="PlushLab for Zed: PlushLab Night, PlushLab Day and PlushLab Icons"></p>

# PlushLab for Zed

PlushLab's colours in your editor: the night sky (`#07071a`) and the one pale
indigo accent (`#a5b0f8`), with mint for what's added and rose for what's
gone — the same as the app (see `DESIGN.md` in PlushLab).

- **PlushLab Night** — the dark theme, as the app.
- **PlushLab Day** — a light one from the logo's light colours.
- **PlushLab Icons** (and **PlushLab Icons Light**) — folders with cat ears,
  the PlushLab cat on READMEs and `CLAUDE.md` / `AGENTS.md`, and an icon per
  kind of file (TypeScript, React, JSON, Markdown, CSS, images, git, env,
  Docker, SQL, shell, Rust, Python, Go, tests, lock files…).

## Install (from this folder)

1. In Zed: ⌘⇧P › **zed: install dev extension**, and pick this folder
   (`~/Projects/PlushLab-Zed`).
2. ⌘K ⌘T › **PlushLab Night** (or Day).
3. ⌘⇧P › **icon theme selector: toggle** › **PlushLab Icons**.

Or in `~/.config/zed/settings.json`:

```json
{
  "theme": { "mode": "system", "dark": "PlushLab Night", "light": "PlushLab Day" },
  "icon_theme": { "mode": "system", "dark": "PlushLab Icons", "light": "PlushLab Icons Light" }
}
```

## Changing it

The files are generated: change the colours in `scripts/build-themes.py`, the
icons and which files get them in `scripts/build-icons.py`, then

```sh
python3 scripts/build-themes.py   # themes/plushlab.json
python3 scripts/build-icons.py    # icons/*.svg and icon_themes/plushlab-icons.json
python3 scripts/build-banner.py   # assets/banner.svg and .png (needs Google Chrome)
```

and ⌘⇧P › **zed: rebuild dev extension**. Icons are 16×16 SVGs in the app's
colours (`DESIGN.md` in PlushLab-App).
