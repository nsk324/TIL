import sys

sys.stdin = open("input2.txt")
T = int(input())

for tc in range(T):
    box = []
    N, M = map(int, input().split()) # 타일 한변, 파리채 한변
    for n in range(N):
        box.append(list(map(int,input().split())))
    # print(box)

    max = 0

    for n in range(N-M+1):
        for nn in range(N-M+1):
            # for i in range(M):
            sum1 = 0
            for mm in range(M):
                sum1 += sum(box[nn+mm][n:n+M])
            if max < sum1:
                max = sum1

    print('#{} {}'.format(tc+1,max))