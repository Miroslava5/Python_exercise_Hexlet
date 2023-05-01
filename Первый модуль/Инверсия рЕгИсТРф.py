

def invert_case(text):
    result = ''
    i = 0
    while i < len(text):
        char_small = text[i].lower()
        char_big = text[i].upper()
        if text[i] == char_small:
            result += char_big
        else:
            result += char_small
        i += 1
    return result

print(invert_case('Hello, World!'))  # hELLO, wORLD!
print(invert_case('I love Python'))  # i LOVE pYTHON

            #Решение учителя
def invert_case(text):
    inverted_text = ''
    for chr in text:
        if chr.lower() == chr:
            inverted_text += chr.upper()

        else:
            inverted_text += chr.lower()

    return inverted_text

