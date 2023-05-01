# моё решение

def rotated_left(some_list):
    copy = some_list[1:] + some_list[:1]
    return copy


def rotated_right(some_list):
    copy = some_list[-1:] + some_list[:-1]
    return copy


print(rotated_left((1, True, 'foo')))  #  true, foo, 1 
print(rotated_left('ABCD'))    
list = ['A', 'B', 'C', 'D']
print(rotated_left(list))  # "BCDA"
print(rotated_right([1, 2, 3, 4]))  # [4, 1, 2, 3]


# BEGIN еще проще решение
def rotated_right(items):
    return items[-1:] + items[:-1]


def rotated_left(items):
    return items[1:] + items[:1]
# END