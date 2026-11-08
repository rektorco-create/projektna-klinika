#!/usr/bin/env python3
"""Kalendar rokova za pretplatu (iCalendar / .ics) i stranica /kalendar/.

Iz alati/pozivi-podaci.json izrađuje:
  kalendar/rokovi.ics            – svi otvoreni pozivi
  kalendar/obrazovanje.ics       – odgoj i obrazovanje
  kalendar/sport.ics             – sport
  kalendar/hrvati-izvan-rh.ics   – Hrvati izvan RH
  kalendar/index.html            – upute i gumbi za Google, Apple i Outlook

Pokreće se automatski na kraju alati/pozivi.py (svako jutro), a može i ručno:
python3 alati/kalendar.py
"""
import json, os, re, html, datetime, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://projektnaklinika.enter.fit"
HOST = "projektnaklinika.enter.fit"
D = json.load(open(os.path.join(ROOT, "alati", "pozivi-podaci.json"), encoding="utf-8"))
pozivi = sorted(D["pozivi"], key=lambda p: (p.get("otvaranje") or p["rok"], p["rok"]))
prov = D.get("provjereno") or datetime.date.today().isoformat()
OUT = os.path.join(ROOT, "kalendar")
os.makedirs(OUT, exist_ok=True)
e = lambda s: html.escape(s, quote=True)

FEEDS = [
    # (datoteka, oznaka, naziv kalendara, područja, boja)
    ("rokovi", "Svi pozivi", "Projektna klinika – rokovi natječaja", ("teal", "orange", "red"), "#12355B"),
    ("obrazovanje", "Odgoj i obrazovanje", "Projektna klinika – rokovi: odgoj i obrazovanje", ("teal",), "#0F6E74"),
    ("sport", "Sport", "Projektna klinika – rokovi: sport", ("orange",), "#C55A1E"),
    ("hrvati-izvan-rh", "Hrvati izvan RH", "Projektna klinika – rokovi: Hrvati izvan RH", ("red",), "#A3262A"),
]
POD = {"teal": "Odgoj i obrazovanje", "orange": "Sport", "red": "Hrvati izvan RH"}


def hrdat(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day}. {d.month}. {d.year}."


# ---------- iCalendar ----------
def esc(s):
    return str(s).replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\r", "").replace("\n", "\\n")


def fold(line):
    """RFC 5545: retci najviše 75 okteta, nastavak počinje razmakom."""
    b = line.encode("utf-8")
    if len(b) <= 75:
        return line
    out, cur = [], b""
    for ch in line:
        c = ch.encode("utf-8")
        if len(cur) + len(c) > (75 if not out else 74):
            out.append(cur.decode("utf-8")); cur = b""
        cur += c
    out.append(cur.decode("utf-8"))
    return "\r\n ".join(out)


def ymd(iso):
    return iso.replace("-", "")


def next_day(iso):
    return (datetime.date.fromisoformat(iso) + datetime.timedelta(days=1)).isoformat()


STAMP = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def event(uid, day, summary, desc, url, cat, alarms):
    L = ["BEGIN:VEVENT", f"UID:{uid}", f"DTSTAMP:{STAMP}",
         f"DTSTART;VALUE=DATE:{ymd(day)}", f"DTEND;VALUE=DATE:{ymd(next_day(day))}",
         f"SUMMARY:{esc(summary)}", f"DESCRIPTION:{esc(desc)}", f"URL:{url}",
         f"CATEGORIES:{esc(cat)}", "TRANSP:TRANSPARENT", "STATUS:CONFIRMED"]
    for trig, txt in alarms:
        L += ["BEGIN:VALARM", "ACTION:DISPLAY", f"DESCRIPTION:{esc(txt)}", f"TRIGGER:{trig}", "END:VALARM"]
    L.append("END:VEVENT")
    return L


def sat(p):
    m = re.search(r"\b(\d{1,2})[:.](\d{2})\b", p.get("rok_tekst", ""))
    return f"{int(m.group(1))}:{m.group(2)}" if m else ""


