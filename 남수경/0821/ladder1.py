def whereigo(x,y):
    
    if 0 <= y+dy[0] and y+dy[0] <=99 and 0 <= x+dx[0] and x+dx[0] <= 99:
        if ladder[y+dy[0]][x+dx[0]] == 1:
            return 0
    if 0 <= y + dy[1] and y + dy[1] <= 99 and 0 <= x + dx[1] and x + dx[1] <= 99:
        if ladder[y+dy[1]][x+dx[1]] == 1:
            return 1
    if ladder[y+dy[2]][x+dx[2]] == 1:
        return 2


import sys
sys.stdin = open("ladder1_input1.txt")

T = 10
for tc in range(T):
    r_tc = int(input())
    ladder = [list(map(int,input().split()))for _ in range(100)]
    x = ladder[99].index(2)
    y = 99

    dx = [1,-1,0] #우 좌 상
    dy = [0,0,-1]

    while y >= 0 :
        k = whereigo(x,y)
        ladder[y][x] = 5
        x = x+dx[k]
        y = y+dy[k]

    # print(ladder)
    print('#{} {}'.format(r_tc,x))

    # for i in range(99)
