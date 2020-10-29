# 1 i 2

lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

print(("W tekście jest {} liter '{}' oraz {} liter '{}'").format(
    lorem.count("Rokicki"[3]), "Rokicki"[3], lorem.count("Maciej"[2]), "Maciej"[2]))

# 4

zmienna_typu_string = "dowolny ciąg tekstowy"

print(dir(zmienna_typu_string))
help(zmienna_typu_string.split())

# 5
print("Maciej"[::-1].capitalize() + " " + "Rokicki"[::-1].capitalize())

# 6

lista = [x for x in range(1, 11)]
nowaLista = lista[5:]
del lista[5:]
print(lista)
print(nowaLista)

# 7

polaczonaLista = [0] + lista + nowaLista

polaczonaLista.sort(reverse=True)

print(polaczonaLista)

# 8

krotki = [(999999, "Imie1", "Nazwisko1"), (999998, "Imie2", "Nazwisko2")]

# 9

studenci = {
    "Student1": {
        "Indeks": 999999,
        "Imie": "Imie1",
        "Nazwisko": "Nazwisko1",
        "Wiek": 21,
        "Email": "email1@email.com",
        "RokUrodzenia": 1999,
        "Adres": "Adres1"
    },
    "Student2": {
        "Indeks": 999998,
        "Imie": "Imie2",
        "Nazwisko": "Nazwisko2",
        "Wiek": 22,
        "Email": "email2@email.com",
        "RokUrodzenia": 1998,
        "Adres": "Adres2"
    }
}

# print(studenci["Student2"]["Imie"])

# 10
lista = [123456789, 123456789, 123456788,
         123456788, 123456788, 123456787, 123456786]
lista = set(lista)
print(lista)

# 11
[print(x) for x in range(1, 11)]

# 12
[print(x) for x in range(100, 19, -5)]

# 13

samochod1 = {
    "Marka": "BMW",
    "Model": "Gruz",
    "RokProdukcji": 1995,
    "Przebieg": 2003
}

samochod2 = {
    "Marka": "Volvo",
    "Model": "XD60",
    "RokProdukcji": 2015,
    "Przebieg": 200365
}

samochod3 = {
    "Marka": "Ford",
    "Model": "Mondeo",
    "RokProdukcji": 1999,
    "Przebieg": 320452
}

listaSlownikow = [
    samochod1,
    samochod2
]

for samochod in listaSlownikow:
    str = ""
    for key in samochod.keys():
        str += "{}: {} ".format(key, samochod[key])

    print(str)
