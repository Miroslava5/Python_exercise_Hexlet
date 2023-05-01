def show(image):
    for line in image:
        print(line)

def snail_path(matrix):
    result = []
    while len(matrix):
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1] 
    return result
    



 
print(snail_path([[1, 2], [3, 4]]))
# [1, 2, 4, 3]

print(snail_path([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(snail_path([['b', 'c', 'a'], ['3', True, 11], [None, 'foo', 0]]))
# ['b', 'c', 'a', 11, 0, 'foo', None, '3', True]
