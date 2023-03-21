# LABORATORIJSKA VJEZBA 2

from datetime import date

# Podaci o kolegiju
ime_kolegija = input("Unesite ime kolegija: ").upper()
ects_bodovi = int(input("Unesite ECTS bodove za kolegij: "))

# Stvaranje rječnika za kolegij
kolegij = {
    "ime": ime_kolegija, "ects": ects_bodovi
}

# Podaci o ispitu
dan = int(input("Unesite dan ispita: "))
mjesec = int(input("Unesite mjesec ispita: "))
godina = int(input("Unesite godinu ispita: "))

# Stvaranje objekta datuma
datum_ispita = date(godina, mjesec, dan)

# Stvaranje rječnika za ispit
ispit = {
    "kolegij": kolegij, "datum": datum_ispita
}

# Podaci o studentu
ime_studenta = input("Unesite ime studenta: ").capitalize()
prezime_studenta = input("Unesite prezime studenta: ").capitalize()

# Stvaranje rječnika za studenta
student = {
    "ispit": ispit, "ime": ime_studenta, "prezime": prezime_studenta
}

# Ispis
print("Student", ime_studenta, prezime_studenta)
print("je prijavio ispit iz kolegija", student["ispit"]["kolegij"]["ime"])
print("koji će se održati:", student["ispit"]["datum"])
