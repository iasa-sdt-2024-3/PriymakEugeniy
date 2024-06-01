from abc import ABC, abstractmethod

class FileSystemItem(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_info(self):
        pass

class File(FileSystemItem):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    def get_info(self):
        return f"File: {self._name}, Size: {self._size} bytes"

    @property
    def size(self):
        return self._size

class Folder(FileSystemItem):
    def __init__(self, name):
        super().__init__(name)
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def get_info(self):
        return f"Folder: {self._name}, Contains: {[child.name for child in self._children]}"

    @property
    def children(self):
        return self._children

class Shortcut(FileSystemItem):
    def __init__(self, name, target):
        super().__init__(name)
        self._target = target

    def get_info(self):
        return f"Shortcut: {self._name}, Target: {self._target.name}"

    @property
    def target(self):
        return self._target

# Приклади використання
file1 = File("document.txt", 1024)
file2 = File("image.jpg", 2048)
folder = Folder("Documents")
folder.add_child(file1)
folder.add_child(file2)

shortcut = Shortcut("document shortcut", file1)

# Виведення інформації про об'єкти
print(folder.get_info())
print(file1.get_info())
print(shortcut.get_info())