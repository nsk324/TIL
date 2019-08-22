import sys
sys.stdin = open("그래프경로_input.txt")

def dfs(v):
    visited[v] = 1
    # print(v, end=' ')

    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0: # 현재 v와 연결되어있으며 방문한 적이 없는 w에대해
            dfs(w) # 불러오쇼




T = int(input())
for tc in range(T):
    V,E = map(int,input().split()) #노드, 줄의 갯수
    G = [[0 for _ in range(V+1)] for _ in range(V+1)] # range 넘지 말라규
    visited = [0 for _ in range(V+1)]
    for i in range(E):
        inp,outp = map(int,input().split())
        G[inp][outp] =1


    S,D = map(int,input().split()) #출발 노드, 도착 노드
    dfs(S)
    if visited[D] ==1:
        print('#{} 1'.format(tc+1))
    else:
        print('#{} 0'.format(tc+1))