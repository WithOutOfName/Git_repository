# Задача 12
s = int(input('x + y = '))
p = int(input('x * y = '))
x = 1
while x < s:
    y = s - x
    if x * y == p and x <= 1000 and y <= 1000:
        print(f' x = {x}, y = {y}')
        exit()
    x += 1
print('end of program')
