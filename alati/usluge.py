# -*- coding: utf-8 -*-
"""Generira /usluge/index.html (stranica usluga Projektne klinike) i dodaje je u sitemap.xml.
Pokretanje: python3 alati/usluge.py  (sadržaj se mijenja ovdje, ne u HTML-u)."""
import os, re, json, datetime, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://projektnaklinika.enter.fit"
OUT = os.path.join(ROOT, "usluge")
os.makedirs(OUT, exist_ok=True)
e = lambda s: html.escape(s, quote=True)
danas = datetime.date.today().isoformat()

src = open(os.path.join(ROOT, "alati", "pozivi.py"), encoding="utf-8").read()
CSS = re.search(r'CSS = """(.*?)"""', src, re.S).group(1)
CSS += """
.svc{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin:8px 0 0}
@media (max-width:700px){.svc{grid-template-columns:1fr}}
.card{background:var(--surface);border-radius:18px;box-shadow:var(--shadow);padding:22px 24px;border-top:6px solid var(--acc);display:grid;gap:10px;align-content:start}
.card h3{margin:0;font-size:21px;line-height:1.25}
.card .k{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--acc)}
.card p{margin:0;color:var(--muted);font-size:16.5px}
.card ul{margin:0;padding-left:20px;font-size:16.5px}.card li{margin:3px 0}
.card .fit{font-size:15px;color:var(--ink);background:var(--bg);border-radius:10px;padding:8px 12px}
.who{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 0;padding:0;list-style:none}
.who li{background:var(--surface);box-shadow:inset 0 0 0 1.5px var(--line);border-radius:999px;padding:6px 14px;font-size:16px}
.flow{counter-reset:s;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;margin:8px 0 0;padding:0;list-style:none}
@media (max-width:860px){.flow{grid-template-columns:1fr}}
.flow li{counter-increment:s;background:var(--surface);border-radius:16px;box-shadow:var(--shadow);padding:16px 16px 18px;font-size:16px;color:var(--muted)}
.flow li:before{content:counter(s);display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;border-radius:50%;background:var(--navy);color:#fff;font-weight:700;margin-bottom:8px}
.flow b{display:block;color:var(--ink);font-size:17px;margin-bottom:2px}
.faq details{background:var(--surface);border-radius:14px;box-shadow:var(--shadow);padding:14px 18px;margin:0 0 10px}
.faq summary{cursor:pointer;font-weight:700;font-size:17.5px}
.faq p{margin:8px 0 0;color:var(--muted)}
.ctarow{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:14px}
.btn.ghost{background:transparent;color:#fff;box-shadow:inset 0 0 0 2px rgba(255,255,255,.6)}
"""

USLUGE = [
    ("#0F6E74", "Prije prijave", "Provjera prihvatljivosti i projektna ideja",
     "Opišete što želite napraviti, a mi provjerimo koji otvoreni ili najavljeni poziv tome odgovara, jeste li prihvatljiv prijavitelj i kako ideju složiti da nosi bodove.",
     ["izbor poziva i provjera uvjeta za prijavitelja i partnere",
      "okvir projekta: ciljevi, ciljna skupina, glavne aktivnosti",
      "procjena isplati li se prijava s obzirom na rok i bodovanje"],
     "Kad imate ideju, a niste sigurni za koji poziv i jeste li prihvatljivi."),
    ("#C55A1E", "Prijava", "Priprema cijele prijave",
     "Pišemo prijavu s vama, od opisa projekta do predaje, prema kriterijima bodovanja iz uputa za prijavitelje.",
     ["opis projekta, aktivnosti, pokazatelji i vremenski plan",
      "proračun usklađen s aktivnostima i pravilima poziva",
      "okupljanje partnera i izjave o partnerstvu",
      "obrasci, prilozi i predaja u sustav"],
     "Kad nemate vremena ili iskustva, a poziv je važan."),
    ("#A3262A", "Drugo mišljenje", "Provjera prijave prije predaje",
     "Prijavu pišete sami, a mi je prije predaje pročitamo s tablicom ocjenjivanja u ruci i javimo što treba popraviti.",
     ["prihvatljivost, formalni uvjeti i prilozi",
      "proračun: prihvatljivi troškovi, limiti, zbrojevi",
      "usklađenost s kriterijima i konkretni prijedlozi poboljšanja"],
     "Kad je prijava gotova ili skoro gotova – idealno barem tjedan dana prije roka."),
    ("#12355B", "Provedba", "Upravljanje provedbom projekta",
     "Kad projekt dobije financiranje, vodimo administrativni dio provedbe da se sredstva iskoriste i ne izgube.",
     ["plan nabave i dokumentacija za nabave",
      "zahtjevi za nadoknadom sredstava i izvješća",
      "praćenje pokazatelja, vidljivost i komunikacija s posredničkim tijelom"],
     "Kad je ugovor potpisan, a nemate tim za administraciju projekta."),
]

