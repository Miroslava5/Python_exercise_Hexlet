def is_power_of_three(num):
    num_test = num 
    while num_test >= 3:
        if num_test % 3 != 0:
            return False
        else:
            num_test /= 3
    else:
        if num_test == 1:
            return True
    return False

    
print(is_power_of_three(28))  # True
print(is_power_of_three(2))  # False
print(is_power_of_three(9))  # True

