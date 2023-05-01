

def diff(num_1, num_2):
    if abs(num_1) >=360:
        num_1 = num_1 % 360
    if abs(num_2) >=360:
        num_2 = num_2 % 360
    value = max(num_1, num_2) - min(num_1, num_2)
    if abs(value) <=180:
        return abs(value)
    return 360 - abs(value)
    
    
print(diff(-100, 200))
# 45
#print(diff(0, 180))
# 180
#print(diff(0, 190))  # не 190, а 170, потому что 170 меньше
# 170
#print(diff(120, 280))
# 160