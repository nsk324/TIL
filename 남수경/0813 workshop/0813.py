import sys
sys.stdin = open("input.txt",'r')

T = 10

for tc in range(T):
    numbers = int(input())
    datas = list(map(int,input().split()))
    hi = 1
    while hi <= numbers:
        max = 0
        min = 101
        for i in range(len(datas)):
            if datas[i] > max:
                max = datas[i]
            if datas[i] < min:
                min = datas[i]
        
        datas[datas.index(max)] = max - 1
        datas[datas.index(min)] = min + 1

        if max-min <=1:
            hi = numbers
        hi += 1
    
    max = 0
    min = 101    
    
    for i in range(len(datas)):
        if datas[i] > max:
            max = datas[i]
        if datas[i] < min:
            min = datas[i]
        
    
    print('#{} {}'.format(tc+1, max-min))
