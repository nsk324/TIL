def isblock(x,y):
    global k
    if x < 0 or x >= r :
        k += 1
        return True
    if y < 0 or y >= r :
        k += 1
        return True
    if arr[y][x] != 0:
        k += 1
        return True
    return False



T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


for tc in range(T):
    r = int(input()) # 한 면의 길이
    x, y = 0, 0
    testx, testy = 0, 0
    num = 0
    k = 0
    arr = [[0 for _ in range(r)] for _ in range(r)] #값 넣을 빈 리스트 만들기


    while num < r**2:
        num +=1
        y, x = testy, testx
        arr[y][x] = num
        testx = x + dx[k]
        testy = y + dy[k]


        if testx<0 or testx >= r or testy<0 or testy >= r or  arr[testy][testx] != 0:
            k = (k+1) % 4
            testx = x + dx[k]
            testy = y + dy[k]


        # if isblock(testx,testy) == False:
        #     num += 1
        #     x = testx
        #     y = testy

    print(arr)