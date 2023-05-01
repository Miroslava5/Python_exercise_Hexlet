def normalize_url(text):
    if text[0:8] == 'https://':
        return text
    elif text[0:7] == 'http://':
        return text.replace('http://', 'https://')
    else:
        return 'https://' + text
    
print(normalize_url('https://ya.ru'))  # https://ya.ru
print(normalize_url('google.com'))  # https://google.com
print(normalize_url('http://ai.fi'))  # https://ai.fi
