arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n):
    for j in range(n): #원소 수 만큼 비트 비교 ( 0부터 n까지인데)
    	if i & (1<<j): # j는 거꿀로 움직인돠 > i의 j 번째 비트가 1  이면 j 번째 원소를 출력한다.
            print(arr[j], end=", ") # 출력되면
    print()