KOME = ["škole i vrtići", "učenički domovi", "općine i gradovi", "županije i osnivači ustanova",
        "sportski klubovi i savezi", "udruge", "hrvatske zajednice i ustanove izvan RH"]

KORACI = [("Upit", "Pišete nam preko obrasca ili e-pošte: tko ste, što planirate i za koji poziv, ako ga znate."),
          ("Razgovor", "Kratko porazgovaramo i provjerimo poziv, rok i uvjete."),
          ("Ponuda", "Šaljemo pisanu ponudu s opsegom posla, rokovima i cijenom – prije nego što išta počne."),
          ("Rad", "Radimo s vama prema planu unatrag od roka predaje, uz redovite provjere."),
          ("Predaja i dalje", "Prijava se predaje na vrijeme, a mi pratimo pojašnjenja, rezultate i provedbu.")]

FAQ = [("Možete li jamčiti da će projekt biti odobren?",
        "Ne. Ishod ovisi o ocjenjivanju i raspoloživim sredstvima, i to nitko ne može obećati. Možemo osigurati da je prijava formalno ispravna, da proračun prati aktivnosti i da je svaki kriterij bodovanja dokazan."),
       ("Koliko unaprijed se trebamo javiti?",
        "Što ranije, to bolje. Za veće prijave (npr. ESF+) javite se nekoliko tjedana prije roka, a za manje pozive barem dva tjedna. Za provjeru gotove prijave dovoljno je tjedan dana."),
       ("Koliko košta?",
        "Cijenu dogovaramo unaprijed, u pisanoj ponudi, prema opsegu posla i vrsti poziva. Za upravljanje provedbom naknada je razmjerna vrijednosti projekta. Prvi upit ništa ne obvezuje."),
       ("Već smo počeli pisati – možete li uskočiti?",
        "Da. Tada je obično najbolja provjera prijave prije predaje ili preuzimanje dijelova koji vam idu najteže, npr. proračuna."),
       ("Radite li s ustanovama izvan Hrvatske?",
        "Da, s hrvatskim zajednicama, udrugama, općinama i ustanovama izvan RH koje se prijavljuju na pozive Središnjeg državnog ureda za Hrvate izvan RH i druge pozive za koje su prihvatljive.")]

cards = "".join(
    f'<article class="card" style="--acc:{a}"><span class="k">{e(k)}</span><h3>{e(n)}</h3><p>{e(o)}</p>'
    f'<ul>{"".join(f"<li>{e(x)}</li>" for x in st)}</ul><p class="fit"><strong>Za vas ako:</strong> {e(fit[0].lower() + fit[1:])}</p></article>'
    for a, k, n, o, st, fit in USLUGE)
who = "".join(f"<li>{e(x)}</li>" for x in KOME)
flow = "".join(f"<li><b>{e(t)}</b>{e(d)}</li>" for t, d in KORACI)
faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)

