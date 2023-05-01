

def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index


# BEGIN
def find_second_index(value, items):
    iterator = iter(items)
    first = find_index(value, iterator)
    if first is None:
        return first
    second = find_index(value, iterator)
    if second is not None:
        return first + second + 1

print(find_second_index('n', 'banana'))  # 4
print(find_second_index('a', 'cat') is None)  # True