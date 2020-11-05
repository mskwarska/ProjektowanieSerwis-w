


# 1.Pobierz ze strony https://pl.lipsum.com/ tekst akapitu
# o tytule „Czym jest Lorem Ipsum” i przypisz go do zmiennej.
tekst= "Przejdź na stronę https://pyformat.info/ a następnie zapisz w oddzielnym pliku .py i wykonaj 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”, których nie było w przykładach z tego podrozdziału (np. z wyrównaniem, ilością pozycji liczby, znakiem itp.)"

# 2.Wyświetl na konsoli tekst postaci "W tekście jest {liczba_liter1} liter ...
# oraz {liczba_liter2} liter ...” . W miejsca { } podstaw zmienne, które będą przechowywały liczbę wystąpień danych liter. Litery, które mają być wyszukane powinny zostać przekazane jako indeks do 3 znaku nazwiska oraz 2 znaku imienia osoby wykonującej ćwiczenie, np. imie = „Krzysztof”, nazwisko = „Ropiak”, litera_1 = imie[2], litera_2 = nazwisko[3].
liczba_liter_h=tekst.count("h")
liczba_liter_z=tekst.count("z")
print("W tekście jest " + str(liczba_liter_h) + " liter h oraz " + str(liczba_liter_z) + " liter z")

# 4
zmienna_typu_string="Hello my friend"
print(dir(zmienna_typu_string))
#help(zmienna_typu_string.islower())

# 5
imie="Marta"
nazwisko="Skwarska"
print(imie[::-1].capitalize() + " " + nazwisko[::-1].capitalize())

# 6
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
helper = lista[:len(lista)//2]
nowa_lista = lista[len(lista)//2:]
lista=helper
print(lista)
print(nowa_lista)

# 7.Połącz te listy ponownie. Dodaj do listy wartość „0” na początku.
# Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.
lista_cala=lista+nowa_lista
print(lista_cala)
lista_cala.insert(0,0)
lista_cala=sorted(lista_cala, reverse=True) #Descending
print(lista_cala)

# 8 Za pomocą krotek stwórz listę studentów swojej grupy przypisując
# numer indeksu do imienia i nazwiska (dane nie muszą być prawdziwe). - lista krotek

lista_studentow=[(12345, 'Adam', 'Wiśniewski'), (25985, 'Kasia', 'Zielińska'), (34582, 'Hubert', 'Byczewski'), (41253, 'Wiesia', 'Zduńczyk')]
print("Lista krotek:\n", lista_studentow)

# 9 Przekształć poprzednie zadanie na słownik, a następnie dodaj pary zawierające wiek,
# adres email, rok urodzenia oraz adres.
print("Słownik ")
#słownik_studentów=dict.fromkeys(lista_studentow, lista_studentow[0][0]) z przypisaniem klucza jako indeks jak dla każdego to for
#słownik_studentów = dict.fromkeys(lista_studentow) # lista na słownik
print("Słownik z nowymi osobami")
lista_studentow_slownik= {
    "St1": {
        "indeks": lista_studentow[0][0],
        "imie" : lista_studentow[0][1],
        "nazwisko" : lista_studentow[0][2],
        "wiek" : 23,
        "email" : "adam@student.pl",
        "rok urodzenia" : 1997,
        "adres" : "Warszawa 15"
            },
    "St2" : {
        "indeks": lista_studentow[1][0],
        "imie" : lista_studentow[1][1],
        "nazwisko" : lista_studentow[1][2],
        "wiek" : 24,
        "email" : "kasia@student.pl",
        "rok urodzenia" : 1996,
        "adres" : "Płock 75"
    },
    "St3" : {
        "indeks": lista_studentow[2][0],
        "imie" : lista_studentow[2][1],
        "nazwisko" : lista_studentow[2][2],
        "wiek" : 22,
        "email" : "hubert@student.pl",
        "rok urodzenia" : 1998,
        "adres" : "Lublin 15"
    }

}

# 10 Stwórz listę zawierającą numery telefonów z powtórzeniami,
# a następnie usuń powtórzenia za pomocą rzutowania na set;
numery=[123456789, 123456789, 236548523, 234589617, 987654321, 9974451202, 236548523]
print(numery)
numery=list(set(numery))
print(numery)
# 11 Korzystając z funkcji range wypisz elementy rosnąco od 1 - 10
for i in range(1,11):
    print(i)

# 12 Korzystając z funkcji range wypisz elementy malejąco od 100 - 20, co 5 wartości.
for i in range(100, 19, -5):
    print(i)

# 13 Połącz całą wiedzę wydobytą z zajęć (i zadań) i stwórz program
# wypisujący dane z listy, która zawiera # kilka słowników
# (dane wypisz w postaci jednego string'a odpowiednio go formatując).

imiona_damskie={
    1 : "Marta",
    2 : "Daria",
    3 : "Kasia"
}

imiona_męskie={
    1 : "Tomek",
    2 : "Dominik",
    3 : "Paweł"
}

lista_imion= [imiona_damskie, imiona_męskie]
listToStr = ' '.join(map(str, lista_imion)) #za pomoca list comprehension
print(listToStr)