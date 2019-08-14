import sys
sys.stdin = open("2.txt",'r')

arr = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    arr[i] = list(map(int, input().split()))

for y in range(len(arr)):
    for x in range(y+1, len(arr[y])):
        #  이미 x에서 y 보다 크다 햇으니... if x < y :
            arr[x][y], arr[y][x] = arr[y][x], arr[x][y]

for y in range(len(arr)):
    for x in range(len(arr[x])):
        print(arr[y][x], end=" ")

    print()