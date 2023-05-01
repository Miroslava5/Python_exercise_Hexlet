
def sum_of_intervals(intervals):
    result = ['_'] * max(max(intervals))
    for [x, y] in intervals:
        result[x:y] = '1' * (y-x)
    return result.count('1')
 

         



print(sum_of_intervals([[1, 1], ])) # 0
print(sum_of_intervals([[1, 2], [50, 100], [60, 70], ])) # 51
print(sum_of_intervals([[1, 2], [5, 10], ])) # 6