import sys
def dfs(N):
    if N == 2:
        return 3
    if N == 1:
        return 1

    if N % 2: #홀수이면
        return dfs(N - 2) * (dfs(2)-1)*2 +1
    else: #짝수이면
        return dfs(N - 1) * 2 + 1

sys.stdin = open('종이붙이기_input.txt')
T = int(input())
for tc in range(T):
    # visited = [0,1,3,5]
    N = int(input())//10
    print('#{} {}'.format(tc+1, dfs(N)))
