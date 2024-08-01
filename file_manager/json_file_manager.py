import json


class JsonFileManager:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file_get_keys(self):
        try:
            with open(self.file_name, 'r') as file:
                file_data = json.load(file)
            return file_data.keys()
        except Exception as error:
            print(error)
            return []

    def read_file_get_json(self):
        try:
            with open(self.file_name, 'r') as file:
                file_data = json.load(file)
            return file_data
        except Exception as error:
            print(error)
            return {}
