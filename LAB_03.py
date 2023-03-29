from datetime import date
kolegiji = []

broj_kolegija= int(input("Unesite broj kolegija: "))

for i in range(1, broj_kolegija+1):
    kolegij = {}

    kolegij['ime'] = input(f"Unesite ime {i}. kolegija: ")
    kolegij['ECTS'] = int(input(f"Unesite broj ects-a {i}. kolegija: "))

    kolegiji.append(kolegij)


ispiti = []

broj_ispita = int(input("Unesite broj ispita: "))

#ISPIT JE PREDSTAVLJEN RIJECNIKOM KOJI SADRZI KOLEGIJ(IME,ECTS) I DATUM
for i in range(1, broj_ispita+1):
    ispit = {}

    print("Popis kolegija: ")
    for j, kolegij in enumerate(kolegiji, start = 1):
        print(f"\t{j}. {kolegij['ime']}")

    odabrani_kolegij = int(input("Unesite kolegij: "))

    ispit['kolegij'] = kolegiji[odabrani_kolegij-1]

    dan = int(input(f"Unesite dan {i}. ispita: "))
    mjesec = int(input(f"Unesite mjesec {i}. ispita: "))
    godina = int(input(f"Unesite godinu {i}. ispita: "))
    ispit['datum'] = date(godina, mjesec, dan)

    ispiti.append(ispit)

"""ISPIS ZA 2.ZADATAK
print("Popis svih ispita: ")
for ispit in ispiti:
    print(f"\t Ispit iz kolegija {ispit['kolegij']['ime']},")
    print(f"\tkoji nosi {ispit['kolegij']['ECTS']} bodova održat će se {ispit['datum']}")
"""

studenti = []

broj_studenta= int(input("Unesite broj studenta: "))
for i in range(1, broj_studenta+1):
    student = {}

    for j,

        student['ime'] = input(f"Unesite ime {i}. kolegija: ")
        student['prezime'] = int(input(f"Unesite broj ects-a {i}. kolegija: "))

        studenti.append(student)

