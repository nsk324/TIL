def BFS(G,v):
    queue = []
    queue.append(v)
    visited[v] = 1
    print(v)
    while queue:
        t = queue.pop(0)
        for i in range(1,8):
            if G[t][i] == 1:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = visited[t] + 1
                    print(i, visited[i]-1)



str = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'

nodes = list(map(int,str.split()))

G = [[0 for _ in range(8)] for _ in range(8)]

for i in range(len(nodes)//2):
    G[nodes[i+i]][nodes[i+i+1]] = 1
    G[nodes[i + i+1]][nodes[i + i]] = 1

visited = [0]*8


BFS(G,1)