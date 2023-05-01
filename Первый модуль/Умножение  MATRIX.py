def show(image):
    for line in image:
        print(line)

def multiply(list_1, list_2):
    result = []
    if len(list_1[0]) != len(list_2):
        return False
    list_2 = list(zip(*list_2))
    for element_2 in list_2:
        itog = []
        for element_1 in list_1:
            mul = 0
            para = list(zip(element_2, element_1))
            for x,y in para:
                mul += x*y
            itog.append(mul)
        result.extend([itog])
        print(result)
    result = list(map(list, list(zip(*result))))
    return result

a = [[1, 2, 1], [0, 1, 0], [2, 3, 4]]
b = [[2, 5],[6, 7],[1, 8]]
show(multiply(a, b))

""""
C = [
  [2, 5],
  [6, 7],
  [1, 8],
]
D = [
  [1, 2, 1],
  [0, 1, 0],
]

show(multiply(C, D))  # [[2, 9, 2], [6, 19, 6], [1, 10, 1]]
"""
