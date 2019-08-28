import sys
sys.stdin = open('토너먼트_input.txt')
T = int(input())

def team(player_list):
    n = len(player_list)

    if n == 2  : # 토너먼트 2 또는 1일때 (더 나뉠 수 없을 때)
        # print(player_list)
        stack.append(winner(player_list))
        return
    if n == 1:
        # print(player_list)
        stack.append(player_list[0])
        return

    team(player_list[:(1+n)//2])
    team(player_list[(1+n)//2 :])


def winner(team):
    print(team)
    if player[team[1]] == None:
        return team[]
    if player[team[0]-1] == player[team[1]-1] :
        return team[0]

    if player[team[0]-1] == 1 and  player[team[1]-1] == 2:
        return team[1]

    if player[team[0]-1] == 1 and  player[team[1]-1] == 3:
        return team[0]

    if player[team[0]-1] == 2 and  player[team[1]-1] == 1:
        return team[0]

    if player[team[0]-1] == 2 and  player[team[1]-1] == 3:
        return team[1]

    if player[team[0]-1] == 3 and  player[team[1]-1] == 1:
        return team[1]

    if player[team[0]-1] == 3 and  player[team[1]-1] == 2:
        return team[1]


for tc in range(T):
    N = int(input())
    stack = []

    # 총 N-1 회 하는데 깊이는 이로 나눈 몫
    player = list(map(int,input().split()))
    player_list = [i for i in range(1,N+1)] # 플레이어 번호
    team(player_list)

    while len(stack) >= 3:
        player_list = stack
        stack = []
        team(player_list)


    print('#{} {}'.format(tc+1,winner(stack)))

