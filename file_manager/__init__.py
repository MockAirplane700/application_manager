from file_manager.json_file_manager import JsonFileManager


class FileManager:

    def __init__(self, json_file_name):
        self.json_file = json_file_name
        self.json_manager = JsonFileManager(self.json_file)

    def read_file_get_keys(self):
        return self.json_manager.read_file_get_keys()

    def read_file_get_json(self):
        return self.json_manager.read_file_get_json()


