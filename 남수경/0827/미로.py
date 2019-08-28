import sys
sys.stdin = open('미로_input.txt')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def iswall(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return True
    if miro[y][x] == '1':
        return True
    # print(False)
    return False

def canigo(x,y):
    global flag

    for i in range(4):
        testx = x + dx[i]
        testy = y + dy[i]
        if iswall(testx,testy):
             continue
        else:
            if miro[testy][testx] != '3':
                miro[y][x]='1'
                canigo(testx,testy)
            else:
                flag = 1
                return



T = int(input())
# print(T)

for tc in range(T):
    flag = 0
    N = int(input()) # 변의 길이
    miro = [[i for i in input()] for _  in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[j][i] == '2':
                x,y = i,j #처음 좌표

    canigo(x,y)
    print('#{} {}'.format(tc+1,flag))