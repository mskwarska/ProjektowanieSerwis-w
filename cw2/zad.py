# 1 i 2

lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

print(("W tekście jest {} liter '{}' oraz {} liter '{}'").format(lorem.count("Rokicki"[3]), "Rokicki"[3], lorem.count("Maciej"[2]), "Maciej"[2]))

# 4

zmienna_typu_string = "dowolny ciąg tekstowy"

print(dir(zmienna_typu_string))
help(zmienna_typu_string.split())

# 5
print("Maciej Rokicki".lower()[::-1])

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

Imie1Naziwsko1 = (999999)
Imie2Naziwsko2 = (999998)

# 9

studenci = dict

# 10
lista = [123456789, 123456789, 123456788, 123456788, 123456788, 123456787, 123456786]
lista = set(lista)
print(lista)

# 11
[print(x) for x in range(1, 11)]

# 12
[print(x) for x in range(100, 19, -5)]