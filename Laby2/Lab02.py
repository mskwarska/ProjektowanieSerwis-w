
from file_manager import FileManager

# 1 Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list.
# Następnie zwróć listę,   która będzie posiadać parzyste indeksy z listy a_list
# oraz nieparzyste z b_list.

def changeLists(a_list, b_list):
    helper = []
    for i, v in enumerate(a_list):
        if i % 2 == 0:
            helper.append(a_list[i])
    for i, v in enumerate(b_list):
        if i % 2 == 1:
            helper.append(b_list[i])
    return helper
print(changeLists([1,2,3,4,5,6,7,8,9], [0,2,4,6,1,3,9,10,13,15]))


# 2 Stwórz funkcję, która przyjmuje parametr data_text, a następnie zwróci następujące informacje o parametrze w formie słownika (dict):
# length: długość podanego tekstu,
# letters: lista znaków w wyrazie np. ['D', 'o', 'g'],
# big_letters: zamieniony parametr w kapitaliki np. DOG
# small_letters: zamieniony parametr w małe litery np. dog
def split(word):
    return [char for char in word]
def textInfo(data_text):
    return {
        "length" : len(data_text),
        "letters" : split(data_text),
        "big_letters" : data_text.upper(),
        "small_letters" : data_text.lower(),
        }

print(textInfo("Pies"))


# 3 Stwórz funkcję, która przyjmie jako parametry text oraz letter, a następnie zwróci wynik usunięcia
# wszytkich wystąpień wartości w letter z tekstu text.
def returnLetter(text, letter):
    text=text.replace(letter, '')
    return text
print(returnLetter("Kotekplotek", 'o'))


# 4 Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza na Fahrenheit, Rankine, Kelvin.
# Typ konwersji powinien być przekazany w parametrze temperature_type i uwzględniać błędne wartości.
def tempConversion(tempersture_type, temperature):
    if tempersture_type =="Fahrenheit":
        return ((temperature*9)/5) +32
    elif tempersture_type =="Rankine":
        return (temperature+273.15)*1.8
    elif tempersture_type == "Kelvin":
        return temperature+273
    else:
        return "Wrong temperature type"

print(tempConversion("Fahrenheit", 5))
print(tempConversion("Kelvin", 5))
print(tempConversion("Rankine", 100))
print(tempConversion("kelwwinki", 100))


# 5 Stwórz klasę Calculator, która będzie posiadać funkcje add, difference, multiply, divide.
class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+ self.b
    def difference(self):
        return  self.a- self.b
    def multiply(self):
        return  self.a* self.b
    def divide(self):
        return self.a/ self.b

przyklad= Calculator(5,2)
print(przyklad.divide())

# 6 Stwórz klasę ScienceCalculator, która dziedziczy po klasie Calculator i dodaj dodatkowe funkcje np. potęgowanie.
class ScienceCalculator(Calculator):
    def power(self):
        return  pow(self.a, self.b)
scienceCalculatorExample=ScienceCalculator(3,3)
print(scienceCalculatorExample.power())


# 7 Stwórz funkcję, która wypisuje podany tekst od tyłu np. koteł -> łetok.
def reverseText(text):
    print(text[::-1])

reverseText("koteł")


# 9 Zaimportuj klasę FileManager w innym pliku, a następnie zademonstruj działanie klasy.
example= FileManager('plik.txt')
print(example.read_file())
example.update_file(" Dodany tekst")
print(example.read_file())


#10 W folderze projektu stwórz nowy virtualenv, a następnie zainstaluj moduł: https://github.com/yougov/chucknorris.
# Stwórz nowy moduł chuck_norris w swoim projekcie i stwórz funkcję która podłączy się pod ściągnięty moduł.


