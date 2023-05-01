
def triangle(num_str):
    if num_str == 0:
        return [1]
    elif num_str == 1:
        return [1,1]
    index = 2
    result = [1, 1]
    result_stack = []
    while index <= num_str:
        for (i, _) in enumerate(result):
            if i < len(result)-1:
                result_stack.append(result[i] + result[i+1])
            else:
                break
        result[1:-1] = result_stack[:]
        index +=1
        result_stack = []
    return result

    

print(triangle(5))  # [1 2 1]
print(triangle(4))  # [1, 4, 6, 4, 1]
print(triangle(15))  # 4

#0:      1
#1:     1 1
#2:    1 2 1
#3:   1 3 3 1
#4:  1 4 6 4 1

                   #РЕШЕНИЕ УЧИТЕЛЯ

# BEGIN
# Определяем функцию для вычисления факториала
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def triangle(row_number):
    numbers_count = row_number + 1
    line = []
    calculated = fact(row_number)
    for i in range(numbers_count):
        # Для вычисления числа заданной строки используем формулу
        # расчёта биноминальных коэффициентов С(n, k) = n! / (k! * (n - k)!)
        line.append(calculated / (fact(i) * fact(row_number - i)))
    return line


# Alternative solutions
#
#
# def triangle(row):
#     line = [1]
#     for i in range(row):
#         line.append(line[i] * ((row - i) / (i + 1)))
#     return line
#
#
# from operator import add
#
#
# def triangle(row_number):
#     row = [1]
#     for _ in range(row_number):
#         row = list(map(  # [x,y,z]
#             add,         # x y z 0
#             row + [0],   # + + + +
#             [0] + row,   # 0 x y z
#         ))
#     return row
# END