message = input('''Введите:
  сообщение: ''')
direction = input('направление: ')    # шифрование или дешифрование;
language = input('язык алфавита: ')  # русский или английский;
shift_step = int(input('шаг сдвига (со сдвигом вправо): '))
s = ''

if language == 'английский':
    quantity_letters = 26
    last = 'z'
    first = 'a'
elif language == 'русский':
    quantity_letters = 32
    last = "я"
    first = 'а'

# Нормализация шага сдвига
shift_step = shift_step % quantity_letters

if direction == 'шифрование':
    for c in message:
        if c.isalpha():
            a = 0
            if c.isupper():
                a += 1
                c = c.lower()
            c = ord(c) + shift_step
            if c > ord(last):
                c = c - quantity_letters
            c = chr(c)
            if a == 1:
                c = c.upper()
            s += c
        else:
            s += c

elif direction == 'дешифрование':
    for c in message:
        if c.isalpha():
            a = 0
            if c.isupper():
                a += 1
                c = c.lower()
            c = ord(c) - shift_step
            if c < ord(first):
                c = c + quantity_letters
            # Исправлена опечатка (кириллическая 'с' была заменена на латинскую)
            c = chr(c)
            if a == 1:
                c = c.upper()
            s += c
        else:
            s += c

print(s)
