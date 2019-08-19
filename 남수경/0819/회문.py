import sys
import copy

sys.stdin = open("input.txt")

T = 10
for tc in range(T):
    N = int(input()) #찾아야하는 회문의 길이
    box1 = []#[[0 for _ in range(8)] for _  in range(8)]
    box2 = []
    # print(N)
    for row in range(8):
        box1.append(list(input()))
        print(box1)

    box2 = copy.deepcopy(box1)
    for i in range(8):
        for j in range(8):
            if i > j:
                box2[i][j], box2[j][i] = box2[j][i], box2[i][j]

    # print(box2)

    cnt = 0

    for row in range(8):
        for col in range(0,8-N+1):
            # print(box1[row][col:col+N])
            if box1[row][col:col+N] == box1[row][col:col + N][::-1]:
                cnt += 1
            # print(box1[row][col:col + N][::-1])

    for row in range(8):
        for col in range(0,8-N+1):
            # print(box1[row][col:col+N])
            if box2[row][col:col+N] == box2[row][col:col + N][::-1]:
                cnt += 1

    print(cnt)