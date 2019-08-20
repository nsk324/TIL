import sys
sys.stdin = open("구간합.txt",'r')

T = int(input())

for tc in range(T):
    [N,M] = list(map(int,input().split()))
    ais = list(map(int,input().split()))
    sums = []
    min = 124654648641313
    max = 0
    for i in range(N-M+1):
        ai = 0
        for j in range(M):
            ai += ais[i+j]
        sums += [ai]

    for sum in sums:
        if sum < min:
            min = sum

        if sum > max:
            max = sum

    print('#{} {}'.format(tc+1, max-min))

