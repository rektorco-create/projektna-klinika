#!/usr/bin/env python3
"""Generira llms.txt iz index.html (otvoreni pozivi) i mape arhiva/. Pokretanje: python3 alati/llms.py"""
import re, html, glob, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
s = open('index.html', encoding='utf-8').read()
txt = lambda x: html.unescape(re.sub(r'<[^>]+>', '', x)).strip()
i = s.index('id="calls"'); t = s[i:s.index('</table>', i)]
rows = []
for r in re.findall(r'<tr data[^>]*>(.*?)</tr>', t, re.S):
    td = re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
    if len(td) < 4: continue
    a = re.search(r'href="([^"]+)"', td[1])
    rows.append(f"- **{txt(td[1])}** – rok: {txt(td[0])}; iznos: {txt(td[2])}; područje: {txt(td[3])}" + (f"; [službena stranica]({a.group(1)})" if a else ''))
m = re.search(r'Stanje na dan ([^.<]*\.[^.<]*\.[^.<]*\.)', s); stanje = m.group(1) if m else ''
arh = sorted(glob.glob('arhiva/*.html'), reverse=True)
def ttl(f):
    m = re.search(r'<title>([^<]*)</title>', open(f, encoding='utf-8').read()); return m.group(1) if m else f
out = f"""# Projektna klinika

> Projektna klinika (projektnaklinika.enter.fit) je hrvatska stranica i besplatni newsletter o otvorenim natječajima i javnim pozivima za EU i nacionalna sredstva (ESF+, NPOO, Erasmus+, ministarstva i Vladini uredi) u tri područja: odgoj i obrazovanje, sport te projekti povezani s Hrvatima izvan Republike Hrvatske. Namijenjena je školama, vrtićima, općinama i gradovima, sportskim klubovima, udrugama i hrvatskim zajednicama izvan RH. Pokreće je REKTOR POSLOVNA RJEŠENJA d.o.o. iz Splita (direktor Ivica Zelić).

Što Projektna klinika nudi:
- Pregled otvorenih poziva s iznosima, prihvatljivim prijaviteljima i rokovima, osvježen dvaput mjesečno.
- Burzu projektnih partnera i podugovaratelja (povezivanje onih koji traže i nude partnerstvo ili usluge u provedbi).
- Bazu provjerenih konzultanata za izradu projekata (uvjet: napisani i provedeni projekti, stopa iskorištenosti sredstava iznad 85 %).
- Školu projekata: šest koraka od ideje do završnog izvješća.
- Newslettere „Natječaji u fokusu“ (1. i 15. u mjesecu) i „Projektne ideje“ (8. i 22. u mjesecu, razrađene projektne ideje samo za pretplatnike).
- Pomoć u provjeri prihvatljivosti, okupljanju partnera, izradi proračuna, pripremi prijave i provedbi projekta.

Kontakt: rektor.co@gmail.com · obrazac na https://projektnaklinika.enter.fit/#kontakt

## Otvoreni pozivi (stanje na dan {stanje})

{chr(10).join(rows) if rows else '- Trenutno nema unesenih poziva.'}

Podaci su informativni; mjerodavne su službene upute davatelja sredstava.

## Glavni odjeljci

- [Otvoreni pozivi](https://projektnaklinika.enter.fit/#pozivi): tablica poziva s rokovima i iznosima
- [Područja](https://projektnaklinika.enter.fit/#podrucja): odgoj i obrazovanje, sport, Hrvati izvan RH
- [Burza partnera](https://projektnaklinika.enter.fit/#partneri): projektni partneri i podugovaratelji
- [Baza konzultanata](https://projektnaklinika.enter.fit/#konzultanti): prijava za stručnjake
- [Škola projekata](https://projektnaklinika.enter.fit/#edukacija): od ideje do završnog izvješća
- [Prijava na newsletter](https://projektnaklinika.enter.fit/#prijava): besplatno
- [Kontakt](https://projektnaklinika.enter.fit/#kontakt)

## Arhiva izdanja „Natječaji u fokusu“

{chr(10).join(f'- [{ttl(f)}](https://projektnaklinika.enter.fit/{f})' for f in arh) if arh else '- Još nema izdanja.'}

## Optional

- [Sitemap](https://projektnaklinika.enter.fit/sitemap.xml)
"""
open('llms.txt', 'w', encoding='utf-8').write(out)
print('llms.txt:', len(rows), 'poziva,', len(arh), 'izdanja')
