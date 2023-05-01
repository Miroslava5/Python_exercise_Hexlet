import random
import math

def binary_sum(a, b):
    a = int(a, 2)
    b = int(b, 2)
    sum = format(a + b, 'b')
    return f'{sum}'

print(binary_sum('10', '1'))      # 11
print(binary_sum('1101', '101'))  # 10010
