import sys
sys.stdin = open("회문_input.txt")

T = int(input())

for tc in range(T):
    N, M = map(int,input().split()) # 표 한 변의 길이, 회문의 길이
    box = [input() for _ in range(N)]
    # K = M // 2
    word = []
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            flag2 = 1
            dic = ''

            for k in range(M//2):
                if box[i][j+k] != box[i][j+M-k-1]:
                    flag = 0

                if box[j + k][i] != box[j + M - 1 -k][i]:
                    flag2 = 0


            if flag:
                word.append(box[i][j:j + M])

            if flag2:
                for l in range(M):
                    word.append(box[j+l][i])



    print('#{} {}'.format(tc+1,''.join(word)))


            # if flag:
            #     for
