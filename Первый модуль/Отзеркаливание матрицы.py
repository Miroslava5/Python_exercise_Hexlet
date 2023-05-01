
def mirror_matrix(l):
    if l == [] or l == [[]] or len(l[0]) <= 1:
        return None
    for char in l:
        i = 0
        while i < len(l[0]) // 2:
            char[-1-i] = char[i]
            i += 1
    return l

l = [
    [11, 12, 13, 14, 15, 16],
    [21, 22, 23, 24, 25, 26],
    [31, 32, 33, 34, 35, 36],
    [41, 42, 43, 44, 45, 46],
    [51, 52, 53, 54, 55, 56],
    [61, 62, 63, 64, 65, 66],
]

print(mirror_matrix([1[]])) 
#print(mirror_matrix(l))