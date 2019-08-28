# import sys
#
# sys.stdin = open('Shuffle_input.txt')

T = int(input())

for tc in range(T):
    N = int(input()) #카드의 갯수 1~N까지
    card = list(map(int,input().split())) # 현재 카드가 놓여져잇는..
    # print(sorted(card))
    # print(sorted(card, reverse=True))
    # print(N,card)
    if card == sorted(card) or card == sorted(card, reverse=True):
        print('#{} 0'.format(tc+1))

    card_L = card[: N//2]
    card_R = card[N//2:]


    for x in range(0,N):
        testcard_L = [] + card_L
        testcard_R = [] + card_R
        # print(testcard_L, testcard_R)
        if x <= N//2:
            for i in range(x):
                print(i)
                testcard_L[i], testcard_R[-i] = testcard_R[-i], testcard_L[i]
            print(testcard_L, testcard_R)

        # if x > N//2:
        #     for i in range(x-N//2):
        #         print(i)
