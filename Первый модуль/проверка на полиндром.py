def is_palindrome(text):
    result = ''
    i = 0
    for char in text:
        result = char + result
        i += 1
    if result.lower() == text.lower():
        return True
    return False

print(is_palindrome(''))  # True пустая строка тоже считается палиндромом
print(is_palindrome('Radar')) # True
print(is_palindrome('a')) # True
print(is_palindrome('abs')) # False
print(is_palindrome('ишак ищет у тещи каши')) # True