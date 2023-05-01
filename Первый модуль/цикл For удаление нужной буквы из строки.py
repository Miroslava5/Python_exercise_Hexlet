def filter_string(text, str):
    result = text
    for char in result:
        if char.lower() == str.lower():
            result = result.replace(char, '')
    return result.strip()

text = 'If I look forward I win'
print(filter_string(text, 'i'))  # 'f  look forward  wn'
print(filter_string(text, 'O'))  # 'If I lk frward I win
