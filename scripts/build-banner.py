"""
The repository's banner (GitHub's social preview, 1280×640): the PlushLab cat
and name on the left, a Zed window in PlushLab Night with PlushLab Icons on
the right. Writes assets/banner.svg and renders assets/banner.png with
Google Chrome (headless), with the app's fonts (DM Sans, Geist Mono).

    python3 scripts/build-banner.py
"""
import html, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1280, 640
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

N = dict(bg="#07071a", panel="#0d0d24", card="#15153a", border="#22224f", text="#e6e8f5", heading="#f4f5fb", body="#b9bcd6",
         muted="#8d90b5", faint="#4a4c78", accent="#a5b0f8", mint="#6ee7b7", sky="#7dd3fc", amber="#fcd34d", peach="#fdba74",
         pink="#f0abfc", comment="#6b6e96", punct="#8d90b5", prop="#c8cefc")

_n = 0
def icon(name, x, y, size):
    """An icon from icons/, placed at x,y and scaled to `size`."""
    global _n
    _n += 1
    body = open(os.path.join(ROOT, "icons", f"{name}.svg")).read()
    inner = re.sub(r"^<svg[^>]*>", "", body.strip()).replace("</svg>", "")
    inner = inner.replace('id="g"', f'id="g{_n}"').replace("url(#g)", f"url(#g{_n})")
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 16 16" fill="none">{inner}</svg>'

def logo(x, y, size):
    body = open(os.path.join(ROOT, "logo.svg")).read()
    inner = re.sub(r"^<svg[^>]*>", "", body.strip()).replace("</svg>", "")
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 64 64">{inner}</svg>'

def text(x, y, s, size, color, weight=400, family="DM Sans", anchor="start", spacing=0):
    return (f'<text x="{x}" y="{y}" font-family="{family}, Inter, -apple-system, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}" letter-spacing="{spacing}">{html.escape(s)}</text>')

def chip(x, y, label, dot):
    w = 22 + len(label) * 8.6 + 16
    return (f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="17" fill="{N["card"]}" stroke="{N["border"]}"/>'
            f'<circle cx="{x + 18}" cy="{y + 17}" r="5" fill="{dot}"/>'
            + text(x + 30, y + 22, label, 15, N["body"], 500)), w

parts = []
# Night sky: two soft glows of the accent and a few stars.
parts.append(f'''<defs>
  <radialGradient id="glow1" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{N["accent"]}" stop-opacity=".22"/><stop offset="1" stop-color="{N["accent"]}" stop-opacity="0"/></radialGradient>
  <radialGradient id="glow2" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{N["mint"]}" stop-opacity=".09"/><stop offset="1" stop-color="{N["mint"]}" stop-opacity="0"/></radialGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{N["panel"]}"/><stop offset="1" stop-color="{N["bg"]}"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="{N["bg"]}"/>
<circle cx="930" cy="300" r="470" fill="url(#glow1)"/>
<circle cx="140" cy="620" r="360" fill="url(#glow2)"/>''')
for (sx, sy, r, o) in [(70, 60, 1.4, .5), (420, 90, 1, .35), (560, 40, 1.6, .45), (330, 560, 1.2, .3), (1230, 70, 1.3, .4),
                        (1180, 600, 1, .3), (610, 600, 1.4, .35), (40, 380, 1, .3), (250, 30, 1, .3), (1250, 330, 1.1, .3)]:
    parts.append(f'<circle cx="{sx}" cy="{sy}" r="{r}" fill="{N["heading"]}" opacity="{o}"/>')

# Left: the cat, the name, what's inside.
parts.append(logo(80, 128, 104))
parts.append(text(80, 300, "PlushLab", 72, N["heading"], 500, spacing=-1.5))
parts.append(text(80, 362, "for Zed", 72, N["accent"], 400, spacing=-1.5))
parts.append(text(82, 418, "The night sky and one pale indigo,", 22, N["body"]))
parts.append(text(82, 448, "with file icons that have the cat.", 22, N["body"]))
x = 80
for label, dot in [("PlushLab Night", N["accent"]), ("PlushLab Day", "#d9ddfe"), ("PlushLab Icons", N["mint"])]:
    c, w = chip(x, 486, label, dot)
    parts.append(c)
    x += w + 10