def opis(p, page):
    fin = "\n".join("– " + x for x in p.get("financira", [])[:5])
    return (f"{p['naziv']}\n\nDavatelj: {p['davatelj']}\nRok: {p['rok_tekst']}\nIznos: {p['iznos']}\n"
            f"Tko se može prijaviti: {p['prijavitelji']}\n\nŠto se financira:\n{fin}\n\n"
            f"Detalji na Projektnoj klinici: {page}\nSlužbena objava: {p['izvor']}\n\n"
            f"Pomoć s prijavom: rektor.co@gmail.com · {BASE}/#kontakt\n"
            f"Mjerodavan je izvorni tekst poziva. Podaci provjereni {hrdat(prov)}")


def ics(feed):
    fname, oznaka, calname, podrucja, _ = feed
    L = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Projektna klinika//Rokovi natjecaja//HR",
         "CALSCALE:GREGORIAN", "METHOD:PUBLISH", f"X-WR-CALNAME:{esc(calname)}",
         f"X-WR-CALDESC:{esc('Rokovi otvorenih natječaja i javnih poziva (' + oznaka.lower() + ') koje prati Projektna klinika – ' + BASE + '. Osvježava se svakodnevno.')}",
         "X-WR-TIMEZONE:Europe/Zagreb", "REFRESH-INTERVAL;VALUE=DURATION:PT6H", "X-PUBLISHED-TTL:PT6H"]
    for p in pozivi:
        if p["podrucje"] not in podrucja:
            continue
        page = f"{BASE}/pozivi/{p['slug']}.html"
        h = sat(p)
        L += event(f"{p['slug']}-rok@{HOST}", p["rok"],
                   f"Rok{(' do ' + h) if h else ''}: {p['kratko']}", opis(p, page), page, POD[p["podrucje"]],
                   [("-P7D", f"Za 7 dana ističe rok: {p['kratko']}"), ("-P1D", f"Sutra ističe rok: {p['kratko']}")])
        if p.get("otvaranje"):
            L += event(f"{p['slug']}-otvaranje@{HOST}", p["otvaranje"],
                       f"Otvaraju se prijave: {p['kratko']}", opis(p, page), page, POD[p["podrucje"]],
                       [("-P1D", f"Sutra se otvaraju prijave: {p['kratko']}")])
    L.append("END:VCALENDAR")
    return "\r\n".join(fold(x) for x in L) + "\r\n"


for f in FEEDS:
    open(os.path.join(OUT, f[0] + ".ics"), "w", encoding="utf-8", newline="").write(ics(f))


# ---------- stranica /kalendar/ ----------
src = open(os.path.join(ROOT, "alati", "pozivi.py"), encoding="utf-8").read()
CSS = re.search(r'CSS = """(.*?)"""', src, re.S).group(1)
CSS += """
.feeds{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
@media (max-width:640px){.feeds{grid-template-columns:1fr}}
.feed{background:var(--surface);border-radius:18px;box-shadow:var(--shadow);padding:20px 22px;border-top:6px solid var(--acc);display:grid;gap:12px;align-content:start}
.feed h3{margin:0;font-size:20px}.feed p{margin:0;color:var(--muted);font-size:16px}
.feed .row a{font-size:15px;padding:10px 16px}
.cal-btn{display:inline-flex;align-items:center;gap:8px;background:var(--acc);color:#fff;font-weight:700;text-decoration:none;padding:10px 16px;border-radius:999px;transition:transform .15s}
.cal-btn:hover{transform:translateY(-2px)}
.cal-btn.ghost{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line)}
.copy{font:inherit;font-size:15px;font-weight:700;cursor:pointer;background:transparent;color:var(--ink);border:0;box-shadow:inset 0 0 0 1.5px var(--line);padding:10px 16px;border-radius:999px}
.steps{margin:0;padding-left:22px}.steps li{margin:6px 0}
.upcoming{display:grid;gap:10px}
.upcoming div{display:grid;grid-template-columns:120px 1fr;gap:12px;background:var(--surface);border-radius:14px;box-shadow:var(--shadow);padding:12px 16px;border-left:5px solid var(--acc)}
.upcoming b{color:var(--acc);font-variant-numeric:tabular-nums}
.upcoming a{color:var(--ink);text-decoration:none}.upcoming a:hover{text-decoration:underline}
@media (max-width:560px){.upcoming div{grid-template-columns:1fr;gap:2px}}
"""


