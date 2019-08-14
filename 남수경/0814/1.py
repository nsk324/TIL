import sys

sys.stdin = open("1.txt", 'r')


def isWall(x, y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    return False


def calAbs(y, x):
    if y - x > 0:
        return y - x
    else:
        return x - y


arr = [[0 for _ in range(5)] for _ in range(5)]  # 칼럼 리스트 * 로우 니까 접근할 때 로우접근(y) 그 후 x 접근

for i in range(5):
    arr[i] = list(map(int, input().split()))  # 입력받았돠

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum = 0

for x in range(5):
    for y in range(5):
        for mode in range(4):
            testX = x + dx[mode]
            testY = y + dy[mode]
            if isWall(testX, testY) == False:
                sum += calAbs(arr[y][x], arr[testY][testX])

print("sum = {}".format(sum))