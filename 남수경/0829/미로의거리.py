import sys
sys.stdin = open("미로_input.txt")


def iswall(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return True
    if maze[y][x] == '1':
        return True
    return False


def canigo(x,y):
    global li
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    li = []
    for i in range(4):
        testx = x + dx[i]
        testy = y + dy[i]
        if iswall(testx,testy) == False:
            # x = testx
            # y = testy
            li.append((testx,testy))





def bfs(x,y):
    queue = []
    queue.append((x,y))
    visited[y][x]= 1
    while queue:

        tx,ty = queue.pop(0)

        canigo(tx,ty)

        for i in li:
            ux,uy = i
            if visited[uy][ux] == 0:
                queue.append((ux,uy))
                visited[uy][ux] = visited[ty][tx]+1









T = int(input())
for tc in range(T):
    N = int(input()) #한 변의 길이
    maze = [input()for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    x,y = 0,0
    li = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                x,y = j,i

    bfs(x,y)
    print(visited)


    for i in range(N):
        for j in range(N):
            if maze[i][j] == '3':
                if visited[i][j] >= 2:
                    print('#{} {}'.format(tc+1,visited[i][j] -2))
                else:
                    print('#{} {}'.format(tc+1, visited[i][j]))