def buttons(fname, calname, acc):
    https = f"{BASE}/kalendar/{fname}.ics"
    webcal = f"webcal://{HOST}/kalendar/{fname}.ics"
    g = "https://calendar.google.com/calendar/render?cid=" + urllib.parse.quote(webcal, safe="")
    o = ("https://outlook.live.com/calendar/0/addfromweb?url=" + urllib.parse.quote(https, safe="")
         + "&name=" + urllib.parse.quote(calname, safe=""))
    m365 = ("https://outlook.office.com/calendar/0/addfromweb?url=" + urllib.parse.quote(https, safe="")
            + "&name=" + urllib.parse.quote(calname, safe=""))
    return (f'<div class="row">'
            f'<a class="cal-btn" href="{e(g)}" target="_blank" rel="noopener" data-goatcounter-click="kalendar-google-{fname}">Google kalendar</a>'
            f'<a class="cal-btn" href="{e(webcal)}" data-goatcounter-click="kalendar-apple-{fname}">iPhone / Mac</a>'
            f'<a class="cal-btn ghost" href="{e(o)}" target="_blank" rel="noopener" data-goatcounter-click="kalendar-outlook-{fname}">Outlook.com</a>'
            f'<a class="cal-btn ghost" href="{e(m365)}" target="_blank" rel="noopener" data-goatcounter-click="kalendar-m365-{fname}">Outlook (posao / škola)</a>'
            f'<button class="copy" type="button" data-url="{e(https)}" data-goatcounter-click="kalendar-kopiraj-{fname}">Kopiraj poveznicu</button>'
            f'</div>')


OPIS = {"rokovi": "Svi rokovi na jednom mjestu – obrazovanje, sport i Hrvati izvan RH.",
        "obrazovanje": "Za škole, vrtiće, učeničke domove, osnivače ustanova i JLP(R)S.",
        "sport": "Za sportske klubove, saveze i školska sportska društva.",
        "hrvati-izvan-rh": "Za hrvatske zajednice, udruge, općine i ustanove izvan RH i one koje s njima surađuju."}
feeds_html = ""
for fname, oznaka, calname, podrucja, acc in FEEDS:
    n = sum(1 for p in pozivi if p["podrucje"] in podrucja)
    feeds_html += (f'<div class="feed" style="--acc:{acc}"><h3>{e(oznaka)}</h3><p>{e(OPIS[fname])} Trenutačno {n} '
                   f'{"poziv" if n % 10 == 1 and n % 100 != 11 else "poziva"}.</p>{buttons(fname, calname, acc)}</div>')

ACC = {"teal": "#0F6E74", "orange": "#C55A1E", "red": "#A3262A"}
today = datetime.date.today().isoformat()
up = [p for p in sorted(pozivi, key=lambda p: p["rok"]) if p["rok"] >= today][:6]
up_html = "".join(
    f'<div style="--acc:{ACC[p["podrucje"]]}"><b>{hrdat(p["rok"])}</b><a href="/pozivi/{p["slug"]}.html">{e(p["kratko"])}</a></div>'
    for p in up)

url = BASE + "/kalendar/"
title = "Kalendar rokova natječaja – pretplata za Google, Apple i Outlook | Projektna klinika"
desc = ("Rokovi otvorenih natječaja i javnih poziva za odgoj i obrazovanje, sport i Hrvate izvan RH izravno u vašem kalendaru. "
        "Besplatna pretplata za Google kalendar, iPhone, Mac i Outlook, s podsjetnikom 7 dana i 1 dan prije roka.")
ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "WebPage", "@id": url, "url": url, "name": title, "description": desc, "inLanguage": "hr", "dateModified": prov,
     "isPartOf": {"@type": "WebSite", "name": "Projektna klinika", "url": BASE + "/"}},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Naslovnica", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Kalendar rokova", "item": url}]}]}

