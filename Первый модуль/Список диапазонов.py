
def summary_ranges(numbers):
    result = []
    stack = []
    for (i, char) in  enumerate(numbers):     
        if (len(numbers[i+1:]) > 0) and (numbers[i+1] - numbers[i] == 1):
            stack.append(char)
        else:
            stack.append(char)
            #print(stack)
            if len(stack) > 1:
                result.append(f'{stack[0]}->{stack[-1]}')
            stack = []
    return result


print(summary_ranges([]))# []
print(summary_ranges([1]))# []
print(summary_ranges([1, 2, 3])) # ['1->3']
print(summary_ranges([0, 1, 2, 4, 5, 7])) # ['0->2', '4->5']
print(summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5]))
# ['110->112', '-5->-4']