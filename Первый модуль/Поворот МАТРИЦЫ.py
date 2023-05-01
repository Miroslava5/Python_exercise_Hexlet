
def transposed(matrix):
    x = len(matrix[0])
    y = len(matrix)
    result = [[''] * y for i in range(x)]
    for (index, string) in enumerate(matrix):
        for (i, num) in enumerate(string):
            result[i][index] = num
    return result

print(transposed([[1]])) # [[1]]
print(transposed([[1, 2], [3, 4]])) # [[1, 3], [2, 4]]
print(transposed([[1, 2], [3, 4], [5, 6]]))
# [[1, 3, 5], [2, 4, 6]]
print(transposed(transposed([[1, 2]])) == [[1, 2]]) #True

#РЕШЕНИЕ УЧИТЕЛЯ
# BEGIN
def transposed(matrix):
    result = []
    for column in zip(*matrix):
        result.append(list(column))
    return result
# END
