# -*- coding: utf-8 -*-
"""Generira /vodici/<slug>/index.html i /vodici/index.html iz alati/vodici_sadrzaj.py
te ih dodaje u sitemap.xml. Pokreće se iz alati/pozivi.py (svaki dan) ili samostalno."""
import os, re, json, html, datetime, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "alati"))
from vodici_sadrzaj import VODICI  # noqa: E402
from vodici_ilustracije import IKONE  # noqa: E402

BASE = "https://projektnaklinika.enter.fit"
OUT = os.path.join(ROOT, "vodici")
e = lambda s: html.escape(s, quote=True)
strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()
MJ = ["siječnja", "veljače", "ožujka", "travnja", "svibnja", "lipnja", "srpnja", "kolovoza", "rujna", "listopada", "studenoga", "prosinca"]


def hrdat(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day}. {d.month}. {d.year}."


podaci = json.load(open(os.path.join(ROOT, "alati", "pozivi-podaci.json"), encoding="utf-8"))
POZ = {p["slug"]: p for p in podaci["pozivi"]}
danas = datetime.date.today().isoformat()

src = open(os.path.join(ROOT, "alati", "pozivi.py"), encoding="utf-8").read()
CSS = re.search(r'CSS = """(.*?)"""', src, re.S).group(1)
CSS += """
.toc{background:var(--surface);border-radius:16px;box-shadow:var(--shadow);padding:16px 20px;margin:18px 0}
.toc b{display:block;margin-bottom:6px}.toc ul{margin:0;padding-left:20px;columns:2;column-gap:28px}
@media (max-width:640px){.toc ul{columns:1}}
.toc a{color:var(--ink)}
.facts2{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:18px 0}
@media (max-width:760px){.facts2{grid-template-columns:1fr 1fr}}@media (max-width:460px){.facts2{grid-template-columns:1fr}}
.facts2 div{background:var(--surface);border-radius:14px;box-shadow:var(--shadow);padding:12px 16px;border-top:4px solid var(--acc)}
.facts2 dt{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--acc)}
.facts2 dd{margin:4px 0 0;font-size:16.5px}
.status{background:#FBEEE5;color:#5C2A0A;border-left:5px solid #C55A1E;border-radius:12px;padding:12px 16px;margin:14px 0}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .status{background:#3a2516;color:#F8DCCB}}
.g h2{scroll-margin-top:20px}
.g section{margin:30px 0}
.g p,.g li{font-size:17.5px}
.t{width:100%;border-collapse:collapse;background:var(--surface);border-radius:14px;overflow:hidden;box-shadow:var(--shadow);font-size:16px}
.t th{background:var(--acc);color:#fff;text-align:left;padding:10px 12px;font-size:14.5px}
.t td{padding:10px 12px;border-top:1px solid var(--line);vertical-align:top}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch}
ul.check{list-style:none;padding:0}ul.check li{position:relative;padding-left:30px;margin:8px 0}
ul.check li:before{content:"";position:absolute;left:0;top:5px;width:18px;height:18px;border:2px solid var(--acc);border-radius:5px}
.tip{background:var(--surface);border-left:5px solid var(--gold,#F2A65A);border-radius:12px;padding:14px 18px;box-shadow:var(--shadow)}
.calc{background:var(--surface);border-radius:16px;box-shadow:var(--shadow);padding:18px 20px;border-top:6px solid var(--acc)}
.calc label{display:block;font-weight:700;margin-bottom:6px}
.calc input{font:inherit;font-size:18px;padding:10px 12px;border-radius:10px;border:1.5px solid var(--line);background:var(--bg);color:var(--ink);width:160px;max-width:100%}
.calc output{display:block;margin-top:12px;font-size:17px}
.calc output b{font-size:22px;color:var(--acc)}
.faq details{background:var(--surface);border-radius:14px;box-shadow:var(--shadow);padding:14px 18px;margin:0 0 10px}
.faq summary{cursor:pointer;font-weight:700;font-size:17.5px}
.faq p{margin:8px 0 0;color:var(--muted)}
.vlist{display:grid;gap:14px}
.vlist a{display:block;background:var(--surface);border-radius:16px;box-shadow:var(--shadow);padding:18px 20px;border-left:6px solid var(--acc);color:var(--ink);text-decoration:none}
.vlist a:hover h2{text-decoration:underline}
.vlist h2{margin:0 0 6px;font-size:20px}.vlist p{margin:0;color:var(--muted);font-size:16px}
.ctarow{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:14px}
.btn.ghost2{background:transparent;color:#fff;box-shadow:inset 0 0 0 2px rgba(255,255,255,.6)}
@keyframes vfloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
.float{animation:vfloat 6s ease-in-out infinite}.float.d2{animation-delay:-2s}.float.d3{animation-delay:-4s}
@media (prefers-reduced-motion:reduce){.float{animation:none}}
.vhero{position:relative;overflow:hidden;background:linear-gradient(135deg,#12355B 0%,#0D2846 70%);color:#fff;border-radius:24px;padding:30px 30px 26px;display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,.65fr);gap:18px;align-items:center;margin:16px 0 20px;box-shadow:var(--shadow)}
.vhero:before{content:"";position:absolute;inset:0 0 auto 0;height:6px;background:linear-gradient(90deg,#0F6E74 0 33%,#C55A1E 33% 66%,#A3262A 66%)}
.vhero:after{content:"";position:absolute;right:-80px;bottom:-120px;width:340px;height:340px;border-radius:50%;background:var(--acc);opacity:.25}
.vhero>*{position:relative;z-index:1}
.vhero .over{display:inline-block;background:rgba(255,255,255,.14);color:#fff;border-radius:999px;padding:5px 12px;font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.vhero h1{color:#fff;margin:12px 0 10px;font-size:clamp(28px,4.2vw,42px);line-height:1.12}
.vhero .lede{color:#D7E2EE;margin:0 0 14px}
.vhero .pub{margin:0 0 16px;color:#F2A65A;font-weight:700;font-size:16.5px}
.vhero svg{width:100%;max-width:300px;justify-self:center;filter:drop-shadow(0 18px 30px rgba(0,0,0,.25))}
.chips2{display:flex;flex-wrap:wrap;gap:8px}
.chips2 span{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.18);border-radius:999px;padding:7px 14px;font-size:15.5px;color:#fff}
.chips2 b{color:#F2A65A;margin-right:6px}
@media (max-width:760px){.vhero{grid-template-columns:1fr;padding:24px 20px}.vhero svg{max-width:200px;order:-1}}
.g{counter-reset:sec}
.g section.num>h2{display:flex;align-items:center;gap:12px}
.g section.num>h2:before{counter-increment:sec;content:counter(sec);flex:none;display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:12px;background:var(--acc);color:#fff;font-size:18px}
.bars{display:grid;gap:10px;background:var(--surface);border-radius:16px;box-shadow:var(--shadow);padding:18px 20px;margin:0 0 16px}
.bar{display:grid;grid-template-columns:minmax(0,1fr) 52px;gap:4px 12px;align-items:center}
.bar span{font-size:15.5px}.bar b{text-align:right;font-variant-numeric:tabular-nums;color:var(--acc)}
.bar i{grid-column:1/-1;height:12px;border-radius:999px;background:var(--line);overflow:hidden;display:block}
.bar i:after{content:"";display:block;height:100%;width:var(--w);background:var(--c);border-radius:999px}
.road{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;counter-reset:rd}
@media (max-width:860px){.road{grid-template-columns:1fr 1fr}}@media (max-width:480px){.road{grid-template-columns:1fr}}
.road li{counter-increment:rd;background:var(--surface);border-radius:16px;box-shadow:var(--shadow);padding:16px;position:relative;border-top:5px solid var(--acc)}
.road li:last-child{background:var(--acc);color:#fff}.road li:last-child small{color:#fff}
.road b{display:block;font-size:17px;margin-bottom:4px}.road small{display:block;color:var(--muted);font-size:15.5px;line-height:1.5}
.vcards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
@media (max-width:900px){.vcards{grid-template-columns:1fr}}
.vcard{display:flex;flex-direction:column;background:var(--surface);border-radius:20px;box-shadow:var(--shadow);overflow:hidden;color:var(--ink);text-decoration:none;transition:transform .2s}
.vcard:hover{transform:translateY(-4px)}
.vcard .art{background:linear-gradient(135deg,#12355B,#0D2846);padding:14px 20px 4px;border-top:6px solid var(--acc);display:flex;justify-content:center}
.vcard .art svg{width:100%;max-width:220px;height:auto}
.vcard .bd{padding:18px 20px 20px;display:grid;gap:8px;flex:1}
.vcard .k{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--acc)}
.vcard h2{margin:0;font-size:20px;line-height:1.25}.vcard p{margin:0;color:var(--muted);font-size:15.5px}
.vcard .go{margin-top:auto;font-weight:700;color:var(--acc)}
"""

