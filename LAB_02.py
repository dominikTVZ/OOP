from datetime import date

kolegij = {}

kolegij["ime"] = input("Unesite ime kolegija: ").upper()
kolegij["bodovi"] = int(input("Unesite ECTS bodove za kolegij: "))


ispit = {}

ispit["kolegij"]= kolegij


dan = ispit["dan"] = int(input("Unesite dan: "))
mjesec = ispit["mjesec"] = int(input("Unesite mjesec: "))
godina = ispit["godina"] = int(input("Unesite godinu: "))
ispit["datum"] = date(godina, mjesec, dan)

student = {}

student["ispit"]= ispit


student["ime"] = input("Unesite ime studenta: ")
student["prezime"] = input("Unesite prezime studenta: ")

print("Student", student["ime"], student["prezime"])
print("je prijavio ispit iz kolegija", student["ispit"]["kolegij"]["ime"], "koji će se održati datuma: ", student["ispit"]["datum"])