page = f"""<!doctype html>
<html lang="hr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" type="text/calendar" title="Projektna klinika – rokovi natječaja" href="{BASE}/kalendar/rokovi.ics">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website">
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
<main><div class="wrap">
  <a class="back" href="/#rokovi">← Natrag na portal Projektna klinika</a>
  <nav class="crumbs" aria-label="Putanja"><a href="/">Naslovnica</a> › Kalendar rokova</nav>
  <h1>Rokovi natječaja u vašem kalendaru</h1>
  <p class="lede">Pretplatite se jednom – rokovi otvorenih poziva sami se pojavljuju u vašem Google, Apple ili Outlook kalendaru i osvježavaju se kad dodamo novi poziv ili se rok promijeni. Besplatno, bez prijave i bez e-pošte.</p>
  <section class="feeds" aria-label="Odaberite kalendar">{feeds_html}</section>
  <section class="box"><h2>Kako to radi</h2>
    <ol class="steps">
      <li>Kliknite gumb za svoj kalendar i potvrdite dodavanje. Na računalu je za Google kalendar potrebno biti prijavljen u Google račun.</li>
      <li>Za svaki poziv dobivate događaj na dan roka (i na dan otvaranja prijava, ako se poziv tek otvara), s iznosom, prihvatljivim prijaviteljima i poveznicom na detalje.</li>
      <li>Kalendar se osvježava sam. Google ga osvježava svakih nekoliko sati do jednom dnevno, Apple i Outlook prema svojim postavkama.</li>
      <li>Želite podsjetnik prije roka? Apple kalendar i Outlook prikazuju podsjetnik 7 dana i 1 dan prije roka (ako ih niste isključili). U Google kalendaru podsjetnik za pretplaćeni kalendar uključite u postavkama tog kalendara (Obavijesti o događajima).</li>
      <li>Kalendar uklanjate kao i svaki drugi – u postavkama kalendara odaberite „Ukloni“ ili „Otkaži pretplatu“.</li>
    </ol>
  </section>
  <section><h2>Sljedeći rokovi</h2><div class="upcoming">{up_html}</div></section>
  <section class="help"><h2>Želite i projektne ideje za ove pozive?</h2><p>Newsletter „Natječaji u fokusu“ (1. i 15. u mjesecu) donosi nove pozive, a „Projektne ideje“ razrađene ideje za pretplatnike.</p><a class="btn" href="/#prijava" data-goatcounter-click="kalendar-newsletter">Prijavite se besplatno →</a></section>
  <p class="note">Podaci su preuzeti sa službenih stranica davatelja i provjereni {hrdat(prov)} Mjerodavan je izvorni tekst poziva. Izravne poveznice na kalendare: <a href="/kalendar/rokovi.ics">rokovi.ics</a> · <a href="/kalendar/obrazovanje.ics">obrazovanje.ics</a> · <a href="/kalendar/sport.ics">sport.ics</a> · <a href="/kalendar/hrvati-izvan-rh.ics">hrvati-izvan-rh.ics</a></p>
</div></main>
<footer><div class="wrap"><span>Projektna klinika · <a href="/">projektnaklinika.enter.fit</a></span><span>© 2026 REKTOR POSLOVNA RJEŠENJA d.o.o.</span></div></footer>
<script>document.querySelectorAll('.copy').forEach(function(b){{b.addEventListener('click',function(){{var u=b.dataset.url,t=b.textContent;function ok(){{b.textContent='Kopirano ✓';setTimeout(function(){{b.textContent=t}},2000)}}if(navigator.clipboard){{navigator.clipboard.writeText(u).then(ok,function(){{prompt('Kopirajte poveznicu:',u)}})}}else{{prompt('Kopirajte poveznicu:',u)}}}})}});</script>
</body>
</html>
"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page)

# sitemap: /kalendar/ (jednom; datum osvježi)
sp = os.path.join(ROOT, "sitemap.xml")
sm = open(sp, encoding="utf-8").read()
entry = f'<url><loc>{BASE}/kalendar/</loc><lastmod>{prov}</lastmod><changefreq>daily</changefreq><priority>0.7</priority></url>'
if f"<loc>{BASE}/kalendar/</loc>" in sm:
    sm = re.sub(r'<url><loc>' + re.escape(BASE) + r'/kalendar/</loc>.*?</url>', entry, sm)
else:
    sm = sm.replace("\n</urlset>", "\n  " + entry + "\n</urlset>")
open(sp, "w", encoding="utf-8").write(sm)

print(f"Kalendar: {len(pozivi)} poziva, {len(FEEDS)} .ics datoteka + kalendar/index.html")
