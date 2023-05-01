import random
import math

def fib(num):
    list_fib = []
    list_fib.extend([0, 1])
    i = 2
    while i <= num:
        sum = list_fib[(i - 2)] + list_fib[(i-1)]
        list_fib.append(sum)
        i += 1
    return list_fib[num]


print(fib(0))  # 2
print(fib(5))  # 5
print(fib(10))  # 55
