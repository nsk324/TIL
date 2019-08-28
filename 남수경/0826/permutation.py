def printArr(n):
    for i in range(n):
        print(arr[i],end=' ')
    print()

def perm(n,k):
    if k == n:
        printArr(n)
    else:
        for i in range(k,n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k] #다시 위의 노드로 가서 초기화해주가

arr = [1,3,4]
perm(3,0)