#!/usr/bin/env python3
"""Dnevna snimka stranica davatelja sredstava i GoatCounter statistike (pokreće GitHub Actions).

Rezultat ide u granu „podaci“ (radni direktorij OUT):
  davatelji/<oznaka>.txt   – čitljiv tekst stranice + popis poveznica
  davatelji/novo/<…>.txt   – nove podstranice (poveznice koje se jučer nisu pojavljivale), najviše MAX_NOVIH
  davatelji/stanje.json    – kad je što snimljeno, HTTP status, greške
  davatelji/vidjene-poveznice.json – sve dosad viđene poveznice (za otkrivanje novih)
  goatcounter/GGGG-MM-DD.json – statistika za jučer (ako postoji tajna GOATCOUNTER_TOKEN)
Poštuje robots.txt: adrese koje robots zabranjuje se ne otvaraju.
"""
import datetime, hashlib, html, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request, urllib.robotparser
from html.parser import HTMLParser

OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
UA = "ProjektnaKlinikaBot/1.0 (+https://projektnaklinika.enter.fit; rektor.co@gmail.com)"
MAX_NOVIH = 60

IZVORI = {
    "eufondovi": ["https://eufondovi.gov.hr/", "https://eufondovi.gov.hr/pozivi/"],
    "esf": ["https://esf.hr/esfplus/naslovnica/", "https://esf.hr/esfplus/natjecaji/"],
    "fondovieu": ["https://fondovieu.gov.hr/", "https://fondovieu.gov.hr/pozivi"],
    "mzom": ["https://mzom.gov.hr/istaknute-teme/natjecaji-196/196"],
    "mints": ["https://mints.gov.hr/javni-pozivi-i-natjecaji-11414/11414", "https://mint.gov.hr/javni-pozivi-i-natjecaji-11414/s-p-o-r-t/22182",
              "https://mints.gov.hr/sport-21838/21838", "https://mints.gov.hr/turizam-21837/21837"],
    "hrvatiizvanrh": ["https://hrvatiizvanrh.gov.hr/natjecaji-574/574", "https://hrvatiizvanrh.gov.hr/vijesti/8"],
    "mdu": ["https://mdu.gov.hr/javni-pozivi/5923", "https://mdu.gov.hr/vijesti-4693/4693"],
    "mvep": ["https://mvep.gov.hr/ministarstvo/natjecaji/9625"],
    "rrvz": ["https://rrvz.hr/"],
    "mingo": ["https://mingo.gov.hr/javni-pozivi-i-natjecaji-7371/javni-pozivi-i-natjecaji-ministarstva/otvoreni-javni-pozivi-i-natjecaji/7390"],
    "mzozt": ["https://mzozt.gov.hr/javni-pozivi-i-natjecaji-7371/javni-pozivi-i-natjecaji-ministarstva/otvoreni-javni-pozivi-i-natjecaji/7390",
              "https://mzozt.gov.hr/novosti-8/8"],
    "mrosp": ["https://mrosp.gov.hr/", "https://mrosp.gov.hr/pristup-informacijama-16/natjecaji-pozivi-i-zaposljavanje/udruge-u-sustavu-socijalne-skrbi-natjecaji-pozivi-i-obrasci/11791",
              "https://mrosp.gov.hr/pristup-informacijama-16/natjecaji-pozivi-i-zaposljavanje/ostali-natjecaji-i-pozivi/13690"],
    "razvoj": ["https://razvoj.gov.hr/", "https://razvoj.gov.hr/vijesti/8"],
    "ampeu": ["https://www.ampeu.hr/natjecaji", "https://www.ampeu.hr/novosti"],
    "udruge": ["https://udruge.gov.hr/natjecaji-5503/5503"],
    "min-kulture": ["https://min-kulture.gov.hr/natjecaji-16274/javni-pozivi-404/404"],
    "asoo": ["https://www.asoo.hr/"],
    "aem": ["https://aem.hr/"],
}
# Podstranice koje su vjerojatno objave (ne izbornici, slike ni datoteke)
PRESKOCI = re.compile(r"\.(jpe?g|png|gif|svg|webp|css|js|ico|zip|docx?|xlsx?|pptx?)(\?|$)|/(tag|category|author|feed|wp-json|wp-login)/|mailto:|tel:|javascript:", re.I)


