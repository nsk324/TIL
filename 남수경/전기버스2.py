import sys

sys.stdin = open('전기버스.txt','r')

T = int(input())

for i in range(T):
    K,N,M = map(int,input().split())
    loca = list(map(int,input().split())) + [N]
    number = 0
    k = K

    for j in range(N+1):
        if j < N and k == 0 and j not in loca[:-1]:
            print('#{} 0'.format(i+1))
            break

        else:
            if j in loca[:-1]:
                if k < loca[loca.index(j)+1]-j:
                    k = K-1
                    number += 1

                else:
                    k -=1
            else:
                k-=1
    if j ==N:
        print('#{} {}'.format(i+1,number))