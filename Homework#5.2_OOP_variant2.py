from abc import ABC, abstractmethod

class DataType(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def validate(self, data):
        pass

    @abstractmethod
    def show(self, data):
        pass

class NumericType(DataType):
    def __init__(self, name):
        super().__init__(name)

    def validate(self, data):
        # перевірка на числовий тип
        return isinstance(data, (int, float))

    def show(self, data):
        # Повертає числове значення як строку
        return str(data)

class IntegerType(NumericType):
    def __init__(self):
        super().__init__("Integer")

    def validate(self, data):
        # Перевірка, чи є дані цілим числом
        return isinstance(data, int)

    def show(self, data):
        return str(data)

class FloatType(NumericType):
    def __init__(self):
        super().__init__("Float")

    def validate(self, data):
        # Перевірка, чи є дані float
        return isinstance(data, float)

    def show(self, data):
        return str(data)

class TextType(DataType):
    def __init__(self, name):
        super().__init__(name)

    def validate(self, data):
        # Тут буде перевірка на строковий тип
        return isinstance(data, str)

    def show(self, data):
        # Повертає текстові дані
        return data

class DateTimeType(DataType):
    def __init__(self, name):
        super().__init__(name)

    def validate(self, data):
        # Тут буде перевірка на тип дати і часу
        # Для простоти перевіряємо чи це строка (в реальному випадку перевірка була б складнішою)
        return isinstance(data, str)

    def show(self, data):
        # Повертає дату і час у вигляді строки
        return data

# Приклади використання
numeric_type = NumericType("Numeric")
integer_type = IntegerType()
float_type = FloatType()
text_type = TextType("Text")
datetime_type = DateTimeType("DateTime")

print(numeric_type.name)
print(integer_type.name)
print(float_type.name)
print(text_type.name)
print(datetime_type.name)