class Tekst(HTMLParser):
    BLOK = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "section", "article", "td", "th", "dd", "dt", "header", "footer"}

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base, self.dijelovi, self.poveznice, self.skip, self.a = base, [], [], 0, None

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg", "template"):
            self.skip += 1
        elif tag in self.BLOK:
            self.dijelovi.append("\n")
        if tag == "a":
            href = dict(attrs).get("href")
            self.a = [urllib.parse.urljoin(self.base, href.strip()), []] if href else None

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg", "template") and self.skip:
            self.skip -= 1
        elif tag in self.BLOK:
            self.dijelovi.append("\n")
        if tag == "a" and self.a:
            t = " ".join("".join(self.a[1]).split())
            if t:
                self.poveznice.append((t, self.a[0].split("#")[0]))
            self.a = None

    def handle_data(self, d):
        if self.skip:
            return
        self.dijelovi.append(d)
        if self.a is not None:
            self.a[1].append(d)

    def rezultat(self):
        t = "".join(self.dijelovi)
        t = re.sub(r"[ \t\r\f\v]+", " ", t)
        t = re.sub(r"\n\s*\n+", "\n", t)
        return "\n".join(l.strip() for l in t.split("\n") if l.strip())


_robots = {}


def dopusteno(url):
    p = urllib.parse.urlsplit(url)
    root = f"{p.scheme}://{p.netloc}"
    if root not in _robots:
        rp = urllib.robotparser.RobotFileParser()
        try:
            req = urllib.request.Request(root + "/robots.txt", headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20) as r:
                rp.parse(r.read().decode("utf-8", "replace").splitlines())
        except Exception:
            rp.parse([])  # nema robots.txt → sve dopušteno
        _robots[root] = rp
    return _robots[root].can_fetch(UA, url)


def dohvati(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "hr,en;q=0.5"})
    with urllib.request.urlopen(req, timeout=45) as r:
        raw = r.read(8_000_000)
        cs = r.headers.get_content_charset() or "utf-8"
        return r.status, r.geturl(), r.headers.get_content_type(), raw.decode(cs, "replace")


