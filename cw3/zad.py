from file_manager import FileManager
from chuck_norris import Podlacz

#1
def zad1(a_list, b_list):
    return a_list[::2] + b_list[1::2]

listaA = [1,2,3,4,5,6,7,8,9,10]
listaB = [11,12,13,20]

print(zad1(listaA, listaB))

#2
def zad2(data_text):
    return {
        "length": len(data_text),
        "letters": list(data_text),
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    }

print(zad2("Jakiś teKst"))

#3
def zad3(text, letter):
    return text.translate({ord(i): None for i in letter})

print(zad3("Jakiś tekst", "ś"))

#4
def zad4(celsius, temperature_type):
    return {
        'Fahrenheit': 32 + 1.8 * celsius,
        'Rankine': 32 + 1.8 * celsius + 459.67 if 32 + 1.8 * celsius >= -459.67 else "Błędna wartość",
        'Kelvin': celsius + 273.15 if celsius >= -273.15 else "Błędna wartość"
    }[temperature_type]

print(zad4(-100, 'Kelvin'))

#5
class Calculator:

    def add(self, a, b):
        return a+b

    def difference(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b

#6
class ScienceCalculator(Calculator):
    def pow(self, a, b):
        return pow(a, b)

#7
def zad7(text):
    print(text[::-1])

zad7("koteł")

#9

fm = FileManager('file.txt')
print(fm.read_file())
fm.update_file("Nowy tekst")
print(fm.read_file())

#10
c = Podlacz()
print(c.random('Janet'))