sum = 0
arr = list(map(int, input().split()))

for i in range(1, 1 << len(arr)): # 부분 갯수 수만큼 만들어주기위해 2**n 번 합니다. 어차피 0 은 아님요 ( 그래서 1부터임)
    sum = 0 # 각 부분집합 합을 0이라고 초기화하기
    for j in range(len(arr)): # i를 이진법으로 하고 1의 위치를 알아보기 위해 for를 돌립니다.
        if i & (1<<j) : # 마 니 j 번째에 1 있나?
            sum += arr[j] #잇으면 합해라

    if sum == 10: #그 i번째 부분집합의 합이 10인가?
        for j in range(len(arr)): #그면 뽑기위해 다시 부분집합 다 만드세여
            if i & (1 << j): # 마 니 j번째에 1 잇나?
                print(arr[j], end= " ") #있으면 나와라

        print() # 한 부분집합이 끝나면 엔터 드감