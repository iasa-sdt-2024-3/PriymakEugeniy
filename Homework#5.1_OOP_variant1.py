class DataStorage:
    def __init__(self, name):
        self.name = name

    def store_data(self, data):
        return 100

    def retrieve_data(self, key):
        return 100


class Local(DataStorage):
    def __init__(self, name):
        super().__init__(name)

    def store_data(self, data):
        return 100

    def retrieve_data(self, key):
        return 100


class Web(DataStorage):
    def __init__(self, name, url):
        super().__init__(name)
        self.url = url

    def store_data(self, data):
        return 100

    def retrieve_data(self, key):
        return 100


class Removable(DataStorage):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location

    def store_data(self, data):
        return 100

    def retrieve_data(self, key):
        return 100

local_storage = Local("Local storage")
web_storage = Web("Web storage", "http://test.com")
removable_storage = Removable("Removable storage", "USB Drive")

print(local_storage.name)
print(web_storage.name)
print(removable_storage.name)