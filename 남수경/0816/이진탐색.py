import sys
sys.stdin = open('이진탐색.txt','r')

def binarysearch(l,r,p): # 처음, 마지막, 목표값

    global cnt

    cnt += 1
    c = (l+r)//2 #중간값

    if c == p:
        return cnt
    elif c > p :
        return binarysearch(l,c,p)
    else:
        return binarysearch(c,r,p)




T = int(input())
for tc in range(T):
    P, Pa, Pb = map(int,input().split()) #Pa,Pb : 각각 찾아야 할 페이지, P:총 페이지
    l, r = 1, P
    cnt = 0
    cnta = binarysearch(l,r,Pa)
    cnt = 0
    cntb = binarysearch(l,r,Pb)
    if cnta > cntb:
        print('#{} B'.format(tc+1))
    elif cnta < cntb:
        print('#{} A'.format(tc + 1))
    else:
        print('#{} 0'.format(tc + 1))