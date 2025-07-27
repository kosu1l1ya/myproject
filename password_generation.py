import random
digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
ambiguous_symbols = 'il1Lo0O'
chars = ''

quantity_passwords = int(input('''Введите:
  Количество паролей для генерации '''))
len_password = int(input('Длину одного пароля '))
digit = input('Включать ли цифры 0123456789? ')
upper_case = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')
lower_case = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')
punct = input('Включать ли символы !#$%&*+-=?@^_? ')
amb = input('Исключать ли неоднозначные символы il1Lo0O? ')

if digit == 'да':
    chars += digits
if upper_case == 'да':
    chars += uppercase_letters
if lower_case == 'да':
    chars += lowercase_letters
if punct == 'да':
    chars += punctuation
if amb == 'да':
    for c in ambiguous_symbols:
        chars = chars.replace(c, '')


def generate_password(chars, len_password):
    password = random.sample(chars, len_password)
    return ''.join(password)


for _ in range(quantity_passwords):
    print(generate_password(chars, len_password))
