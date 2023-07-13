# задача №10.
list_c = []
n = int(input('Введите сколько всего монет в штуках '))
for i in range(n):
    print('Орёл введи 1. Решка введи 0')
    coin = int(input(f' {i+1} монета: '))
    while coin != 1 and coin != 0:
        print('Вводи только 1 или 0!')
        coin = int(input(f' {i+1} монета: '))
    list_c.append(coin)
print(list_c)
eagle_count = 0
tails_count = 0
for i in range(n):
    if list_c[i] == 1:
        eagle_count += 1
    else:
        tails_count += 1
print(f'Всего {eagle_count} орлов и {tails_count} решек ')
if eagle_count < tails_count:
    s = eagle_count
else:
    s = tails_count
print(s)
