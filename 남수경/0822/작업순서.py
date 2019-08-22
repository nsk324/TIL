import sys

def f_f(box):
    for j in range(1,V+1):
        sum = 0
        for i in range(1,V+1):
            sum += G[i][j]
        if sum ==0:
            return j


def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0: # 현재 v와 연결되어있으며 방문한 적이 없는 w에대해
            dfs(w)




sys.stdin = open("작업순서.input.txt")
T = 3
for tc in range(T):
    V,E = map(int,input().split()) #노드의 갯수, 입력의 갯수
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V + 1)]
    sen = list(map(int,input().split()))
    print(sen)
    for i in range(len(sen)//2):
        G[sen[i+i]][sen[i+i+1]] = 1

    print(f_f(G))