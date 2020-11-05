class FileManager:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        file = open(self.file_name, 'r', encoding='utf-8')
        output = file.read()
        file.close()
    
        return output
    
    def update_file(self, text_data):
        file = open(self.file_name, 'a', encoding='utf-8')
        file.write("\n" + text_data)
        file.close()
    