# Right: a Zed window in PlushLab Night.
wx, wy, ww, wh = 620, 96, 600, 448
parts.append(f'<rect x="{wx}" y="{wy + 10}" width="{ww}" height="{wh}" rx="18" fill="#000" opacity=".35"/>')
parts.append(f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" rx="16" fill="{N["bg"]}" stroke="{N["border"]}"/>')
parts.append(f'<path d="M{wx} {wy + 16} a16 16 0 0 1 16 -16 H{wx + ww - 16} a16 16 0 0 1 16 16 V{wy + 40} H{wx} Z" fill="{N["panel"]}"/>')
for i, col in enumerate(["#fca5a5", "#fcd34d", "#6ee7b7"]):
    parts.append(f'<circle cx="{wx + 22 + i * 18}" cy="{wy + 20}" r="5.5" fill="{col}" opacity=".85"/>')
parts.append(text(wx + ww / 2, wy + 25, "plushlab — page.tsx", 13, N["muted"], 400, anchor="middle"))
parts.append(f'<line x1="{wx}" y1="{wy + 40}" x2="{wx + ww}" y2="{wy + 40}" stroke="{N["border"]}"/>')

# The project panel, with PlushLab Icons.
px, pw = wx, 206
parts.append(f'<path d="M{px} {wy + 41} H{px + pw} V{wy + wh} H{px + 16} a16 16 0 0 1 -16 -16 Z" fill="{N["panel"]}"/>')
parts.append(f'<line x1="{px + pw}" y1="{wy + 41}" x2="{px + pw}" y2="{wy + wh}" stroke="{N["border"]}"/>')
tree = [
    (0, "chevron-down", "folder-open", "plushlab", False),
    (1, "chevron-down", "folder-open", "src", False),
    (2, "chevron-right", "folder", "components", False),
    (2, None, "react", "page.tsx", True),
    (2, None, "typescript", "route.ts", False),
    (2, None, "css", "globals.css", False),
    (1, "chevron-right", "folder", "public", False),
    (1, None, "env", ".env", False),
    (1, None, "plushlab", "README.md", False),
    (1, None, "markdown", "DESIGN.md", False),
    (1, None, "json", "package.json", False),
    (1, None, "docker", "Dockerfile", False),
    (1, None, "git", ".gitignore", False),
]
ty = wy + 58
for depth, chevron, ico, name, selected in tree:
    rx = px + 12 + depth * 14
    if selected:
        parts.append(f'<rect x="{px + 6}" y="{ty - 3}" width="{pw - 12}" height="26" rx="6" fill="{N["accent"]}" opacity=".16"/>')
    if chevron:
        parts.append(icon(chevron, rx, ty + 3, 14))
    parts.append(icon(ico, rx + 16, ty + 1, 18))
    parts.append(text(rx + 40, ty + 15, name, 14, N["heading"] if selected else N["text"] if chevron else N["body"], 400))
    ty += 28

# The editor: a tab, line numbers, code in PlushLab Night's colours.
ex = px + pw
parts.append(f'<rect x="{ex}" y="{wy + 41}" width="{ww - pw}" height="34" fill="{N["panel"]}"/>')
parts.append(f'<rect x="{ex}" y="{wy + 41}" width="138" height="34" fill="{N["bg"]}"/>')
parts.append(f'<line x1="{ex}" y1="{wy + 75}" x2="{wx + ww}" y2="{wy + 75}" stroke="{N["border"]}"/>')
parts.append(f'<line x1="{ex + 138}" y1="{wy + 41}" x2="{ex + 138}" y2="{wy + 75}" stroke="{N["border"]}"/>')
parts.append(icon("react", ex + 14, wy + 50, 16))
parts.append(text(ex + 38, wy + 63, "page.tsx", 13, N["heading"], 500))

K, F, S, NUM, T, C, P, V, PR, TG = N["accent"], N["sky"], N["mint"], N["peach"], N["amber"], N["comment"], N["punct"], N["text"], N["prop"], N["pink"]
code = [
    [("import", K), (" { ", P), ("Plush", V), (" } ", P), ("from", K), (' "@/lab"', S), (";", P)],
    [],
    [("// A cat that ships on time.", C)],
    [("export", K), (" ", V), ("function", K), (" ", V), ("Purr", F), ("({ ", P), ("name", V), (" }: ", P), ("Props", T), (") {", P)],
    [("  ", V), ("const", K), (" naps ", V), ("=", K), (" ", V), ("3", NUM), (";", P)],
    [("  ", V), ("return", K), (" (", P)],
    [("    <", P), ("Plush", TG), (" mood", PR), ("=", P), ('"calm"', S), (" naps", PR), ("={", P), ("naps", V), ("}>", P)],
    [("      {", P), ("name", V), ("}", P)],
    [("    </", P), ("Plush", TG), (">", P)],
    [("  );", P)],
    [("}", P)],
]
cy = wy + 104
for i, line in enumerate(code):
    active = i == 4
    if active:
        parts.append(f'<rect x="{ex + 1}" y="{cy - 17}" width="{ww - pw - 1}" height="26" fill="{N["accent"]}" opacity=".06"/>')
    parts.append(text(ex + 34, cy, str(i + 1), 13, N["accent"] if active else N["faint"], 400, "Geist Mono", "end"))
    italic = ' font-style="italic"'
    spans = "".join(f'<tspan fill="{c}"{italic if c == C else ""}>{html.escape(s)}</tspan>' for s, c in line)
    parts.append(f'<text x="{ex + 50}" y="{cy}" font-family="Geist Mono, SF Mono, Menlo, monospace" font-size="14" xml:space="preserve">{spans}</text>')
    if active:
        parts.append(f'<rect x="{ex + 50 + 18 * 8.4}" y="{cy - 14}" width="2" height="18" fill="{N["accent"]}"/>')
    cy += 28

# The status bar.
parts.append(f'<path d="M{ex} {wy + wh - 30} H{wx + ww} V{wy + wh - 16} a16 16 0 0 1 -16 16 H{ex} Z" fill="{N["panel"]}"/>')
parts.append(f'<line x1="{ex}" y1="{wy + wh - 30}" x2="{wx + ww}" y2="{wy + wh - 30}" stroke="{N["border"]}"/>')
parts.append(f'<circle cx="{ex + 18}" cy="{wy + wh - 15}" r="4" fill="{N["mint"]}"/>')
parts.append(text(ex + 30, wy + wh - 10, "PlushLab Night", 12, N["muted"]))
parts.append(text(wx + ww - 16, wy + wh - 10, "TypeScript React", 12, N["muted"], anchor="end"))

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">' + "".join(parts) + "</svg>\n"
assets = os.path.join(ROOT, "assets")
os.makedirs(assets, exist_ok=True)
open(os.path.join(assets, "banner.svg"), "w").write(svg)

# Render with the app's fonts.
page = os.path.join(assets, ".banner.html")
open(page, "w").write(
    '<!doctype html><html><head><meta charset="utf-8">'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=Geist+Mono&display=block">'
    '<style>html,body{margin:0;background:#07071a}svg{display:block}</style></head><body>' + svg + "</body></html>"
)
png = os.path.join(assets, "banner.png")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={W},{H}", "--virtual-time-budget=4000",
                f"--screenshot={png}", f"file://{page}"], check=True, capture_output=True)
os.remove(page)
print("assets/banner.svg, assets/banner.png")
