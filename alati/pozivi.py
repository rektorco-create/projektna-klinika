#!/usr/bin/env python3
"""Izrađuje zasebnu stranicu za svaki otvoreni poziv (pozivi/<slug>.html) i popis pozivi/index.html
iz alati/pozivi-podaci.json. Pokretanje iz korijena repozitorija: python3 alati/pozivi.py"""
import json, html, os, datetime, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://projektnaklinika.enter.fit"
D = json.load(open(os.path.join(ROOT, "alati", "pozivi-podaci.json"), encoding="utf-8"))
OUT = os.path.join(ROOT, "pozivi")
os.makedirs(OUT, exist_ok=True)

POD = {"teal": ("Odgoj i obrazovanje", "#0F6E74"), "orange": ("Sport", "#C55A1E"), "red": ("Hrvati izvan RH", "#A3262A")}
MJ = ["siječnja", "veljače", "ožujka", "travnja", "svibnja", "lipnja", "srpnja", "kolovoza", "rujna", "listopada", "studenoga", "prosinca"]
e = lambda s: html.escape(s, quote=True)

def hrdat(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day}. {d.month}. {d.year}."

def hrdat_dugo(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day}. {MJ[d.month-1]} {d.year}."

CSS = """
:root{--bg:#F7F9FB;--surface:#FFFFFF;--ink:#16202B;--muted:#56616E;--line:#E7ECF2;--navy:#12355B;--navy-2:#0D2846;--teal:#0F6E74;--gold:#F2A65A;--shadow:0 1px 2px rgba(18,53,91,.04),0 10px 30px rgba(18,53,91,.07);color-scheme:light}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0C1218;--surface:#16202B;--ink:#E8EDF3;--muted:#9AA7B5;--line:#223040;--navy:#0B2440;--navy-2:#081B31;--teal:#4FB3B8;--shadow:0 1px 2px rgba(0,0,0,.3),0 10px 30px rgba(0,0,0,.35);color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0C1218;--surface:#16202B;--ink:#E8EDF3;--muted:#9AA7B5;--line:#223040;--navy:#0B2440;--navy-2:#081B31;--teal:#4FB3B8;--shadow:0 1px 2px rgba(0,0,0,.3),0 10px 30px rgba(0,0,0,.35);color-scheme:dark}
*{box-sizing:border-box}html,body{margin:0}
body{background:var(--bg);color:var(--ink);font-family:"Source Sans 3","Segoe UI",Arial,sans-serif;font-size:18px;line-height:1.65;-webkit-font-smoothing:antialiased;min-height:100vh;display:flex;flex-direction:column}
.rule{display:flex;height:6px}.rule span{flex:1}.rule span:nth-child(1){background:#0F6E74}.rule span:nth-child(2){background:#C55A1E}.rule span:nth-child(3){background:#A3262A}
header{background:radial-gradient(120% 140% at 85% 20%,#1C4A7A 0%,var(--navy) 45%,var(--navy-2) 100%);color:#fff}
.wrap{max-width:880px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
header .wrap{padding-block:18px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
header img{display:block;height:48px;width:auto}
header nav a{color:#DCE7F3;text-decoration:none;font-weight:600;font-size:16px;margin-left:18px}
header nav a:hover{color:#fff}
main{flex:1}main .wrap{padding-block:28px 72px;display:grid;gap:24px}
.back{justify-self:start;display:inline-flex;align-items:center;gap:6px;background:var(--surface);color:var(--ink);font-weight:700;font-size:16px;text-decoration:none;padding:10px 18px;border-radius:999px;box-shadow:var(--shadow);transition:transform .15s}
.back:hover{transform:translateX(-3px)}
.crumbs{font-size:15px;color:var(--muted)}.crumbs a{color:var(--muted)}
.tag{display:inline-block;font-weight:700;font-size:14px;letter-spacing:.06em;text-transform:uppercase;color:#fff;padding:4px 12px;border-radius:999px;justify-self:start}
h1{font-weight:700;font-size:clamp(28px,4.6vw,42px);line-height:1.15;letter-spacing:-.015em;margin:0;text-wrap:balance}
h2{font-size:24px;margin:0 0 8px;line-height:1.25}
.lede{margin:0;color:var(--muted);font-size:19px}
.sum{margin:0;max-width:70ch}
.count{display:flex;align-items:center;gap:14px;background:var(--surface);border-radius:18px;box-shadow:var(--shadow);padding:16px 20px;border-left:6px solid var(--acc)}
.count b{font-size:34px;line-height:1;color:var(--acc);font-variant-numeric:tabular-nums}
.count span{color:var(--muted)}
.facts{background:var(--surface);border-radius:18px;box-shadow:var(--shadow);padding:6px 22px;margin:0}
.facts div{display:grid;grid-template-columns:200px 1fr;gap:12px;padding:14px 0;border-bottom:1px solid var(--line)}
.facts div:last-child{border-bottom:0}
.facts dt{font-weight:700;color:var(--muted);font-size:16px}.facts dd{margin:0}
@media (max-width:620px){.facts div{grid-template-columns:1fr;gap:2px}}
.box{background:var(--surface);border-radius:18px;box-shadow:var(--shadow);padding:22px 24px}
.box ul{margin:0;padding-left:22px}.box li{margin:4px 0}
.help{background:var(--navy);color:#fff;border-radius:18px;padding:26px 26px;display:grid;gap:12px}
.help h2{color:#fff}.help p{margin:0;color:#DCE7F3}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--gold);color:#12355B;font-weight:700;text-decoration:none;padding:13px 22px;border-radius:999px;justify-self:start;transition:transform .15s,box-shadow .15s}
.btn:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(0,0,0,.18)}
.btn.ghost{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line)}
.row{display:flex;flex-wrap:wrap;gap:10px}
.note{font-size:15px;color:var(--muted);margin:0}
a{color:var(--teal)}a:focus-visible{outline:3px solid var(--gold);outline-offset:2px}
.list{display:grid;gap:12px}
.list a{display:grid;grid-template-columns:140px 1fr;gap:14px;align-items:center;background:var(--surface);border-radius:16px;box-shadow:var(--shadow);padding:14px 18px;text-decoration:none;color:var(--ink);border-left:5px solid var(--acc);transition:transform .2s}
.list a:hover{transform:translateY(-3px)}
.list .d{font-weight:700;color:var(--acc);font-variant-numeric:tabular-nums}
.list small{display:block;color:var(--muted);font-size:15px}
@media (max-width:560px){.list a{grid-template-columns:1fr;gap:2px}header nav a{margin-left:0;margin-right:16px}}
footer{background:var(--navy-2);color:#AFC3DA;font-size:14px}
footer .wrap{padding-block:24px 28px;display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px}
footer a{color:#AFC3DA}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

COUNT_JS = """<script>(function(){var el=document.getElementById('cd');if(!el)return;var due=el.dataset.due,open=el.dataset.open;var t=new Date();t.setHours(0,0,0,0);function d(s){var p=s.split('-');return new Date(+p[0],+p[1]-1,+p[2]);}
var n=Math.round((d(due)-t)/864e5);var b=el.querySelector('b'),s=el.querySelector('span');
if(open&&d(open)>t){var o=Math.round((d(open)-t)/864e5);b.textContent=o;s.textContent=(o===1?'dan':'dana')+' do otvaranja zaprimanja prijava';return;}
if(n<0){b.textContent='—';s.textContent='Rok za prijavu je istekao. Pogledajte aktualne pozive na naslovnici.';return;}
if(n===0){b.textContent='Danas';s.textContent='je zadnji dan za prijavu';return;}
b.textContent=n;s.textContent=(n%10===1&&n%100!==11?'dan':'dana')+' do roka za prijavu';})();</script>"""

def ukratko(p):
    return (f"Poziv „{p['naziv']}“ – davatelj: {p['davatelj']}. Rok: {p['rok_tekst']}. Iznos: {p['iznos']}. "
            f"Prijaviti se mogu: {p['prijavitelji']}. Prijava: {p['prijava']}.")

def md(p, pod):
    url = f"{BASE}/pozivi/{p['slug']}.html"
    fin = "\n".join(f"- {x}" for x in p["financira"])
    izv = p["izvor"] + (f"\n- Dokumentacija: {p['izvor2']}" if p.get("izvor2") else "")
    otv = f"\n- **Otvaranje zaprimanja prijava:** {hrdat(p['otvaranje'])}" if p.get("otvaranje") else ""
    return f"""# {p['naziv']}

