                 #решение учителя
def encrypt(word):
    result = ''
    i = 0
    while i < len(word):
        result += word[i:i + 2][::-1]
        i += 2
    return result

                #мое решение

def encrypt(text):
    if len(text) <= 1:
        return text    
    i = 0
    result = ''
    while i < len(text) - 2:
        result += text[i+1] + text[i]
        i += 2
    if len(text) % 2 == 0:
        result += text[-1] + text[-2]
    else:
        result += text[-1]
    return result
    

print(encrypt("move")) # 'omev'
print(encrypt("attack")) # 'taatkc'
print(encrypt("go!")) # 'og!'