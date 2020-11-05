

# 8 Stwórz nowy moduł w projekcie o nazwie file_manager. Stwórz klasę FileManager z parametrem w konstruktorze file_name.
# Klasa będzie zawierać dwie metody: read_file oraz update_file. Funkcja update_file powinna zawierac parametr text_data,
# które w efekcie ma być dopisane na końcu pliku. Funkcja read_file powinna zwrócić zawartość pliku.

class FileManager():
    def __init__(self, file_name):
        self.file_name=file_name

    def read_file(self):
        f = open(self.file_name, "r")
        if f.mode == 'r':
            contents = f.read()
            print(contents)

    def update_file(self, text_data):
        self.text_data = text_data
        f = open(self.file_name, "a") # a jesli chcemy dopisac coś do pliku
        f.write(text_data)
        f.close()





