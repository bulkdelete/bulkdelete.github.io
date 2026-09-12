# Generates the search-intent how-to pages + sitemap.xml. Run: python gen_howto.py
# ponytail: one template, three pages; add a dict entry to add a page.
import datetime, pathlib

SITE = "https://bulkdeletetools.com"
PAGES = [
    {
        "file": "how-to-delete-all-tiktok-videos.html",
        "title": "How to delete all your TikTok videos at once (2026)",
        "desc": "TikTok has no bulk delete. Here is the fastest manual way and a free browser extension that deletes all your TikTok videos, reposts, likes and favorites in one pass.",
        "eyebrow": "TikTok",
        "accent": "#e23b2e",
        "video": "oWJ61VjoUxE",
        "chrome": "https://chromewebstore.google.com/detail/dlmdmkbajbiieiecpcohafipiefnlgnd",
        "edge": "https://microsoftedge.microsoft.com/addons/detail/mgoepogjokiliobjhlkdeedoeffhejmk",
        "product": "Bulk Delete Videos on TikTok",
        "intro": "TikTok only lets you delete videos one at a time, on the phone or in TikTok Studio. If you have dozens or hundreds, that is an afternoon of tapping. This page covers the manual route and the one-click route.",
        "sections": [
            ("The manual way", "Open TikTok Studio at tiktok.com/tiktokstudio/content on a computer. Each video has a three-dot menu with Delete. It is still one at a time, but faster than the app. Deleted videos go to Recently deleted and can be restored for 30 days."),
            ("Delete all TikTok videos with the extension", "Install Bulk Delete Videos on TikTok, open TikTok Studio, click the extension icon, and press Find them. Filter by date or caption keyword if you only want some of them, check the list, type the number shown, and press Delete. It removes them at a safe pace and reports what went. Free for 20 a day; $6.99 once for unlimited."),
            ("How to delete all your TikTok reposts", "Reposts live on the Reposts tab of your profile. Open it, click the extension, choose Reposts, and follow the same find, confirm, remove steps. There is no manual bulk option for reposts either."),
            ("How to remove all liked videos and favorites on TikTok", "Same flow on the Liked and Favorites tabs of your profile. Choose the matching option in the extension. Nothing is deleted from anyone else's account; you are only removing your own like or save."),
            ("Is it safe?", "The extension runs only in your browser on your own signed-in account. No login to us, no servers, nothing collected. Deleted videos stay in TikTok's Recently deleted for 30 days, so a mistake is reversible."),
        ],
    },
    {
        "file": "how-to-clear-youtube-watch-later.html",
        "title": "How to clear YouTube Watch Later, Liked videos and history at once (2026)",
        "desc": "YouTube only removes watched videos from Watch Later. Here is how to clear Watch Later, Liked videos, watch history and playlists in bulk with a free browser extension.",
        "eyebrow": "YouTube",
        "accent": "#e23b2e",
        "video": "KWyBcFUsYfw",
        "chrome": None,
        "edge": "https://microsoftedge.microsoft.com/addons/detail/kdbgopmdkbcjadidalplbjemamkojdeo",
        "product": "Bulk Delete for YouTube",
        "intro": "YouTube gives you exactly one bulk option: Remove watched videos from Watch Later. Everything else, including Liked videos and any playlist you made, is one click per video, and Watch Later caps at 5,000.",
        "sections": [
            ("Clear watched videos only (built in)", "On the Watch Later page, open the three-dot menu at the top and choose Remove watched videos. This only removes what YouTube has marked as watched."),
            ("Clear all of Watch Later with the extension", "Install Bulk Delete for YouTube, open youtube.com/playlist?list=WL, click the extension, choose Watch Later, and press Find them. Review the list, type the number, and remove. Afterwards it reloads the page and tells you exactly how many are gone. Free for 20 a day; $6.99 once for unlimited."),
            ("How to remove all liked videos on YouTube", "Open your Liked videos list (playlist LL), click the extension, choose Liked videos. YouTube does not redraw that page after an unlike, so the extension verifies by reloading and re-counting."),
            ("How to clear YouTube watch history in bulk", "YouTube has a Clear all watch history button in the History page menu. If you want to remove only some entries, the extension's Watch history option lets you filter by title keyword first."),
            ("Empty any playlist you own", "Open the playlist, click the extension, choose A playlist of yours. Works on any list=PL playlist that belongs to you."),
            ("Is it reversible?", "Yes. Save, like, or watch a video again and it comes back. The extension runs only in your browser, on your account, with nothing collected."),
        ],
    },
    {
        "file": "how-to-unlike-all-spotify-songs.html",
        "title": "How to unlike all your Spotify Liked Songs at once (2026)",
        "desc": "Spotify has no bulk unlike. Here is the fastest manual way and a free browser extension that clears your Liked Songs in one pass, with a preview and confirmation.",
        "eyebrow": "Spotify",
        "accent": "#1db954",
        "video": "H39BWe1Xj2k",
        "chrome": "https://chromewebstore.google.com/detail/iapabcolefaeoefimmhlcpjbphmkfifo",
        "edge": "https://microsoftedge.microsoft.com/addons/detail/ibfchjifbckpkckhkhnnaednflldpnie",
        "product": "Bulk Delete for Spotify",
        "intro": "Spotify's Liked Songs list has no select-all and no clear button. If you inherited a shared account, changed taste, or just want a clean slate, here are the two ways to empty it.",
        "sections": [
            ("The manual way", "On the desktop app or open.spotify.com, open Liked Songs, click the first track, Shift-click a track further down to select a range, then right-click and choose Remove from your Liked Songs. Roughly 50 to 100 at a time is practical."),
            ("Unlike everything with the extension", "Install Bulk Delete for Spotify, open open.spotify.com/collection/tracks, click the extension, and press Find them. Filter by title keyword if you want to keep some, review the list, type the number, and remove. It unlikes at a safe pace and reports what went. Free for 20 a day; $6.99 once for unlimited."),
            ("Does this delete the songs?", "No. Unliking only removes the song from your Liked Songs list. Re-like any song to bring it back. Your playlists are untouched."),
            ("Is it safe?", "The extension runs only in your browser on your own signed-in Spotify account. No login to us, no servers, nothing collected."),
        ],
    },
]

