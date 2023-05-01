from collections import Counter

def show(image):
    for line in image:
        print(line)

def visualize(array, bar_char = '₽'):
    stack = ''
    counter = Counter(array)
    count_most = sorted(Counter(array).most_common())
    count_most_mod = list(zip(*count_most))
    result = [[' ']*(len(count_most_mod[0]) + 1) for i in range(len(counter))]
    sum = list(count_most_mod[1])
    for index, char in enumerate(count_most_mod[0]):
        result[index][0] = f'{char}'
        result[index][1:sum[index]] = [bar_char*2] * count_most[index][1]
        result[index][sum[index]+1:sum[index]+2] = f'{sum[index]}'
    result_new = list(map(list, list(zip(*result))[::-1]))
    result_new.insert(-1, ['---'*(len(result_new[-1])-1)+'--'])
    for element in result_new:
        for char in element:
            stack +=  (char if len(char) != 1 else  char +' ') + ' '
        stack = stack[:-1]
        stack += '\n'
    stack = stack[:-1]
    return stack

print(visualize(( 1, 20, 2, 5, 20, 3, 5, 2, 10, 2, 20, 2, 20, 1, 2, 1, 1, 2, 10, 20, 3), bar_char='$'))
# => 5
# => ₽₽ 4  4
# => ₽₽ ₽₽ ₽₽    3
# => ₽₽ ₽₽ ₽₽    ₽₽
# => ₽₽ ₽₽ ₽₽ 1  ₽₽
# => ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
# => --------------
# => 1  2  3  10 20
