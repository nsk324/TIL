import sys

sys.stdin = open('전기버스.txt','r')

T = int(input())

for tc in range(T):
    K,N,M = map(int,input().split())
    oil = [0]+ list(map(int,input().split())) + [N]
    oil_between = []
    number = 0
    hi = 0
    k = K
    for i in range(1,len(oil)):
        oil_between += [oil[i]-oil[i-1]]
    oil_between += [0]

    for j in range(len(oil_between)-1):
        if oil_between[j] > K:
            print('#{} 0'.format(tc+1))
        else:
            if k < oil_between[j] + oil_between[j+1]:
                k = K
                number += 1
                hi += 1
            else:
                k -= oil_between[j]
                hi += 1

    if hi == len(oil_between)-1:
        print('#{} {}'.format(tc + 1, number))