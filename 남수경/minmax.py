import sys
sys.stdin = open('minmax.txt','r')

T = int(input())

for i in range(T):
    tc = int(input())
    numbers = list(map(int,input().split()))
    min = 12465451321465465486465131
    max = 0
    for j in range(tc):
        if numbers[j] < min:
            min = numbers[j]
        if numbers[j] > max:
            max = numbers[j]

    print('#{} {}'.format(i+1, max-min))