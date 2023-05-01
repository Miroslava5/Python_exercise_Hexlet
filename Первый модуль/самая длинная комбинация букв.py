
def find_longest_length(string):
    result = []
    for (index, _) in enumerate(string):
        stack = ''
        i = index
        while i < len(string):
            if stack.find(string[i:i+1]) == -1:
                stack += string[i:i+1]
                i += 1
            else:     
                break         
        result.append(stack)
        max_len = len(max(result, key=len))
    return max_len if string != '' else 0

print(find_longest_length(''))
print(find_longest_length('qweqrty')) #6
print(find_longest_length('abcdeef'))  # 5
print(find_longest_length('jabjcdel'))  # 7