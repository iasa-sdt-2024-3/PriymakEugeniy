#Функція, що знаходить наступне більше число, утворене з цифр даного числа
def next_bigger(n):
    digits = list(str(n))
    for i in range(len(digits)-2, -1, -1):
        if digits[i] < digits[i+1]:
            for j in range(len(digits)-1, i, -1):
                if digits[j] > digits[i]:
                    digits[i], digits[j] = digits[j], digits[i]
                    digits = digits[:i+1] + sorted(digits[i+1:])
                    return int(''.join(digits))
    return -1

# Приклади використання
print(next_bigger(12))  # 21
print(next_bigger(513))  # 531
print(next_bigger(2017))  # 2071
print(next_bigger(9))  # -1
print(next_bigger(111))  # -1
print(next_bigger(531))  # -1