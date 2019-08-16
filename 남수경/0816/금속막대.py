import sys
sys.stdin = open("금속막대.txt")

T = int(input())
for tc in range(T):
    N = int(input()) # 나사의 갯수
    bolts = []
    bolt = list(map(int,input().split()))

    # print(bolt)
    for n in range(N):
        bolts.append(bolt[n+n:n+n+2])

    # num_num = {}
    for num in range(len(bolts)):
        if bolt.count(bolts[num][0]) == 1:
            first_bolt = bolts[num]
        if bolt.count(bolts[num][1]) == 1:
            last_bolt = bolts[num]

    # print(first_bolt, last_bolt)
    result = []
    result.append(first_bolt)
    bolts.pop(bolts.index(last_bolt))

    while first_bolt[1] != last_bolt[0]:
        for i in bolts:
            if first_bolt[1] == i[0]:
                result.append(i)
                first_bolt = i

    result.append(last_bolt)


    # print(result)
    print('#{}'.format(tc + 1),end=' ')
    for i in result:
        for j in i:
            print(j,end=' ')
    print()