CALC_JS = """<script>(function(){var i=document.getElementById('uc'),o=document.getElementById('uo');if(!i)return;function f(n){return n.toLocaleString('hr-HR',{minimumFractionDigits:0,maximumFractionDigits:2})+' €'}
function r(){var n=parseInt(i.value,10);if(!(n>0)){o.innerHTML='Upišite broj učenika.';return}var a=n*500,b=2500,c=(a+b)*0.02,d=Math.min(a+b+c,10000000);
o.innerHTML='Najveći iznos koji možete tražiti: <b>'+f(d)+'</b><br><small>'+n+' × 500 € = '+f(a)+' + vidljivost 2.500 € + neizravni 2 % = '+f(c)+'</small>'+(d<40000?'<br><strong>Ispod najmanjeg iznosa od 40.000 € – projekt nije prihvatljiv. Razmislite o zajedničkoj prijavi preko osnivača s drugim jednosmjenskim školama.</strong>':'');}
i.addEventListener('input',r);r()})();</script>"""


def head(title, desc, url, ld):
    return f"""<!doctype html>
<html lang="hr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
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
<nav aria-label="Glavna navigacija"><a href="/pozivi/">Svi pozivi</a><a href="/vodici/">Vodiči</a><a href="/usluge/">Usluge</a></nav></div></header>
"""


