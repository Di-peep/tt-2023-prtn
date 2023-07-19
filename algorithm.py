def get_unique_char(string: str) -> str:
    if type(string) is not str:
        raise TypeError

    if string.count(' ') > 0:
        first_uniq_chars = ''.join([get_unique_char(word) for word in string.split()])
        return get_unique_char(first_uniq_chars)

    for char in string:
        if string.count(char) == 1:
            return char
    
    return ''
