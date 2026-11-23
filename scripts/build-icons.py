import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I = os.path.join(ROOT, "icons")

def svg(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">{body}</svg>\n'

# A folder with two cat ears on its tab; open = lid tilted forward.
def folder(color, ink):
    return svg(
        f'<path d="M1.5 4.5 L2.4 2.2 L3.6 3.4 H5.2 L6.4 2.2 L7.3 4.5 H13.2 a1.3 1.3 0 0 1 1.3 1.3 V12 a1.5 1.5 0 0 1 -1.5 1.5 H3 a1.5 1.5 0 0 1 -1.5 -1.5 Z" fill="{color}"/>'
        f'<path d="M5.6 10.3 q0.9 -0.9 1.8 0 M8.6 10.3 q0.9 -0.9 1.8 0" stroke="{ink}" stroke-width="0.9" stroke-linecap="round"/>'
    )

def folder_open(color, ink):
    return svg(
        f'<path d="M1.5 4.5 L2.4 2.2 L3.6 3.4 H5.2 L6.4 2.2 L7.3 4.5 H12.5 a1 1 0 0 1 1 1 V7 H4.2 a1 1 0 0 0 -0.95 0.7 L1.5 12.6 Z" fill="{color}" opacity=".55"/>'
        f'<path d="M3.4 7.6 H14.6 a0.6 0.6 0 0 1 0.57 0.8 L13.6 12.9 a0.9 0.9 0 0 1 -0.85 0.6 H2.2 a0.6 0.6 0 0 1 -0.57 -0.8 L2.9 7.95 a0.55 0.55 0 0 1 0.5 -0.35 Z" fill="{color}"/>'
        f'<path d="M6 11.2 q0.9 -0.9 1.8 0 M9 11.2 q0.9 -0.9 1.8 0" stroke="{ink}" stroke-width="0.9" stroke-linecap="round"/>'
    )

def page(color, glyph=""):
    return svg(
        f'<path d="M3.5 1.5 H9.5 L12.5 4.5 V13.5 a1 1 0 0 1 -1 1 H3.5 a1 1 0 0 1 -1 -1 V2.5 a1 1 0 0 1 1 -1 Z" stroke="{color}" stroke-width="1.1" stroke-linejoin="round"/>'
        f'<path d="M9.5 1.5 V4.5 H12.5" stroke="{color}" stroke-width="1.1" stroke-linejoin="round"/>' + glyph
    )

def badge(color, glyph):
    return svg(f'<rect x="1.5" y="1.5" width="13" height="13" rx="3" fill="{color}"/>' + glyph)

INK = "#07071a"
C = dict(indigo="#a5b0f8", muted="#8d90b5", mint="#6ee7b7", sky="#7dd3fc", amber="#fcd34d", peach="#fdba74", pink="#f0abfc", rose="#fca5a5")

icons = {
    "folder": folder(C["indigo"], INK),
    "folder-open": folder_open(C["indigo"], INK),
    "folder-light": folder("#7c85e8", "#ffffff"),
    "folder-open-light": folder_open("#7c85e8", "#ffffff"),
    "chevron-right": svg('<path d="M6 4 L10 8 L6 12" stroke="#8d90b5" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>'),
    "chevron-down": svg('<path d="M4 6 L8 10 L12 6" stroke="#8d90b5" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>'),
    "file": page(C["muted"]),
    # The PlushLab cat (the brand mark, simplified for 16px): READMEs and PlushLab files.
    "plushlab": svg(
        '<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9ddfe"/><stop offset="1" stop-color="#8f98ef"/></linearGradient></defs>'
        '<path d="M11.6 11.2 C13.5 11.2 14.1 12.2 14.1 13.5 C14.1 14.7 14.5 15.2 15.3 14.8" stroke="#a5b0f8" stroke-width="1.1" stroke-linecap="round"/>'
        '<path d="M1.3 5.6 L2.3 1.9 L4.8 4 H8.3 L10.8 1.9 L11.8 5.6 V10.5 a2.3 2.3 0 0 1 -2.3 2.3 H3.6 a2.3 2.3 0 0 1 -2.3 -2.3 Z" fill="url(#g)"/>'
        '<path d="M4 10.2 q0.9 -0.9 1.8 0 M7.8 10.2 q0.9 -0.9 1.8 0" stroke="#07071a" stroke-width="0.8" stroke-linecap="round"/>'
    ),
    "typescript": badge(C["sky"], f'<path d="M4.2 6 H8.8 M6.5 6 V11.5" stroke="{INK}" stroke-width="1.5" stroke-linecap="round"/><path d="M12 6.3 a1.6 1.4 0 1 0 -1.6 1.6 a1.6 1.4 0 1 1 -1.6 1.9" stroke="{INK}" stroke-width="1.3" stroke-linecap="round"/>'),
    "javascript": badge(C["amber"], f'<path d="M7 5.5 V10 a1.6 1.6 0 0 1 -3 0.8" stroke="{INK}" stroke-width="1.5" stroke-linecap="round"/><path d="M12.2 6.3 a1.6 1.4 0 1 0 -1.6 1.6 a1.6 1.4 0 1 1 -1.6 1.9" stroke="{INK}" stroke-width="1.3" stroke-linecap="round"/>'),
    "react": svg(f'<ellipse cx="8" cy="8" rx="6.5" ry="2.6" stroke="{C["sky"]}" stroke-width="1"/><ellipse cx="8" cy="8" rx="6.5" ry="2.6" stroke="{C["sky"]}" stroke-width="1" transform="rotate(60 8 8)"/><ellipse cx="8" cy="8" rx="6.5" ry="2.6" stroke="{C["sky"]}" stroke-width="1" transform="rotate(-60 8 8)"/><circle cx="8" cy="8" r="1.3" fill="{C["sky"]}"/>'),
    "json": svg(f'<path d="M5.5 2.5 C3.8 2.5 4.3 6.8 2.5 8 C4.3 9.2 3.8 13.5 5.5 13.5 M10.5 2.5 C12.2 2.5 11.7 6.8 13.5 8 C11.7 9.2 12.2 13.5 10.5 13.5" stroke="{C["amber"]}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>'),
    "markdown": page(C["indigo"], f'<path d="M5 11 V7.5 L6.5 9.2 L8 7.5 V11" stroke="{C["indigo"]}" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 7.5 V11 M9 10 L10 11 L11 10" stroke="{C["indigo"]}" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/>'),
    "css": svg(f'<path d="M6 2.5 L4.8 13.5 M11.2 2.5 L10 13.5 M2.8 5.8 H13.6 M2.4 10.2 H13.2" stroke="{C["pink"]}" stroke-width="1.3" stroke-linecap="round"/>'),
    "html": svg(f'<path d="M5.5 4 L1.8 8 L5.5 12 M10.5 4 L14.2 8 L10.5 12" stroke="{C["peach"]}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 3 L7 13" stroke="{C["peach"]}" stroke-width="1.1" stroke-linecap="round" opacity=".6"/>'),
    "image": svg(f'<rect x="1.8" y="2.8" width="12.4" height="10.4" rx="1.8" stroke="{C["mint"]}" stroke-width="1.1"/><circle cx="10.6" cy="6" r="1.2" fill="{C["mint"]}"/><path d="M2.4 12 L6 8.2 L9 11 L10.6 9.6 L13.8 12.4" stroke="{C["mint"]}" stroke-width="1.1" stroke-linejoin="round"/>'),
    "git": svg(f'<circle cx="4.5" cy="3.5" r="1.6" stroke="{C["rose"]}" stroke-width="1.1"/><circle cx="4.5" cy="12.5" r="1.6" stroke="{C["rose"]}" stroke-width="1.1"/><circle cx="11.5" cy="5.5" r="1.6" stroke="{C["rose"]}" stroke-width="1.1"/><path d="M4.5 5.1 V10.9 M11.5 7.1 C11.5 9.5 8 9 4.9 10.9" stroke="{C["rose"]}" stroke-width="1.1" stroke-linecap="round"/>'),
    "lock": svg(f'<rect x="3" y="7" width="10" height="7" rx="1.6" stroke="{C["muted"]}" stroke-width="1.1"/><path d="M5.2 7 V5 a2.8 2.8 0 0 1 5.6 0 V7" stroke="{C["muted"]}" stroke-width="1.1"/><circle cx="8" cy="10.4" r="0.9" fill="{C["muted"]}"/>'),
    "config": svg(f'<path d="M2.5 4.5 H13.5 M2.5 8 H13.5 M2.5 11.5 H13.5" stroke="{C["indigo"]}" stroke-width="1.1" stroke-linecap="round" opacity=".55"/><circle cx="10" cy="4.5" r="1.6" fill="{C["indigo"]}"/><circle cx="5.5" cy="8" r="1.6" fill="{C["indigo"]}"/><circle cx="11" cy="11.5" r="1.6" fill="{C["indigo"]}"/>'),
    "env": svg(f'<circle cx="5" cy="8" r="2.8" stroke="{C["amber"]}" stroke-width="1.2"/><path d="M7.8 8 H14 M12 8 V10.3 M14 8 V9.8" stroke="{C["amber"]}" stroke-width="1.2" stroke-linecap="round"/>'),
    "database": svg(f'<ellipse cx="8" cy="3.8" rx="5" ry="1.9" stroke="{C["mint"]}" stroke-width="1.1"/><path d="M3 3.8 V12.2 c0 1.05 2.24 1.9 5 1.9 s5 -0.85 5 -1.9 V3.8 M3 8 c0 1.05 2.24 1.9 5 1.9 s5 -0.85 5 -1.9" stroke="{C["mint"]}" stroke-width="1.1"/>'),
    "docker": svg(f'<path d="M1.8 8.6 H13.4 c0.9 0 1.5 -0.9 1.2 -1.6 c-0.8 0.2 -1.5 0 -1.7 -0.6 C12 11.8 8.8 13.5 5.8 13.5 C3.4 13.5 2 11.4 1.8 8.6 Z" stroke="{C["sky"]}" stroke-width="1.1" stroke-linejoin="round"/><path d="M3.5 6.2 H5.7 V8.4 H3.5 Z M6.2 6.2 H8.4 V8.4 H6.2 Z M8.9 6.2 H11.1 V8.4 H8.9 Z M6.2 3.6 H8.4 V5.8 H6.2 Z" fill="{C["sky"]}"/>'),
    "shell": svg(f'<rect x="1.5" y="2.5" width="13" height="11" rx="2" stroke="{C["mint"]}" stroke-width="1.1"/><path d="M4.2 6.2 L6.4 8 L4.2 9.8 M7.8 10.4 H11.6" stroke="{C["mint"]}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>'),
    "rust": svg(f'<circle cx="8" cy="8" r="4.6" stroke="{C["peach"]}" stroke-width="1.2"/><circle cx="8" cy="8" r="1.6" fill="{C["peach"]}"/>' + "".join(f'<rect x="7.3" y="0.9" width="1.4" height="2.2" rx="0.4" fill="{C["peach"]}" transform="rotate({d} 8 8)"/>' for d in range(0, 360, 45))),
    "python": svg(f'<path d="M8 1.8 H6 a2 2 0 0 0 -2 2 V6 H8.5 V6.7 H3.6 a2 2 0 0 0 -2 2 V10 a2 2 0 0 0 2 2 H4.6 V9.8 a1.8 1.8 0 0 1 1.8 -1.8 H9.7 a1.8 1.8 0 0 0 1.8 -1.8 V3.8 a2 2 0 0 0 -2 -2 Z" fill="{C["sky"]}"/><path d="M8 14.2 H10 a2 2 0 0 0 2 -2 V10 H7.5 V9.3 H12.4 a2 2 0 0 0 2 -2 V6 a2 2 0 0 0 -2 -2 H11.4 V6.2 a1.8 1.8 0 0 1 -1.8 1.8 H6.3 a1.8 1.8 0 0 0 -1.8 1.8 V12.2 a2 2 0 0 0 2 2 Z" fill="{C["amber"]}"/>'),
    "go": svg(f'<path d="M1.5 6 H5 M0.8 8 H4 M1.5 10 H5" stroke="{C["sky"]}" stroke-width="1.1" stroke-linecap="round"/><circle cx="10" cy="8" r="4.3" stroke="{C["sky"]}" stroke-width="1.3"/><circle cx="10" cy="8" r="1.3" fill="{C["sky"]}"/>'),
    "text": page(C["muted"], f'<path d="M5 7.5 H10 M5 9.5 H10 M5 11.5 H8" stroke="{C["muted"]}" stroke-width="1" stroke-linecap="round"/>'),
    "test": svg(f'<path d="M6 1.8 V6.2 L2.6 12.6 a1 1 0 0 0 0.9 1.5 H12.5 a1 1 0 0 0 0.9 -1.5 L10 6.2 V1.8 M5 1.8 H11" stroke="{C["mint"]}" stroke-width="1.1" stroke-linejoin="round" stroke-linecap="round"/><path d="M4.2 10 H11.8" stroke="{C["mint"]}" stroke-width="1.1"/>'),
}
for name, body in icons.items():
    open(os.path.join(I, f"{name}.svg"), "w").write(body)

suffixes = {
    "ts": "typescript", "mts": "typescript", "cts": "typescript",
    "js": "javascript", "mjs": "javascript", "cjs": "javascript",
    "tsx": "react", "jsx": "react",
    "json": "json", "jsonc": "json", "json5": "json",
    "md": "markdown", "mdx": "markdown",
    "css": "css", "scss": "css", "sass": "css", "less": "css",
    "html": "html", "htm": "html", "svg": "image",
    "png": "image", "jpg": "image", "jpeg": "image", "gif": "image", "webp": "image", "ico": "image", "avif": "image",
    "lock": "lock",
    "toml": "config", "yaml": "config", "yml": "config", "ini": "config", "conf": "config", "xml": "config",
    "env": "env",
    "sql": "database", "prisma": "database", "db": "database", "sqlite": "database",
    "sh": "shell", "bash": "shell", "zsh": "shell", "fish": "shell",
    "rs": "rust", "py": "python", "go": "go",
    "txt": "text", "log": "text",
    "test.ts": "test", "test.tsx": "test", "spec.ts": "test", "spec.tsx": "test", "test.js": "test",
}
stems = {
    "README": "plushlab", "README.md": "plushlab", "CLAUDE.md": "plushlab", "AGENTS.md": "plushlab", "DESIGN.md": "plushlab",
    ".gitignore": "git", ".gitattributes": "git", ".gitmodules": "git",
    "Dockerfile": "docker", "docker-compose.yml": "docker", "docker-compose.yaml": "docker", "compose.yml": "docker", "compose.yaml": "docker",
    ".env": "env", ".env.local": "env", ".env.example": "env", ".env.production": "env",
    "package-lock.json": "lock", "pnpm-lock.yaml": "lock", "yarn.lock": "lock", "Cargo.lock": "lock", "go.sum": "lock",
    "Makefile": "shell", "LICENSE": "text",
}
keys = sorted(set(suffixes.values()) | set(stems.values()) | {"default"})
file_icons = {k: {"path": f"./icons/{'file' if k == 'default' else k}.svg"} for k in keys}

def theme(name, appearance, light):
    f = "folder-light" if light else "folder"
    o = "folder-open-light" if light else "folder-open"
    return {
        "name": name,
        "appearance": appearance,
        "directory_icons": {"collapsed": f"./icons/{f}.svg", "expanded": f"./icons/{o}.svg"},
        "chevron_icons": {"collapsed": "./icons/chevron-right.svg", "expanded": "./icons/chevron-down.svg"},
        "file_stems": stems,
        "file_suffixes": suffixes,
        "file_icons": file_icons,
    }

out = {"$schema": "https://zed.dev/schema/icon_themes/v0.3.0.json", "name": "PlushLab Icons", "author": "PlushLab",
       "themes": [theme("PlushLab Icons", "dark", False), theme("PlushLab Icons Light", "light", True)]}
json.dump(out, open(os.path.join(ROOT, "icon_themes/plushlab-icons.json"), "w"), indent=2)
print(len(icons), "icons;", len(keys), "file types")
