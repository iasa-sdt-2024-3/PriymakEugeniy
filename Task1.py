#Функція для фільтрації списку, що видаляє текст і залишає лише цілі числа
def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]

# Приклади використання
print(filter_list([1, 2, 'a', 'b']))  # [1, 2]
print(filter_list([1, 'a', 'b', 0, 15]))  # [1, 0, 15]
print(filter_list([1, 2, 'aasf', '1', '123', 123]))  # [1, 2, 123]