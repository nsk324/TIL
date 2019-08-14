numbers = list(map(int, input().split()))
i = 0
j = 0
for num in numbers:
    if num % 3 == 0:
        i += 1
    if num % 4 == 0:
        j += 1
print('Multiples of 3 : {}'.format(i))
print('Multiples of 5 : {}'.format(j))