CSS = """
  :root{--ground:#faf6f5;--surface:#fff;--ink:#1c1512;--muted:#7a6c68;--hair:#ebe0dd;--accent:ACCENT;--radius:14px;--display:"Bricolage Grotesque",Georgia,serif;--body:"IBM Plex Sans",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace}
  @media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ground:#16100e;--surface:#1e1613;--ink:#f4ece9;--muted:#b09d97;--hair:#352824}}
  :root[data-theme="dark"]{--ground:#16100e;--surface:#1e1613;--ink:#f4ece9;--muted:#b09d97;--hair:#352824}
  *{box-sizing:border-box}html,body{overflow-x:hidden}
  body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--body);line-height:1.65;-webkit-font-smoothing:antialiased}
  .wrap{max-width:760px;margin:0 auto;padding:0 24px}
  a{color:inherit}
  h1,h2{font-family:var(--display);text-wrap:balance;margin:0;line-height:1.1;letter-spacing:-.02em}
  header{border-bottom:1px solid var(--hair)}
  .bar{display:flex;align-items:center;justify-content:space-between;height:64px}
  .brand{display:flex;align-items:center;gap:10px;font-family:var(--display);font-weight:800;font-size:18px;text-decoration:none}
  .glyph{width:30px;height:30px;border-radius:8px;background:var(--accent);display:grid;place-items:center;color:#fff;font-size:16px}
  .eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
  h1{font-size:clamp(30px,5vw,44px);font-weight:800;margin:12px 0 16px}
  .lede{font-size:18px;color:var(--muted);margin:0 0 24px}
  .video{position:relative;padding-top:56.25%;border-radius:var(--radius);overflow:hidden;border:1px solid var(--hair);background:#000;margin:0 0 28px}
  .video iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
  h2{font-size:24px;font-weight:700;margin:32px 0 8px}
  p{margin:0 0 14px}
  .cta{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:24px 0;padding:20px;background:var(--surface);border:1px solid var(--hair);border-radius:var(--radius)}
  .btn{display:inline-flex;align-items:center;font-weight:600;font-size:15px;padding:12px 20px;border-radius:10px;text-decoration:none;border:1px solid transparent}
  .btn-primary{background:var(--accent);color:#fff}
  .btn-ghost{border-color:var(--hair);background:var(--surface)}
  .price{font-family:var(--mono);font-size:13px;color:var(--muted)}
  footer{padding:32px 0 48px;color:var(--muted);font-size:13px;border-top:1px solid var(--hair);margin-top:40px}
"""

def render(p):
    btns = ""
    if p["chrome"]:
        btns += f'<a class="btn btn-primary" href="{p["chrome"]}" target="_blank" rel="noopener">Get it for Chrome</a>\n      '
    btns += f'<a class="btn {"btn-ghost" if p["chrome"] else "btn-primary"}" href="{p["edge"]}" target="_blank" rel="noopener">Get it for Edge</a>'
    if not p["chrome"]:
        btns += '\n      <span class="price">Chrome version pending Google\'s new-publisher limit; the Edge build installs in Chrome-based browsers.</span>'
    sections = "\n".join(f"    <h2>{h}</h2>\n    <p>{b}</p>" for h, b in p["sections"])
    faq_json = ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' % (jsonstr(h), jsonstr(b))
        for h, b in p["sections"])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title"]} | Bulk Delete Tools</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{SITE}/{p["file"]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;600&display=swap">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json}]}}</script>
<style>{CSS.replace("ACCENT", p["accent"])}</style>
</head>
<body>
<header><div class="wrap bar">
  <a class="brand" href="/"><span class="glyph">&#128465;</span> Bulk Delete Tools</a>
  <a class="btn btn-ghost" href="/#products">All products</a>
</div></header>
<main class="wrap">
  <article>
    <span class="eyebrow">{p["eyebrow"]} &middot; how-to</span>
    <h1>{p["title"]}</h1>
    <p class="lede">{p["intro"]}</p>
    <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{p["video"]}" title="{p["product"]} walkthrough" loading="lazy" allow="accelerometer; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
{sections}
    <div class="cta">
      {btns}
      <span class="price">Free 20/day &middot; <b>$6.99</b> once &middot; no subscription</span>
    </div>
  </article>
</main>
<footer class="wrap">
  Bulk Delete Tools is not affiliated with {p["eyebrow"]}. Questions or refunds: support@bulkdeletetools.com &middot; <a href="/#privacy">Privacy</a> &middot; <a href="/">Home</a>
</footer>
</body>
</html>
"""

def jsonstr(s):
    import json; return json.dumps(s, ensure_ascii=False)

root = pathlib.Path(__file__).parent
for p in PAGES:
    (root / p["file"]).write_text(render(p), encoding="utf-8")
today = datetime.date.today().isoformat()
urls = ["", "deletetik-alternative.html"] + [p["file"] for p in PAGES]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{SITE}/{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n"
(root / "sitemap.xml").write_text(sitemap, encoding="utf-8")
(root / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
print("wrote", [p["file"] for p in PAGES], "sitemap.xml robots.txt")
