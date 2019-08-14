import sys
sys.stdin = open("input.txt", 'r')

T = 10
for tc in range(T):
    test = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max = 0

    for col in range(100):
        sum = 0
        for row in range(100):
            sum += arr[col][row]
        if sum > max:
            max = sum


    for row in range(100):
        sum = 0
        for col in range(100):
            sum += arr[col][row]
        if sum > max:
            max = sum

    sum = 0
    for col in range(100):
        sum += arr[col][col]
    if sum > max:
        max = sum


    sum = 0
    for row in range(99,-1,-1):
        sum += arr[row][99-row]
    if sum > max:
        max = sum

    print(max)