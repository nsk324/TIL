def dfs(x,y):
    visited[y][x] = cnt
    box[y][x] = 0

    for k in range(4):
        testx = x + dx[k]
        testy = y + dy[k]
        if isblock(testx,testy) == False :
            dfs(testx,testy)


def isblock(x,y):
    if x < 0 or x >= D or y<0 or y>=D or box[y][x] == 0:
        return True
    return False

import sys
sys.stdin = open("두더지input.txt")
D = int(input())
box = [list(map(int,input().split())) for _ in range(D)]
cnt = 0
visited = [[0 for _ in range(D)] for _ in range(D)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in range(D):
    for j in range(D):
        if box[i][j] == 1:
            cnt += 1
            dfs(j,i)

answer = []
for i in range(1,cnt+1):
    sum = 0
    for j in range(len(visited)):
        sum += (i * visited[j].count(i)) / i
    answer.append(int(sum))
answer.sort()



print(cnt)
print(answer.pop())
print(answer.pop())
print(answer.pop())