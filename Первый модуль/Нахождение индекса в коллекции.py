# моё решение

def find_index(what_find, when_find):
    for (index, element) in enumerate(when_find):
        if element == what_find:
            return index
        else:
            continue
    return None
        



print(find_index('t', 'cat'))  # 2
print(find_index(5, [1, 2, 3, 4, 5, 6, 7]))  # 4
print(find_index(42, []) is None)  # True
print(find_index('!', 'abc') is None)  # True