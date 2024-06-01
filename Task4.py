#Функція для підрахунку пар чисел в масиві, сума яких дорівнює заданому числу
def count_pairs(arr, target):
    count = 0
    seen = {}
    for num in arr:
        complement = target - num
        if complement in seen:
            count += seen[complement]
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    return count

# Приклад використання
arr = [1, 3, 6, 2, 2, 0, 4, 5]
target = 5
print(count_pairs(arr, target)) 