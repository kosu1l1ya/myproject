from random import randint

message = input('Введите сообщение: ').split()
language = input('язык алфавита: ')  # русский или английский;


if language == 'английский':
    quantity_letters = 26
    last = 'z'
    first = 'a'

elif language == 'русский':
    quantity_letters = 32
    last = "я"
    first = 'а'


f = []

for i in range(len(message)):
    word = ''
    len_i = 0
    s1 = message[i]
    for c in s1:
        if c.isalpha():
            len_i += 1
    for c in s1:
        if c.isalpha():
            a = 0
            if c.isupper():
                a += 1
                c = c.lower()
            c = ord(c) + len_i
            if c > ord(last):
                c = c - quantity_letters
            c = chr(c)
            if a == 1:
                c = c.upper()
            word += c
        else:
            word += c
    f.append(word)

print(*f)
