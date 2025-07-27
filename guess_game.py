from random import randint

r = randint(1, 100)

print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 100:
            return True
        else:
            return False
    else:
        return False


while True:
    a = input('Введите целое число от 1 до 100 :')
    if not is_valid(a):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    a = int(a)
    if a == r:
        print('Вы угадали, поздравляем!')
        break
    elif a < r:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Ваше число больше загаданного, попробуйте еще разок')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