FOOT = """<footer><div class="wrap"><span>Projektna klinika · <a href="/">projektnaklinika.enter.fit</a></span><span>© 2026 REKTOR POSLOVNA RJEŠENJA d.o.o.</span></div></footer>
</body>
</html>
"""


def sid(i):
    return f"s{i + 1}"


written = []
for v in VODICI:
    p = POZ.get(v["poziv"])
    url = f"{BASE}/vodici/{v['slug']}/"
    title = v["naslov"] + " | Projektna klinika"
    secs = v["sekcije"]
    toc = "".join(f'<li><a href="#{sid(i)}">{e(t)}</a></li>' for i, (t, _) in enumerate(secs))
    toc += '<li><a href="#pitanja">Česta pitanja</a></li>'
    if v.get("kalkulator"):
        toc = '<li><a href="#kalkulator">Kalkulator najvećeg iznosa</a></li>' + toc
    chips = "".join(f"<span><b>{e(a)}</b>{e(b)}</span>" for a, b in v.get("chips", []))
    facts = "".join(f"<div><dt>{e(k)}</dt><dd>{e(x)}</dd></div>" for k, x in v["ukratko"])
    body_secs = ""
    for i, (t, parts) in enumerate(secs):
        inner = "".join(f'<div class="tw">{x}</div>' if x.startswith("<table") else x for x in parts)
        if t.startswith("Kako se boduje") and v.get("bodovi"):
            mx = max(b for _, b in v["bodovi"])
            cols = ["#0F6E74", "#C55A1E", "#A3262A", "#12355B", "#F2A65A", "#1C7A86"]
            inner = '<div class="bars" aria-label="Najviše bodova po kriteriju">' + "".join(
                f'<div class="bar"><span>{e(n)}</span><b>{b}</b><i style="--w:{b / mx * 100:.0f}%;--c:{cols[k % len(cols)]}"></i></div>'
                for k, (n, b) in enumerate(v["bodovi"])) + "</div>" + inner
        body_secs += f'<section class="num" id="{sid(i)}"><h2>{e(t)}</h2>{inner}</section>'
        if i == 1 and v.get("kalkulator"):
            pass
    calc = ""
    if v.get("kalkulator"):
        calc = ('<section id="kalkulator"><h2>Kalkulator: koliko najviše možete tražiti</h2>'
                '<div class="calc"><label for="uc">Broj učenika koji nastavu pohađaju u jednoj smjeni (ŠeR, 1. 10. 2026.), u svim školama u projektu</label>'
                '<input id="uc" type="number" min="1" step="1" value="100" inputmode="numeric"><output id="uo" aria-live="polite"></output>'
                '<p class="note" style="margin-top:10px">Formula iz Uputa za prijavitelje: broj učenika × 500 € + 2.500 € + 2 % neizravnih troškova. Uz to, iznos za aktivnosti ne smije prijeći broj skupina × 2.000 €.</p></div></section>')
    road = ""
    if v.get("koraci"):
        road = '<section id="put"><h2>Put do predaje</h2><ol class="road">' + "".join(f"<li><b>{e(a)}</b><small>{e(b)}</small></li>" for a, b in v["koraci"]) + "</ol></section>"
        toc = toc.replace('<li><a href="#pitanja">', '<li><a href="#put">Put do predaje</a></li><li><a href="#pitanja">')
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in v["faq"])
    status = f'<p class="status"><strong>Stanje poziva:</strong> {e(v["status"])}</p>' if v.get("status") else ""
    poz_link = f'<a href="/pozivi/{p["slug"]}.html">stranica poziva s rokom i iznosom</a> · ' if p else ""
    subj = "Upit – " + v["kratko"]
    mailto = "mailto:rektor.co@gmail.com?subject=" + __import__("urllib.parse").parse.quote(subj)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "@id": url + "#clanak", "headline": v["h1"], "name": v["naslov"], "description": v["opis"],
         "url": url, "inLanguage": "hr", "datePublished": v["provjereno"], "dateModified": v["provjereno"],
         "author": {"@type": "Organization", "name": "Projektna klinika", "url": BASE + "/"},
         "publisher": {"@type": "Organization", "name": "Projektna klinika", "logo": {"@type": "ImageObject", "url": BASE + "/logo/logo-ikona-512.png"}},
         "about": {"@type": "MonetaryGrant", "name": p["naziv"] if p else v["kratko"], "url": v["izvor"]},
         "isBasedOn": v["izvor"]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in v["faq"]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Naslovnica", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Vodiči za prijavu", "item": BASE + "/vodici/"},
            {"@type": "ListItem", "position": 3, "name": v["kratko"], "item": url}]}]}
    body = f"""<main><div class="wrap g" style="--acc:{v['acc']}">
  <a class="back" href="/vodici/">← Svi vodiči za prijavu</a>
  <nav class="crumbs" aria-label="Putanja"><a href="/">Naslovnica</a> › <a href="/vodici/">Vodiči</a> › {e(v['kratko'])}</nav>
  <header class="vhero"><div><span class="over">Vodič za prijavu</span><h1>{e(v['h1'])}</h1><p class="pub">{e(v.get('publika', ''))}</p><p class="lede">{e(v['uvod'])}</p>
    <div class="chips2">{chips}</div></div>{IKONE.get(v.get('ikona'), '')}</header>
  {status}
  <dl class="facts2">{facts}</dl>
  <nav class="toc" aria-label="Sadržaj"><b>Sadržaj</b><ul>{toc}</ul></nav>
  {calc}
  {body_secs}
  {road}
  <section><h2>Savjet Projektne klinike</h2><p class="tip">{e(v['savjet'])}</p></section>
  <section class="faq" id="pitanja"><h2>Česta pitanja</h2>{faq}</section>
  <section class="help"><h2>Želite da prijavu pripremimo ili provjerimo zajedno?</h2><p>Pomažemo s prihvatljivošću, partnerima, proračunom i cijelom prijavom – ili pročitamo vašu gotovu prijavu prije predaje.</p>
    <div class="ctarow"><a class="btn" href="/usluge/?ref=vodic" data-goatcounter-click="vodic-usluge-{v['slug']}">Pogledajte usluge →</a><a class="btn ghost2" href="{e(mailto)}" data-goatcounter-click="vodic-mail-{v['slug']}">Pošaljite upit</a></div></section>
  <section class="box"><h2>Besplatno uz prijavu na newsletter</h2><p style="margin:0 0 12px">Kontrolni popis „Prije predaje prijave“ (PDF) – više od 40 provjera u osam koraka – te dvaput mjesečno novi pozivi s rokovima i razrađene projektne ideje.</p><a class="btn" href="/#prijava" data-goatcounter-click="vodic-newsletter-{v['slug']}">Prijavite se →</a></section>
  <p class="note">Vodič je izrađen prema dokumentu: {e(v['izvor_tekst'])}. Provjereno {hrdat(v['provjereno'])} Izvor: <a href="{e(v['izvor'])}" target="_blank" rel="noopener">službena dokumentacija poziva</a>. Vidi i: {poz_link}<a href="/kalendar/">kalendar rokova</a>. Vodič je informativan i ne zamjenjuje Upute za prijavitelje ni njihove izmjene – mjerodavan je uvijek službeni tekst poziva. Projektna klinika nije povezana s davateljem sredstava.</p>
</div></main>
"""
    d = os.path.join(OUT, v["slug"])
    os.makedirs(d, exist_ok=True)
    js = CALC_JS if v.get("kalkulator") else ""
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(head(title, v["opis"], url, ld) + body + js + "\n" + FOOT)
    written.append(v)

