import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def a(hex6, alpha=1.0):
    return f"{hex6}{round(alpha * 255):02x}"

def theme(name, appearance, c):
    s = {
        "background.appearance": "opaque",
        "background": c["bg"], "surface.background": c["surface"], "elevated_surface.background": c["elevated"],
        "panel.background": c["panel"], "panel.focused_border": c["accent"],
        "border": c["border"], "border.variant": c["border_soft"], "border.focused": c["accent"], "border.selected": c["accent"],
        "border.transparent": "#00000000", "border.disabled": c["border_soft"],
        "element.background": c["element"], "element.hover": c["hover"], "element.active": c["active"], "element.selected": c["selected"], "element.disabled": c["element"],
        "ghost_element.background": "#00000000", "ghost_element.hover": c["hover"], "ghost_element.active": c["active"], "ghost_element.selected": c["selected"], "ghost_element.disabled": "#00000000",
        "drop_target.background": a(c["accent"], 0.15),
        "text": c["text"], "text.muted": c["muted"], "text.placeholder": c["placeholder"], "text.disabled": c["placeholder"], "text.accent": c["accent"],
        "icon": c["text_soft"], "icon.muted": c["muted"], "icon.disabled": c["placeholder"], "icon.placeholder": c["placeholder"], "icon.accent": c["accent"],
        "status_bar.background": c["chrome"], "title_bar.background": c["chrome"], "title_bar.inactive_background": c["chrome"],
        "toolbar.background": c["editor"], "tab_bar.background": c["chrome"], "tab.inactive_background": c["chrome"], "tab.active_background": c["editor"],
        "search.match_background": a(c["accent"], 0.25), "search.active_match_background": a(c["amber"], 0.35),
        "scrollbar.thumb.background": a(c["accent"], 0.18), "scrollbar.thumb.hover_background": a(c["accent"], 0.32), "scrollbar.thumb.border": "#00000000",
        "scrollbar.track.background": "#00000000", "scrollbar.track.border": "#00000000",
        "editor.foreground": c["text"], "editor.background": c["editor"], "editor.gutter.background": c["editor"],
        "editor.subheader.background": c["surface"], "editor.active_line.background": a(c["accent"], 0.06), "editor.highlighted_line.background": a(c["accent"], 0.1),
        "editor.line_number": c["line_number"], "editor.active_line_number": c["accent"], "editor.invisible": c["border"],
        "editor.wrap_guide": a(c["accent"], 0.08), "editor.active_wrap_guide": a(c["accent"], 0.16),
        "editor.document_highlight.read_background": a(c["accent"], 0.12), "editor.document_highlight.write_background": a(c["accent"], 0.2),
        "editor.indent_guide": a(c["accent"], 0.08), "editor.indent_guide_active": a(c["accent"], 0.22),
        "terminal.background": c["editor"], "terminal.foreground": c["text"], "terminal.bright_foreground": c["heading"], "terminal.dim_foreground": c["muted"],
        "link_text.hover": c["accent"],
        "conflict": c["amber"], "conflict.background": a(c["amber"], 0.12), "conflict.border": a(c["amber"], 0.4),
        "created": c["green"], "created.background": a(c["green"], 0.12), "created.border": a(c["green"], 0.4),
        "deleted": c["red"], "deleted.background": a(c["red"], 0.12), "deleted.border": a(c["red"], 0.4),
        "modified": c["amber"], "modified.background": a(c["amber"], 0.12), "modified.border": a(c["amber"], 0.4),
        "error": c["red"], "error.background": a(c["red"], 0.12), "error.border": a(c["red"], 0.4),
        "warning": c["amber"], "warning.background": a(c["amber"], 0.12), "warning.border": a(c["amber"], 0.4),
        "success": c["green"], "success.background": a(c["green"], 0.12), "success.border": a(c["green"], 0.4),
        "info": c["sky"], "info.background": a(c["sky"], 0.12), "info.border": a(c["sky"], 0.4),
        "hint": c["muted"], "hint.background": a(c["accent"], 0.08), "hint.border": a(c["accent"], 0.25),
        "hidden": c["placeholder"], "hidden.background": "#00000000", "hidden.border": c["border_soft"],
        "ignored": c["placeholder"], "ignored.background": "#00000000", "ignored.border": c["border_soft"],
        "predictive": c["placeholder"], "predictive.background": "#00000000", "predictive.border": c["border_soft"],
        "renamed": c["sky"], "renamed.background": a(c["sky"], 0.12), "renamed.border": a(c["sky"], 0.4),
        "unreachable": c["muted"], "unreachable.background": "#00000000", "unreachable.border": c["border_soft"],
        "players": [
            {"cursor": c["accent"], "background": c["accent"], "selection": a(c["accent"], 0.24)},
            {"cursor": c["green"], "background": c["green"], "selection": a(c["green"], 0.2)},
            {"cursor": c["pink"], "background": c["pink"], "selection": a(c["pink"], 0.2)},
            {"cursor": c["amber"], "background": c["amber"], "selection": a(c["amber"], 0.2)},
            {"cursor": c["sky"], "background": c["sky"], "selection": a(c["sky"], 0.2)},
            {"cursor": c["peach"], "background": c["peach"], "selection": a(c["peach"], 0.2)},
        ],
    }
    for i, k in enumerate(["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]):
        s[f"terminal.ansi.{k}"] = c["ansi"][i]
        s[f"terminal.ansi.bright_{k}"] = c["ansi_bright"][i]
        s[f"terminal.ansi.dim_{k}"] = c["ansi"][i] + "b3"
    x = c["syntax"]
    st = lambda color, **kw: {"color": color, "font_style": kw.get("style"), "font_weight": kw.get("weight")}
    s["syntax"] = {
        "attribute": st(x["type"]), "boolean": st(x["number"]), "comment": st(x["comment"], style="italic"), "comment.doc": st(x["comment_doc"], style="italic"),
        "constant": st(x["number"]), "constructor": st(x["type"]), "embedded": st(c["text"]), "emphasis": st(c["accent"], style="italic"),
        "emphasis.strong": st(c["accent"], weight=700), "enum": st(x["type"]), "function": st(x["function"]), "hint": st(c["muted"]),
        "keyword": st(x["keyword"]), "label": st(x["keyword"]), "link_text": st(x["function"], style="italic"), "link_uri": st(x["function"]),
        "namespace": st(c["text_soft"]), "number": st(x["number"]), "operator": st(x["operator"]), "predictive": st(c["placeholder"], style="italic"),
        "preproc": st(x["keyword"]), "primary": st(c["text"]), "property": st(x["property"]), "punctuation": st(x["punct"]),
        "punctuation.bracket": st(x["punct"]), "punctuation.delimiter": st(x["punct"]), "punctuation.list_marker": st(c["accent"]),
        "punctuation.special": st(x["tag"]), "selector": st(x["tag"]), "selector.pseudo": st(x["keyword"]), "string": st(x["string"]),
        "string.escape": st(x["tag"]), "string.regex": st(x["regex"]), "string.special": st(x["tag"]), "string.special.symbol": st(x["number"]),
        "tag": st(x["tag"]), "text.literal": st(x["string"]), "title": st(c["heading"], weight=700), "type": st(x["type"]),
        "variable": st(c["text"]), "variable.special": st(x["regex"]), "variant": st(x["type"]),
    }
    return {"name": name, "appearance": appearance, "style": s}

# Night, softened for long reading: near-white on near-black glares (about 17:1),
# so the page is a shade lighter and the text a shade dimmer (about 12:1).
night = dict(
    bg="#0b0b20", chrome="#101029", panel="#101029", editor="#0b0b20", surface="#101029", elevated="#17173d",
    border="#24245a", border_soft="#18183f", element="#17173d", hover="#1e1e4a", active="#27275e", selected="#27275e",
    text="#cdd0e6", text_soft="#a9acc9", heading="#e1e3f2", muted="#8487ab", placeholder="#5b5e86", line_number="#3f4170",
    accent="#a5b0f8", green="#7ed7b0", red="#efa3a3", amber="#ecc95e", sky="#86c9ec", pink="#e2a9ef", peach="#f2b27a",
    ansi=["#17173d", "#efa3a3", "#7ed7b0", "#ecc95e", "#a5b0f8", "#e2a9ef", "#86c9ec", "#c3c6dd"],
    ansi_bright=["#4a4c78", "#f6c3c3", "#a5e6c9", "#f3dc8f", "#c4caf6", "#efcaf6", "#b3dcf2", "#e1e3f2"],
    syntax=dict(keyword="#a5b0f8", function="#86c9ec", string="#7ed7b0", number="#f2b27a", type="#ecc95e", property="#bcc2ee",
                comment="#6b6e96", comment_doc="#7c7fa3", tag="#e2a9ef", regex="#efa3a3", operator="#949ff2", punct="#8487ab"),
)
day = dict(
    bg="#f7f7fc", chrome="#eef0fb", panel="#eef0fb", editor="#ffffff", surface="#f4f5fb", elevated="#ffffff",
    border="#d9dcf2", border_soft="#e6e8f5", element="#eef0fb", hover="#e4e7fb", active="#d9ddfe", selected="#d9ddfe",
    text="#1b1c3a", text_soft="#3b3d63", heading="#07071a", muted="#5d6088", placeholder="#9a9dbd", line_number="#b4b7d3",
    accent="#5d64cf", green="#047857", red="#b91c1c", amber="#a16207", sky="#0369a1", pink="#a21caf", peach="#c2410c",
    ansi=["#1b1c3a", "#b91c1c", "#047857", "#a16207", "#5d64cf", "#a21caf", "#0e7490", "#d9dcf2"],
    ansi_bright=["#5d6088", "#dc2626", "#059669", "#ca8a04", "#7c85e8", "#c026d3", "#0891b2", "#f4f5fb"],
    syntax=dict(keyword="#5d64cf", function="#0e7490", string="#047857", number="#c2410c", type="#a16207", property="#444a9c",
                comment="#8b8eae", comment_doc="#7c7fa3", tag="#a21caf", regex="#b91c1c", operator="#555dbd", punct="#6b6e96"),
)
out = {"$schema": "https://zed.dev/schema/themes/v0.2.0.json", "name": "PlushLab", "author": "PlushLab",
       "themes": [theme("PlushLab Night", "dark", night), theme("PlushLab Day", "light", day)]}
json.dump(out, open(os.path.join(ROOT, "themes/plushlab.json"), "w"), indent=2)
print("ok")
