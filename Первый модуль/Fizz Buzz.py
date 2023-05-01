import random
import math

def fizz_buzz(begin, end):
    result = ''
    if begin > end:
        return result
    x = begin
    while x <= end:
        if (x % 3 == 0 and x % 5 == 0):
            result += 'FizzBuzz '
        elif x % 3 == 0:
            result += 'Fizz '
        elif x % 5 == 0:
            result += 'Buzz '
        else:
            result += f'{x} '
        x += 1
    return result.strip()


print(fizz_buzz(1, 5))
# => 1 2 Fizz 4 Buzz
print(fizz_buzz(11, 20))
# => 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz

