def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))

def is_happy_number(number):
    index = number
    count = 0
    while index != 1 and count <= 10:
        count += 1
        index = sum_of_square_digits(index)
    return True if index == 1 else False

print(is_happy_number(0))
print(is_happy_number(2))

#Счастливые числа
#Назовем счастливыми те числа, которые в результате
# ряда преобразований вида сумма квадратов 
# цифр превратятся в единицу. Например:
# 7   -> 7^2 = 49
# 49  -> 4^2 + 9^2 = 97
# 97  -> 9^2 + 7^2 = 130
# 130 -> 1^2 + 3^2 + 0^2 = 10
# 10  -> 1^2 + 0^2 = 1
# Вывод: исходное число 7 — счастливое.