def snimi(url, putanja):
    """Vraća (zapis stanja, poveznice)."""
    z = {"url": url, "datoteka": os.path.relpath(putanja, OUT), "snimljeno": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")}
    if not dopusteno(url):
        z["greska"] = "robots.txt zabranjuje"
        return z, []
    for pokusaj in (1, 2):
        try:
            st, konacni, tip, body = dohvati(url)
            z.update(status=st, konacni_url=konacni, tip=tip)
            if tip != "text/html":
                z["greska"] = f"nije HTML ({tip})"
                return z, []
            p = Tekst(konacni)
            p.feed(body)
            tekst = p.rezultat()
            nasl = re.search(r"<title[^>]*>(.*?)</title>", body, re.S | re.I)
            z["naslov"] = html.unescape(" ".join(nasl.group(1).split())) if nasl else ""
            z["znakova"] = len(tekst)
            vidj, pov = set(), []
            for t, h in p.poveznice:
                if h.startswith("http") and (t, h) not in vidj:
                    vidj.add((t, h)); pov.append((t, h))
            os.makedirs(os.path.dirname(putanja), exist_ok=True)
            with open(putanja, "w", encoding="utf-8") as f:
                f.write(f"URL: {konacni}\nSnimljeno: {z['snimljeno']}\nNaslov: {z['naslov']}\n\n{tekst}\n\n== POVEZNICE ==\n")
                f.writelines(f"{t} | {h}\n" for t, h in pov)
            return z, pov
        except urllib.error.HTTPError as e:
            z.update(status=e.code, greska=f"HTTP {e.code}")
        except Exception as e:
            z["greska"] = f"{type(e).__name__}: {e}"[:300]
        if pokusaj == 1:
            time.sleep(20)
    return z, []


def oznaka(url):
    p = urllib.parse.urlsplit(url)
    s = re.sub(r"[^a-z0-9]+", "-", (p.netloc + p.path).lower()).strip("-")[:90]
    return s + "-" + hashlib.sha1(url.encode()).hexdigest()[:6]


def davatelji():
    d = os.path.join(OUT, "davatelji")
    os.makedirs(d, exist_ok=True)
    vp = os.path.join(d, "vidjene-poveznice.json")
    vidjene = json.load(open(vp, encoding="utf-8")) if os.path.exists(vp) else {}
    prvi_put = not vidjene
    stanje, kandidati = {"pokrenuto": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "izvori": {}, "nove_podstranice": []}, []
    for izvor, urlovi in IZVORI.items():
        stanje["izvori"][izvor] = []
        for url in urlovi:
            z, pov = snimi(url, os.path.join(d, oznaka(url) + ".txt"))
            stanje["izvori"][izvor].append(z)
            dom = urllib.parse.urlsplit(z.get("konacni_url", url)).netloc.replace("www.", "")
            for t, h in pov:
                if h in vidjene:
                    continue
                vidjene[h] = {"tekst": t[:200], "izvor": izvor, "prvi_put": datetime.date.today().isoformat()}
                ista = urllib.parse.urlsplit(h).netloc.replace("www.", "") == dom
                if not prvi_put and ista and not PRESKOCI.search(h) and len(t) >= 15:
                    kandidati.append((izvor, t, h))
            time.sleep(2)
    for izvor, t, h in kandidati[:MAX_NOVIH]:
        z, _ = snimi(h, os.path.join(d, "novo", oznaka(h) + ".txt"))
        z.update(izvor=izvor, tekst_poveznice=t)
        stanje["nove_podstranice"].append(z)
        time.sleep(2)
    stanje["nove_preskoceno_zbog_limita"] = max(0, len(kandidati) - MAX_NOVIH)
    stanje["prvo_pokretanje"] = prvi_put
    json.dump(vidjene, open(vp, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    json.dump(stanje, open(os.path.join(d, "stanje.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def goatcounter():
    tok = os.environ.get("GOATCOUNTER_TOKEN", "").strip()
    d = os.path.join(OUT, "goatcounter")
    os.makedirs(d, exist_ok=True)
    jucer = (datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))) - datetime.timedelta(days=1)).date().isoformat()
    rez = {"dan": jucer, "snimljeno": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")}
    if not tok:
        rez["greska"] = "nema tajne GOATCOUNTER_TOKEN u postavkama repozitorija"
    else:
        base = "https://projektnaklinika.goatcounter.com/api/v0"
        q = urllib.parse.urlencode({"start": jucer, "end": jucer})
        for k, put in (("ukupno", f"/stats/total?{q}"), ("stranice", f"/stats/hits?{q}&limit=50"), ("izvori", f"/stats/toprefs?{q}&limit=30"),
                       ("drzave", f"/stats/locations?{q}&limit=15")):
            try:
                req = urllib.request.Request(base + put, headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json", "User-Agent": UA})
                with urllib.request.urlopen(req, timeout=45) as r:
                    rez[k] = json.loads(r.read().decode())
            except urllib.error.HTTPError as e:
                rez[k] = {"greska": f"HTTP {e.code}", "tijelo": e.read().decode("utf-8", "replace")[:300]}
            except Exception as e:
                rez[k] = {"greska": f"{type(e).__name__}: {e}"[:300]}
            time.sleep(1)
    json.dump(rez, open(os.path.join(d, f"{jucer}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(rez, open(os.path.join(d, "zadnje.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    goatcounter()
    davatelji()
    print("Gotovo.")
