import sys
sys.stdin = open("회문2_input.txt")



def hi(box):
    for i in range(100,0,-1):# 회문의 길이
        for row in range(100): #
            for col in range(100-i+1): # 회문대상이되는 세로?
                flag1 = 1
                flag2 = 1
                for k in range(i//2):
                    if box[row][col+k] != box[row][col + i - k - 1]:
                        flag1 = 0

                    if box[col+k][row] != box[col + i - k - 1][row]:
                        flag2 = 0

                if flag1 or flag2:
                    return i

T = 10



for tc in range(T):
    testcase = input()
    box = [input() for _ in range(100)]
    # print(box)
    print('#{} {}'.format(testcase,hi(box)))

    # for i in range(100,0,-1):# 회문의 길이
    #     for row in range(100)
    #         for col in range(100-i+1): # 회문대상이되는 세로?
    #             for j in range(i):
    #                 flag = 1
    #                 for k in range(i//2):
    #                     if box[i][j + k] != box[i][j + M - k - 1]:
    #                         flag = 0
    #
    #                     if box[j + k][i] != box[j + M - 1 - k][i]:
    #                         flag = 0
    #
    #                 if flag :


