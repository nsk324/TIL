import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(T):
    row, col = map(int, input().split())
    # row = int(input())
    # col = int(input()) #이차원일경우 가로세로 길이를 가르쳐준다
    #미리 빈 이차열배열을 만들어보쟈 5(col)개짜리가 3줄이다
    # data = [0 for _ in range(col)]

    #1.
    # data = [[0 for _ in range(col)] for _ in range(row)]
    #
    # for i in range(row):
    #     data[i] = list(map(int, input().split()))
    #
    # for i in range(row):
    #     for j in range(col):
    #         print(data[i][j], end=" ")
    #    print() # 한 row 한 후 줄바꿈

    #2
    data = [list(map(int,input().split())) for _ in range (row) ]
    print(data)