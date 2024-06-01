#Функція для обробки списку гостей, сортування та форматування у вигляді рядка
def meeting(s):
    guests = s.upper().split(';')
    guests = [guest.split(':')[::-1] for guest in guests]
    guests.sort()
    result = ''.join(f"({last}, {first})" for first, last in guests)
    return result

# Приклад використання
s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(s))  # "(CORWILL, ALFRED)(CORWILL, FIRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"