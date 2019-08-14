import sys
sys.stdin = open("숫자카드.txt","r")

T = int(input())

for tc in range(T):
    N = int(input())
    ais = int(input())
    ai = []
    for n in range(N):
        ai += [ais % 10]
        ais = ais // 10

    aidic = {}

    for i in ai:
        if i not in aidic:
            aidic[i] = 1
        else:
            aidic[i] += 1
    maxai = 0
    for j in aidic:

        if aidic[j] > maxai:
            maxai = aidic[j]
            maxaikey = j
        elif aidic[j] == maxai:
            if j > maxaikey:
                maxaikey = j

    print('#{} {} {}'.format(tc+1,maxaikey,maxai))