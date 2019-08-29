import sys
sys.stdin = open("노드_input.txt")
T=int(input())


def bfs(Gr,S):
    queue = []
    visited[S] += 1
    queue.append(S)

    while queue:
        t = queue.pop(0)
        for i in range(1,V+1):
            if Gr[t][i] == 1:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] += visited[t]+1

for tc in range(T):
    V,E = map(int,input().split()) # 노드 갯수, 간선 갯수

    Gr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for _ in range(E):
        f,o = map(int,input().split())
        Gr[f][o] = 1
        Gr[o][f] = 1

    S,G = map(int,input().split()) # 출발노드, 도착노드

    bfs(Gr,S)
    if visited[G] == 0:
        print('#{} {}'.format(tc+1,visited[G]))
    else:
        print('#{} {}'.format(tc+1,visited[G]-1))


