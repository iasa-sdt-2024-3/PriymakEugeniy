#Функція, що знаходить перший неповторюваний символ у рядку
def first_non_repeating_letter(s):
    s_lower = s.lower()
    for i, char in enumerate(s_lower):
        if s_lower.count(char) == 1:
            return s[i]
    return ''

# Приклади використання
print(first_non_repeating_letter('stress'))  # 't'
print(first_non_repeating_letter('sTreSS'))  # 'T'
print(first_non_repeating_letter('aabbcc'))  # ''