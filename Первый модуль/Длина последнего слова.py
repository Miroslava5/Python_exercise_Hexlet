
def length_of_last_word(text):
    result = text
    result = result.replace('\n', ' ')
    result = result.replace('\t', ' ')
    result = result.strip()
    i = 0
    while i < len(result):
        if result[i] == ' ':
            result = result[i+1:]
            i = 0
        else:
            i += 1
    return len(result)

    # Реализуйте функцию length_of_last_word(),
    # которая возвращает длину последнего слова
    # переданной на вход строки.
    #   Словом считается любая последовательность
    #   не содержащая пробелы, символы перевода строки
    #   \n и табуляции \t.

print(length_of_last_word('')) # 0
print(length_of_last_word('man in Black')) # 5
print(length_of_last_word('hello, world!     ')) # 6
print(length_of_last_word('hello\t\nworld')) # 5   