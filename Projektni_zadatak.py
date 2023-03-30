from datetime import date

korisnik = {}

korisnik["ime"] = input("Unesite ime korisnika: ").title()
korisnik["prezime"] = input("Unesite prezime korisnika: ").title()
korisnik["telefon"] = int(input("Unesite telefon korisnika: "))
korisnik["email"] = input("Unesite email korisnika: ").strip()


artikl = {}

artikl["naslov"] = input("Unesite naslov artikla: ")
artikl["opis"] = input("Unesite opis artikla: ")
artikl["cijena"] = float(input("Unesite cijenu artikla: "))

prodaja = {}

dan = int(input("Unesite dan isteka prodaje: "))
mjesec = int(input("Unesite mjesec isteka prodaje: "))
godina = int(input("Unesite godinu isteka prodaje: "))

prodaja["datum"] = date(godina, mjesec, dan)
prodaja["artikl"] = artikl
prodaja["korisnik"] = korisnik

#ISPIS ZA 1.PROGRAMSKI ZADATAK

print("Informacije o artiklu: ")
print("\t Naslov: ", prodaja["artikl"]["naslov"])
print("\t", prodaja["artikl"]["opis"])
print("\t Cijena: ", prodaja["artikl"]["cijena"])

print("Datum isteka prodaje: ")
print("\t Dan: ", prodaja["datum"].day)
print("\t Mjesec: ", prodaja["datum"].month)
print("\t Godina: ", prodaja["datum"].year)

print("Informacije o korisniku: ")
print("\t", prodaja["korisnik"]["ime"], prodaja["korisnik"]["prezime"])
print("\t Telefon: ", prodaja["korisnik"]["telefon"])
print("\t Email: ", prodaja["korisnik"]["email"])

#2.PROGRAMSKI ZADATAK



korisnici = ()

broj_korisnika = int(input("Unesite broj korisnika: "))

for i in range(1, broj_korisnika+1):
    korisnici = []

    for j in range(1, broj_korisnika+1):
        korisnik  = {}



kategorije = ()

prodaje = ()

