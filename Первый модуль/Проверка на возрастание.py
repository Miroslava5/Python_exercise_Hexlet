
def is_continuous_sequence(numbers):
    if len(numbers) <=1:
        return False
    i = 1
    while i < len(numbers):
        if (numbers[i] - numbers[i-1]) == 1:
            i += 1
        else:
            return False
    return True 





print(is_continuous_sequence([10, 11, 12, 13]))  # True
print(is_continuous_sequence([-5, -4, -3]))  # True
print(is_continuous_sequence([10, 11, 12, 14, 15]))  # False
print(is_continuous_sequence([1, 2, 2, 3]))  # False
print(is_continuous_sequence([7]))  # False
print(is_continuous_sequence([]))  # False