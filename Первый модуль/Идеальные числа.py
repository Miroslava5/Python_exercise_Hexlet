def is_perfect(number):
    if number == 0:
        return False
    count = 0
    div = number - 1
    while div >= 1:
        if number % div == 0:
            count += div
        div -= 1
    return count == number

print(is_perfect(0))  # True
print(is_perfect(8128))  # False

        #Решение учителя
def is_perfect(number):
    if number < 6:
        return False

    limit = number // 2 + 1
    sum = 0
    for divisor in range(1, limit):
        if number % divisor == 0:
            sum += divisor

    return sum == number