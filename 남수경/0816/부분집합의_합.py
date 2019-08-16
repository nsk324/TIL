import sys
sys.stdin = open('부분집합의_합.txt','r')

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for tc in range(T):
    N, K = map(int,input().split())
    cnt2 = 0
    for i in range(1 << 12): #(0부터 2**12까지)
        cnt = 0
        i_set = 0
        for j in range(12): # 원소 수 만큼 비트 비교 ( 0부터 n-1까지인데)
            if i & (1 << j):  # j는 거꿀로 움직인돠 > i의 j 번째 비트가 1  이면 j 번째 원소를 출력한다.
                cnt += 1
                i_set += A[j]

        if cnt == N and i_set == K:
            cnt2 += 1

    print('#{} {}'.format(tc+1,cnt2))