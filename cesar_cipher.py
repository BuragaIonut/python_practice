def cesar_cipher(string, n):
    new_string = []
    for i in string:
        if i != ' ':
            new_string.append(chr(ord(i) + n))
        else:
            new_string.append(' ')
    return ''.join(new_string)


print(cesar_cipher('abcd xyz', 4))