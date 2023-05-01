

def hamming_weight(number):
    i = 0
    bin_number = format(number, 'b')
    for item in bin_number:
        if item == '1': 
            i += 1  
    return i
    

print(hamming_weight(0))  # 0
print(hamming_weight(4))  # 1
print(hamming_weight(101))  # 4