> {ukratko(p)}

- **Područje:** {pod}
- **Davatelj:** {p['davatelj']}
- **Rok:** {p['rok_tekst']}{otv}
- **Iznos:** {p['iznos']}
- **Tko se može prijaviti:** {p['prijavitelji']}
- **Kako se prijaviti:** {p['prijava']}

## Što se financira

{fin}

## Izvori

- Službena objava: {izv}
- Stranica na Projektnoj klinici: {url}

Podaci provjereni {hrdat(prov)} Mjerodavan je izvorni tekst poziva. Pomoć s prijavom: rektor.co@gmail.com (Projektna klinika, https://projektnaklinika.enter.fit/#kontakt).
"""

def head(title, desc, url, ld, alt=None):
    return f"""<!doctype html>
<html lang="hr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">{f'{chr(10)}<link rel="alternate" type="text/markdown" title="Sažetak poziva za AI asistente" href="{alt}">' if alt else ''}
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="article">
<meta property="og:locale" content="hr_HR">
<meta property="og:site_name" content="Projektna klinika">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/fonts/fonts.css">
<meta name="theme-color" content="#12355B">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
<script data-goatcounter="https://projektnaklinika.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</head>
<body>
<div class="rule"><span></span><span></span><span></span></div>
<header><div class="wrap"><a href="/" aria-label="Projektna klinika – naslovnica"><img src="/logo/logo-vodoravni-tamni.svg" width="160" height="48" alt="Projektna klinika"></a>
<nav aria-label="Glavna navigacija"><a href="/pozivi/">Svi pozivi</a><a href="/#prijava">Newsletter</a><a href="/#kontakt">Kontakt</a></nav></div></header>
"""

FOOT = """<footer><div class="wrap"><span>Projektna klinika · <a href="/">projektnaklinika.enter.fit</a></span><span>© 2026 REKTOR POSLOVNA RJEŠENJA d.o.o.</span></div></footer>
"""

prov = D["provjereno"]
danas = datetime.date.today().isoformat()
# pozivi kojima je rok prošao ne dobivaju stranicu (stare se brišu niže)
pozivi = sorted([p for p in D["pozivi"] if p["rok"] >= danas], key=lambda p: p.get("otvaranje") or p["rok"])
written = []

for p in pozivi:
    pod, acc = POD[p["podrucje"]]
    url = f"{BASE}/pozivi/{p['slug']}.html"
    title = f"{p['kratko']} – rok {hrdat(p['rok'])} | Projektna klinika"
    desc = f"{p['naziv']}. Rok: {p['rok_tekst']}. Iznos: {p['iznos']}. Tko se može prijaviti, što se financira i kako se prijaviti."
    if len(desc) > 300: desc = desc[:297].rsplit(" ", 1)[0] + "…"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url, "url": url, "name": title, "description": desc, "inLanguage": "hr",
         "dateModified": prov, "isPartOf": {"@type": "WebSite", "name": "Projektna klinika", "url": BASE + "/"},
         "publisher": {"@id": BASE + "/#org"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Projektna klinika", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Otvoreni pozivi", "item": BASE + "/pozivi/"},
            {"@type": "ListItem", "position": 3, "name": p["kratko"], "item": url}]},
        {"@type": "MonetaryGrant", "name": p["naziv"], "description": ukratko(p), "url": p["izvor"],
         "funder": {"@type": "Organization", "name": p["davatelj"]}, "subjectOf": {"@id": url}}]}
    fin = "".join(f"<li>{e(x)}</li>" for x in p["financira"])
    izvori = f'<a href="{e(p["izvor"])}" target="_blank" rel="noopener">Službena objava poziva</a>'
    if p.get("izvor2"):
        izvori += f' · <a href="{e(p["izvor2"])}" target="_blank" rel="noopener">dokumentacija</a>'
    slicni = [q for q in pozivi if q is not p and q["podrucje"] == p["podrucje"]][:3]
    sl = "".join(f'<a href="/pozivi/{q["slug"]}.html" style="--acc:{acc}"><span class="d">{hrdat(q["rok"])}</span><span>{e(q["kratko"])}<small>Iznos: {e(q["iznos"])}</small></span></a>' for q in slicni)
    subj = "Upit – " + p["kratko"]
    mailto = "mailto:rektor.co@gmail.com?subject=" + re.sub(r"%20", "%20", __import__("urllib.parse").parse.quote(subj))
    opn = f' data-open="{p["otvaranje"]}"' if p.get("otvaranje") else ""
    body = f"""<main><div class="wrap" style="--acc:{acc}">
  <a class="back" href="/#pozivi">← Natrag na portal Projektna klinika</a>\n  <nav class="crumbs" aria-label="Putanja"><a href="/">Naslovnica</a> › <a href="/pozivi/">Otvoreni pozivi</a> › {e(pod)}</nav>
  <span class="tag" style="background:{acc}">{e(pod)}</span>
  <h1>{e(p['naziv'])}</h1>
  <p class="lede">{e(p['davatelj'])}</p>
  <p class="sum"><b>Ukratko:</b> {e(ukratko(p))}</p>
  <div class="count" id="cd" data-due="{p['rok']}"{opn}><b>{hrdat(p['rok'])}</b><span>rok za prijavu</span></div>
  <dl class="facts">
    <div><dt>Rok</dt><dd>{e(p['rok_tekst'])}</dd></div>
    <div><dt>Iznos</dt><dd>{e(p['iznos'])}</dd></div>
    <div><dt>Tko se može prijaviti</dt><dd>{e(p['prijavitelji'])}</dd></div>
    <div><dt>Kako se prijaviti</dt><dd>{e(p['prijava'])}</dd></div>
    <div><dt>Davatelj</dt><dd>{e(p['davatelj'])}</dd></div>
  </dl>
  <p class="note"><a href="/kalendar/" data-goatcounter-click="poziv-kalendar">Kalendar rokova</a> – ovaj i ostali rokovi automatski u vašem Google, Apple ili Outlook kalendaru.</p>
  <section class="box"><h2>Što se financira</h2><ul>{fin}</ul></section>
  <section class="help" aria-label="Pomoć s prijavom">
    <h2>Trebate pomoć s prijavom na ovaj poziv?</h2>
    <p>Provjerit ćemo prihvatljivost vaše ustanove i ideje, pomoći okupiti partnere, složiti proračun i pripremiti prijavu do roka.</p>
    <div class="row"><a class="btn" href="{e(mailto)}">Pošaljite upit →</a><a class="btn ghost" style="color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.4)" href="/#kontakt">Više o pomoći</a></div>
  </section>
  <section class="box"><h2>Ne propustite sljedeći poziv</h2><p style="margin:0 0 12px">Besplatni newsletter „Natječaji u fokusu“ dvaput mjesečno donosi nove pozive za škole, vrtiće, sportske klubove, udruge, općine i Hrvate izvan RH – s iznosima i rokovima.</p><a class="btn" href="/#prijava">Prijava na newsletter →</a></section>
  {f'<section><h2>Slični pozivi – {e(pod)}</h2><div class="list">{sl}</div></section>' if sl else ''}
  <p class="note">Izvor: {izvori}. Podaci provjereni {hrdat(prov)} Prije prijave uvijek provjerite izvorni tekst poziva i natječajnu dokumentaciju – mjerodavna je službena objava.</p>
</div></main>
"""
    open(os.path.join(OUT, p["slug"] + ".md"), "w", encoding="utf-8").write(md(p, pod))
    open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8").write(head(title, desc, url, ld, f"{BASE}/pozivi/{p['slug']}.md") + body + FOOT + COUNT_JS + "\n</body>\n</html>\n")
    written.append(p["slug"])

# popis svih poziva
url = BASE + "/pozivi/"
title = "Otvoreni natječaji i javni pozivi za škole, sport i Hrvate izvan RH | Projektna klinika"
desc = f"Popis otvorenih natječaja i javnih poziva za odgoj i obrazovanje, sport i Hrvate izvan RH, s rokovima, iznosima i prihvatljivim prijaviteljima. Stanje {hrdat(prov)}"
ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "CollectionPage", "@id": url, "url": url, "name": title, "description": desc, "inLanguage": "hr", "dateModified": prov},
    {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{BASE}/pozivi/{p['slug']}.html", "name": p["kratko"]} for i, p in enumerate(pozivi)]}]}
grupe = ""
for k, (pod, acc) in POD.items():
    items = [p for p in pozivi if p["podrucje"] == k]
    if not items: continue
    li = "".join(f'<a href="/pozivi/{p["slug"]}.html" style="--acc:{acc}"><span class="d">{("od " + hrdat(p["otvaranje"])) if p.get("otvaranje") else hrdat(p["rok"])}</span><span>{e(p["kratko"])}<small>Iznos: {e(p["iznos"])}</small></span></a>' for p in items)
    grupe += f'<section id="{k}"><h2>{e(pod)}</h2><div class="list">{li}</div></section>'
body = f"""<main><div class="wrap">
  <a class="back" href="/#pozivi">← Natrag na portal Projektna klinika</a>\n  <nav class="crumbs" aria-label="Putanja"><a href="/">Naslovnica</a> › Otvoreni pozivi</nav>
  <h1>Otvoreni natječaji i javni pozivi</h1>
  <p class="lede">Za odgoj i obrazovanje, sport i Hrvate izvan RH. Stanje na dan {hrdat(prov)} Kliknite poziv za rok, iznos, prihvatljive prijavitelje i način prijave.</p>
  <a class="btn ghost" href="/kalendar/" data-goatcounter-click="pozivi-kalendar">Rokovi u vašem kalendaru →</a>
  {grupe}
  <section class="help"><h2>Ne znate koji je poziv za vas?</h2><p>Opišite nam ustanovu i ideju – javit ćemo vam koji pozivi dolaze u obzir.</p><a class="btn" href="mailto:rektor.co@gmail.com?subject=Koji%20poziv%20je%20za%20nas%3F">Pošaljite upit →</a></section>
  <p class="note">Prije prijave uvijek provjerite izvorni tekst poziva – mjerodavna je službena objava davatelja.</p>
</div></main>
"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(head(title, desc, url, ld) + body + FOOT + "</body>\n</html>\n")
# obriši stranice poziva kojih više nema u podacima ili su istekle
for f in os.listdir(OUT):
    if (f.endswith(".html") or f.endswith(".md")) and f not in ("index.html",) and f.rsplit(".", 1)[0] not in written:
        os.remove(os.path.join(OUT, f)); print("Uklonjeno:", f)

# naslovnica: poveznice u tablici otvorenih poziva vode na stranicu poziva
ip = os.path.join(ROOT, "index.html")
ix = open(ip, encoding="utf-8").read()
a, b = ix.find('<table id="calls">'), ix.find('</table>', ix.find('<table id="calls">'))
if a > 0:
    t = ix[a:b]
    for p in pozivi:
        for old in (f'<a href="{p["izvor"]}" target="_blank" rel="noopener">', f'<a href="{e(p["izvor"])}" target="_blank" rel="noopener">'):
            t = t.replace(old, f'<a href="/pozivi/{p["slug"]}.html" target="_blank" rel="noopener">')
        t = t.replace(f'<a href="/pozivi/{p["slug"]}.html">', f'<a href="/pozivi/{p["slug"]}.html" target="_blank" rel="noopener">')
    t = re.sub(r'<a href="/pozivi/([^"]+)\.html">', lambda m: m.group(0) if m.group(1) in written else '<a href="#">', t)
    t = re.sub(r'<a href="/pozivi/([^"]+)\.html"( target="_blank" rel="noopener")?>', lambda m: m.group(0) if m.group(1) in written else '<a href="#pozivi">', t)
    ix = ix[:a] + t + ix[b:]
    open(ip, "w", encoding="utf-8").write(ix)

# sitemap: zadrži sve što nije u /pozivi/, dodaj /pozivi/ i stranice poziva
sp = os.path.join(ROOT, "sitemap.xml")
sm = open(sp, encoding="utf-8").read()
sm = re.sub(r'\s*<url><loc>[^<]*/pozivi/[^<]*</loc>.*?</url>', '', sm)
add = f'\n  <url><loc>{BASE}/pozivi/</loc><lastmod>{prov}</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>'
add += "".join(f'\n  <url><loc>{BASE}/pozivi/{x}.html</loc><lastmod>{prov}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>' for x in written)
sm = sm.replace("\n</urlset>", add + "\n</urlset>")
open(sp, "w", encoding="utf-8").write(sm)

full = f"""# Projektna klinika – otvoreni pozivi (puni opis)

> Svi otvoreni natječaji i javni pozivi koje prati Projektna klinika (https://projektnaklinika.enter.fit) za odgoj i obrazovanje, sport i Hrvate izvan RH. Stanje na dan {hrdat(prov)} Podaci su preuzeti sa službenih stranica davatelja; mjerodavan je izvorni tekst poziva.

"""
for k, (pod, _) in POD.items():
    items = [p for p in pozivi if p["podrucje"] == k]
    if not items: continue
    full += f"## {pod}\n\n" + "\n".join(md(p, pod).replace("\n# ", "\n### ").replace("# ", "### ", 1).replace("\n## ", "\n#### ") for p in items) + "\n"
open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8").write(full)

print(f"Izrađeno: {len(written)} stranica poziva + pozivi/index.html")

# kalendar rokova za pretplatu (kalendar/*.ics i kalendar/index.html)
import subprocess, sys
subprocess.run([sys.executable, os.path.join(ROOT, "alati", "kalendar.py")], check=True)
