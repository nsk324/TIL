import sys
sys.stdin = open('색칠하기.txt','r')

T = int(input())
for tc in range(T):
    bg = [[0 for _ in range(10)] for _ in range(10) ]
    number = int(input())
    cnt = 0

    for num in range(number):
        hi = list(map(int,input().split())) # 그 한줄한줄
        for col in range(hi[0],hi[2]+1):
            for row in range(hi[1],hi[3]+1):
                if hi[-1] == 1:
                    bg[row][col] += 1
                else:
                    bg[row][col] += 2

    for col in range(10):
        for row in range(10):
            if bg[col][row] == 3:
                cnt += 1

    print('#{} {}'.format(tc+1,cnt))
