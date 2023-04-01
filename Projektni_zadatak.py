from datetime import date

#2.PROGRAMSKI ZADATAK

korisnici = []
broj_korisnika = int(input("Unesite broj korisnika: "))

for i in range(1, broj_korisnika+1):
    korisnik = {}

    korisnik['ime'] = input("Unesite ime korisnika: ").title()
    korisnik['prezime'] = input("Unesite prezime korisnika: ").title()
    korisnik['telefon'] = int(input("Unesite telefon korisnika: "))
    korisnik['email'] = input("Unesite email korisnika: ").strip()
    korisnici.append(korisnik)


kategorije = []
broj_kategorija = int(input("Unesite broj kategorija: "))

for i in range(1, broj_kategorija+1):
    kategorija = {}

    kategorija['naziv'] = input(f"Unesite naziv {i} kategorije: ")

    kategorija['artikli']= []
    broj_artikla = int(input(f"Unesite broj artikla za {i} kategoriju: "))
    for j in range(1, broj_artikla+1):
        artikl = {}
        artikl['naslov'] = input(f"Unesite naslov {j} artikla: ")
        artikl['opis'] = input(f"Unesite opis {j} artikla: ")
        artikl['cijena'] = float(input(f"Unesite cijenu {j} artikla: "))

    kategorije.append(kategorija)


prodaje = []
broj_prodaja  = int(input("Unesite broj prodaja: "))

for i in range(1, broj_prodaja+1):
    prodaja = {}


    prodaja['artikli'] = kategorije
    prodaja['korisnik'] = korisnici

    dan = int(input(f"Unesite dan isteka {i}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {i}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {i}. prodaje: "))
    prodaja['datum'] = date(godina, mjesec, dan)

    print(f"Odaberite korisnika {i}. prodaje: ")

    for j, korisnik in enumerate(korisnici, start=1):
        print(f"\t{j}. {korisnik['ime']} {korisnik['prezime']}")

    odabrani_korisnik = int(input("Odabrani korisnik: "))

    print(f"Odaberite kategoriju {i} prodaje: ")

    for k, kategorija in enumerate(kategorije, start=1):
        print(f"\t{k}. {kategorija['naziv']} ")

    odabrana_kategorija = int(input("Odabrana kategorija: "))

    print(f"Odaberite artikl {i}.prodaje: ")
    for z, kategorija in enumerate(kategorije, start=1):
        print(f"\t{z}. {kategorija['artikli']}")


    odabrani_artikl = int(input("Odabrani artikl: "))

    prodaje.append(prodaja)






