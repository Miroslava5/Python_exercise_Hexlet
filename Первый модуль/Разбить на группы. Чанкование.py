
def chunked(num, list):
    ostatok = len(list) % num
    result = []
    i = 0
    while i < len(list) - ostatok:
        result += [list[i:i+num]]
        i += num
    if ostatok != 0:
        result += [list[-ostatok:]]
    return result


print(chunked(2, ['a', 'b', 'c', 'd']))  # [['a', 'b'], ['c', 'd']]
print(chunked(3, ['a', 'b', 'c', 'd']))  # [['a', 'b', 'c'], ['d']]
print(chunked(3, 'foobar'))  # ['foo', 'bar']
print(chunked(10, (42,)))  # [(42,)]