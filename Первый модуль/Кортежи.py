import random

def sort_pair(para_number):
    (num1, num2) = para_number
    if num1 >= num2:
        return (num1, num2)
    else:
    return (num2, num1)

print(sort_pair((-5, 5)))