import sys
sys.stdin = open('피자_input.txt')

def bake():
    for i in range(N):
        oven.append(pizza_num.pop(0))
    while 1:
        if oven[0] != 0:
            pizzas[oven[0]-1] = pizzas[oven[0]-1]//2
        if pizzas[oven[0]-1] == 0:
            oven.pop(0)
            if pizza_num != []:
                oven.insert(0, pizza_num.pop(0))
            elif pizza_num == []:
                oven.insert(0, 0)
            if oven.count(0) == N-1:
                for i in oven:
                    if i != 0:
                        x = i
                        return x
        check = oven.pop(0)
        oven.append(check)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    pizza_num = []
    for i in range(M):
        pizza_num += [i+1]
    oven = []
    print('#{} {}' .format(tc, bake()))