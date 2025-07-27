message = input('Введите сообщение: ')
language = input('язык алфавита: ')  # русский или английский;
f = []

if language == 'английский':
    quantity_letters = 26
    last = 'z'
    first = 'a'
elif language == 'русский':
    quantity_letters = 32
    last = "я"
    first = 'а'

for i in range(1, 26):
    s = str(i) + ' '
    for c in message:
        if c.isalpha():
            a = 0
            if c.isupper():
                a += 1
                c = c.lower()
            c = ord(c) - i
            if c < ord(first):
                c = c + quantity_letters
            c = chr(c)
            if a == 1:
                c = c.upper()
            s += c
        else:
            s += c
    f.append(s)
print(*f, sep='\n')
