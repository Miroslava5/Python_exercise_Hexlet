import random
import math

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        i = 2
        num0 = 0
        num1 = 1
        while i <= num:
            num2 = num0 + num1
            num0 = num1
            num1 = num2  
            i += 1
    return num2


print(fib(1))  # 2
print(fib(5))  # 5
print(fib(10))  # 55
