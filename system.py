a = int(input('Введите'))
s = ''
while True:
    s += str(a % 16)
    a //= 16
    if a > 16:
        s += str(a)
        break
print(s)
