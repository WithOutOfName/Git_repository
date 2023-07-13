# задача 14
n = int(input('Введите число: n = '))
for i in range (n + 1):
    f = 2 ** i
    if f <= n:
        print(f' i = {i}, 2^{i}, = {f}')
    else:
        break
print('end of program')
