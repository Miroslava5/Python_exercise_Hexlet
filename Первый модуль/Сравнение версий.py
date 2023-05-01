

def compare_version(vers1, vers2):
    v1 = vers1.split('.')
    v2 = vers2.split('.')
    
    if int(v1[0]) > int(v2[0]):
        return 1
    elif int(v1[0]) < int(v2[0]):
        return -1
    else:
        if int(v1[1]) > int(v2[1]):
            return 1
        elif int(v1[1]) < int(v2[1]):
            return -1
        else:
            return 0


#print(compare_version("0.1", "0.2"))  # -1
print(compare_version("0.2", "0.12"))  # 1
#print(compare_version("4.2", "4.2"))  # 0
