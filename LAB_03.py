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

for i in range(1, broj_ispita+1):
    ispit = {}

    for j, kolegij in enumerate(kolegiji, start = 1):
        print(f"\t{j}. {kolegij['ime']}")

    odabrani_kolegij = int(input("Odaberite kolegij: "))

    ispit['kolegij'] = kolegiji[odabrani_kolegij-1]


    dan = int(input(f"Unesite dan {i}. ispita: "))
    mjesec = int(input(f"Unesite mjesec {i}. ispita: "))
    godina = int(input(f"Unesite godinu {i}. ispita: "))

    ispit["datum"] = date(godina, mjesec, dan)
    ispiti.append(ispit)

    kolegiji.append(kolegij)

    print("Popis svih ispita: ")
    print(f"\t Ispit iz kolegija ")