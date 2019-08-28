import sys

sys.stdin = open('사각형_input.txt')


T = int(input())
levels = [ i for i in range(11)]
def canigo(y1,x1,y2,x2,level):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if box[y][x] > level:
                return False

    return True



for tc in range(T):
    N,M,K = map(int,input().split())
    box = [[0 for _ in range(M)] for _ in range(N)]



    for k in range(K):
        y1,x1,y2,x2,level = map(int,input().split())
        if canigo(y1,x1,y2,x2,level) == True:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    box[y][x] = level
    list_box = []
    for i in levels:
        total = 0
        for y in range(N):
            for x in range(M):
                if box[y][x] == i:
                    total += 1
        list_box.append(total)
    print(box)
    print('#{} {}'.format(tc+1, max(list_box)))