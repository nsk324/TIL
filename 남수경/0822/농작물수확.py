T = int(input())
N = int(input())
land = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    land[i] = list(map(int,input().split()))
print(land)