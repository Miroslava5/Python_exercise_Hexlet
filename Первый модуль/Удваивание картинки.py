
def enlarge(image):
    result = []
    for element in image:
        element_result = ''
        i = 0
        while i < len(element):
            element_result += f'{element[i]*2}'
            i += 1
        result.append(element_result)
        result.append(element_result)
    return result

        

    

def show(image):
    for line in image:
        print(line)

#dot = ['@']
#show(enlarge(dot))
# => @@
# => @@
frame = [
    '****',
    '*  *',
    '*  *',
    '****'
]
show(frame)
# => ****
# => *  *
# => *  *
# => ****
show(enlarge(frame))
# => ********
# => ********
# => **    **
# => **    **
# => **    **
# => **    **
# => ********
# => ********