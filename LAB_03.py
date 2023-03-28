"""""
zivotinje = []

broj_zivotinja = int(input("Unesite broj životinja: "))

for i in range(broj_zivotinja):
    zivotinja = {}

    zivotinja["ime"] = input("Unesite ime zivotinje: ")
    zivotinja["vrsta"] = input("Unesite vrstu zivotinje: ")

    zivotinje.append(zivotinja)

for zivotinja in zivotinje:
    print(zivotinja["ime"])
   

zivotinje = ["Dino", "Kira", "Šnjofavac"]

for index, zivotinja in enumerate(zivotinje, start = 1):
    print(f'{index}. {zivotinja}')


korisnik = {
    "ime": "Ivan",
    "prezime":"Ivic",
    "godine":24
}
for value in korisnik:
    print(value, end = " ")
    print()

for key, value in korisnik.items():
    print(f"{key}{value}", end = " ")
    print()
for value in korisnik.values():
    print(f"{value}",end = "")
    print()
"""""