# popis vodiča
url = BASE + "/vodici/"
title = "Vodiči za prijavu na natječaje – korak po korak | Projektna klinika"
desc = "Praktični vodiči za prijavu na otvorene pozive za škole, vrtiće, općine, sportske klubove i udruge: tko se može prijaviti, troškovi, bodovanje, dokumenti i najčešće pogreške."
items = "".join(f'<a class="vcard" href="/vodici/{v["slug"]}/" style="--acc:{v["acc"]}"><div class="art">{IKONE.get(v.get("ikona"), "")}</div><div class="bd"><span class="k">{e(" · ".join(a + " " + b for a, b in v.get("chips", [])[:1]))}</span><h2>{e(v["h1"])}</h2><p>{e(v.get("publika", ""))}</p><span class="go">Pročitajte vodič →</span></div></a>' for v in written)
ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "CollectionPage", "@id": url, "url": url, "name": title, "description": desc, "inLanguage": "hr", "dateModified": danas},
    {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{BASE}/vodici/{v['slug']}/", "name": v["h1"]} for i, v in enumerate(written)]}]}
body = f"""<main><div class="wrap">
  <a class="back" href="/">← Natrag na portal Projektna klinika</a>
  <nav class="crumbs" aria-label="Putanja"><a href="/">Naslovnica</a> › Vodiči</nav>
  <h1>Vodiči za prijavu na natječaje</h1>
  <p class="lede">Za veće otvorene pozive pročitali smo upute za prijavitelje, bodovne tablice i objavljena pitanja i odgovore te ih složili u pregledan vodič: tko se može prijaviti, što se financira, kako se boduje, koji dokumenti trebaju i gdje prijave najčešće padaju.</p>
  <div class="vcards">{items}</div>
  <section class="help"><h2>Za koji poziv vam treba vodič?</h2><p>Javite nam se – vodiče pišemo za pozive koji najviše zanimaju škole, općine, klubove i udruge.</p><div class="ctarow"><a class="btn" href="/usluge/?ref=vodici">Usluge →</a><a class="btn ghost2" href="/pozivi/">Svi otvoreni pozivi</a></div></section>
</div></main>
"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(head(title, desc, url, ld) + body + FOOT)

# sitemap
sp = os.path.join(ROOT, "sitemap.xml")
sm = open(sp, encoding="utf-8").read()
urls = [(BASE + "/vodici/", danas)] + [(f"{BASE}/vodici/{v['slug']}/", v["provjereno"]) for v in written]
for u, lm in urls:
    entry = f'<url><loc>{u}</loc><lastmod>{lm}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>'
    if f"<loc>{u}</loc>" in sm:
        sm = re.sub(r'<url><loc>' + re.escape(u) + r'</loc>.*?</url>', entry, sm)
    else:
        sm = sm.replace("\n</urlset>", "\n  " + entry + "\n</urlset>")
open(sp, "w", encoding="utf-8").write(sm)
print(f"Vodiči: {len(written)} + vodici/index.html")
