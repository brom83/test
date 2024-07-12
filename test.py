from random import randint

a = [randint(1, 50) for i in range(10)]
a.sort()
print(a)

value = 25

left = 0
right = len(a) - 1
center = (left + right) // 2

while a[center] != value:
    if value > a[center]:
        left = center + 1
    else:
        right = center - 1
    center = (left + right) // 2
    if left >= right:
        break

if value == a[center]:
    print('ID =', center)
else:
    print('No value')
