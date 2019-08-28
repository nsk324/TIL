data = [1,2,3,4,5,6,7,8,9,10]
N = 10
A = [0 for _ in range(N)]
count = 0
total = 0

def printSet(n,sum):
    # global count
    # count += 1
    # print("{} : ".format(count),end='') #생성되는 부분집합 개수
    # for i in range(n):# 각 부분 원소 출력
    #     if A[i] ==1:#이면 포함된것과 같으므로 출력
    #         print(data[i], end='')
    # sum = 0
    # for i in range(n):
    #     if A[i] ==1:
    #         sum += data[i]
    #
    # if sum == 10:
    #     for i in range(n):
    #         if A[i] == 1:
    #             print(data[i], end = '')
    #     print()
    global count
    if sum == 10:
        count += 1
        for i in range(n):
            if A[i] == 1:
                print(data[i], end = '')
        print()


def powerset(n,k,sum):
    global total
    ###
    if sum > 10:
        return
    ###
    total += 1
    if n == k :
        if sum ==10 :
            printSet(n,sum)

    else:
        A[k] = 1
        powerset(n,k+1,sum+data[k])
        A[k] = 0
        powerset(n,k+1,sum)


powerset(N,0,0)