url = BASE + "/usluge/"
title = "Usluge – priprema prijava na natječaje i upravljanje EU projektima | Projektna klinika"
desc = ("Pomoć školama, vrtićima, općinama, sportskim klubovima, udrugama i Hrvatima izvan RH: provjera prihvatljivosti, "
        "priprema prijave, provjera prijave prije predaje i upravljanje provedbom projekata.")
mail = ("mailto:rektor.co@gmail.com?subject=" + "Upit%20za%20uslugu%20%E2%80%93%20Projektna%20klinika")
ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "WebPage", "@id": url, "url": url, "name": title, "description": desc, "inLanguage": "hr", "dateModified": danas,
     "isPartOf": {"@type": "WebSite", "name": "Projektna klinika", "url": BASE + "/"}},
    {"@type": "ProfessionalService", "@id": url + "#usluga", "name": "Projektna klinika", "url": url,
     "email": "rektor.co@gmail.com", "areaServed": ["HR", "BA"], "inLanguage": "hr",
     "parentOrganization": {"@type": "Organization", "name": "REKTOR POSLOVNA RJEŠENJA d.o.o."},
     "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Usluge Projektne klinike", "itemListElement": [
         {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "description": o}} for _, _, n, o, _, _ in USLUGE]}},
    {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Naslovnica", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Usluge", "item": url}]}]}

page = f"""<!doctype html>
<html lang="hr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
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
  <a class="back" href="/">← Natrag na portal Projektna klinika</a>
  <nav class="crumbs" aria-label="Putanja"><a href="/">Naslovnica</a> › Usluge</nav>
  <h1>Pomoć s projektom – od ideje do provedbe</h1>
  <p class="lede">Na portalu pratimo otvorene pozive i objavljujemo projektne ideje. Kad vam treba više od toga, pomažemo s prijavom i provedbom: provjerimo prihvatljivost, složimo projekt prema kriterijima bodovanja, pripremimo ili provjerimo prijavu i vodimo administraciju odobrenog projekta.</p>
  <section aria-label="Usluge"><div class="svc">{cards}</div></section>
  <section><h2>S kim radimo</h2><ul class="who">{who}</ul></section>
  <section><h2>Kako izgleda suradnja</h2><ol class="flow">{flow}</ol></section>
  <section class="faq"><h2>Česta pitanja</h2>{faq}</section>
  <section class="help"><h2>Recite nam što planirate</h2><p>Napišite ukratko tko ste, što želite napraviti i do kada. Odgovaramo u pravilu u roku od dva radna dana.</p>
    <div class="ctarow"><a class="btn" href="/#kontakt" data-goatcounter-click="usluge-obrazac">Pošaljite upit →</a><a class="btn ghost" href="{e(mail)}" data-goatcounter-click="usluge-mail">rektor.co@gmail.com</a></div></section>
  <p class="note">Sami pišete prijavu? Pretplatnici newslettera besplatno dobivaju <a href="/#prijava" data-goatcounter-click="usluge-kontrolni-popis">kontrolni popis „Prije predaje prijave“</a>, za veće pozive pripremili smo <a href="/vodici/" data-goatcounter-click="usluge-vodici">vodiče za prijavu</a>, a rokove otvorenih poziva možete pratiti i u <a href="/kalendar/">svom kalendaru</a>.</p>
</div></main>
<footer><div class="wrap"><span>Projektna klinika · <a href="/">projektnaklinika.enter.fit</a></span><span>© 2026 REKTOR POSLOVNA RJEŠENJA d.o.o.</span></div></footer>
</body>
</html>
"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page)

sp = os.path.join(ROOT, "sitemap.xml")
sm = open(sp, encoding="utf-8").read()
entry = f'<url><loc>{url}</loc><lastmod>{danas}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>'
if f"<loc>{url}</loc>" in sm:
    sm = re.sub(r'<url><loc>' + re.escape(url) + r'</loc>.*?</url>', entry, sm)
else:
    sm = sm.replace("\n</urlset>", "\n  " + entry + "\n</urlset>")
open(sp, "w", encoding="utf-8").write(sm)
print("usluge/index.html")
