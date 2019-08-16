import sys
sys.stdin = open('특별한_정렬.txt','r')

def selectionSort2(a):
    for i in range(0, len(a) -1):
        if i % 2:
            min = i
            for j in range(i+1, len(a)):
                if a[min] > a[j]:
                    min = j
            a[i], a[min] = a[min], a[i]
        else:
            max = i
            for j in range(i + 1, len(a)):
                if a[max] < a[j]:
                    max = j
            a[i], a[max] = a[max], a[i]
    return a[:10]


T = int(input())
for tc in range(T):
    N = int(input())
    P = list(map(int,input().split()))
    print('#{}'.format(tc),end=' ')
    for i in selectionSort2(P):
        print(i, end=' ')
    print()


    # def selectionSort(a):
    #     for i in range(0, len(a) - 1):
    #         min = i
    #         for j in range(i + 1, len(a)):
    #             if a[min] > a[j]:
    #                 min = j
    #             a[i], a[min] = a[min], a[i]
    #
    #
    # data = [64, 25, 10, 22, 11]
    # selectionSort(data)
    # print(data)