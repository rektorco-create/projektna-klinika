# -*- coding: utf-8 -*-
"""Sadržaj vodiča za prijavu. Svaka tvrdnja temelji se na Uputama za prijavitelje i
objavljenim pitanjima i odgovorima (datum provjere u polju 'provjereno').
HTML je dopušten u tekstovima (već escapiran gdje treba)."""

VODICI = [
{
 "slug": "mdu-aktivnosti-za-djecu-2026",
 "poziv": "mdu-edukativne-kulturne-sportske-aktivnosti-djeca-2026",
 "acc": "#0F6E74",
 "kratko": "MDU – aktivnosti za djecu (općine i gradovi)",
 "naslov": "Kako se prijaviti na MDU poziv za edukativne, kulturne i sportske aktivnosti za djecu 2026.",
 "h1": "MDU poziv za aktivnosti djece: vodič za prijavu",
 "opis": "Praktični vodič za općine i gradove: tko se može prijaviti, partneri, prihvatljivi troškovi, kako se boduje (100 bodova), dokumenti i najčešće pogreške. Rok 19. 11. 2026. u 16:00.",
 "provjereno": "2026-11-08",
 "izvor": "https://mdu.gov.hr/javni-pozivi/program-provedbe-edukativnih-kulturnih-i-sportskih-aktivnosti-za-predskolsku-djecu-te-djecu-od-1-do-4-razreda-osnovne-skole-u-lokalnim-zajednicama/7674",
 "izvor_tekst": "Upute za prijavitelje (19. 10. 2026.), Prilog 1. Ocjenjivanje kvalitete projekta i Pitanja i odgovori 1–3, mdu.gov.hr",
 "ukratko": [
  ("Rok", "19. 11. 2026. do 16:00"),
  ("Iznos", "10.000 – 70.000 € po projektu, bez obveznog sufinanciranja"),
  ("Prijavitelj", "općina, grad ili Grad Zagreb (županije ne)"),
  ("Partneri", "neobvezno, najviše dva: JLS, javne ustanove, udruge, zaklade, vjerske zajednice"),
  ("Provedba", "od 7. 9. 2026. do dana prije početka školske godine 2027./2028."),
  ("Predaja", "samo elektronički, eprijave-mindu.gov.hr"),
 ],
 "uvod": "Ministarstvo demografije i useljeništva daje ukupno 5 milijuna eura za besplatne organizirane programe za djecu predškolske dobi i učenike od 1. do 4. razreda u njihovo slobodno vrijeme – tijekom školske godine i praznika. Prijavljuje se jedinica lokalne samouprave, a programe često provode partneri: knjižnica, vrtić, škola, sportski klub ili udruga.",
 "sekcije": [
  ("Tko se može prijaviti i s kim", [
   "<p>Prijavitelj je <strong>općina ili grad</strong> (i Grad Zagreb) koji ispunjava kriterij dobrog financijskog upravljanja iz Zaključka Vlade od 16. 4. 2026. – podatke za provjeru dostavlja Ministarstvo financija. Županije nisu prihvatljive kao prijavitelji.</p>",
   "<p><strong>Partnerstvo nije obvezno.</strong> Ako ga imate, dopuštena su najviše dva partnera: druga jedinica lokalne samouprave, javna ustanova (vrtić, škola, knjižnica, centar za kulturu…), udruga, zaklada ili vjerska zajednica. Partner mora imati stvarnu, unaprijed opisanu i mjerljivu ulogu, a odabir partnera morate provesti transparentno i dokumentirano.</p>",
   "<ul><li>Jedna JLS – <strong>jedna prijava</strong>; ako ih pošaljete više, u postupak ulazi zadnja.</li><li>Prijavitelj ne može istovremeno biti partner u drugoj prijavi.</li><li>Partner smije biti <strong>samo u jednoj prijavi</strong> – ako se pojavi u dvije, u postupak ulazi ranije podnesena.</li></ul>",
  ]),
  ("Što se financira", [
   "<p>Obvezne su dvije aktivnosti: <strong>priprema i provedba programa</strong> za djecu i <strong>promidžba i vidljivost</strong>. Programi mogu biti dugotrajni (cijela školska godina ili polugodište), kratkotrajni (samo praznici) ili u ciklusima, a sudjelovanje djece mora biti <strong>potpuno besplatno</strong>. Djeca ne moraju živjeti u vašoj općini.</p>",
   "<p>Četiri prioritetna područja:</p><ol><li>kultura, umjetnost, povijest, hrvatski jezik, običaji i tradicija</li><li>sport i rekreacija</li><li>priroda i zaštita okoliša te poljoprivreda</li><li>podrška u učenju – čitanje, pisanje, strani jezici, STEM</li></ol>",
   "<p>Nije prihvatljivo opremanje i uređenje objekata ni gradnja i adaptacija.</p>",
  ]),
  ("Troškovi: što prolazi, a što ne", [
   "<table class='t'><tr><th>Prihvatljivo</th><th>Ograničenje / napomena</th></tr>"
   "<tr><td>Plaće osoba zaposlenih kod <strong>partnera</strong> (i novo zapošljavanje)</td><td>Plaće zaposlenika općine/grada <strong>nisu</strong> prihvatljive. Zaposlenici škola i vrtića – samo za dodatni rad izvan redovnog programa.</td></tr>"
   "<tr><td>Vanjski suradnici (ugovor o djelu, autorski ugovor), vanjski stručnjaci za programe</td><td>Ne za pisanje prijave ni za provedbu javne nabave.</td></tr>"
   "<tr><td>Oprema i materijal</td><td>Najviše <strong>40 %</strong> ukupnih prihvatljivih troškova; nabaviti prije aktivnosti kojoj služi.</td></tr>"
   "<tr><td>Ulaznice, kotizacije, prijevoz na izlete, užina</td><td>Užina samo ako je opravdana trajanjem aktivnosti.</td></tr>"
   "<tr><td>Najam prostora i opreme, tisak materijala</td><td>Ako je potreban za program.</td></tr>"
   "<tr><td>Promidžba i vidljivost</td><td>Najviše <strong>4.000 €</strong> s PDV-om.</td></tr>"
   "<tr><td>Neizravni troškovi</td><td>Do <strong>7 %</strong> izravnih troškova, bez dokazivanja računima.</td></tr>"
   "</table>",
   "<p><strong>Neprihvatljivo</strong> je, među ostalim: prijevoz djece do mjesta održavanja programa i sudjelovanje roditelja, međusobna naplata kotizacija između prijavitelja i partnera, vozila, leasing, rabljena oprema, amortizacija i povrativi PDV.</p>",
  ]),
  ("Kako se boduje (najviše 100 bodova)", [
   "<table class='t'><tr><th>Kriterij</th><th>Bodovi</th><th>Kako do najviše bodova</th></tr>"
   "<tr><td>1a Doprinos prioritetnim područjima</td><td>0–20</td><td>Jasno opisan doprinos <strong>tri ili više</strong> područja = 20. Dva područja ili jedno s kontinuiranim programom = 10, jedno = 5.</td></tr>"
   "<tr><td>1b Potrebe ciljne skupine</td><td>0–20</td><td>Potrebe djece opisane u <strong>lokalnom kontekstu</strong> (brojke, nedostupni sadržaji, djeca izvan vrtića) i jasna korist.</td></tr>"
   "<tr><td>2a Proračun</td><td>0–10</td><td>Svaka stavka vezana uz aktivnost, realne tržišne cijene.</td></tr>"
   "<tr><td>2b Način provedbe</td><td>0–20</td><td>Detaljno: tko, što, kada, gdje, koliko skupina, podjela odgovornosti s partnerima.</td></tr>"
   "<tr><td>3a Indeks razvijenosti</td><td>0–25</td><td>Ne ovisi o vama: I.–II. skupina 25, III.–IV. 20, V. 15, VI. 10, VII. 5, VIII. 0.</td></tr>"
   "<tr><td>3b Brdsko-planinsko područje ili otok</td><td>0–5</td><td>Ne ovisi o vama.</td></tr>"
   "</table>",
   "<p>Kod jednakog broja bodova prednost ima bolja ocjena kriterija 1b, zatim 3a, pa veći broj djece. Sredstva se dodjeljuju po rang-listi, a dodijeljeni iznos može biti i manji od traženog.</p>",
  ]),
  ("Dokumenti za prijavu", [
   "<ul class='check'><li>Prijavni obrazac – ispunjava se izravno u sustavu eprijave-mindu.gov.hr (registrirajte se na vrijeme)</li><li>Obrazac 1. Izjava prijavitelja – datirana, potpisana i ovjerena pečatom</li><li>Obrazac 2. Izjava partnera – za svakog partnera posebno</li><li>Obrazac 3. Proračun u formatu .xlsx</li><li>Potvrda Porezne uprave o stanju javnog duga, ne starija od 30 dana – za prijavitelja i za svakog partnera</li></ul>",
  ]),
  ("Najčešće pogreške", [
   "<ul><li>Plaće zaposlenika općine u proračunu – nisu prihvatljive; osoblje planirajte kod partnera.</li><li>Isti partner u dvije prijave (npr. klub koji pristane svim općinama) – ulazi samo ranija prijava.</li><li>Oprema iznad 40 % ili nabavljena nakon početka aktivnosti kojoj služi.</li><li>Naplata sudjelovanja ili „simbolična članarina“ – program mora biti besplatan.</li><li>Trošak konzultanta za pisanje prijave u proračunu – nije prihvatljiv.</li><li>Potvrda Porezne starija od 30 dana na dan predaje.</li></ul>",
  ]),
  ("Nakon odobrenja", [
   "<p>U roku od 30 dana od potpisa ugovora dostavljate revidirani proračun i bjanko zadužnicu na iznos najmanje 5 % veći od dodijeljenog. Za svaku osobu koja radi s djecom, prije prvog rada s djecom, dostavljate izjavu o suglasnosti za uvid u kaznenu evidenciju i uvjerenje da se ne vodi kazneni postupak. Za svaku aktivnost vodite evidenciju sudionika. Zadnji zahtjev za isplatu podnosi se do 30. 9. 2027., a završno izvješće do 30. 11. 2027.</p>",
  ]),
 ],
 "faq": [
  ("Mora li općina sufinancirati projekt?", "Ne. Prema objavljenim odgovorima Ministarstva, Upute ne propisuju obvezno vlastito sufinanciranje ni intenzitet potpore po skupini razvijenosti. Dodijeljeni iznos može biti jednak ili manji od traženog."),
  ("Može li se platiti dodatni rad učiteljice ili odgojiteljice?", "Može, ako je partner škola ili vrtić i ako se radi o dodatnom radu na programu izvan redovnog odgojno-obrazovnog programa, u slobodno vrijeme djece. Rad koji je dio redovnog programa ustanove ne financira se iz projekta."),
  ("Je li trošak pripreme prijave ili javne nabave prihvatljiv?", "Ne. Troškovi vanjskih stručnjaka odnose se na pripremu i provedbu programa za djecu, a ne na izradu projektnog prijedloga, a usluga provedbe javne nabave nije navedena kao prihvatljiv trošak."),
  ("Mogu li sudjelovati djeca iz drugih općina?", "Mogu. Poziv ne ograničava ciljnu skupinu prema prebivalištu; odabir sudionika mora biti transparentan i nediskriminirajući."),
  ("Do kada se mogu postavljati pitanja?", "Najkasnije 10 dana prije roka, na programi_projekti@mdu.hr – za ovaj poziv do 9. 11. 2026."),
 ],
 "savjet": "Za sportske klubove, knjižnice i udruge: prijavitelj je uvijek općina ili grad, a partner smije biti u samo jednoj prijavi. Javite se svojoj općini što prije i ponudite gotov program s brojem djece, terminima i troškovima.",
},
{
 "slug": "esf-cjelodnevna-skola-ii",
 "poziv": "esf-izvannastavne-aktivnosti-cjelodnevna-skola-ii",
 "acc": "#0F6E74",
 "kratko": "ESF+ – izvannastavne aktivnosti, cjelodnevna škola II",
 "naslov": "Kako se prijaviti na ESF+ poziv za izvannastavne aktivnosti – cjelodnevna škola II (SF.2.4.06.14)",
 "h1": "ESF+ cjelodnevna škola II: vodič za prijavu",
 "opis": "Vodič za osnovne škole i osnivače: tko se može prijaviti, kako izračunati najveći iznos, što se financira, kako se boduje (prag 60 bodova) i koji dokumenti trebaju. Rok 23. 11. 2026. u 16:00.",
 "provjereno": "2026-11-08",
 "izvor": "https://eu-pozivi.eufondovi.gov.hr/call/?id=bf68b5ce-2dfb-43be-a4c7-42133f33f82b",
 "izvor_tekst": "Upute za prijavitelje poziva SF.2.4.06.14 (7. 10. 2026.), eKohezija / EU fondovi",
 "ukratko": [
  ("Rok", "23. 11. 2026. do 16:00 (eKohezija)"),
  ("Iznos", "od 40.000 € do iznosa izračunatog prema broju učenika; 100 % bespovratno"),
  ("Prijavitelj", "osnivač škole (RH, grad, općina, županija) ili jednosmjenska osnovna škola"),
  ("Provedba", "od 1. 9. 2026., 18–22 mjeseca, najkasnije do 1. 7. 2028."),
  ("Prag", "najmanje 60 od 100 bodova"),
  ("Ukupno", "20 milijuna € (ESF+ 85 %)"),
 ],
 "uvod": "Poziv financira izvannastavne aktivnosti u osnovnim školama s nastavom u jednoj smjeni, kao pripremu za uvođenje cjelodnevne škole, kroz dvije školske godine – 2026./2027. i 2027./2028. Novac ide u materijale, opremu i izvanučioničku nastavu, a ne u plaće voditelja.",
 "kalkulator": True,
 "sekcije": [
  ("Tko se može prijaviti", [
   "<ul><li><strong>Osnivač</strong> (Republika Hrvatska, grad, općina ili županija) – obvezno u partnerstvu sa <strong>svim svojim jednosmjenskim školama</strong> čiji učenici sudjeluju.</li><li><strong>Osnovna škola</strong> s nastavom u jednoj smjeni (u matičnoj ili barem jednoj područnoj školi) – samostalno ako sudjeluju samo njezini učenici; ako sudjeluju i druge škole, s njima u partnerstvu.</li></ul>",
   "<p>Status jednosmjenske škole provjerava se u Registru MZOM-a (ŠeR) na dan <strong>1. 10. 2026.</strong> Nisu prihvatljive škole iz Eksperimentalnog programa cjelodnevne škole ni škole koje su potpisale ugovor ili su partneri u prethodnom pozivu SF.2.4.06.09.</p>",
   "<p>Prijavitelj i partneri zajedno moraju imati prihode od najmanje 25 % planiranih troškova i barem dvoje zaposlenih (osnivači – JLP(R)S i tijela državne uprave – to ne dokazuju). Jedan prijavitelj – jedna prijava; partner smije biti samo u jednoj prijavi.</p>",
  ]),
  ("Što se financira", [
   "<p>Jedina obvezna (i jedina dopuštena) aktivnost je <strong>organizacija i provedba izvannastavnih aktivnosti</strong>: sport i tjelesni razvoj, kreativne i umjetničke kompetencije, digitalne kompetencije, osobne i socijalne vještine, pomoć u učenju, intelektualni razvoj i specifične kompetencije. Uz nju opisujete komunikaciju i vidljivost te upravljanje projektom.</p>",
   "<ul><li>Skupine imaju najmanje <strong>8 učenika</strong> (iznimke: škole s manje od 10 učenika, posebne ustanove i odjeli za učenike s teškoćama).</li><li>Aktivnosti se provode samo u jednosmjenskim školama (matičnim ili područnim).</li><li>Najmanje <strong>20 skupina</strong> ukupno kroz obje godine; ista skupina u obje godine broji se kao dvije.</li><li>U svakoj školskoj godini barem <strong>40 % učenika</strong> koji nastavu pohađaju u jednoj smjeni mora završiti barem jedan program (dokazuje se e-dnevnikom i popisom s OIB-om).</li></ul>",
  ]),
  ("Troškovi", [
   "<table class='t'><tr><th>Vrsta troška</th><th>Ograničenje</th></tr>"
   "<tr><td>Literatura, odgojno-obrazovni i potrošni materijali, didaktika; oprema (IKT, licence, namještaj); izvanučionička nastava i ekskurzije (prijevoz, ulaznice, smještaj, obroci, dnevnice za učenike, pratitelje i učitelje)</td><td>Prosječno do <strong>2.000 € po skupini</strong> godišnje (broj skupina × 2.000 €)</td></tr>"
   "<tr><td>Komunikacija i vidljivost</td><td>Do <strong>2.500 €</strong></td></tr>"
   "<tr><td>Neizravni troškovi</td><td>Paušal <strong>2 %</strong> izravnih troškova</td></tr>"
   "</table>",
   "<p><strong>Nisu prihvatljivi:</strong> plaće za provedbu izvannastavnih aktivnosti, vanjske usluge stručnjaka, školski obroci, udžbenici za obvezni kurikulum, prijevoz učenika do škole, adaptacija prostora, vozila te aktivnosti već financirane iz drugih programa (Eksperimentalni program CDŠ, MZOM-ovi pozivi za izvannastavne aktivnosti, poziv SF.2.4.06.09). Sudjelovanje se ne smije naplaćivati.</p>",
  ]),
  ("Kako se boduje (prag 60 od 100)", [
   "<table class='t'><tr><th>Kriterij</th><th>Bodovi</th><th>Kako do najviše bodova</th></tr>"
   "<tr><td>Broj škola</td><td>0–1</td><td>Više od jedne ustanove = 1.</td></tr>"
   "<tr><td>Udio učenika 2026./2027. i 2027./2028.</td><td>2 × 0–10</td><td>Više od 90 % učenika u jednoj smjeni = 10 (80–90 % = 8, 70–80 % = 6, 60–70 % = 4, 50–60 % = 2, 40–50 % = 1).</td></tr>"
   "<tr><td>Analiza potreba</td><td>0–10</td><td>Opis stanja <strong>po svakoj školi</strong> i jasno kako projekt rješava problem.</td></tr>"
   "<tr><td>Broj skupina</td><td>0–9</td><td>Više od 30 = 9; 26–30 = 6; 21–25 = 3; 20 = 0.</td></tr>"
   "<tr><td>Proračun i provedba</td><td>2–10</td><td>Svaka stavka nužna; razrađeni koraci, rokovi i uloge partnera.</td></tr>"
   "<tr><td>Inovativnost</td><td>0–10</td><td>Više <strong>novih</strong> aktivnosti kojih nije bilo 2025./2026. = 2; <strong>volontiranje učenika u lokalnoj zajednici</strong> = 8.</td></tr>"
   "<tr><td>Horizontalna načela</td><td>0–15</td><td>Udio programa iz digitalnih vještina, ekološke osviještenosti i osobnih/socijalnih vještina (uklj. pomoć u učenju i učenike s teškoćama) – za svako područje 30 % i više = 5. Svako mora biti obrazloženo.</td></tr>"
   "<tr><td>Iskustvo i suradnja</td><td>0–20</td><td>Iskustvo u 3+ projekta iste ili veće vrijednosti i sličnim aktivnostima = 10; suradnja s <strong>više lokalnih dionika</strong> (klub, knjižnica, udruga – neformalno) = 10.</td></tr>"
   "<tr><td>Regionalni razvoj</td><td>1–5</td><td>Prema indeksu razvijenosti.</td></tr>"
   "</table>",
   "<p>Ciljeve postavite realno: ispod 85 % ostvarenja pokazatelja slijede financijske korekcije (2–10 % ukupnih troškova), a kod mjerljivih ishoda i strože.</p>",
  ]),
  ("Dokumenti za prijavu", [
   "<ul class='check'><li>Prijavni obrazac u sustavu eKohezija</li><li>Obrazac 1. Izjava prijavitelja – datirana od 7. 10. 2026. do dana predaje, potpis ovlaštene osobe u mandatu i pečat (uz punomoć ako potpisuje opunomoćenik)</li><li>Obrazac 2. Izjava partnera – za svaku partnersku školu</li><li>Obrazac 3. Podaci o izvannastavnim aktivnostima s troškovnikom (Excel)</li><li>Zadnji godišnji financijski izvještaj, gdje je primjenjivo</li></ul>",
   "<p>Potvrdu Porezne uprave o stanju duga tijelo će zatražiti kasnije, tijekom procjene kvalitete.</p>",
  ]),
  ("Najčešće pogreške", [
   "<ul><li>Traženi iznos iznad najvećeg dopuštenog za vaš broj učenika – prijava se isključuje (vidi kalkulator).</li><li>Traženi iznos ispod 40.000 € – i to je isključenje; male škole zato se udružuju preko osnivača.</li><li>Plaće voditelja ili vanjski treneri u proračunu.</li><li>Manje od 20 skupina ili manje od 40 % učenika u nekoj od godina.</li><li>Škola s nastavom u dvije smjene u projektu – njezini troškovi nisu prihvatljivi.</li><li>Izjave potpisane prije objave poziva ili od osobe kojoj je istekao mandat.</li></ul>",
  ]),
 ],
 "faq": [
  ("Koliko najviše možemo tražiti?", "Najveći iznos = broj učenika u jednoj smjeni (ŠeR na dan 1. 10. 2026.) × 500 € + 2.500 € za vidljivost + 2 % neizravnih troškova. Za školu sa 100 učenika to je 53.550 €. Najmanji iznos je 40.000 €."),
  ("Mogu li se iz projekta platiti voditelji aktivnosti?", "Ne. Plaće za provedbu izvannastavnih aktivnosti nisu prihvatljiv trošak ovog poziva, kao ni vanjske usluge stručnjaka; aktivnosti vode djelatnici škole. Projekt financira materijale, opremu i izvanučioničku nastavu."),
  ("Može li prijavu podnijeti škola bez osnivača?", "Može, ako ima nastavu u jednoj smjeni i ako u projektu sudjeluju samo njezini učenici. Ako sudjeluju učenici drugih škola, s njima je obvezno partnerstvo."),
  ("Je li poziv „tko prvi, njegov“?", "Ne. Poziv je otvoren do 23. 11. 2026., a projekti se rangiraju prema bodovima nakon procjene; potrebno je najmanje 60 bodova."),
 ],
 "savjet": "Najviše bodova se gubi na udjelu učenika i broju skupina. Prije pisanja s razrednicima procijenite koliko učenika realno možete uključiti u svakoj godini i postavite cilj malo ispod te brojke – bodovi rastu s udjelom, a korekcije prijete ako cilj ne ostvarite.",
},
{
 "slug": "esf-sport-djeca-i-mladi-u-riziku",
 "poziv": "esf-djeca-mladi-rizik-socijalne-iskljucenosti-sport",
 "acc": "#C55A1E",
 "kratko": "ESF+ – sport za djecu i mlade u riziku od socijalne isključenosti",
 "naslov": "Kako se prijaviti na ESF+ poziv Uključivanje djece i mladih u riziku od socijalne isključenosti u sport (SF.3.4.08.07)",
 "h1": "ESF+ sport za djecu i mlade u riziku: vodič za prijavu",
 "opis": "Vodič za sportske udruge i škole sa školskim sportskim društvom: ciljne skupine i dokazi, minimalni broj treninga, paušal 40 %, bodovanje (prag 70) i dokumenti. Poziv je obustavljen do 23. 11. 2026.",
 "provjereno": "2026-11-08",
 "izvor": "https://mints.gov.hr/javni-pozivi-i-natjecaji-11414/s-p-o-r-t/22182",
 "izvor_tekst": "Upute za prijavitelje poziva SF.3.4.08.07 i obavijesti Ministarstva turizma i sporta (eKohezija, mints.gov.hr)",
 "ukratko": [
  ("Status", "obustavljen do kraja dana 23. 11. 2026.; krajnji rok 31. 12. 2026. u 16:00"),
  ("Iznos", "50.000 – 150.000 €; do 98 % bespovratno"),
  ("Prijavitelj", "sportska udruga u Evidenciji pravnih osoba u sportu ili OŠ/SŠ sa školskim sportskim društvom"),
  ("Trajanje", "12–36 mjeseci od stupanja ugovora na snagu"),
  ("Način dodjele", "otvoreni trajni poziv – prijave se obrađuju redom zaprimanja"),
  ("Prag", "najmanje 70 od 100 bodova"),
 ],
 "uvod": "Poziv financira redovite sportske i sportsko-rekreativne programe i edukativne radionice za djecu i mlade u riziku od socijalne isključenosti, djecu s teškoćama u razvoju, mlade s invaliditetom te djecu i mlađe punoljetne osobe s problemima u ponašanju. Prijave se obrađuju redom zaprimanja, a poziv se obustavlja kad prijave dosegnu do 120 % raspoloživog novca – zato je prijavu najbolje imati spremnu prije ponovnog otvaranja.",
 "status": "Ministarstvo je obustavu zaprimanja prijava od travnja 2026. produljivalo više puta; zadnja obavijest (7. 10. 2026.) produljuje je do kraja dana 23. 11. 2026. Prije predaje provjerite najnoviju obavijest – i datum ponovnog otvaranja i moguće izmjene Uputa.",
 "sekcije": [
  ("Tko se može prijaviti i s kim", [
   "<ul><li><strong>Udruge</strong> upisane u Registar udruga i u Evidenciju pravnih osoba u sportu (sportski klubovi i savezi).</li><li><strong>Osnovne i srednje škole</strong> koje imaju osnovano školsko sportsko društvo (provjera u registru Hrvatskog školskog sportskog saveza).</li></ul>",
   "<p>Partneri nisu obvezni, ali donose bodove (do 5). Mogu biti: ustanove u sustavu sporta ili socijalne skrbi, škole sa ŠSD-om, visoka učilišta, dječji vrtići te udruge iz sporta, socijalne skrbi ili s djelatnostima pomoći djeci, mladima i osobama s invaliditetom.</p>",
   "<p>Prijavitelj i partneri zajedno moraju imati prihode od najmanje 25 % planiranih troškova te barem jednog zaposlenog <strong>ili</strong> volontera (prema zadnjem godišnjem financijskom izvješću). Jedan prijavitelj – jedna prijava (vrijedi prva podnesena); partner smije biti u više prijava.</p>",
  ]),
  ("Ciljne skupine i kako se dokazuju", [
   "<table class='t'><tr><th>Skupina</th><th>Dokaz (uz osobnu iskaznicu ili rodni list)</th></tr>"
   "<tr><td>Djeca (do 18) i mladi (18–30) čija su oba roditelja nezaposlena</td><td>potvrda HZZ-a</td></tr>"
   "<tr><td>… roditelja korisnika dječjeg doplatka (minimalna primanja)</td><td>rješenje o doplatku za djecu</td></tr>"
   "<tr><td>… bez odgovarajuće roditeljske skrbi</td><td>rješenje/uvjerenje Hrvatskog zavoda za socijalni rad</td></tr>"
   "<tr><td>… samohranih roditelja / iz jednoroditeljskih obitelji</td><td>smrtni list, presuda o razvodu, potvrda HZSR-a ili druga javna isprava</td></tr>"
   "<tr><td>… iz obitelji s troje ili više djece</td><td>rodni listovi ili izvadak iz matice rođenih za svako dijete</td></tr>"
   "<tr><td>Djeca s teškoćama u razvoju i mladi s invaliditetom</td><td>liječnička dokumentacija, upis u Registar osoba s invaliditetom ili nalaz/rješenje</td></tr>"
   "<tr><td>Djeca i mlađe punoljetne osobe (18–21) s problemima u ponašanju</td><td>rješenje/uvjerenje HZSR-a</td></tr></table>",
   "<p>Za svakog sudionika prikupljate ime i prezime, OIB, spol, datum rođenja, status na tržištu rada i status obrazovanja. Sudionici se odabiru <strong>redoslijedom zaprimanja prijava</strong>, a o projektu ih obavještavate javno (npr. preko mrežne stranice).</p>",
  ]),
  ("Što se financira i minimalni opseg", [
   "<ul><li><strong>Sportski i sportsko-rekreativni programi</strong> (postojeći ili unaprijeđeni) – svaki program najmanje <strong>70 treninga po 45 minuta</strong> u godini dana, uključujući praznike; dopuštena je prilagodba i stručna podrška za djecu s teškoćama.</li><li><strong>Edukativne radionice</strong> o sportu i zdravim navikama – najmanje 2, svaka barem 120 minuta i 10 sudionika iz ciljne skupine.</li><li><strong>Vidljivost</strong> – završna konferencija i barem jedan promotivni materijal.</li></ul>",
   "<p>Sudionik se računa kao uspješan kad prisustvuje na barem <strong>60 % predviđenih sati</strong> programa. Upute za taj pokazatelj kao minimalnu vrijednost navode vrijednost pokazatelja broja sudionika – planirajte zato da gotovo svi upisani sudionici redovito dolaze i provjerite tumačenje u objavljenim pitanjima i odgovorima. Izrada novog programa nije prihvatljiv trošak.</p>",
  ]),
  ("Troškovi: plaće + paušal 40 %", [
   "<p>Proračun je jednostavan: planirate samo <strong>izravne troškove osoblja</strong> (zaposleni po ugovoru o radu; satnica = zadnji godišnji bruto trošak ÷ 1.720 sati), a <strong>svi ostali troškovi</strong> – oprema, najam dvorane, prijevoz na natjecanja, kotizacije, hrana, radionice, vidljivost i neizravni troškovi – pokrivaju se paušalom od <strong>40 % troškova osoblja</strong>, bez dokazivanja računima.</p>",
   "<p>Primjer: 80.000 € troškova osoblja + 32.000 € paušala = 112.000 €. Neprihvatljivo je, među ostalim, ugovor o djelu za vlastite zaposlenike, podugovaranje samih partnera, vozila, rabljena oprema i aktivnosti izvan Hrvatske.</p>",
  ]),
  ("Kako se boduje (prag 70 od 100)", [
   "<table class='t'><tr><th>Kriterij</th><th>Bodovi</th><th>Kako do najviše bodova</th></tr>"
   "<tr><td>Broj sudionika</td><td>0–30</td><td>10 sudionika = 0, svaki sljedeći +2; <strong>više od 24 = 30</strong>.</td></tr>"
   "<tr><td>Potrebe ciljnih skupina</td><td>2–10</td><td>Lokalni podaci i jasna korist.</td></tr>"
   "<tr><td>Broj programa</td><td>0–5</td><td>6 i više programa = 5.</td></tr>"
   "<tr><td>Broj radionica</td><td>0–5</td><td>7 i više = 5.</td></tr>"
   "<tr><td>Izvedivost</td><td>2–10</td><td>Usklađeni aktivnosti, rokovi i proračun.</td></tr>"
   "<tr><td>Održivost</td><td>0–10</td><td>8 i više novouključenih sudionika u programe nakon projekta = 10.</td></tr>"
   "<tr><td>Horizontalna načela</td><td>5–15</td><td>Konkretne mjere za nediskriminaciju, ravnopravnost spolova i pristupačnost – 5 po načelu.</td></tr>"
   "<tr><td>Stručnost osoblja</td><td>2–10</td><td>Jasno opisane kvalifikacije trenera i stručnjaka.</td></tr>"
   "<tr><td>Partnerstvo</td><td>0–5</td><td>Samostalna prijava = 0; jasno opisana uloga partnera = 5.</td></tr></table>",
  ]),
  ("Dokumenti za prijavu", [
   "<ul class='check'><li>Prijavni obrazac u sustavu eKohezija (predložak obrasca dostupan je uz poziv)</li><li>Obrazac 1. Izjava prijavitelja – potpis ovlaštene osobe upisane u registar i pečat</li><li>Obrazac 2. Izjava partnera – za svakog partnera</li><li>Potvrda Porezne uprave o stanju duga, ne starija od datuma objave poziva – za prijavitelja i partnere</li><li>Zadnji godišnji financijski izvještaj, ako nije javno dostupan u registrima</li></ul>",
  ]),
  ("Najčešće pogreške", [
   "<ul><li>Škola bez upisanog školskog sportskog društva kao prijavitelj.</li><li>Sudionici bez dokaza o pripadnosti ciljnoj skupini – ne broje se u pokazatelje.</li><li>Program kraći od 70 treninga u godini.</li><li>Previsoko postavljen broj sudionika koji neće redovito dolaziti – korekcije na kraju projekta.</li><li>Prijava pripremljena tek nakon otvaranja – kod obrade redom zaprimanja kasni se.</li></ul>",
  ]),
 ],
 "faq": [
  ("Kada se poziv ponovno otvara?", "Prema zadnjoj obavijesti Ministarstva turizma i sporta obustava traje do kraja dana 23. 11. 2026. Krajnji rok poziva je 31. 12. 2026. u 16:00 ili do iscrpljenja sredstava. Obustava je dosad produljivana više puta, pa prije predaje provjerite najnoviju obavijest."),
  ("Može li klub prijaviti trenere na ugovor o djelu?", "Projekt financira izravne troškove osoblja koji proizlaze iz ugovora o radu ili rješenja. Ugovor o djelu za vlastite zaposlenike koji primaju redovnu plaću nije prihvatljiv; ostale vanjske usluge pokrivaju se paušalom od 40 %."),
  ("Trebamo li račune za opremu i dvoranu?", "Ostali troškovi pokrivaju se paušalom od 40 % troškova osoblja i pri provjeri zahtjeva za nadoknadom ne dokazuju se računima (osim kod sumnje na nepravilnost). Plaćanja i pravila nabave i dalje morate poštovati."),
  ("Mogu li postavljati pitanja dok je poziv obustavljen?", "Ne – u vrijeme obustave Ministarstvo nije obvezno odgovarati. Pitanja se šalju na esf.pozivi@mints.hr najkasnije 14 dana prije isteka roka."),
 ],
 "savjet": "Najviše bodova nosi broj sudionika (do 30) – ali samo ako za svakoga imate dokaz o pripadnosti ciljnoj skupini i ako će redovito dolaziti. Dokumentaciju sudionika (rješenja o doplatku, potvrde HZSR-a, liječničku dokumentaciju) skupljajte već sada, uz suglasnost roditelja.",
},
]
