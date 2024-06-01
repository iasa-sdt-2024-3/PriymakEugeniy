#Функція для обчислення цифрового кореня числа
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Приклади використання
print(digital_root(16))  # 7
print(digital_root(942))  # 6
print(digital_root(132189))  # 6
print(digital_root(493193))  # 2